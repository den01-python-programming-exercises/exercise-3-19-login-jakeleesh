def main():
    #write your code below this line
    user = input("Enter username:")
    password = input("Enter password:")
    if ((user == "grace" and password == "hopper") or (user == "emma" and password == "haskell")):
        print("You have successfully logged in!")
    else:
        print("Incorrect username or password!")

if __name__ == '__main__':
    main()
