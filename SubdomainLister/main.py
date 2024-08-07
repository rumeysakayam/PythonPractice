import requests

target_input = "google.com"

with open("subdomainlist.txt", "r") as subdomain_list:
    for word in subdomain_list:
        word = word.strip()
        url = "http://" + word + "." + target_input
        try:
            response = requests.get(url)
        except requests.exceptions.ConnectionError:
            pass
        if response:
            print("Found subdomain ---> " + url)
