import uuid

from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select

from db import engine, SQLModel

from schemas import (
    Movie,
    CreateMovieRequest,
    CreateMovieResponse,
    UpdateMovieRequest,
    UpdateMovieResponse,
    DeleteMovieResponse,
)

def get_db():
    with Session(bind=engine) as session:
        yield session

movies: list[Movie] = [
    Movie(movie_id=str(uuid.uuid4()), name="Spider-Man", year=2002),
    Movie(movie_id=str(uuid.uuid4()), name="Thor: Ragnarok", year=2017),
    Movie(movie_id=str(uuid.uuid4()), name="Iron Man", year=2008),
]

with Session(bind=engine) as session:
    if len(session.exec(select(Movie)).all()) == 0:
        for movie in movies:
            session.add(Movie(**movie.model_dump()))
        session.commit()
    

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/movies", response_model=list[Movie], status_code=status.HTTP_200_OK, tags=["Movies"])
async def get_movies(session: Session = Depends(get_db)) -> list[Movie]:
    movies = session.exec(select(Movie)).all()
    return movies
    

@app.post("/movies", response_model=CreateMovieResponse, status_code=status.HTTP_201_CREATED, tags=["Movies"])
async def create_movie(new_movie: CreateMovieRequest, session: Session = Depends(get_db)) -> CreateMovieResponse:
    movie: Movie = Movie.model_validate(new_movie)
    session.add(movie)
    session.commit()
    session.refresh(movie)
    return CreateMovieResponse(id=movie.movie_id)
    
@app.put("/movies/{movie_id}", response_model=UpdateMovieResponse,
         responses={
             status.HTTP_200_OK: {
                 "description": "Item updated successfully",
                 "content": {
                     "application/json": {
                         "example": {
                             "success": True
                         }
                     }
                 }
             },
             status.HTTP_201_CREATED: {
                 "description": "Item created successfully",
                 "content": {
                     "application/json": {
                         "example": {
                             "success": True
                         }
                     }
                 }
             }
         }, tags=["Movies"])
async def update_movie(movie_id: uuid.UUID, updated_movie: UpdateMovieRequest, session: Session = Depends(get_db)) -> UpdateMovieResponse:
    movie: Movie = session.exec(select(Movie).where(Movie.movie_id == str(movie_id))).first()
    if movie is None:
        movie: Movie = Movie(**updated_movie.model_dump(), movie_id=str(movie_id))
        session.add(movie)
        session.commit()
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=UpdateMovieResponse(success=True).model_dump())
    for attr, value in updated_movie.model_dump().items():
        setattr(movie, attr, value)
    session.commit()
    return UpdateMovieResponse(success=True)

    
@app.delete("/movies/{movie_id}", tags=["Movies"])
async def delete_movie(movie_id: uuid.UUID) -> DeleteMovieResponse:
    movie: Movie = session.exec(select(Movie).where(Movie.movie_id == str(movie_id))).first()
    if movie is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Movie ID: {movie_id} not found.")
    session.delete(movie)
    session.commit()
    return DeleteMovieResponse(success=True)