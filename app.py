import pandas as pd
from bs4 import BeautifulSoup
import os

# Read the content of the txt file
file_name = "scion111423.txt"
with open(file_name, "r") as file:
    data = file.read()


# Parse the XML content
soup = BeautifulSoup(data, "xml")

# Extract the desired information
info_tables = soup.find_all("infoTable")

# Create lists to store the extracted data
issuers = []
values = []
sole_votes = []
shared_votes = []
none_votes = []

# Iterate over each infoTable and extract the relevant data
for table in info_tables:
    issuers.append(table.find("nameOfIssuer").text)
    values.append(table.find("value").text)
    sole_votes.append(table.find("Sole").text)
    shared_votes.append(table.find("Shared").text)
    none_votes.append(table.find("None").text)

# Create a pandas DataFrame
df = pd.DataFrame({
    "Name of Issuer": issuers,
    "Value": values,
    "Sole Votes": sole_votes,
    "Shared Votes": shared_votes,
    "None Votes": none_votes
})

# Get the base name of the input file
base_name = os.path.splitext(file_name)[0]

# Write the DataFrame to an Excel file
output_file = f"{base_name}.xlsx"
df.to_excel(output_file, index=False)

print("Excel file generated successfully.")
