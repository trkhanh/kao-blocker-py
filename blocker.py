import time
from datetime import datetime
# Development hosts
dev_host_pathname = "hosts"

# Path for Windows Operating System
host_pathname = r"C:\Windows\System32\drivers\etc\hosts"

# Path for mac
# host_pathname = r"/private/etc/hosts"

# Path for linux
# host_pathname = r"/etc/hosts"

your_os = "window"


def get_os_path(i):
    switcher = {
        'window': r"C:\Windows\System32\drivers\etc\hosts",
        'mac': r"/private/etc/hosts",
        'linux': r"/etc/hosts",
    }
    return switcher.get(i, "Invalid Os")


"""CONFIG HERE
    @blocked_websites: For list of site to block
    @redirect: Redirect to default => someMovation.html
    #YOUR_OS: Your OS
"""
YOUR_OS = 'window'
# CONFIG HERE !!!!!!!!!!!!! ⚙
host_pathname = get_os_path(YOUR_OS)
# CONFIG HERE !!!!!!!!!!!!! ⚙
redirect = "127.0.0.1"
# CONFIG HERE !!!!!!!!!!!!! ⚙
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
        with open(host_pathname, 'r+') as file:
            content = file.read()
            for website in blocked_websites:
                if website in content:
                    pass
                else:
                    try:
                        file.write(redirect + " " + website+"\n")
                        print(content)
                    except:
                        print("Something went wrong")

    else:
        with open(host_pathname, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for eachline in content:
                if not any(website in eachline for website in blocked_websites):
                    file.write(eachline)
            file.truncate()
        print("Website blocker is deactivated")
    time.sleep(10)
