import discord, time

def hasAttachments(message):
    if (len(message.attachments) == 0):
        return False
    attachmentString = ""
    for attachment in message.attachments:
        attachmentString += attachment.filename + "\n"
    return attachmentString


def timeToUnix(stamp: str):
    stamp, form = time.split(" ")
    if form.lower() == "m":
        stamp = time.ctime() + int(stamp * 60)
    elif form.lower() == "h":
        stamp = time.ctime() + int(stamp * 3600)
    elif form.lower() == "d":
        stamp = time.ctime() + int(stamp * 86400)
    else:
        print("Not defined")
    return stamp
    