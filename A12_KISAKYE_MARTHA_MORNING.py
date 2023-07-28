#KISAKYE MARTHA JANEPHER
#21/U/10006/EVE
#210071006

# Exercise
# extract all bird species from this website url https://xeno-canto.org
# and generate the csv file or the JSON file format  for te bird species family and more
# extract all bird songs from this website https://xeno-canto.org
# use this API to get data. the endpoint for the website is at https://https://xeno-canto.org/api/2/recordings.

from bs4 import BeautifulSoup
import requests
import json

def bird_species(query):
     url = f"https://xeno-canto.org/api/2/recordings?query={query}"
     response = requests.get(url)

     if response.status_code == 200:
         data = response.json()
         species_list = []

         for recording in data['recordings']:
             species_name = recording['en']
             family_name = f"{recording['gen']} {recording['sp']}"
             locality = recording['loc']
             country = recording['cnt']

             # Append the information to the list in the form of a dictionary.
             species_list.append({
                 'species_name': species_name,
                 'family_name': family_name,
                 'locality': locality,
                 'country': country,
             })

         return species_list
     else:
         print(f"Failed to fetch data. Status code: {response.status_code}")
         return []

if __name__ == "__main__":
    # Get data for bird species in Uganda
    query = "cnt:Uganda"
    bird_species_data = bird_species(query)

    if bird_species_data:
        json_filename = "bird_species.json"
        with open(json_filename, 'w') as json_file:
            json.dump(bird_species_data, json_file, indent=4)
        print(f"Data saved to {json_filename}.")
    else:
        print("No data retrieved.")


# 2. Extract all the bird songs from the website.

def get_all_bird_songs():
    base_url = "https://xeno-canto.org/api/2/recordings"
    page = 1
    bird_songs = []

    while True:
        url = f"{base_url}?query=X&page={page}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            total_recordings = int(data['numRecordings'])
            num_pages = int(data['numPages'])

            for recording in data['recordings']:
                bird_songs.append({
                    'song_name': recording['en'],
                    'bird_family': f"{recording['gen']} {recording['sp']}",
                    'locality': recording['loc'],
                    'country': recording['cnt'],
                    'audio_url': recording['file']
                })

            if len(bird_songs) >= total_recordings:
                break

            page += 1
        else:
            print(f"Failed to fetch data for page {page}. Status code: {response.status_code}")
            break

    return bird_songs

if __name__ == "__main__":
    bird_songs = get_all_bird_songs()

    if bird_songs:
        json_filename = "bird_songs.json"
        with open(json_filename, 'w') as json_file:
            json.dump(bird_songs, json_file, indent=4)
        print(f"Data saved to {json_filename}.")
    else:
        print("No data retrieved.")

