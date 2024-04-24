from uuid import UUID
import uuid

from pydantic import field_validator
from sqlmodel import SQLModel, Field


class BaseMovie(SQLModel):
    name: str
    year: int

class CreateMovieRequest(BaseMovie):
    pass

class UpdateMovieRequest(BaseMovie):
    pass

class Movie(BaseMovie, table=True):
    movie_id: str | None = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)

    @field_validator("movie_id", mode="before", check_fields=False)
    def convert_uuid_to_str(cls, v: uuid) -> str:
        if isinstance(v, UUID):
            return str(v)
        raise ValueError 
        
class CreateMovieResponse(SQLModel):
    id: UUID

class UpdateMovieResponse(SQLModel):
    success: bool

class DeleteMovieResponse(SQLModel):
    success: bool