# Election_Analysis

## Overview of the Election Audit

Tom, an employee of the Colorado Board of Elections, has been tasked with developing a python script to analyze voting data from a congressional voting district. The script should be able to tally the total vote count, votes for each candidate and votes by county. The script should break down vote percentage by county and by candidate. It should also determine the winner of the election and which county had the highest voter turnout. All of this data should be output to a text file. If this script is successful then it could be deployed to audit other elections.

## Election Audit Results

* There were 368,711 votes cast in this election

* County votes broke down as follows:
    Jefferson: 10.5% (38,855)
    Denver: 82.8% (306,055)
    Arapahoe: 6.7% (24,801)

* The county with the largest voter turnout was Denver

* The candidate votes broke down as follows:

    Charles Casper Stockham: 23.0% (85,213)
    Diana DeGette: 73.8% (272,892)
    Raymon Anthony Doane: 3.1% (11,606)

* Diana DeGette won the election with 73.8% of the vote and 272,892 votes


This data was generated and printed out in a text file by the script as seen below.

![text_file_output.png](https://github.com/mcwatts88/Election-Analysis/blob/main/Resources/text_file_output.png)

## Election Audit Summary

This script utilizes the csv module of python to read election data stored in a csv file. This script can be modified to run for any election as long as the county and candidate columns are specified in the code correctly. If a local election is being analyzed the the county specific section of code could be changed to polling location as all the votes would be in the same county. If the election was statewide you could include district data as well and have it counted in the same for loop.