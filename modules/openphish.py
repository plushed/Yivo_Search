

def openphish(args):
    args.k = args.k.rstrip("/")
    # Perform get request
    value = args.k
    with open('./feed.txt', "r", newline='') as file:
        for line in file:
            line = line.rstrip()
            line = line.rstrip('/')
            line = line.lstrip('http://')
            line = line.lstrip('https://')
            if args.k == line:
                return True