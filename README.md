# Election_Analysis

## Project Overview

A Colorado Board of Elections requires to complete the election audit of a recent local congressional election. To determine the winner of the election, this project was conducted to count the total number of votes and calculate the votes for each candidate and each county. A complete list of candidates and counties together with each vote count and percentage have been prepared also, using python 3 retrieving data from the csv data file. The final analysis results reveal the details of the winning candidate as well as the county with the highest turnout.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code-insiders, 1.65.0

## Election-Audit Results
The analysis of the election show that:
- There were 369,711 votes cast in this congressional election in total.
- The county vote results were:
    - Jefferson: 10.5% of the votes and 38,855 voter turnout.
    - Denver: 82.8% of the votes and 306,055 voter turnout.
    - Arapahoe: 6.7% of the votes and 24,801 voter turnout.
- The analysis indicates that Denver was the County with largest voter turnout in a total of 306,055.
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the votes and 85,213 of votes.
    - Diana DeGette received 73.8% of the votes  and 272,892 of votes.
    - Raymon Anthony Doane received 3.1% of the votes and 11,606 of votes.
- The winner is Diana DeGette, receiving 272,892 vote counts, which is 73.8% of the total votes.

## Election-Audit Summary
This script is able to retrieve data from csv files and conduct election analysis on the data. Further, specific modifications can be made to apply the script on any other election. 
- 1. We may define a variable to store the file name which needs to be analyzed. The function of input() can be used to assign the file name to the subject variable. Any election data is able to be analyzed by this script.
    ![inputcsv_1](https://github.com/hankai26/Election_Analysis/blob/main/Resources/inputcsv_1.png)
    ![inputcsv_2](https://github.com/hankai26/Election_Analysis/blob/main/Resources/inputcsv_2.png)

- 2. If the other election data file is located in another folder, the path should be also modified in the script.
    ![csvfolder_1](https://github.com/hankai26/Election_Analysis/blob/main/Resources/csvfolder_1.png)

    ![csvfolder_2](https://github.com/hankai26/Election_Analysis/blob/main/Resources/csvfolder_2.png)

- 3. Similarly, the path of the file where to save the election result should be also revised allowing the user to input.
    ![savefile_1](https://github.com/hankai26/Election_Analysis/blob/main/Resources/savefile_1.png)

    ![savefile_2](https://github.com/hankai26/Election_Analysis/blob/main/Resources/savefile_2.png)

- 4. Reviewing the print out information, we could also store the election type or location to a variable. The user should then be able to select the election location via input input() function, e.g. Federal, City, Local, etc.
    ![area_1](https://github.com/hankai26/Election_Analysis/blob/main/Resources/area_1.png)
    ![area_2](https://github.com/hankai26/Election_Analysis/blob/main/Resources/area_2.png)
    ![area_3](https://github.com/hankai26/Election_Analysis/blob/main/Resources/area_3.png)

Including the modification options, this script should be able to apply to other election analysis allowing the user to select.