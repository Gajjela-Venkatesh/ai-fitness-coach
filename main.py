from fastapi import FastAPI, Request, Form, HTTPException, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
from typing import Dict, List, Optional
from gtts import gTTS
import os
import json
import google.generativeai as genai
from dotenv import load_dotenv
import random
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import models
from passlib.context import CryptContext

# Initialize database
models.Base.metadata.create_all(bind=engine)

load_dotenv()
api_key = os.getenv('GOOGLE_API_KEY')
secret_key = os.getenv('SESSION_SECRET_KEY', 'a_very_secret_key_12345') # Use env or fallback for dev
genai.configure(api_key=api_key)

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=secret_key)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Password utility
pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def get_current_user(request: Request, db: Session = Depends(get_db)):
    user_id = request.session.get("user_id")
    if not user_id:
        return None
    return db.query(models.User).filter(models.User.id == user_id).first()

def login_required(user: Optional[models.User] = Depends(get_current_user)):
    if not user:
        raise HTTPException(status_code=303, detail="Not logged in", headers={"Location": "/login"})
    return user

# Exercise metadata for AI fallbacks (if needed)
exercise_params = {
    "Push-ups": {"sets": 3, "reps": "10-15"},
    "Lower": {"sets": 3, "reps": "12-15"}
}

def get_ai_workout_plan(user, feedback_history=[]):
    model = genai.GenerativeModel('gemini-flash-latest')
    feedback_context = f"Recent user feedback: {', '.join(feedback_history)}" if feedback_history else "No recent feedback."
    
    prompt = f"""
    Generate a highly professional, 7-day workout plan for a user with the following profile:
    - Age: {user.age}
    - Gender: {user.gender}
    - Goal: {user.goal}
    - Experience: {user.experience}
    - Equipment: {user.equipment}
    - Environment: {user.environment}
    
    {feedback_context}
    
    Guidelines:
    1. Provide a varied and effective routine for each day.
    2. If feedback says "Hard", decrease intensity slightly. If "Easy", increase it.
    3. Use JSON format exactly as follows:
    {{
        "Monday": {{ "type": "Muscle Group/Type", "exercises": [{{ "exercise": "Name", "sets": 3, "reps": "12", "rest": "60s", "notes": "Form tip" }}] }},
        ...
    }}
    4. Only return the raw JSON object. Use valid exercise names and professional notes.
    """
    
    try:
        response = model.generate_content(prompt)
        text = response.text.strip()
        if "```json" in text:
            text = text.split("```json")[1].split("```")[0].strip()
        elif "```" in text:
            text = text.split("```")[1].split("```")[0].strip()
        return json.loads(text)
    except Exception as e:
        print(f"AI Generation Error: {e}")
        return None

def get_ai_nutrition_tips(user, feedback_history=[]):
    model = genai.GenerativeModel('gemini-flash-latest')
    feedback_context = f"Recent user feedback: {', '.join(feedback_history)}" if feedback_history else "No recent feedback."
    
    prompt = f"""
    Provide 5 high-quality, actionable, and professional nutrition tips for a {user.age} year old {user.gender} aiming for {user.goal}.
    
    {feedback_context}
    
    Return the tips as a simple JSON list of strings: ["Tip 1", "Tip 2", ...]
    Only return the raw JSON list.
    """
    
    try:
        response = model.generate_content(prompt)
        text = response.text.strip()
        if "```json" in text:
            text = text.split("```json")[1].split("```")[0].strip()
        elif "```" in text:
            text = text.split("```")[1].split("```")[0].strip()
        return json.loads(text)
    except Exception as e:
        print(f"AI Generation Error: {e}")
        return []

def analyze_feedback(feedback):
    if "hard" in feedback.lower(): return "Hard"
    elif "easy" in feedback.lower(): return "Easy"
    else: return "Moderate"

@app.get("/")
async def landing(request: Request, user: Optional[models.User] = Depends(get_current_user)):
    if user: return RedirectResponse("/home")
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/signup")
async def signup_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.post("/api/register")
async def register_user(
    request: Request,
    username: str = Form(...), password: str = Form(...), age: int = Form(...),
    gender: str = Form(...), goal: str = Form(...), equipment: str = Form(...),
    environment: str = Form(...), experience: str = Form(...), db: Session = Depends(get_db)
):
    # Check if user exists
    existing = db.query(models.User).filter(models.User.username == username).first()
    if existing:
        return templates.TemplateResponse("register.html", {"request": request, "error": "Username already taken"})
    
    db_user = models.User(
        username=username, 
        password=get_password_hash(password), # Hashed password
        age=age, gender=gender,
        goal=goal, equipment=equipment, environment=environment, experience=experience
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    request.session["user_id"] = db_user.id
    return RedirectResponse("/home", status_code=303)

@app.get("/login")
async def login_p(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/api/login")
async def login_u(request: Request, username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == username).first()
    if user and verify_password(password, user.password):
        request.session["user_id"] = user.id
        return RedirectResponse("/home", status_code=303)
    return templates.TemplateResponse("login.html", {"request": request, "error": "Invalid username or password"})

@app.get("/home")
async def home_dashboard(request: Request, user: models.User = Depends(login_required)):
    return templates.TemplateResponse("home.html", {"request": request, "user": user})

@app.get("/edit-profile")
async def edit_profile(request: Request, user: models.User = Depends(login_required)):
    return templates.TemplateResponse("edit_profile.html", {"request": request, "user": user})

@app.post("/api/update-profile")
async def update_profile(
    request: Request,
    username: str = Form(...), password: str = Form(None),
    age: int = Form(...), gender: str = Form(...), goal: str = Form(...),
    equipment: str = Form(...), environment: str = Form(...), experience: str = Form(...),
    db: Session = Depends(get_db), current_user: models.User = Depends(login_required)
):
    current_user.username, current_user.age, current_user.gender = username, age, gender
    current_user.goal, current_user.equipment, current_user.environment, current_user.experience = goal, equipment, environment, experience
    if password:
        current_user.password = get_password_hash(password)
    db.commit()
    return RedirectResponse("/home", status_code=303)

@app.post("/api/generate-workout")
async def generate_w(request: Request, db: Session = Depends(get_db), user: models.User = Depends(login_required)):
    workout = db.query(models.Workout).filter(models.Workout.user_id == user.id).first()
    
    feedback_history = db.query(models.Feedback).filter(models.Feedback.user_id == user.id)\
        .order_by(models.Feedback.id.desc()).limit(3).all()
    history_texts = [f"{fb.analysis_result}: {fb.feedback_text}" for fb in feedback_history]
    
    if not workout:
        plan = get_ai_workout_plan(user, history_texts)
        if not plan:
            return templates.TemplateResponse("workout.html", {"request": request, "error": "AI Coach is busy. Try again later!", "username": user.username, "user": user})
        workout = models.Workout(user_id=user.id, plan_json=json.dumps(plan))
        db.add(workout)
        db.commit()
    else:
        plan = json.loads(workout.plan_json)
        
    return templates.TemplateResponse("workout.html", {"request": request, "workout_plan": plan, "username": user.username, "user": user})

@app.get("/api/nutrition-tips")
async def nutrition_t(request: Request, db: Session = Depends(get_db), user: models.User = Depends(login_required)):
    feedback_history = db.query(models.Feedback).filter(models.Feedback.user_id == user.id)\
        .order_by(models.Feedback.id.desc()).limit(3).all()
    history_texts = [f"{fb.analysis_result}: {fb.feedback_text}" for fb in feedback_history]
    
    base_tips = get_ai_nutrition_tips(user, history_texts)
    adaptive_tips = db.query(models.AdaptiveTip).filter(models.AdaptiveTip.user_id == user.id).all()
    all_tips = base_tips + [tip.tip_text for tip in adaptive_tips]
    return templates.TemplateResponse("nutrition.html", {"request": request, "tips": all_tips, "username": user.username, "user": user})

@app.post("/api/feedback")
async def process_f(request: Request, feedback: str = Form(...), db: Session = Depends(get_db), user: models.User = Depends(login_required)):
    result = analyze_feedback(feedback)
    db_feedback = models.Feedback(user_id=user.id, feedback_text=feedback, analysis_result=result)
    db.add(db_feedback)
    
    db.add(models.AdaptiveTip(user_id=user.id, tip_text=f"Last workout was marked as {result}. Adjusting next strategy accordingly."))
    db.commit()

    # Trigger a RE-generation for the next time
    workout = db.query(models.Workout).filter(models.Workout.user_id == user.id).first()
    if workout:
        db.delete(workout)
        db.commit()

    return RedirectResponse("/home", status_code=303)

@app.get("/logout")
async def logout(request: Request):
    request.session.clear()
    return RedirectResponse("/", status_code=303)
