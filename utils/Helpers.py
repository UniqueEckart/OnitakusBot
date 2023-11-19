import discord

def hasAttachments(message):
    if (len(message.attachments) == 0):
        return False
    attachmentString = ""
    for attachment in message.attachments:
        attachmentString += attachment.filename + "\n"
    return attachmentString