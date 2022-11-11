import plotly.graph_objects as go
from HandleCSVdata import *

####################################################
# Used to extract the unique elements from an array
def unique(Array):

    UniqueArray = [] # np.array([])
    
    for x in Array:
        
        if x not in UniqueArray:
            UniqueArray.append(x)

    return UniqueArray
####################################################

####################################################
# Main
filename  = 'LoserBarMusic.csv'
logs      = readData(filename)
Users     = []

for log in logs:
    Users.append(log[0])

UniqueUsers = unique(Users)

NumberOfMessagesByUser = []

for UniqueUser in UniqueUsers:
    Count = 0

    for User in Users:
        if User == UniqueUser:
            Count += 1

    NumberOfMessagesByUser.append(Count)

fig = go.Figure(data=[go.Pie(labels=UniqueUsers, values=NumberOfMessagesByUser,
                             textinfo='label+percent',
                             insidetextorientation='radial',
                             )])
fig.update_traces(textfont_size=20)
fig.show()
####################################################