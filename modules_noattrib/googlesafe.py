import requests

def googlesafe(gsafe_url, gsafe_key, args):
    try:
            # Make API call
        post_data = {
                "client": {
                    "clientId": "yourclient",
                    "clientVersion": "1.5.2"
                },
                "threatInfo": {
                    "threatTypes": ["THREAT_TYPE_UNSPECIFIED", "MALWARE","SOCIAL_ENGINEERING","UNWANTED_SOFTWARE","POTENTIALLY_HARMFUL_APPLICATION"],
                    "platformTypes": ["ANY_PLATFORM"],
                    "threatEntryTypes": ["URL"],
                    "threatEntries": [
                        {"url": args.k},
                    ]
                    }
            }
        url = requests.post(gsafe_url + "?key=" + gsafe_key, json=post_data)

        with url as result:
        # Check web response
            if result.status_code == 200:
                data = result.json()
                # If no records located - print message and write results to output
                if data:
                    gsafe_result = "True"
                else:
                    gsafe_result = "False"

            else:
                gsafe_result = "False"
        return gsafe_result
    except SystemError:
        print("Failed to query.")