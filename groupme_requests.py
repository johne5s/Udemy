import requests
URLBASE = "https://api.groupme.com/v3"
TOKEN = "GET THE TOKEN FROM THE WEBSITE"


def make_group(token, name):
    group_id = None

def make_bot():
    bot_id = None

def send_message():
    message = "This is a test message"

def AskUserForInput():
    while True:
        try:
            #Ask the user to Hit or Stay
            result = int(input("Press 1 to Great a new group \nPress 2 to send a message to the group\n"))
        except:
            print("Not an int")
            continue
        else:
            # No error so do the else
            if result == 1 or result == 2:
                return result


if __name__ == "__main__":
    AskUserForInput()