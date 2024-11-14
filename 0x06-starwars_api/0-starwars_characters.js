#!/usr/bin/node
const util = require('util');
const request = util.promisify(require('request'));
const filmID = process.argv[2];

async function starwarsCharacters(filmId) {
  const endpoint = `https://swapi-api.hbtn.io/api/films/${filmId}`;

  try {
    // Fetch the film details
    const response = await request(endpoint);
    const film = JSON.parse(response.body);
    const characters = film.characters;

    // Fetch and print each character's name in order
    for (const url of characters) {
      const characterResponse = await request(url);
      const character = JSON.parse(characterResponse.body);
      console.log(character.name);
    }
  } catch (error) {
    console.error('Error fetching data:', error.message);
  }
}

starwarsCharacters(filmID);
