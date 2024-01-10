import csv
import re

# File names
input_file = "features_2.txt.csv"
output_file = "feature-list.txt"

# Store unique features
unique_features = set()

try:
    # Open CSV file
    with open(input_file, 'r', newline='') as csvfile:
        # Create a CSV reader
        csv_reader = csv.DictReader(csvfile)

        # Loop through each row
        for row in csv_reader:
            # Extract features from column and remove text within brackets
            features = row["features"].split(",")
            cleaned_features = [re.sub(r'\([^)]*\)', '', feature).strip() for feature in features]

            # Add cleaned features to the set
            unique_features.update(cleaned_features)

    # Sort features alphabetically
    sorted_features = sorted(unique_features)

    # Output to text file
    with open(output_file, 'w') as textfile:
        for feature in sorted_features:
            textfile.write(feature.strip() + '\n')

    print(f"Done writing to {output_file}.")
except FileNotFoundError:
    print(f"File {input_file} not found.")
