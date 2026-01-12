from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
from passlib.context import CryptContext

# Setup password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def fix_passwords():
    db = SessionLocal()
    try:
        users = db.query(models.User).all()
        print(f"Found {len(users)} users. Checking for plain text passwords...")
        
        count = 0
        for user in users:
            # Simple check: bcrypt hashes start with $2b$ or similar. 
            # If it doesn't look like a hash, we hash it.
            if not user.password.startswith("$"):
                print(f"Updating password for user {user.username}...")
                user.password = get_password_hash(user.password)
                count += 1
        
        if count > 0:
            db.commit()
            print(f"Updated {count} user passwords to hashes.")
        else:
            print("No plain text passwords found.")
            
    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    fix_passwords()
