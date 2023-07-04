import os
import csv
# list to store ballot ID, county, and candidate into arrays
ballot =[]
county =[]
candidate =[]

# open and read file in csv dictionary reader
with open ("election_data.csv", "r") as file:
    csvElection= csv.reader(file)
    header = next(csvElection)
 
    for row in csvElection:
        ballot.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
# total number of votes casted
    sizeBallot=len(ballot)
  
# a complete list of candidates and total of voutes they recieved.
    candidate_count=dict((x,candidate.count(x)) for x in set(candidate))
 
# the percentage of votes each candidate won
 
    percent_candidate_count= dict(zip(candidate_count.keys(),map(lambda x:x/int(sizeBallot)*100,candidate_count.values())))
    k=3
    percent_candidate_count_= {key:round(percent_candidate_count[key],k) for key in percent_candidate_count}
# the winner of the electrion based on popular vote and her/his total votes
winner_candidate=max(candidate_count, key=candidate_count.get)
winner_vote=max(candidate_count.values())

# print election results
print("Election Results")
print("-------------------------")
print("Total Votes:", sizeBallot)
print("-------------------------")
print("Winner Votes:",winner_candidate, winner_vote)
print("-------------------------")
print("Candidate: (Total Vote, Percentage)")

# zip two dictionaries and print combined dictioanry for i in combined_dict
keys=candidate_count.keys()
values= zip(candidate_count.values(),percent_candidate_count_.values())
combined_dict=dict(zip(keys,values))
for i in combined_dict:
    print(i,":", combined_dict[i])

# specify file path and write summary into text file
output_path=os.path.join("..","output","election_summary.txt")
f=open("eletion_summary.txt", "w")
f.write("Election Results\n")
f.write("-----------------\n")
f.write("Total Votes:"+ str(sizeBallot)+'\n')
f.write("-----------------\n")
# write dictionary to text file by dict.keys()
for key in combined_dict:
    f.write(str(key)+":"+str(combined_dict[key]))
    f.write("\n")
f.write("------------------\n")
f.write("Winner:" + str(winner_candidate)+'\n')
f.write("-------------------")
f.close()       