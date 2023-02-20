import os
import csv
import json

# Set the path to the folder containing the CSV files
folder_path = "/Users/pearl/Documents/GitHub/Table-Fact-Checking/data/all_csv"

# Create a new path to save JSON files
new_dir = '/Users/pearl/Documents/GitHub/Table-Fact-Checking/data/all_json'
os.makedirs(new_dir, exist_ok=True)

# Get a list of all the CSV files in the folder
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# Loop through the CSV files in order and read them into Pandas dataframes
for csv_file in sorted(csv_files):

    csv_file_path = os.path.join(folder_path, csv_file)
    # df = pd.read_csv(csv_path)
    json_file = csv_file.split(".")[0] + ".json"
    json_file_path = os.path.join(new_dir, json_file)

    # Set the path to the CSV file

    # Open the CSV file for reading
    with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
        # Use csv.DictReader to parse the CSV file into a list of dictionaries
        csv_reader = csv.DictReader(csv_file, delimiter='#')

        # Initialize an empty dictionary to hold the converted data
        data_dict = {}

        # Loop through the rows of the CSV file and convert them to a dictionary
        for row in csv_reader:
            # print("reading",row)
            for key, value in row.items():
                if key not in data_dict:
                    data_dict[key] = [value]
                else:
                    data_dict[key].append(value)

    # Convert the data dictionary to JSON format
    with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
        json.dump(data_dict, jsonfile, ensure_ascii=False)

    # Print the JSON data to the console
