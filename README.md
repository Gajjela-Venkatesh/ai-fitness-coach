🚀 AI Fitness Coach
An AI-Powered Personalized Fitness & Nutrition Coaching Platform

AI Fitness Coach is a modern, intelligent fitness application built using FastAPI and Google Gemini AI. It delivers personalized workout routines and nutrition guidance by adapting to individual goals, equipment availability, and continuous user feedback.

📌 Project Overview

The platform functions as a virtual personal trainer, leveraging generative AI to create adaptive fitness experiences. By incorporating a smart feedback loop, the system continuously improves recommendations to ensure long-term effectiveness and user engagement.

✨ Key Features
🏋️ Personalized Workout Plans

Generates structured 7-day workout schedules

Tailored to age, fitness goals, and available equipment

🥗 AI-Driven Nutrition Guidance

Provides actionable nutrition tips

Aligned with individual fitness objectives

🔁 Smart Feedback Loop

Collects user feedback (Easy / Moderate / Hard)

Dynamically adjusts future workout intensity

👤 User Authentication & Profiles

Secure registration and login

Persistent user profiles for personalized coaching

⚡ Real-Time AI Coaching

Powered by Google’s gemini-flash-latest model

Fast, context-aware responses

🛠️ Technology Stack
🔹 Backend

FastAPI (Python 3.10+)

🔹 Database

SQLite

SQLAlchemy ORM

🔹 AI Engine

Google Gemini API (gemini-flash-latest)

🔹 Frontend

HTML

Jinja2 Templates

Vanilla CSS

⚙️ Setup & Execution
📥 1. Clone the Repository
git clone <repository-url>
cd ai-fitness-coach

🧪 2. Create & Activate Virtual Environment
python -m venv venv
.\venv\Scripts\activate   # Windows
source venv/bin/activate # macOS/Linux

📦 3. Install Dependencies
pip install -r requirements.txt

🔐 4. Environment Configuration

Create a .env file in the project root:

GOOGLE_API_KEY=your_google_api_key
SESSION_SECRET_KEY=your_secret_key

▶️ 5. Run the Application
uvicorn main:app --reload


🌐 Access the app at: http://127.0.0.1:8000

🎯 Use Cases

AI-powered personal fitness coaching

Adaptive nutrition recommendation systems

FastAPI + Generative AI portfolio projects

Health & wellness SaaS prototypes

📜 License
MIT License

This project is open-source and available under the MIT License.
