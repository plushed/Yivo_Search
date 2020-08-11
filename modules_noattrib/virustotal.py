import requests
import base64

VERSION = "0.1"

#####################################
#  VT Main #
#####################################w

def vt_main(vt_url, vt_api, args, search_type):

    if search_type == True:
        vt_collection = 'ip_addresses'
        vt_request = vt_url + vt_collection
        vt_header = {'x-apikey': vt_api}
        vt_value = args.k
        # Call IP search function
        url = requests.get(vt_request + '/' + vt_value, headers=vt_header)
        with url as result:
            # Check web response
            if result.status_code == 200:
                # Assign JSON response to data variable
                data = result.json()
                for obj in data:
                    self = extract_values(data, 'self')
                    link = (str(self))
                    category = extract_values(data, 'category')
                    # Convert category to list
                    category = list(category.split(" "))
                    # Get totals
                    harmless_count = category.count('harmless')
                    undetected_count = category.count('undetected')
                    suspicious_count = category.count('suspicious')
                    malicious_count = category.count('malicious')
                    # Calculate percentage of detections

                    result = (str(suspicious_count + malicious_count) + '/' + str(harmless_count + undetected_count))
                    return result
            # Typical errors
            else:
                return "Failed"
    else:
        vt_collection = 'urls'
        vt_header = {'x-apikey': vt_api}
        # Covert to byte type for base64 encoding
        vt_value = args.k
        vt_value = vt_value.encode('utf-8')
        # Perform base64 encoding
        vt_value = base64.urlsafe_b64encode(vt_value)
        # Covert back to string for strip
        vt_value = str(vt_value).strip("b'")
        vt_value = vt_value.strip("=")
        vt_request = vt_url + vt_collection
        url = requests.get(vt_request + '/' + vt_value, headers=vt_header)
        with url as result:
            # Check web response
            if result.status_code == 200:
                # Assign JSON response to data variable
                data = result.json()
                for obj in data:
                    self = extract_values(data, 'self')
                    link = (str(self))
                    category = extract_values(data, 'category')
                    # Convert category to list
                    category = list(category.split(" "))
                    # Get totals
                    harmless_count = category.count('harmless')
                    undetected_count = category.count('undetected')
                    suspicious_count = category.count('suspicious')
                    malicious_count = category.count('malicious')
                    # Calculate percentage of detections
                    result = (str(suspicious_count + malicious_count) + '/' + str(harmless_count + undetected_count))
                    return result
                # Typical errors
                else:
                    return "Failed"

# Function to pull from nested JSON output
def extract_values(obj, key):
    """Pull all values of specified key from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    results = extract(obj, arr, key)
    results = ' '.join(map(str, results))
    return results

