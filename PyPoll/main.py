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
print(f"Khan: {str(k_percent) + str(k)}")
print(f"Correy: {str(c_percent) + str(c)}")
print(f"Li: {str(l_percent) + str(l)}")
print(f"O'Tooley: {str(o_percent) + str(o)}")
print("----------------------------------------------------")
print("Winner: ")
print("----------------------------------------------------")

with open('mainEnd.txt', 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow("Election Results")
    csvwriter.writerow("----------------------------------------------------")
    csvwriter.writerow(f"Total Votes: {total}")
    csvwriter.writerow("----------------------------------------------------")
