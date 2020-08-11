def abusech(args):
    args.k = args.k.rstrip("/")
    # Perform get request
    with open('./urlhaus.abuse.ch.txt', "r", newline='') as file:
        for line in file:
            line = line.rstrip()
            line = line.rstrip('/')
            if args.k == line:
                print("True")
