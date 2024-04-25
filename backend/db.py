from sqlmodel import SQLModel, create_engine

import schemas

sql_name = "movie-app"
sql_url = f"postgresql://postgres:postgres@localhost:5433/{sql_name}"

engine = create_engine(sql_url, echo=True)


SQLModel.metadata.create_all(engine)