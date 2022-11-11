import csv

# Read CSV file
def readData(File):

    with open(File, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        messages = []

        for row in reader:
            messages.append(row)
            print(f'{",".join(row)}')

        del messages[0]
        return messages

# Append CSV file with new logs
def writeData(logs, File):
    with open(File, 'a') as csv_file:
        for log in logs:
            csv_file.write("\n" + log)