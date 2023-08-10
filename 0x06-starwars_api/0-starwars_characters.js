#!/usr/bin/node
/* Script that prints all characters of a Star Wars movie */

const request = require('request');
const urlApi = 'https://swapi-api.hbtn.io/api/films/';
const movieId = process.argv[2];

request(urlApi + movieId, (error, response, body) => {
  if (error) throw error;
  const characters = JSON.parse(body).characters;
  showNames(characters);
});

const showNames = (names, i = 0) => {
  if (i === names.length) return;
  request(names[i], (error, response, body) => {
    if (error) throw error;
    console.log(JSON.parse(body).name);
    showNames(names, i + 1);
  });
};
