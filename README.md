# SteelHacks 2020 - Füd Network

## Install with Docker
1. Install Docker with `docker-compose` [Check here](https://docs.docker.com/compose/install/)
2. For the first time use `docker-compose build` in the root directory of this repo
3. To run the dev server just type `docker-compose up` into the terminal

## Dev Overview
* `app` - the folder that has all of the code for the server
  * `static` - static assets such as images and css
  * `templates` - Templates that generate the html views
  * `data.py` - Classes and functions relating to our recipe data
  * `main.py` - This is the file that has the code for our views
* `download_data.py` - code to download data from spoonacular with a valid api key
