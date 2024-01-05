// src/context/AnimeContext.js
import React, { createContext, useContext, useState, useEffect } from 'react';

export const AnimeContext = createContext();

export const AnimeProvider = ({ children }) => {
  const [animeList, setAnimeList] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [selectedAnimeId, setSelectedAnimeId] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        setIsLoading(true);

        // Fetch data from your API
        const response = await fetch('http://localhost:8080/browse', {
          credentials: 'include',
        });

        const data = await response.json();

        // Update the animeList in the context
        setAnimeList(data);

        setIsLoading(false);
      } catch (error) {
        console.error('Error fetching anime list:', error);
        setIsLoading(false);
      }
    };

    fetchData();
  }, [setAnimeList, setIsLoading]);

  return (
    <AnimeContext.Provider value={{
      animeList,
      setAnimeList,
      isLoading,
      setIsLoading,
      selectedAnimeId,
      setSelectedAnimeId
    }}>
      {children}
    </AnimeContext.Provider>
  );
};

export const useAnimeContext = () => {
  const context = useContext(AnimeContext);

  if (!context) {
    throw new Error('useAnimeContext must be used within an AnimeProvider');
  }

  return context;
};
