def abusech(args):
    args.k = args.k.rstrip("/")
    args.k = args.k.lstrip('http://')
    args.k = args.k.lstrip('https://')
    # Perform get request
    with open('./urlhaus.abuse.ch.txt', "r", newline='') as file:
        for line in file:
            line = line.rstrip()
            line = line.rstrip('/')
            line = line.lstrip('http://')
            line = line.lstrip('https://')
            if args.k == line:
                print("True")
