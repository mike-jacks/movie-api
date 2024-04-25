"use client";
import React, { useState, useEffect, useCallback } from "react";
import Movies from "./Movies";
import AddMovieForm from "./AddMovieForm";

// In App component

function App() {
  const [movies, setMovies] = useState([]);

  const fetchMovies = useCallback(() => {
    fetch("http://localhost:8000/movies")
      .then((response) => response.json())
      .then((data) => setMovies(data))
      .catch((err) => console.error("Error fetching movies:", err));
  }, []);

  useEffect(() => {
    fetchMovies();
  }, [fetchMovies]);

  const deleteMovie = (movieId: string) => {
    fetch(`http://localhost:8000/movies/${movieId}`, {
      method: "DELETE",
    })
      .then((response) => {
        if (response.ok) {
          fetchMovies(); // Re-fetch movies after deleting
        }
      })
      .catch((err) => console.error("Error deleting movie:", err));
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-semibold text-center">Movie Catalog</h1>
      <AddMovieForm onMovieAdded={fetchMovies} />
      <Movies movies={movies} deleteMovie={deleteMovie} />
    </div>
  );
}

export default App;
