from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from database import Base
import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    age = Column(Integer)
    gender = Column(String)
    goal = Column(String)
    equipment = Column(String)
    environment = Column(String)
    experience = Column(String)

    workouts = relationship("Workout", back_populates="owner")
    feedbacks = relationship("Feedback", back_populates="owner")
    adaptive_tips = relationship("AdaptiveTip", back_populates="owner")

class Workout(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    plan_json = Column(Text)

    owner = relationship("User", back_populates="workouts")

class Feedback(Base):
    __tablename__ = "feedbacks"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    feedback_text = Column(String)
    analysis_result = Column(String)

    owner = relationship("User", back_populates="feedbacks")

class AdaptiveTip(Base):
    __tablename__ = "adaptive_tips"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    tip_text = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    owner = relationship("User", back_populates="adaptive_tips")
