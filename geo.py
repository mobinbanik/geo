import reverse_geocoder as rg

def get_country(lat, lon):
    coordinates = (lat, lon)
    results = rg.search(coordinates)
    return results[0]['cc']

if __name__ == '__main__':
    latitude = 40.892370
    longitude = 22.058916
    country = get_country(latitude, longitude)
    print(f'The country for coordinates ({latitude}, {longitude}) is {country}')
