import requests

def phishtank(args):
    try:
        url = requests.get('https://www.yivointel.com/phishtank/online-valid.json')
        print(url)
        with url as result:
        # Check web response
            if result.status_code == 200:
                data = result.json()
                for obj in data:
                    if args.k in (obj.values()):
                        phishtank_result = "True"
                        break
                    else:
                        phishtank_result = "False"
            else:
                print("No Result")
    except SystemError:
        print("Failed to query.")

    return phishtank_result
