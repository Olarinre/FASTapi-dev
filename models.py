from datetime import datetime
from datetime import datetime
from sqlmodel import SQLModel, Field
from sqlalchemy import func
from sqlalchemy.sql import expression
from typing import Optional



class Posts(SQLModel, table = True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    content: str
    published: bool = True



class Users(SQLModel, table = True):
    id: int = Field(default=None, primary_key=True)
    email: str = Field(index=True, unique=True)
    password: str
    created_at: datetime = Field(
        sa_column_kwargs={"server_default": func.now()},  # Database default
        default_factory=datetime.utcnow,                  # Python-side default
        nullable=False
    )



