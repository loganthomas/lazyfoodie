# `lazyfoodie`
A simple package for finding (and choosing) nearby restaurants.

## Requirements
- Python 3.7 or later.
- A Google Maps API key.


## API Keys
Each Google Maps Web Service request requires an API key or client ID. API keys
are generated in the 'Credentials' page of the 'APIs & Services' tab of [Google Cloud console](https://console.cloud.google.com/apis/credentials).

For even more information on getting started with Google Maps Platform and generating/restricting an API key, see [Get Started with Google Maps Platform](https://developers.google.com/maps/gmp-get-started) in our docs.

**Important:** This key should be kept secret on your server. For *developers*, it is assumed that you have a `.env` file at the root level of this repo (i.e. `lazyfoodie/.env`) configured with a `gmaps_apikey` variable. The [`python-dotenv`](https://github.com/theskumar/python-dotenv) is used to read this `.env` file and create environment variables from the key-value pairs therein. If you do not have a `.env` file, then you will asked to securely provide your API key via a prompt in the command line.
