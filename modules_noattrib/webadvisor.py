import requests
from bs4 import BeautifulSoup

def webadvisor(websafe_url, args):
    try:
        url = requests.get(websafe_url + args.k)

        with url as result:
        # Check web response
            if result.status_code == 200:
                data = result.content
                # If no records located - print message and write results to output
                soup = BeautifulSoup(data, 'html.parser')
                result = str(soup.select("span.rating"))
                soup = BeautifulSoup(result, 'html.parser')
                result = str(soup.text)
                webadvisor_result = (result.strip('['']'))
                return webadvisor_result
            else:
                print("No Result")
    except SystemError:
        print("Failed to query.")
