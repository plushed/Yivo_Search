import requests
import urllib3

def urlscan(urlscan_url, args):
    try:
            # Make API call
        urllib3.disable_warnings()
        url = requests.get(urlscan_url + args.k, verify = False)
        with url as result:
        # Check web response
            if result.status_code == 200:
                data = result.json()
                # If no records located - print message and write results to output
                if not data['results']:
                    urlscan_result = "False"
                else:
                    val = (data['results'][0])
                    result = (val['result'])
                    url2 = requests.get(result)
                    with url2 as result2:
                        data2 = result2.json()
                        urlscan_result = data2.get('verdicts', {}).get('overall', {}).get('malicious')
            else:
                urlscan_result = "False"
        return urlscan_result
    except SystemError:
        print("Failed to query.")
