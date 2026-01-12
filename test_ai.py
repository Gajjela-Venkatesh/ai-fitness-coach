import google.generativeai as genai
import os
import json
from dotenv import load_dotenv

# Load env directly to be sure
load_dotenv()
api_key = os.getenv('GOOGLE_API_KEY')
print(f"API Key present: {bool(api_key)}")

if api_key:
    genai.configure(api_key=api_key)

class DummyUser:
    age = 30
    gender = "Male"
    goal = "Muscle Gain"
    experience = "Intermediate"
    equipment = "Dumbbells"
    environment = "Home"

def test_ai():
    user = DummyUser()
    print("Testing AI generation...")
    
    model = genai.GenerativeModel('gemini-flash-latest')
    
    prompt = f"""
    Generate a highly professional, 7-day workout plan for a user with the following profile:
    - Age: {user.age}
    - Gender: {user.gender}
    - Goal: {user.goal}
    - Experience: {user.experience}
    - Equipment: {user.equipment}
    - Environment: {user.environment}
    
    Guidelines:
    1. Use JSON format exactly as follows:
    {{
        "Monday": {{ "type": "Muscle Group/Type", "exercises": [{{ "exercise": "Name", "sets": 3, "reps": "12", "rest": "60s", "notes": "Form tip" }}] }},
        ...
    }}
    2. Only return the raw JSON object.
    """
    
    try:
        response = model.generate_content(prompt)
        text = response.text.strip()
        print(f"Raw response: {text[:200]}...") # Print start of response
        
        if "```json" in text:
            text = text.split("```json")[1].split("```")[0].strip()
        elif "```" in text:
            text = text.split("```")[1].split("```")[0].strip()
            
        json_data = json.loads(text)
        print("JSON parsing successful.")
        print(json.dumps(json_data, indent=2)[:200])
        return True
    except Exception as e:
        print(f"AI Generation Error: {e}")
        return False

if __name__ == "__main__":
    if not api_key:
        print("Error: No API KEY found.")
    else:
        test_ai()
