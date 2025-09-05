from sqlmodel import SQLModel, create_engine, Session

database="fastapi"
postgres_url = f"postgresql://postgres:Ayobami%40090499@localhost/{database}"

engine= create_engine(postgres_url)

#create the database
SQLModel.metadata.create_all(engine)

#print to verify
print("Database created successfully")

#dependency


def get_session():
    with Session(engine) as session:
        yield session