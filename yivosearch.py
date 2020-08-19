import argparse
import sys
import configparser
import os.path
import sqlite3
from IPy import IP
from datetime import datetime
from modules.googlesafe import googlesafe
from modules.webadvisor import webadvisor
from modules.phishtank import phishtank
from modules.urlscan import urlscan
from modules.virustotal import vt_main
from modules.openphish import openphish
from modules.ibm import xforce

VERSION = "0.1"


# Banner
def banner():
    banner = '''
  .*.  , _    __ _  _.._. _.|_ 
\_|| \/ (_)  _) (/,(_][  (_.[ )
._|                
'''
    print(banner)
    print("**********************Yivo Search -v" + VERSION + "**************************")


# Usage
def usage():
    usage = """
        -h --help       Prints this help
        --------------------------Search Methods----------------------------
        -k --keyword    Search specific keywords (URLs)     
        """
    print(usage)
    sys.exit


# Start
#####################################
# Yivo Search #
#####################################

#####################################
# Define DB Connection and Insert #
#####################################
def input_type(args):
    try:
        IP(args.k)
        return True
    except ValueError:
        return False


def db_commit(urlscan_result, gsafe_result, webadvisor_result, phishtank_result, vt_result, openphish_result, ibm_result):
    # Connecting to sqlite
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "yivohunt.db")
    conn = sqlite3.connect(db_path)
    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    # Commit your changes in the database
    # Convert results to String for DB
    urlscan_result = str(urlscan_result)
    openphish_result = str(openphish_result)
    gsafe_result = str(gsafe_result)
    # datetime object containing current date and time
    now = datetime.now()
    created_time = now.strftime("%m/%d/%Y %H:%M:%S")
    # Insert Results
    cursor.execute('INSERT INTO results (created_time, value, engine_urlscan, engine_googlesafe, engine_webadvisor, engine_phishtank, engine_virustotal, engine_openphish, engine_ibm) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                   (created_time, args.k, urlscan_result, gsafe_result, webadvisor_result, phishtank_result, vt_result, openphish_result, ibm_result))
    conn.commit()
    print("Records inserted........")
    # Closing the connection
    conn.close()
    results = [created_time, args.k, urlscan_result, gsafe_result, webadvisor_result, phishtank_result, vt_result,
               openphish_result, ibm_result]
    print(results)

#####################################
# Main Function #
#####################################


def main():
    # Assign variables to arguments parsed
    # Config file processing & analysis
    conf = './conf/config.conf'
    if os.path.exists(conf):
        try:
            config = configparser.ConfigParser()
            config.read(conf)
            # Config.sections()
            # Assign URLscan variables
            urlscan_url = config.get('URLSCAN', 'api_url')
            # Assign Gsafe variables
            gsafe_url = config.get('GOOGLESAFE', 'api_url')
            gsafe_key = config.get('GOOGLESAFE', 'api_key')
            # Assign IBM variables
            ibm_url = config.get('IBM', 'api_url')
            ibm_key = config.get('IBM', 'api_key')
            ibm_pass = config.get('IBM', 'api_password')
            # Assign McAfee variables
            websafe_url = config.get('WEBSAFE', 'api_url')
            # Assign Phishtank variables
            phishtank_url = config.get('PHISHTANK', 'api_url')
            phishtank_key = config.get('PHISHTANK', 'api_key')
            # Assigned VT variables
            vt_api = config.get('VIRUSTOTAL', 'api_key')
            vt_url = config.get('VIRUSTOTAL', 'api_url')

            # Build header
        except:
            sys.exc_info()
    else:
        print("No such file '{}'".format(conf), file=sys.stderr)
        exit()
    # Get Input Type #
    search_type = input_type(args)
    # Initialize Functions from Modules #
    if search_type == True:
        vt_main(vt_url, vt_api, args, search_type)
        vt_result = vt_main(vt_url, vt_api, args, search_type)
    else:
        urlscan(urlscan_url, args)
        googlesafe(gsafe_url, gsafe_key, args)
        webadvisor(websafe_url, args)
        xforce(ibm_url, ibm_key, ibm_pass, args)
        vt_main(vt_url, vt_api, args, search_type)
        openphish(args)
        # Assign function returned results to variables #
        urlscan_result = urlscan(urlscan_url, args)
        gsafe_result = googlesafe(gsafe_url, gsafe_key, args)
        webadvisor_result = webadvisor(websafe_url, args)
        phishtank_result = phishtank(args)
        vt_result = vt_main(vt_url, vt_api, args, search_type)
        openphish_result = openphish(args)
        ibm_result = xforce(ibm_url, ibm_key, ibm_pass, args)

        # Call DB_Commit Function and pass results #
        db_commit(urlscan_result, gsafe_result, webadvisor_result, phishtank_result, vt_result, openphish_result,ibm_result)


if __name__ == '__main__':
    banner()
    usage()
    # Arg Parse
    parser = argparse.ArgumentParser()
    group_creation = parser.add_argument_group('Arguments')
    group_creation.add_argument('-k', '--keyword', help='Keyword search', nargs='?', dest="k")
    args = parser.parse_args()
    main()

