AI Fitness Coach

An AI-powered fitness and nutrition coaching platform built using FastAPI and Google Gemini AI. The application delivers personalized workout plans and nutrition guidance by intelligently adapting to user goals, available equipment, and continuous feedback.

Overview

AI Fitness Coach acts as a virtual personal trainer, combining modern backend technologies with generative AI to create adaptive, user-centric fitness recommendations. The system evolves over time by learning from user feedback, ensuring progressively optimized workout and nutrition plans.

Key Features

Personalized Workout Plans
Automatically generates structured 7-day workout routines based on user age, fitness goals (Muscle Gain, Weight Loss, Maintenance), and available equipment.

AI-Driven Nutrition Guidance
Provides practical, goal-aligned nutrition tips tailored to the user’s fitness profile.

Adaptive Feedback System
Continuously improves recommendations using user feedback (Easy, Moderate, Hard) from previous workouts.

User Authentication & Profiles
Secure user registration, login, and profile management for a personalized coaching experience.

Real-Time AI Responses
Powered by Google’s gemini-flash-latest model for fast and intelligent coaching insights.

Technology Stack

Backend: FastAPI (Python 3.10+)

Database: SQLite with SQLAlchemy ORM

AI Engine: Google Gemini API (gemini-flash-latest)

Frontend: HTML, Jinja2 Templates, Vanilla CSS

Authentication: Session-based authentication

Project Setup & Execution
1. Clone the Repository
git clone <repository-url>
cd ai-fitness-coach

2. Create & Activate Virtual Environment
python -m venv venv
.\venv\Scripts\activate   # Windows
source venv/bin/activate # macOS/Linux

3. Install Dependencies
pip install -r requirements.txt

4. Environment Configuration

Create a .env file in the project root and add the following:

GOOGLE_API_KEY=your_google_api_key
SESSION_SECRET_KEY=your_secret_key

5. Run the Application
uvicorn main:app --reload


Access the application at:
👉 http://127.0.0.1:8000

Use Cases

Personalized fitness coaching

AI-assisted nutrition planning

Adaptive health and wellness applications

FastAPI + Generative AI integration demos

License

This project is licensed under the MIT License.
