from sqlmodel import SQLModel, create_engine

import schemas

sql_name = "database.db"
sql_url = f"sqlite:///{sql_name}"

engine = create_engine(sql_url, echo=True)


SQLModel.metadata.create_all(engine)