import json
import csv

# Function to convert JSON to CSV
def convert_json_to_csv(json_file_path, csv_file_path):
    """
    Convert a JSON file containing FeatureCollection data to a CSV file.

    Parameters:
    json_file_path (str): Path to the input JSON file.
    csv_file_path (str): Path to the output CSV file.
    """
    try:
        # Open the JSON file
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        # Open the CSV file for writing
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')

            # Write the CSV header
            csv_writer.writerow(["Name", "Latitude", "Longitude"])

            # Write data rows
            for feature in data["features"]:
                name = feature["properties"].get("name", "")
                longitude, latitude = feature["geometry"]["coordinates"]

                csv_writer.writerow([name, latitude, longitude])

        print(f"Successfully converted JSON to CSV. Output saved to: {csv_file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Paths to your files
input_json_path = "mapstr.geojson"  # Replace with your JSON file path
output_csv_path = "outputMap.csv"  # Replace with your desired CSV output path

# Run the conversion
convert_json_to_csv(input_json_path, output_csv_path)
