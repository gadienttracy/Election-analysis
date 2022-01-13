#Add dependencies
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

#Create a filename variable to a direct or indirect path to the file.
file_to_save=os.path.join("analysis", "election_analysis.txt")

#initializa a total vote counter
total_votes=0
candidate_options = []
candidate_votes={}
winning_candidate=""
winning_count=0
winning_percentage=0
#Using the with statement open the file and read the file
with open(file_to_load) as election_data:
     
    #to do: read and analyze the data here
     #read the file object with the reader function.
     file_reader = csv.reader(election_data)

     #read the header row
     headers = next(file_reader)
     #Print each row in the CSV file
     for row in file_reader:
          #add to the total vote count.
          total_votes +=1
          #print the unique candidate name from each row
          candidate_name = row [2]
          #If the candidate does not match any existing candidate
          if candidate_name not in candidate_options:
               #add it to the list of candidates
               candidate_options.append(candidate_name)
               #begin tracking the candidate's vote count
               candidate_votes[candidate_name] = 0
          #add a vote to the candidate's count
          candidate_votes[candidate_name] += 1
          
       
#determine the percentage of votes for each candidate by looping through the counts
#1 iterate through the candidate list
for candidate_name in candidate_votes:
     #2 retrieve the vote count of a candidate.
     votes = candidate_votes[candidate_name]
     #Calculate the percentage of votes
     vote_percentage = float(votes) / float(total_votes) * 100
     #print the candidate name and percentage of the votes
     print(f'{candidate_name}: received {vote_percentage:.2f} % ({votes:,})\n') 
       #Determine if the vote count is greater than winning count
     if (votes > winning_count) and (vote_percentage > winning_percentage):

           # If true then set winning_count = to votes and winning % = to vote %
          winning_count = votes
          winning_percentage = vote_percentage
          #set winning candidate=candidate name
          winning_candidate=candidate_name
print(f'{winning_candidate} received {winning_count} total votes for a total of {winning_percentage:.2f} % of the vote')

#3 Print candidate options
#print(candidate_votes)






#Close the file
