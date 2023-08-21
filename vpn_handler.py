import subprocess
import random
import time
import os
from dotenv import load_dotenv

load_dotenv()

mullvad_account_number = os.getenv('MULLVAD_ACCOUNT_NUMBER')


# Switch to a random server
def change_server():
    with open('server_locations.txt', 'r') as server_file:
        data = server_file.read()
    server_locations = data.split('\n')
    location_str = random.choice(server_locations)

    # Set the Mullvad account number
    account_number = ""
    # Run the 'mullvad login' command and provide the account number
    p = subprocess.Popen(['mullvad', 'account', 'login'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    output, _ = p.communicate(input=account_number)
    loc1 = location_str.split(' ')[0]
    try:
        loc2 = location_str.split(' ')[1]
    except Exception:
        change_server()
        return
    print(output)
    command_list = ['mullvad', 'relay', 'set', 'location', f'{loc1}', f'{loc2}']
    command_str = ' '.join(command_list)
    subprocess.Popen(command_str, shell=True)
    subprocess.Popen(['mullvad', 'connect'])
    time.sleep(2)
