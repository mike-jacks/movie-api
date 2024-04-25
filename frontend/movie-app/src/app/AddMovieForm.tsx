"use client";
import React, { useState, FormEvent } from "react";

interface AddMovieFormProps {
  onMovieAdded: () => void; // Type the function prop
}

const AddMovieForm: React.FC<AddMovieFormProps> = ({ onMovieAdded }) => {
  const [name, setName] = useState<string>("");
  const [year, setYear] = useState<string>("");

  const handleSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const postData = {
      name,
      year: parseInt(year, 10),
    };

    fetch("http://localhost:8000/movies", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(postData),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("Movie added:", data);
        setName("");
        setYear("");
        onMovieAdded(); // Call the prop function to refresh movies
      })
      .catch((err) => console.error("Error adding movie:", err));
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div>
        <label htmlFor="name" className="block text-gray-200">
          Movie Name
        </label>
        <input
          type="text"
          id="name"
          value={name}
          onChange={(e: React.ChangeEvent<HTMLInputElement>) => setName(e.target.value)}
          className="border border-gray-600 bg-gray-800 p-2 text-white placeholder-gray-400 focus:border-blue-500"
          required
        />
      </div>
      <div>
        <label htmlFor="year" className="block text-gray-200">
          Year
        </label>
        <input
          type="number"
          id="year"
          value={year}
          onChange={(e: React.ChangeEvent<HTMLInputElement>) => setYear(e.target.value)}
          className="border border-gray-600 bg-gray-800 p-2 text-white placeholder-gray-400 focus:border-blue-500"
          required
        />
      </div>
      <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
        Add Movie
      </button>
    </form>
  );
};

export default AddMovieForm;
