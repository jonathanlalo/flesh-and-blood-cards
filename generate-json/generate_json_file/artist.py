import csv
import json
from pathlib import Path

def generate_json_file():
    print("Generating artist.json from artist.csv...")

    artist_array = []

    csvPath = Path(__file__).parent / "../../csvs/artist.csv"
    jsonPath = Path(__file__).parent / "../../json/artist.json"

    with csvPath.open(newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t', quotechar='"')
        next(reader)

        for row in reader:
            artist_object = {}

            artist_object['name'] = row[0]

            artist_array.append(artist_object)

    json_object = json.dumps(artist_array, indent=4)

    with jsonPath.open('w', newline='\n') as outfile:
        outfile.write(json_object)

    print("Successfully generated artist.json\n")