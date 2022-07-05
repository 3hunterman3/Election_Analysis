import csv
import os

file_to_load = os.path.join('/Users','edwardkim','Desktop','DataClass','Election_Analysis','election_results.csv')

# candidate_option = []
# total_votes_charles = 0
# total_votes_diana = 0
# total_votes_raymon = 0
# complete_total = 0

# with open(file_to_load,'r') as f:
#     lines = csv.reader(f,delimiter=',')
#     header = next(lines)
#     print('header',header)
#     for line in lines:
#         #total amount of votes
#         complete_total += 1
#         #Adding all the candidates votes per person
#         if line[2] == "Charles Casper Stockham":
#             total_votes_charles += 1
#         elif line[2] == 'Diana DeGette':
#             total_votes_diana += 1
#         else:
#             total_votes_raymon += 1 
#         #figuring out names
#         candidate_name = line[2]
#         if candidate_name not in candidate_option:
#             candidate_option.append(candidate_name)

# print("Raymon Anthony Doane: {}, Diana DeGette: {}, Charles Casper Stockham: {}".format(total_votes_raymon,total_votes_diana,total_votes_charles))

file_to_save = os.path.join("analysis","election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate options and candidate votes
candidate_options = []
# 1. Declare the empty dictionary.
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    #  To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name
        # To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
#  To do: print out the winning candidate, vote count and percentage to
#   terminal.
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)