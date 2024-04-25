"use client";
import React, { useState, useEffect, useCallback } from "react"; // Import useCallback

interface Movie {
  movie_id: string;
  name: string;
  year: number;
}

interface MoviesProps {
  movies: Movie[];
  fetchMovies: () => void;
  deleteMovie: (movieId: string) => void;
}

const Movies: React.FC<MoviesProps> = ({ movies, deleteMovie }) => {
  return (
    <div>
      <h1 className="text-xl font-bold text-gray-200">Movies List</h1>
      <ul>
        {movies.map((movie) => (
          <li key={movie.movie_id} className="flex justify-between items-center py-2">
            <span className="text-white">
              {movie.name} ({movie.year})
            </span>
            <button onClick={() => deleteMovie(movie.movie_id)} className="text-red-500 hover:text-red-700 px-3 py-1 bg-gray-800 rounded">
              Delete
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Movies;
