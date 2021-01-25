import time
from datetime import datetime
# Development hosts
dev_host_pathname = "hosts"

# Path for Windows Operating System
host_pathname = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
blocked_websites = ["www.twitter.com", "twitter.com",
                    "facebook.com", "www.facebook.com", "https://www.facebook.com"]


# Accessing and reassigning DateTime
current_year = datetime.now().year
current_month = datetime.now().month
current_day = datetime.now().day
start_time = 8
end_time = 16

"""
If the current datetime falls between the 'start_time' and 'end_time',
websites in the 'blocked_websites' list are written in the hosts file and
redirected to the default localhost or port 127.0.0.1.
"""
while True:
    if datetime(current_year, current_month, current_day, start_time) < datetime.now() < datetime(current_year, current_month, current_day, end_time):
        print("Working hours activated...")
        with open(dev_host_pathname, 'r+') as file:
            content = file.read()
            # print(content)
            for website in blocked_websites:
                if website in content:
                    pass
                else:
                    try:
                        file.write(redirect + " " + website+"\n")
                    except e:
                        print("Something went wrong")

    else:
        with open(dev_host_pathname, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for eachline in content:
                if not any(website in eachline for website in blocked_websites):
                    file.write(eachline)
            file.truncate()
        print("Website blocker is deactivated")
    time.sleep(10)
