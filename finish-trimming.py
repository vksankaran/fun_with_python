## Remove the / and the trailing characers
import pandas as pd
## Remove certain words in a column in an xls
import pandas as pd
import argparse
import os


# Set up argument parser
parser = argparse.ArgumentParser(description="Process a CSV file.")
parser.add_argument("input_file", help="Path to the input CSV file")
args = parser.parse_args()

# Get the input file name and create the output file name
actual_file = args.input_file 
input_file = args.input_file + "_trimmed.csv"

print("Input File is -- > ", input_file)
output_file = os.path.splitext(actual_file)[0] + "_final.csv"
print("Output File is --> ", output_file)

# Load your CSV file
df = pd.read_csv(input_file)

# Replace 'column_name' with the actual name of your column
df['File'] = df['File'].str.replace(r'/.*', '', regex=True)

# Save the modified data to a new CSV file
df.to_csv(output_file, index=False)

print("Trailing text after the last '/' has been removed successfully.")