import pandas as pd
import os
import argparse

# Load the Excel file
#input_file = "CVE_Report_October2024.xlsx"  # Replace with your actual file name
# Set up argument parser
parser = argparse.ArgumentParser(description="Process a CSV file.")
parser.add_argument("input_file", help="Path to the input CSV file")
args = parser.parse_args()

# Get the input file name and create the output file name
input_file = args.input_file

sheet_name = "Detailed-Report"  # Sheet to process

# Read the specific sheet from the Excel file
df = pd.read_excel(input_file, sheet_name=sheet_name)

# Define the values to remove from the "Device-Model" column
values_to_remove = ["ARRIS-XB6", "Comscope-XB7", "Sky-Hub4", "TXB6", "TXCBR"]

# Filter out rows with these values in the "Device-Model" column
filtered_df = df[~df["Device-Model"].isin(values_to_remove)]

# Save the remaining rows to a new CSV file
output_file = "Active-platforms.csv"
filtered_df.to_csv(output_file, index=False)

print(f"Filtered data has been saved to {output_file}")

## remove the -native from the Package name Column

input_file = "Active-platforms.csv"
output_file = "native-package-removed.csv"

# Load the CSV file
df = pd.read_csv(input_file)
strings_to_remove = ["-native", "linux"]

# Filter rows where 'Package-Name' does NOT contain the substrings
filtered_df = df[~df["Package-Name"].str.contains('|'.join(strings_to_remove), case=False, na=False)]

# Save the remaining rows to a new CSV file
filtered_df.to_csv(output_file, index=False)

print(f"Rows without '-native' have been saved to {output_file}")

## Remove the Patched and Ignored rows
# File names
input_file = "native-package-removed.csv"
output_file = "Unpatched-packages.csv"

# Load the CSV file
df = pd.read_csv(input_file)

# Define the values to remove
values_to_remove = ["Patched", "Ignored"]

# Filter rows where "CVE Status" does not contain the specified values
filtered_df = df[~df["CVE Status"].isin(values_to_remove)]

# Save the remaining rows to a new CSV file
filtered_df.to_csv(output_file, index=False)

print(f"Filtered data has been saved to {output_file}")

## Remove Anything that dont contain network and copy the contents to Unpatched-network-cves.csv
input_file = "Unpatched-packages.csv"
output_file= "Unpatched-network-cve.csv"
# Load the CSV file
df = pd.read_csv(input_file)

# Define the values to remove
values_to_remove = [" LOCAL", " PHYSICAL", " ADJACENT_NETWORK"]

# Filter rows where "Vector" does not contain the specified values
filtered_df = df[~df["Vector"].isin(values_to_remove)]

# Save the remaining rows to a new CSV file
filtered_df.to_csv(output_file, index=False)

print(f"Filtered data has been saved to {output_file}")


# File names
input_file = "Unpatched-network-cve.csv"
output_file = "Consolidated-Unpatched-network-cve.csv"

# Load the CSV file
df = pd.read_csv(input_file)

# Group by 'CVE ID' and consolidate 'Device-Model' values
consolidated_df = (
    df.groupby("CVE ID", as_index=False)
    .agg(lambda x: ', '.join(x.unique()) if x.name == "Device-Model" else x.iloc[0])
)

# Save the consolidated data to a new CSV file
consolidated_df.to_csv(output_file, index=False)

###########
# Input and output file names
##########
import pandas as pd

# Input and output file names
input_file = "Consolidated-Unpatched-network-cve.csv"
output_file = "Sorted-Consolidated-Unpatched-network-cve.csv"

# Load the CSV file
df = pd.read_csv(input_file)

# Remove the "Date" column
if "Date" in df.columns:
    df = df.drop(columns=["Date"])

# Sort the rows based on the "Package-Name" column
df = df.sort_values(by="Package-Name")

# Save the modified data to a new CSV file
df.to_csv(output_file, index=False)

input_file = "Sorted-Consolidated-Unpatched-network-cve.csv"
output_file1 = "Unpatched-cve-ge-5.csv"
output_file2 = "Unpatched-cve-le-5.csv"

# Load the CSV file
df = pd.read_csv(input_file)

# Filter rows where "CVSS V3 Score" is greater than or equal to 5.0
filtered_df = df[df["CVSS V3 Score"] >= 5.0]

# Save the filtered rows to a new CSV file
filtered_df.to_csv(output_file1, index=False)

# Filter rows where "CVSS V3 Score" is greater than or equal to 5.0
filtered_df = df[df["CVSS V3 Score"] < 5.0]

# Save the filtered rows to a new CSV file
filtered_df.to_csv(output_file2, index=False)

df = pd.read_csv(output_file1)
print(f"Updated data saved to {output_file1}", len(df)-1)


#print(f"Number of CVEs with CVSS Score more than 5.0", len(df) - 1)
df = pd.read_csv(output_file2)
print(f"Updated data saved to {output_file2}", len(df)-1)

#print(f"Number of CVEs with CVSS Score less than 5.0", len(df)-1)



