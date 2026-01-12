# AI Fitness Coach

A personalized, AI-powered fitness and nutrition platform built with **FastAPI** and **Google Gemini AI**. This application generates customized workout plans and nutrition tips based on user goals, equipment, and feedback.

## Features

-   **Personalized Workouts**: Generates 7-day workout plans tailored to your age, goal (e.g., Muscle Gain, Weight Loss), and available equipment.
-   **AI Nutrition Tips**: Provides actionable nutrition advice based on your profile.
-   **Smart Feedback Loop**: Adapts future recommendations based on your feedback (Easy, Moderate, Hard) from previous sessions.
-   **User Profiles**: Secure login and registration with profile management.
-   **Adaptive Coaching**: Uses Google's `gemini-flash-latest` model for real-time, intelligent responses.

## Tech Stack

-   **Backend**: FastAPI, Python 3.10+
-   **Database**: SQLite, SQLAlchemy
-   **AI Engine**: Google Gemini API (`gemini-flash-latest`)
-   **Frontend**: HTML, Jinja2 Templates, Vanilla CSS

## Setup & partial Run

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd ai-fitness-coach
    ```

2.  **Create a virtual environment**:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # Windows
    source venv/bin/activate # Mac/Linux
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment**:
    Create a `.env` file in the root directory and add your Google API Key:
    ```env
    GOOGLE_API_KEY=your_api_key_here
    SESSION_SECRET_KEY=your_secret_key
    ```

5.  **Run the application**:
    ```bash
    uvicorn main:app --reload
    ```
    Access the app at `http://127.0.0.1:8000`.

## License

MIT
