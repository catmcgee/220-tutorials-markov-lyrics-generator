# 220 Tutorials - Markov Lyrics Generator
A Python script that takes lyrics from your favourite artist and generates their own version using a Markov chain!

## Prerequesities

Before running the code or beginning the tutorial, ensure you have

* Python 3 - https://www.python.org/downloads/
* re 
* urllib
* markovify

`pip install r && pip install urllib && pip install markovify`

## How it works

Our code scrapes the HTML from an artist's page on AZLyrics and gets all the links to the invididual songs. Then it scrapes the HTML of the song pages, finds the section where the lyrics are, and puts these into a string to generate a model for Markovify. The Markovify library uses this string to generate its own lyrics

## Markov Chains

A Markov Chain is a prediction algorithm, predicting what comes next only based on what came before it. In our case, the next word in the lyrics is 'predicted' or generated based on the previous word and how this compares to the original lyrics of the artist - this is why we end up with some pretty funny results!
