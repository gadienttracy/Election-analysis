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
#save results to a text file
with open(file_to_save, "w") as txt_file:
#print the final vote count to the terminal
     election_results = (
          f"\nElection Results\n"
          f"--------------------\n"
          f"Total Votes: {total_votes:,}\n"
          f"--------------------------\n")

     print(election_results, end="")
# Save the final vote count to the text file
     txt_file.write(election_results)

     #determine the percentage of votes for each candidate by looping through the counts
     #1 iterate through the candidate list
     for candidate_name in candidate_votes:
          #2 retrieve the vote count of a candidate.
          votes = candidate_votes[candidate_name]
          #Calculate the percentage of votes
          vote_percentage = float(votes) / float(total_votes) * 100
          #print the candidate name and percentage of the votes
          candidate_results = (f'{candidate_name}: received {vote_percentage:.2f} % ({votes:,})\n') 
          #print each candidate, their voter count, and percentage to the terminal
          print(candidate_results)
          #save candidate results to the text file
          txt_file.write(candidate_results)
          #Determine if the vote count is greater than winning count
          if (votes > winning_count) and (vote_percentage > winning_percentage):

               # If true then set winning_count = to votes and winning % = to vote %
               winning_count = votes
               winning_percentage = vote_percentage
               #set winning candidate=candidate name
               winning_candidate=candidate_name
     winning_candidate_summary = (
          f"-------------------\n"
          f"Winner: {winning_candidate} \n"
          f"received {winning_count:,} \n"
          f"Winning Percentage: {winning_percentage:.2f}\n"
          f"---------------------\n")
     print(winning_candidate_summary)
     #save the winning candidate's name to the text file
     txt_file.write(winning_candidate_summary)
     #3 Print candidate options
     #print(candidate_votes)






     #Close the file
