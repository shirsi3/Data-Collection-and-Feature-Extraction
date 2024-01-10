import subprocess
import os
import csv
import hashlib

# chapter 8 folders 
folders_to_scan = [
    "/home/shirsi/lab2/malware_lab2/malware_data_science/ch8/data/benignware",
    "/home/shirsi/lab2/malware_lab2/malware_data_science/ch8/data/malware",
]

#open csv file named
with open('features.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)

    #column names
    csv_writer.writerow(["md5", "features", "type"])

    # Loop folders
    for folder in folders_to_scan:
        # Loop files
        for file in os.listdir(folder):
            #current path
            current_path = os.path.join(folder, file)

            try:
                # calculate MD5 hash of the file
                md5_hash = hashlib.md5()
                with open(current_path, "rb") as f:
                    for chunk in iter(lambda: f.read(4096), b""):
                        md5_hash.update(chunk)

                # capa command on folder, file
                result = subprocess.run(["./capa", "-v", current_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

                if result.returncode != 0:
                    # skip files with errors
                    print(f"Skipped {current_path}: {result.stderr}")
                    continue

                # extract features
                features = []
                lines = result.stdout.split("\n\n")
                for line in lines[1:]:
                    features.append(line.split("\n")[0])

                # type
                type = "maliciosu" if "malware" in folder else "benignware"

                # putting output to the CSV file
                csv_writer.writerow([md5_hash.hexdigest(), ",".join(features), type])

                print(f"done {current_path}")
            except Exception as e:
                # Handle errors during processing
                print(f"error {current_path}: {str(e)}")
                continue

print("Scan completed")
