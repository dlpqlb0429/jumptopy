import csv

with open('Demographic_Statistics_By_Zip_Code.csv',newline='') as infile:
    data = list(csv.reader(infile))


countParticipantsindex = data[0].index("COUNT CITIZEN STATUS TOTAL")
print("The index of 'COUNT PARTICIPANTS': "+str(countParticipantsindex))


countParticipants = []


for row in data[1:]:
    countParticipants.append(int(row[countParticipantsindex]))

#count_Citizen_Status_Total