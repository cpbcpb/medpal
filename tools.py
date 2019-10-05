from geopy.geocoders import Nominatim

def convert_lonlat_to_address(lonlat):

    geolocator = Nominatim(user_agent="specify_your_app_name_here")
    location = geolocator.reverse(lonlat)

    return location

def convert_address_to_lonlat(address):

    geolocator = Nominatim(user_agent="specify_your_app_name_here")
    location = geolocator.geocode(address)
    # print(location)
    return (location.latitude, location.longitude)


def convert_text_to_list(text):

    my_list = []

    my_list = text

    return my_list
