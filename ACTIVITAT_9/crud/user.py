from sqlalchemy.orm import Session
from models import User
from schemas.user import UserSchema

def read_users(db: Session):
    return db.query(User).all()
