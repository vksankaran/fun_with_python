## Remove certain words in a column in an xls
import pandas as pd
import argparse
import os


# Set up argument parser
parser = argparse.ArgumentParser(description="Process a CSV file.")
parser.add_argument("input_file", help="Path to the input CSV file")
args = parser.parse_args()

# Get the input file name and create the output file name
input_file = args.input_file
output_file = os.path.splitext(input_file)[0] + "_trimmed.csv"

# Load your CSV file
df = pd.read_csv(input_file)
# Replace 'column_name' with the name of your column
string_to_remove='/mnt/jenkins/workspace/TECHNICOLORXB8-Yocto-Nightly/build-tchxb8/tmp/work/cortexa15hf-neon-rdk-linux-gnueabi/'
df['File'] = df['File'].str.replace(r'^.*-gnueabi/', '', regex=True)

# Save the modified data to a new CSV file
df.to_csv(output_file, index=False)

print("The prefix has been removed successfully.")