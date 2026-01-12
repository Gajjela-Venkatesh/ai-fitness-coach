from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
from passlib.context import CryptContext

# Setup password hashing with pbkdf2_sha256
pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

def fix_passwords():
    db = SessionLocal()
    try:
        users = db.query(models.User).all()
        print(f"Found {len(users)} users.")
        
        for user in users:
            # We will force update known users to their expected passwords
            new_pass = "pass123" # Default
            
            if user.username == "vasutech108@gmail.com":
                new_pass = "vasu123"
            elif user.username == "dbuser":
                new_pass = "pass123"
            
            # If the current password is NOT a valid hash, or we just want to force fix it
            # consistently, let's just update it. 
            # Given the previous mess, let's FORCE UPDATE to ensure it works.
            
            print(f"Resetting password for {user.username} to '{new_pass}' (hashed)")
            user.password = pwd_context.hash(new_pass)
        
        db.commit()
        print("All passwords updated successfully.")
            
    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    fix_passwords()
