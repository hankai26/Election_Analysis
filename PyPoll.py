# The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.

import csv
import os
#dir(csv)

# Assign a variable for the file to load and the path.
    # file_to_load = 'Resources/election_results.csv'
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    #election_data = open(file_to_load, "r")

# To do: perform analysis: read and analyze the data.
# Read the file object with the reader function.
    file_reader = csv.reader(election_data)

# Print each row in the CSV file.
    #for row in file_reader:    print(row)
#Print the header row.
    headers = next(file_reader)
    print(headers)


# Close the file.
election_data.close()



# Using the open() function with the "w" mode we will write data to the file.
# Use the open statement to open the file as a text file.
# outfile = open(file_to_save, "w")
    #with open(file_to_save, "w") as outfile:

    # Write some data to the file.
    #outfile.write("Counties in the Election\n")
    #outfile.write("---------------------------\n")
    #outfile.write("Denver\n")
    #outfile.write("Jefferson")

# Close the file
#outfile.close()
