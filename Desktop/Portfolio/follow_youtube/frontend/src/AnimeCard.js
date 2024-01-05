// src/AnimeCard.js

import React, { useState } from 'react';
import axios from 'axios';
import { useAnimeContext } from './context/AnimeContext.js';


function AnimeCard({ anime, onTopRightButtonClick }) {
    const { setAnimeList } = useAnimeContext();
    const [isHovered, setIsHovered] = useState(false);
  
    const setCurrentEpisode = async (newEpisode) => {
      console.log('Updating current episode:', newEpisode);
      try {
        // Update the status in MongoDB
        await axios.put(`http://localhost:8080/browse/${anime._id}/status`, {
          currentEpisode: newEpisode,
        });
  
        // Fetch the updated anime list
        const res = await axios.get('http://localhost:8080/browse');
        console.log("res data: ", res);
  
        // Update the state with the new anime list
        setAnimeList(res.data);
      } catch (error) {
        console.error('Failed to update status:', error);
      }
    };
  
    const handleIncrementEpisode = async () => {
        // Update the current episode by 1
        console.log('Incrementing episode...');
        const newCurrentEpisode = anime.currentEpisode + 1;
        console.log('New episode:', newCurrentEpisode);
    
        // Check the anime status and update accordingly
        if (anime.status === 'Planning') {
          // If the anime is in planning, change the status to Watching
          await setCurrentEpisode(newCurrentEpisode);
        } else if (anime.status === 'Watching') {
          // If the anime is already watching, just increment the episode
          await setCurrentEpisode(newCurrentEpisode);
        } else if (anime.status === 'Completed' && newCurrentEpisode === anime.episodes) {
          // If the anime is completed and the episode is equal to total episodes, change status to Completed
          await setCurrentEpisode(newCurrentEpisode);
        }
    
        // Add any additional logic you need here
      };
  
      return (
        <div
          className={`anime-card ${isHovered ? 'hovered' : ''}`}
          onMouseEnter={() => setIsHovered(true)}
          onMouseLeave={() => setIsHovered(false)}
        >
          <div className="img-container">
            <img src={anime.image} alt={anime.title} />
            <div className="title-and-progress">
            <div className='anime-title'>{anime.title}</div>
            <div label="Progress" className="progress">
                {anime.currentEpisode}/{anime.episodes}
                {isHovered && (
                <span className="plus-progress" onClick={handleIncrementEpisode}>
                    +
                </span>
                )}
            </div>
            </div>
          </div>
          {isHovered && (
            <>
              <button className="top-right-button" onClick={() => onTopRightButtonClick(anime)}>
                •••
              </button>
            </>
          )}
        </div>
      );
  }
  
  export default AnimeCard;