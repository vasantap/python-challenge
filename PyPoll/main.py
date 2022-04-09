import os
import csv

#import and open csv file
csvpath = os.path.join("Resources","election_data.csv")
with open(csvpath) as file:
    
#create csv reader object to read the data
    csvreader = csv.reader(file, delimiter=",")
    csv_header = next(csvreader)
    
#initialize variable and create lists to store data
    total_votes = 0
    candidates = []
    candidate_votes = {}

#loop through each row of data to calculate total votes and candidate votes   
    for row in csvreader:
        total_votes += 1 #total votes

#if candidate is not in list add candidate and set vote count to 1 else add 1 to vote count
        if row[2] not in candidates:
            candidates.append(row[2])
            candidate_votes[row[2]] = 1
        else:
            candidate_votes[row[2]] += 1

#print results to terminal
    winner = max(candidate_votes, key=candidate_votes.get)
    print(f"\nElection Results")
    print(f"-------------------------")
    print(f"Total Votes: {total_votes}")
    print(f"-------------------------")
    for candidate in candidates:
        votes = candidate_votes[candidate]
#calculate percentage of votes 
        vote_percentage = float(votes) / float(total_votes) * 100
        print(f"{candidate}: {vote_percentage:.3f}% ({votes})")
    print(f"-------------------------")
    print(f"Winner: {winner}")
    print(f"-------------------------")

#create text file to write results to
    output_file = os.path.join("analysis", "election_data.txt")
    with open(output_file, "w") as file:
        file.write(f"Election Results\n")
        file.write(f"-------------------------\n")
        file.write(f"Total Votes: {total_votes}\n")
        file.write(f"-------------------------\n")
        for candidate in candidates:
            votes = candidate_votes.get(candidate)
            vote_percentage = float(votes) / float(total_votes) * 100
            file.write(f"{candidate}: {vote_percentage:.3f}% ({votes})\n")
        file.write(f"-------------------------\n")
        file.write(f"Winner: {winner}\n")
        file.write(f"-------------------------\n")
        file.close()
        