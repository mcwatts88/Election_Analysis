# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of the candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The toal number of votes each candidate won
# 5. The winner of the election based on popular vote

import csv

import os

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize total vote counter
total_votes = 0

# Create a candidate list
candidate_options = []

# Create a dictionary to tally votes for each candidate
candidate_votes = {}

# Winning Candidate and Winning Count Tracker

winning_candidate = ""

winning_count = 0

winning_percentage = 0


# Open the election results and read the file
with open(file_to_load) as election_data:

    # To do: perform analysis

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Print the header row
    headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:

        # Add to total votes
        total_votes += 1

        # Print the candidate name for each row
        candidate_name = row[2]

        # Add name to candidate list
        if candidate_name not in candidate_options:

            # add unique candidate to list
            candidate_options.append(candidate_name)

            # Initialize track votes for candidate
            candidate_votes[candidate_name] = 0

        # Add votes to candidate
        candidate_votes[candidate_name] += 1


# Save results to text file
with open(file_to_save, "w") as txt_file:

    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
    )

    print(election_results, end="")

    # Save the final vote count to the text file.
    txt_file.write(election_results)

    for candidate_name in candidate_votes:

        # Retrieve vote count and precentage
        votes = candidate_votes[candidate_name]

        vote_percentage = float(votes) / float(total_votes) * 100

        candidate_results = f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n"

        # Print each candidate, their vote count and percentage
        print(candidate_results)

        # Save the results to the text file
        txt_file.write(candidate_results)

        # Determine the winning vote count, winning percentage and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):

            winning_count = votes

            winning_percentage = vote_percentage

            winning_candidate = candidate_name

    # Print the winning candidate's results to the terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n"
    )
    print(winning_candidate_summary)

    # Save the winning candidate's results to the text file
    txt_file.write(winning_candidate_summary)

