// src/components/AddAnime.js

import React, { useState } from "react";
import axios from 'axios';

export default function AddAnime() {
    
  // Initialize state for form data
  const [formData, setFormData] = useState({
    title: "",
    genres: [],
    episodes: 0,
    currentEpisode: 0,
    image: "",
    description: "",
    characters: [],
    status: "Planning"
    // Add more fields as needed
  });
  console.log("Anime Data: ", formData.genres);

  const [isLoading, setIsLoading] = useState(false);
  const [formErrors, setFormErrors] = useState({});
  const [selectedGenres, setSelectedGenres] = useState([]);
  const availableGenres = ["Action", "Adventure", "Comedy", "Drama", "Fantasy", "Slice of Life", "Romance"];

  const handleChange = (e)=>{
    const { name , value} = e.target;
    setFormData((preve)=>{
        return{
            ...preve,
            [name] : value
        }
    })
}

  const handleStatusChange = (status) => {
    setFormData((prevData) => ({
      ...prevData,
      status,
    }));
  };

  const handleGenreChange = (selectedGenre) => {
    setSelectedGenres((prevGenres) => {
      if (!prevGenres.includes(selectedGenre)) {
        return [...prevGenres, selectedGenre];
      }
      return prevGenres;
    });

    // Set the selected genres directly in the formData
    setFormData((prevData) => ({
      ...prevData,
      genres: [...prevData.genres, selectedGenre],
    }));
  };

  const handleRemoveGenre = (removedGenre) => {
    setSelectedGenres((prevGenres) =>
      prevGenres.filter((genre) => genre !== removedGenre)
    );
  
    // Update genres in formData
    setFormData((prevData) => ({
      ...prevData,
      genres: prevData.genres.filter((genre) => genre !== removedGenre),
    }));
  };

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();

    // Basic form validation
    const errors = {};
    if (!formData.title.trim()) {
      errors.title = "Title is required";
    }
    if (formData.genres.length === 0) {
      errors.genres = "At least one genre is required";
    }

    setFormErrors(errors);

    if (Object.keys(errors).length > 0) {
      // There are validation errors, do not submit the form
      return;
    }

    try {
      setIsLoading(true);
      console.log('Current formData:', formData);

      const res = await axios.post('http://localhost:3000/addanime', formData);
      console.log(res);
      console.log('Request details in addanime:', {
        url: '/api/animes',
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });
  
      if (res.status === 201) {
        // Redirect or perform additional actions on success
        console.log('Anime added successfully!');
        // Clear the form after successful submission
        setFormData({
          title: "",
          genres: [],
          episodes: 0,
          currentEpisode: 0,
          image: "",
          description: "",
          characters: [],
          status: "Planning"
        });
        // You might want to redirect the user to a different page on success
      } else {
        // Handle errors from the backend
        console.error('Failed to add anime:', res.data);
      }
    } catch (error) {
      // Handle network or other errors
      console.error('Error during anime addition:', error);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      {/* Title input */}
      <div>
        <label htmlFor="title">Title:</label>
        <input
          type="text"
          id="title"
          name="title"
          value={formData.title}
          onChange={handleChange}
          required
        />
        {formErrors.title && <div className="error-message">{formErrors.title}</div>}
      </div>

      {/* Genres input */}
      <div>
        <label htmlFor="genres">Genres:</label>
        <select
          id="genres"
          name="genres"
          multiple
          value={selectedGenres}
          onChange={(e) => handleGenreChange((e.target.value))}
          required
        >
          {availableGenres.map((genre) => (
            <option key={genre} value={genre}>
              {genre}
            </option>
          ))}
        </select>
        <div className="selected-genres">
            {selectedGenres.map(genre => (
              <div key={genre} className="selected-genre">
                {genre}
                <button onClick={() => handleRemoveGenre(genre)}>x</button>
              </div>
            ))}
          </div>
        {formErrors.genres && <div className="error-message">{formErrors.genres}</div>}
      </div>

      {/* Episodes input */}
      <div>
        <label htmlFor="episodes">Episodes:</label>
        <input
          type="number"
          id="episodes"
          name="episodes"
          value={formData.episodes}
          onChange={handleChange}
          required
        />
      </div>

      {/* Current Episodes input */}
      <div>
        <label htmlFor="currentEpisode">Current Episodes:</label>
        <input
          type="number"
          id="currentEpisode"
          name="currentEpisode"
          value={formData.currentEpisode}
          onChange={handleChange}
          required
        />
      </div>

      {/* Image input */}
      <div>
        <label htmlFor="image">Image URL:</label>
        <input
          type="text"
          id="image"
          name="image"
          value={formData.image}
          onChange={handleChange}
        />
      </div>

      {/* Description input */}
      <div>
        <label htmlFor="description">Description:</label>
        <input
          type="text"
          id="description"
          name="description"
          value={formData.description}
          onChange={handleChange}
        />
      </div>

      {/* Characters input */}
      <div>
        <label htmlFor="characters">Characters:</label>
        <input
          type="text"
          id="characters"
          name="characters"
          value={formData.characters}
          onChange={handleChange}
        />
      </div>

      {/* Status input (dropdown or radio buttons) */}
      <div>
        <label htmlFor="status">Status:</label>
        <select
          id="status"
          name="status"
          value={formData.status}
          onChange={(e) => handleStatusChange(e.target.value)}
        >
          <option value="Planning">Planning</option>
          <option value="Watching">Watching</option>
          <option value="Completed">Completed</option>
        </select>
      </div>

      {/* Submit button */}
      <div>
        <button className="btn" type="submit" disabled={isLoading}>Add Anime</button>
      </div>
    </form>
  );
}