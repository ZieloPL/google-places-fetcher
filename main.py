from data_fetchers.google_places import GooglePlaces

# Sample query to fetch restaurant data from Google Places
fetcher = GooglePlaces()
fetcher.run("restaurants+in+Krakow")