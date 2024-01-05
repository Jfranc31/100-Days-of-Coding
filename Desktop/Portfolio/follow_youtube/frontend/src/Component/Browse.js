// /src/Component/Browse.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useAnimeContext } from '../context/AnimeContext.js';
import AnimeCard from '../AnimeCard';

const Browse = () => {
    const { animeList, setAnimeList, isLoading, setIsLoading, selectedAnimeId, setSelectedAnimeId } = useAnimeContext();
    //const [showModal, setShowModal] = useState(false);
    const [selectedAnime, setSelectedAnime] = useState(null);
    const [showModal, setShowModal] = useState(false);
    const [searchInput, setSearchInput] = useState('');
    const [selectedGenres, setSelectedGenres] = useState([]);

    const [editedAnime, setEditedAnime] = useState(null);
    const [editedCurrentEpisode, setEditedCurrentEpisode] = useState(null);
    const [editedStatus, setEditedStatus] = useState(null);

    const availableGenres = ["Action", "Adventure", "Comedy", "Drama", "Fantasy", "Slice of Life", "Romance"];

    useEffect(() => {
      axios.get('http://localhost:8080/browse')
        .then(response => setAnimeList(response.data))
        .catch(error => console.error(error));
    }, []);
  
    const filteredAnime = Array.isArray(animeList) ? animeList.filter(anime => {
        const matchesSearch = anime.title.toLowerCase().includes(searchInput.toLowerCase());
        const matchesGenres =
          selectedGenres.length === 0 ||
          selectedGenres.every(genre =>
            anime.genres.map(g => g.genre.toLowerCase()).includes(genre.toLowerCase())
          );
      
        return matchesSearch && matchesGenres;
    }) : [];
  
    const handleTopRightButtonClick = (anime) => {
        setSelectedAnime(anime);
        setShowModal(true);
        setEditedAnime(anime);
        setEditedCurrentEpisode(anime.currentEpisode);
        setEditedStatus(anime.status);
    };

    const handleModalClose = () => {
        setShowModal(false);
        setSelectedAnime(null);
        setEditedAnime(null);
        setEditedCurrentEpisode(null);
        setEditedStatus(null);
      };
    
      const handleSaveChanges = async () => {
        try {
          // Make API request to update currentEpisode and status
          await axios.put(`http://localhost:8080/browse/${editedAnime._id}/status`, {
            currentEpisode: editedCurrentEpisode,
            status: editedStatus,
          });
    
          // Fetch the updated anime list
          const res = await axios.get('http://localhost:8080/browse');
          setAnimeList(res.data);
    
          // Close the modal after saving changes
          handleModalClose();
        } catch (error) {
          console.error('Failed to save changes:', error);
        }
      };

    const handleCardClick = (animeId) => {
        setSelectedAnimeId(animeId);
    };

    const handleGenreChange = (selectedGenre) => {
        setSelectedGenres(prevGenres => {
          if (!prevGenres.includes(selectedGenre)) {
            return [...prevGenres, selectedGenre];
          }
          return prevGenres;
        });
    };

    const handleRemoveGenre = (removedGenre) => {
        setSelectedGenres(prevGenres => prevGenres.filter(genre => genre !== removedGenre));
    };
  
    return (
        <div className="browse-container">
            <div className="filter-container">
                <div className="search-container">
                    <input
                        type="text"
                        placeholder="Search..."
                        value={searchInput}
                        onChange={(e) => setSearchInput(e.target.value)}
                    />
                </div>
                <div className="genre-filter-container">
                    <label>Genres:</label>
                    <select
                        value="" // Use an empty string as the default value
                        onChange={(e) => handleGenreChange(e.target.value)}
                    >
                        <option value="" disabled>Select a genre</option>
                        {availableGenres.map(genre => (
                            <option key={genre} value={genre}>{genre}</option>
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
                </div>
            </div>
            <ul className="anime-list">
                {filteredAnime.map(anime => (
                    <li key={anime._id}>
                        <AnimeCard
                            anime={anime}
                            setAnimeList={setAnimeList}
                            onCardClick={handleCardClick}
                            onTopRightButtonClick={handleTopRightButtonClick}
                        />
                    </li>
                ))}
            </ul>
            {/* Modal */}
            {showModal && (
                <div className="modal-overlay" onClick={handleModalClose}>
                    <div className="modal" onClick={(e) => e.stopPropagation()}>
                        {/* Display the anime information or any other details you want */}
                        <h2>{selectedAnime.title}</h2>
                        <p>Description: {selectedAnime.description}</p>
                        <p>Genres: {selectedAnime.genres.map((genreObj) => genreObj.genre).join(', ')}</p>
                        <label htmlFor="currentEpisode">Current Episode:</label>
                        <input
                            type="number"
                            id="currentEpisode"
                            value={editedCurrentEpisode}
                            onChange={(e) => setEditedCurrentEpisode(e.target.value)}
                        />
                        <label htmlFor="status">Status:</label>
                        <select
                            id="status"
                            value={editedStatus}
                            onChange={(e) => setEditedStatus(e.target.value)}
                        >
                            <option value="Planning">Planning</option>
                            <option value="Watching">Watching</option>
                            <option value="Completed">Completed</option>
                        </select>
                        <button onClick={handleSaveChanges}>Save Changes</button>
                        {/* Add more information as needed */}
                        <button onClick={handleModalClose}>Close</button>
                    </div>
                </div>
            )}
        </div>
    );
  };
  
  export default Browse;

