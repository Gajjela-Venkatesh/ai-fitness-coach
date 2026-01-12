from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
import json

def inspect_workouts():
    db = SessionLocal()
    try:
        workouts = db.query(models.Workout).all()
        print(f"Found {len(workouts)} workout records.")
        for w in workouts:
            print(f"Workout ID: {w.id}, User ID: {w.user_id}")
            print(f"Plan JSON (raw): {w.plan_json}")
            try:
                parsed = json.loads(w.plan_json)
                print(f"Parsed type: {type(parsed)}")
                print(f"Parsed content: {parsed}")
            except Exception as e:
                print(f"JSON Parse Error: {e}")
            print("-" * 20)
    finally:
        db.close()

if __name__ == "__main__":
    inspect_workouts()
