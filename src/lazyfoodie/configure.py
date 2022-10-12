import getpass
import os
from pathlib import Path

import geocoder
import googlemaps
from dotenv import load_dotenv

HERE = Path(__file__).resolve()
ROOT = HERE.parents[2].resolve()


class Configuration:
    def __init__(self, config_path=ROOT.joinpath(".env")):

        # Setup google maps API key
        if Path(config_path).exists():
            print(f"Setting up credentials from {config_path}")
            self.config_path = config_path
            load_dotenv(self.config_path)
        else:
            print(f"Could not find {config_path}. Please provide credentials instead")
            self.config_path = None
            apikey = getpass.getpass(prompt="Google Maps API Key: ")
            os.environ["gmaps_apikey"] = apikey

        # Create access point for googlemaps
        self.gmaps = googlemaps.Client(os.getenv("gmaps_apikey"))

    def get_current_location_geocoder(self):
        """Lat Long"""
        geoloc = geocoder.ip("me")
        print(geoloc.latlng)
        print(geoloc.city)
        return geoloc

    def get_current_location_googlemaps(self):
        """Lat Long"""
        geoloc = self.gmaps.geolocate()
        print(geoloc)
        return geoloc

    def query_location_geocoder(self, addr_string):
        """
        Available attributes:
        - geojson: similar to googlemaps package output
        - json: similar to googlemaps package output
        - wkt
        - osm
        - latlng
        - housenumber
        - postal
        - street
        - street_long
        - city
        - state
        - state_long
        - country
        - country_long
        - bbox: bounding box (see also geojson['bbox'])
        """
        geoloc = geocoder.google(addr_string, key=os.getenv("gmaps_apikey"))
        print(f"bounding box: {geoloc.bbox}")
        print(f"osm: {geoloc.osm}")
        return geoloc

    def query_location_googlemaps(self, addr_string):
        """
        Available attributes:
        - address_components
        - formatted_address
        - geometry
        - place_id
        - types
        """
        response = self.gmaps.geocode(addr_string)
        geoloc = response[0]
        print(f"geometry: {geoloc.get('geometry')}")
        return geoloc


if __name__ == "__main__":
    AUSTIN_CAPITAL_ADDR = "100 Congress Ave., Austin, TX"
    WHITEHOUSE_ADDR = "1600 Pennsylvania Avenue NW, Washington, DC"

    c = Configuration()

    print("{:-^30}".format(" geoencoder "))
    c.get_current_location_geocoder()
    print("{:-^30}".format(" googlemaps "))
    c.get_current_location_googlemaps()
    print()

    print("{:-^30}".format(" geoencoder "))
    c.query_location_geocoder(AUSTIN_CAPITAL_ADDR)
    print("{:-^30}".format(" googlemaps "))
    c.query_location_googlemaps(AUSTIN_CAPITAL_ADDR)
    print()

    print("{:-^30}".format(" geoencoder "))
    c.query_location_geocoder(WHITEHOUSE_ADDR)
    print("{:-^30}".format(" googlemaps "))
    c.query_location_googlemaps(WHITEHOUSE_ADDR)
    print()
