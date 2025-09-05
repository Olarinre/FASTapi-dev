<<<<<<< HEAD
from sqlmodel import Field, SQLModel

class Posts(SQLModel, table = True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    content: str
    published: bool = True



=======
from sqlmodel import Field, SQLModel

class Posts(SQLModel, table = True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    content: str
    published: bool = True



>>>>>>> 412ea3d4ed65787fee44fddbcda2f587423410d6
