from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models

# Ensure tables exist (they should, but good practice)
models.Base.metadata.create_all(bind=engine)

def inspect_users():
    db = SessionLocal()
    try:
        users = db.query(models.User).all()
        print(f"Found {len(users)} users.")
        for user in users:
            print(f"ID: {user.id}, Username: {user.username}, Password Hash: '{user.password}'")
    finally:
        db.close()

if __name__ == "__main__":
    inspect_users()
