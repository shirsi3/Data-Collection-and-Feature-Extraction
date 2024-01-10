# Data-Collection-and-Feature-Extraction
# Lab: Data Processing and Feature Analysis in Python

This lab includes scripts that focus on data scanning, reading, and encoding, each playing a vital role in processing and analyzing data.

## 1. offical_scan.py - Data Scanning and Feature Extraction

- **Functionality:** 
  - Scans specified directories for files.
  - Extracts features from each file and computes their MD5 hashes.
  - Stores the extracted data in a CSV file with columns for MD5 hash, features, and file type (benign/malware).
- **Libraries Used:** subprocess, os, csv, hashlib

## 2. offical_read.py - Reading Data and Extracting Unique Features

- **Functionality:** 
  - Reads data from a CSV file.
  - Extracts and processes features from each row.
  - Identifies and stores unique features in a text file.
- **Libraries Used:** csv, re

## 3. encode2.py - Data Encoding and Processing

- **Functionality:** 
  - Reads a list of unique features from a text file.
  - Loads and processes data from a CSV file, encoding specific features.
  - Generates a new encoded dataset in CSV format.
- **Libraries Used:** csv, re

## General Workflow

1. **Data Collection:** 
   - `offical_scan.py` scans directories and collects data, forming an initial dataset.

2. **Feature Analysis:** 
   - `offical_read.py` processes this dataset to identify and isolate unique features.

3. **Data Encoding:** 
   - `encode2.py` uses these unique features to encode the dataset further for analysis or machine learning purposes.
