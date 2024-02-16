#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const movieEndpoint = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

function sendRequest (characterList, index) {
  if (characterList.length === index) {
    return;
  }

  request(characterList[index], (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
      sendRequest(characterList, index + 1);
    }
  });
}

request(movieEndpoint, (error, response, body) => {
    if (error) {
	console.error(error);
    } else {
	if (response.statusCode === 200) {
	    const characterList = JSON.parse(body).characters;

	    sendRequest(characterList, 0);
	} else {
	    console.error(`Error retrieving film details. Status code: ${response.statusCode}`);
	}
    }
});
