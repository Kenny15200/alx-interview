#!/usr/bin/node
const request = require('request');
const movieID = process.argv[2];

// Check if movieID is provided
if (!movieID) {
  console.error('Usage: ./0-starwars_characters.js <movieID>');
  process.exit(1);
}

// Validate movieID
if (isNaN(movieID) || parseInt(movieID) < 1) {
  console.error('Movie ID must be a positive integer');
  process.exit(1);
}

// URL for the Star Wars API films endpoint
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

// Make a GET request to the API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  // Parse the JSON response
  const data = JSON.parse(body);

  // Extract the characters array from the response
  const characters = data.characters;

  // Print the character names
  characters.forEach(characterUrl => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        return;
      }
      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});

