import os
import csv

csvpath = os.path.join("Resources","election_data.csv")

with open(csvpath) as file:
    csvreader = csv.reader(file, delimiter=",")
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    total_votes = 0
    candidates = []
    candidate_votes = {}
    for row in csvreader:
        total_votes += 1
        if row[2] not in candidates:
            candidates.append(row[2])
            candidate_votes[row[2]] = 1
        else:
            candidate_votes[row[2]] += 1
    print(f"Total Votes: {total_votes}")
    print(f"Candidates: {candidates}")
    print(f"Candidate Votes: {candidate_votes}")
    winner = max(candidate_votes, key=candidate_votes.get)
    print(f"Winner: {winner}")
    print("-------------------------")
    print(f"Election Results")
    print(f"-------------------------")
    print(f"Total Votes: {total_votes}")
    print(f"-------------------------")
    for candidate in candidates:
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        print(f"{candidate}: {vote_percentage:.3f}% ({votes})")
    print(f"-------------------------")
    print(f"Winner: {winner}")
    print(f"-------------------------")
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
        