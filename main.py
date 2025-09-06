import random
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
from sqlmodel import Session, select
from models import Posts, Users
from dbconnect import get_session
import schemas
import utils







"""try:
    conn = psycopg2.connect(
        host="localhost",
        database="fastapi",
        user="postgres",
        password="Ayobami@090499",
        cursor_factory = RealDictCursor   
    )
    cursor = conn.cursor()
    print("Database connection was successful")
except Exception as error:
    print("Database connection failed")
    print("Error:", error)
#end of db conne
# ction.
"""

posts_db = [

    {'title': 'first post', 'content': 'this is the content of the first post', 'id': 1},
    {'title': 'second post', 'content': 'this is the content of the second post', 'id': 2}
]

#findpost function
def find_post(id):
    for post in posts_db:
        if post['id'] == id:
            return post
    return None


#pydantic schema
class New_post(BaseModel):
    title: str
    content: str
    published: bool = True
    




app = FastAPI()

@app.get("/")
async def root():
    return {'message': 'hello world1'}

#get all posts
@app.get('/sqlmodel')
def get_posts(session: Session = Depends(get_session)):
    posts = session.exec(select(Posts)).all()
    return posts


@app.post('/users', status_code=status.HTTP_201_CREATED, response_model=schemas.usersOut)
def create_user(user: Users, session: Session = Depends(get_session)):
    hashed_passsword = utils.hash_password((user.password))
    user.password = hashed_passsword
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


@app.get('/users/{id}', response_model=schemas.usersOut)
def get_user(id: int, session: Session = Depends(get_session)):
    user = session.get(Users, id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with id: {id} was not found")
    return user


@app.get('/auth')
def auth_user(email: str = Body(...), password: str = Body(...), session: Session = Depends(get_session)):
    user = session.exec(select(Users).where(Users.email == email)).first()
    if not utils.authenticate_user(user, password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="invalid credentials")
    return {"message": "successfully authenticated"}

