# write your code here
def n(znak, digit):
    if "-" in znak:
        if len(znak) % 2 == 0:
            return int(digit)
        else:
            return int(digit) * -1
    return digit

while True:
    try:
        z = input()
        if z.startswith('/'):
            if z == "/exit":
                print("Bye!")
                break
            elif z == "/help":
                print("The program calculates the sum of numbers")
                continue
            else:
                print("Unknown command")
        elif z == '':
            continue
        else:
            print(eval(z))
            # y = z.split()
            # print(sum([n(i, j) for i, j in y]))
            continue
    except:
        print("Invalid expression")s.