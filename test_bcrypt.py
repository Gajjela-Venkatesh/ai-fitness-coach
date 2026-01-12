from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

try:
    hash = pwd_context.hash("testpassword")
    print(f"Successfully hashed: {hash}")
    
    verify = pwd_context.verify("testpassword", hash)
    print(f"Successfully verified: {verify}")
except Exception as e:
    print(f"Bcrypt Error: {e}")
