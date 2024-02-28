# - Enter an IP address and find the country that IP is registered in.   

from geopy.geocoders import Nominatim

def ip_to_country(ip_address):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(ip_address)
    if location:
        return location.address.split(",")[-1].strip()
    else:
        return "Country not found for the given IP."

# Example usage
print(ip_to_country("8.8.8.8"))