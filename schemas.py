from sqlmodel import SQLModel, Field
from datetime import datetime


class usersOut(SQLModel):
    id: int
    email: str
    created_at: datetime

    class Config:
        orm_mode = True