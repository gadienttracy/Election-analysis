# Election-analysis
## Purpose: This project evaluates the votes for three candidates in a Colorado election.  
## Project Overview
A CO Board of Elections employee has provided the following tasks to complete the election audit of a recent local congressional election
1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.
6. Calculate the number of votes cast in three counties: Jefferson, Denver, Arapahoe
7. Calculate the percentage of the total votes each county contributed
8. Determine the county with the largest turnout

## Resources
-Data Source: election_results.csv
-Software: Python, Visual Studio Code

## Election-Audit Results
The analysis of the election shows that:
### There were 369,711 votes cast in the election
### The candidates were:
    -Charles Casper Stockham
    -Diana DeGette
    -Raymon Anthony Doane
### The candidate results were:
    -Charles Casper Stockham: received 23.05 % (85,213)
    -Diana DeGette: received 73.81 % (272,892)
    -Raymon Anthony Doane: received 3.14 % (11,606)
### The winner of the election was:
   Winner: Diana DeGette 
   received 272,892 votes
   Winning Percentage: 73.81%
### County Results
    Jefferson: 10.5% (38,855)
    Denver: 82.8% (306,055)
    Arapahoe: 6.7% (24,801)
### Largest Voter Turnout
    Denver had the largest voter count with 306,055 votes.
    
  ![election output](https://user-images.githubusercontent.com/91269696/149407731-05e20be2-a4fe-4371-9cdb-7cc9b6789df9.PNG)
 
## Election-Audit Summary
This script can be used for nearly any election in the future.  If you would like to use this script for future elections there may need to be a few modifications to the script.
The first is to ensure the candidate's name and the name of the county are in the same rows listed in the code (row 1/2 in the code, column 2/3 in the csv file).  The script may need to be modified if they are in a different location than this CSV file.  A second consideration would be telling the code what to do if there were to be a tie in the voter count or the winning percentage, to ensure that both candidates or counties are printed as the winner.
