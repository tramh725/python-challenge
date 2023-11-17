import csv
import os 
election_csv = os.path.join('PyPoll', 'Resources', 'election_data.csv')

voters = []
votes=[int(0), int(0), int(0)]
vote_per=[float(0), float(0), float(0)]
candidates = []

with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    
    csv_header= next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    for row in csvreader: 
        voters.append(row[0])
        if row[2] not in candidates:
            candidates.append(row[2])

        if row[2] == candidates[0]:
            votes[0] = votes[0] + 1
        elif row[2] == candidates[1]:
            votes[1] = votes[1] + 1
        elif row[2] == candidates[2]:
            votes[2] = votes[2] + 1
    vote_per[0] = can_per1 = {'{:.3f}%'.format((votes[0])/(len(voters))*100)}
    vote_per[1] = can_per2 = {'{:.3f}%'.format((votes[1])/(len(voters))*100)}
    vote_per[2] = can_per3 = {'{:.3f}%'.format((votes[2])/(len(voters))*100)}
    
    winning=votes.index(max(votes))
    winner=candidates[winning]
    

print("Election Results")
print("--------------------------------------")
print(f"Total Votes: {len(voters)}")
print("--------------------------------------")
print(f"{candidates[0]} {vote_per[0]} ({votes[0]})")
print(f"{candidates[1]}: {vote_per[1]} ({votes[1]})")
print(f"{candidates[2]}: {vote_per[2]} ({votes[2]})")
print("--------------------------------------")
print(f"Winner: {winner}")
print("--------------------------------------")

text_file = os.path.join("PyPoll", "analysis")
with open(text_file, "w") as text_file:
    print("Election Results",file=text_file)
    print("--------------------------------------",file=text_file)
    print(f"Total Votes: {len(voters)}",file=text_file)
    print("--------------------------------------",file=text_file)
    print(f"{candidates[0]}: {vote_per[0]} ({votes[0]})",file=text_file)
    print(f"{candidates[1]}: {vote_per[1]} ({votes[1]})",file=text_file)
    print(f"{candidates[2]}: {vote_per[2]} ({votes[2]})",file=text_file)
    print("--------------------------------------",file=text_file)
    print(f"Winner: {winner}",file=text_file)
    print("--------------------------------------",file=text_file)
