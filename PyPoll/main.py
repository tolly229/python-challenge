import os
import csv
currentdir = os.getcwd()
path = os.path.join("election_data.csv")
with open(path,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    headers = next(csvreader)

    voter =[]
    county =[]
    candidate =[]

    for row in csvreader:
        voter.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

    total = len(voter)

    k=candidate.count("Khan")
    c=candidate.count("Correy")
    l=candidate.count("Li")
    o=candidate.count("O'Tooley")

    
    
    k_percent= round(k/int(total)*100,2)   
    c_percent= round(c/int(total)*100,2) 
    l_percent= round(l/int(total)*100,2) 
    o_percent= round(o/int(total)*100,2) 
    print(k_percent,c_percent,l_percent,o_percent)

print("Election Results")
print("----------------------------------------------------")
print(f"Total Votes: {total}")
print("----------------------------------------------------")
print(f"Khan: {k_percent} % ({k})")
print(f"Correy: {c_percent} % ({c})}")
print(f"Li: {l_percent} % ({l})}")
print(f"O'Tooley: {o_percent % ({o})")
print("----------------------------------------------------")
print("Winner: ")
print("----------------------------------------------------")

with open('mainEnd.txt', 'w') as txtfile:
    election_results = (
    f"\nElection Results\n"
    f"----------------------------------------------------\n"
    f"Total Votes: {total}"
    f"\n----------------------------------------------------\n")
    txtfile.write(election_results)

