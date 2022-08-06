def get_credentials() -> dict:
    credentials = dict()
    with open('userdata.txt') as f:
        for line in f.readlines():
            try:
                key, value = line.split(": ")
            except ValueError:
                print("Credentials invalid! \n Add email and password to userdata.txt")
                exit(0)
            credentials[key] = value.rstrip(" \n")
    return credentials
