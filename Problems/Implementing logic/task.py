try:
    name, surname = input().split()
    print("Welcome to our party, {} {}".format(name, surname))
except:
    print("You need to enter exactly 2 words. Try again!")