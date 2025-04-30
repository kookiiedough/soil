# MIT License
#
# Copyright (c) 2023 Biodynamic Offline
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

from datetime import datetime
from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel, create_engine, Session


class User(SQLModel, table=True):
    """User model for storing user information."""
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True)
    email: str
    created_at: datetime = Field(default_factory=datetime.now)
    
    # Relationships
    predictions: List["Prediction"] = Relationship(back_populates="user")


class Prediction(SQLModel, table=True):
    """Prediction model for storing soil health predictions."""
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    file_name: str
    gc_content: float
    n_count: int
    read_length_mean: float
    soil_risk: float
    created_at: datetime = Field(default_factory=datetime.now)
    
    # Relationships
    user: Optional[User] = Relationship(back_populates="predictions")


# Database setup
SQLITE_URL = "sqlite:///./biodynamic.db"


def get_engine():
    """Get SQLAlchemy engine."""
    return create_engine(SQLITE_URL, echo=False)


def get_session():
    """Get database session."""
    engine = get_engine()
    with Session(engine) as session:
        yield session


def init_db():
    """Initialize database tables."""
    engine = get_engine()
    SQLModel.metadata.create_all(engine)