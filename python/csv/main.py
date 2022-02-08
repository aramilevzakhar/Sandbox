import csv

#with open('eggs.csv', newline='') as csvfile:
#    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#    for row in spamreader:
#        print(', '.join(row))
#

name_1 = 'Alex'
name_2 = 'Max'

with open('data.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow([name_1, name_2])
