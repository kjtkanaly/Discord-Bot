import csv

# Read CSV file
def readData(File):

    with open(File, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        messages = []

        for row in reader:
            messages.append(row)
            # print(f'{",".join(row)}')

        del messages[0]
        return messages

# Append CSV file with new logs
def writeData(logs, File):
    with open(File, 'a') as csv_file:
        for log in logs:
            csv_file.write("\n" + log)

def updateCSV(logs, File):
    with open(File, 'r') as csv_file:
        Content = csv_file.readlines()

    for log in logs:
        Content.insert(1, log + "\n")

    with open("Test.csv","w") as csv_file:
        for row in Content:
            csv_file.write(row)

# Grabs the first entry in the csv
def getTopRow(File):

    with open(File, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        
        for x in range(0,2):
            row = next(reader)

        return row
