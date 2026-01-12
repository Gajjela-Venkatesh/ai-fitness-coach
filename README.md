AI Fitness Coach

AI Fitness Coach is a personalized, AI-powered fitness and nutrition coaching platform built using FastAPI and Google Gemini AI. The application generates adaptive workout plans and nutrition recommendations based on user goals, available equipment, and continuous feedback.

Project Overview

The platform acts as a virtual fitness coach by leveraging generative AI to deliver structured workout routines and intelligent nutrition guidance. A feedback-driven learning loop enables continuous improvement of recommendations, ensuring relevance and long-term effectiveness.

Key Features
Personalized Workout Planning

Automatically generates 7-day workout plans

Customized based on age, fitness goals, and equipment availability

AI-Driven Nutrition Guidance

Provides actionable nutrition tips aligned with user objectives

Adjusts suggestions based on individual profiles

Adaptive Feedback Mechanism

Collects workout difficulty feedback (Easy, Moderate, Hard)

Dynamically modifies future workout intensity

User Authentication and Profiles

Secure user registration and login

Persistent profiles for personalized coaching

Real-Time AI Coaching

Powered by Google Gemini’s gemini-flash-latest model

Fast and context-aware AI responses

Technology Stack
Backend

FastAPI (Python 3.10+)

Database

SQLite

SQLAlchemy ORM

AI Engine

Google Gemini API (gemini-flash-latest)

Frontend

HTML

Jinja2 Templates

Vanilla CSS

Installation and Setup
1. Clone the Repository
git clone <repository-url>
cd ai-fitness-coach

2. Create and Activate Virtual Environment
python -m venv venv
.\venv\Scripts\activate   # Windows
source venv/bin/activate # macOS/Linux

3. Install Dependencies
pip install -r requirements.txt

4. Environment Configuration

Create a .env file in the root directory:

GOOGLE_API_KEY=your_google_api_key
SESSION_SECRET_KEY=your_secret_key

5. Run the Application
uvicorn main:app --reload


Access the application at:
http://127.0.0.1:8000

Use Cases

AI-powered fitness coaching platforms

Personalized nutrition recommendation systems

FastAPI and Generative AI integration projects

Health and wellness SaaS prototypes

Future Improvements

Workout progress tracking and analytics

Mobile-responsive frontend

Advanced personalization using historical data

Deployment using Docker and cloud services

License

MIT License

This project is licensed under the MIT License.
