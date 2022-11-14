import re

#####################################################################
# Parse Discord Messages for links that start with the provided Tag
def ParseMessagesForURLS(DiscordMessages, URL_Tag):
    MessageData = []

    for message in DiscordMessages:

        # Discord Info
        messageID   = message.id
        authorName  = message.author.name
        dateCreated = message.created_at.strftime("%m/%d/%Y - %H:%M:%S")

        # Spotify Link Info
        ChoppedMessage = message.content.split(URL_Tag)
        ChoppedMessage = ChoppedMessage[1].split(" ")
        ChoppedMessage = ChoppedMessage[0].split("\n")
        Link = ChoppedMessage[0]

        # Link Type
        ChoppedLink = Link.split("/", 1)
        LinkType    = ChoppedLink[0]
        

        log = (str(messageID) + "," + authorName + "," + dateCreated + "," + 
                LinkType + "," + (URL_Tag + Link))

        MessageData.append(log)

    return MessageData
#####################################################################
