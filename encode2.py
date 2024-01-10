import csv
import re

#filenames
unique_features_file = "feature-list.txt"  
data_file = "features_2.txt.csv"  
new_dataset_file = "encode_dataset.csv"  

my_unique_features = []

#read features
with open(unique_features_file, 'r') as features_file:
    # each line and add them to list
    for line in features_file.readlines():
        my_unique_features.append(line.strip())

#create a pattern to match my unique
feature_pattern = '|'.join(re.escape(feature) for feature in my_unique_features)

#data csv file 
with open(data_file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)  #read the first row

    #column "features" 
    features_index = header.index('features')

    #new dataset csv file
    with open(new_dataset_file, 'w', newline='') as output_file:
        csv_writer = csv.writer(output_file)

        #write the header row to new dataset
        header = ["md5hash", "label"] + my_unique_features
        csv_writer.writerow(header)

        #loop through each row in CSV
        for row in csv_reader:
            md5hash, label, feature_str = row[0], row[1], row[features_index]

            #regex to find all matches of my unique features 
            matches = re.findall(feature_pattern, feature_str)

            #create a list to hold feature values, starting with all zeros
            my_row_data = [0] * len(my_unique_features)

            #set the values to 1 features
            for match in matches:
                index = my_unique_features.index(match)
                my_row_data[index] = 1

            #write my row to my dataset CSV file
            csv_writer.writerow([md5hash, label] + my_row_data)

#created my new dataset
print(f"My new dataset is ready and saved as {new_dataset_file}!")
