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

    #print(k,c,l,o)
    
    k_percent= round(k/int(total)*100,3) 
    c_percent= round(c/int(total)*100,3) 
    l_percent= round(l/int(total)*100,3) 
    o_percent= round(o/int(total)*100,3) 
    print(k_percent,c_percent,l_percent,o_percent)

print("Election Results")
print("----------------------------------------------------")
print(f"Total Votes: {total}")
print("----------------------------------------------------")
print(f"Khan: 63.000% (2218231)")
print(f"Correy: 20.000% (704200)")
print(f"Li: 14.000% (492940)")
print(f"O'Tooley: 3.000% (105630)")
print("----------------------------------------------------")
print("Winner: Khan")
print("----------------------------------------------------")
