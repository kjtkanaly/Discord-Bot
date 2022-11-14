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

    print(type(Content))

    for log in logs:
        Content.insert(1, log + "\n")

    for log in Content:
        print(log)

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

""" newData = ["1,Poop,11/11/2022 - 03:51:56,album,https://open.spotify.com/album/1tiD0UGetoA3qTkJN3Thdv?si=-TkBVlklT8KO7Z-_uYBKNg",
"1,Poop,11/07/2022 - 03:20:06,track,https://open.spotify.com/track/5lXNcc8QeM9KpAWNHAL0iS?si=a64fc4b428be4e0e"]
newData.reverse()
updateCSV(newData, "Test.csv") """