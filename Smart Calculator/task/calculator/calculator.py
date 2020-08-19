# write your code here
def all_isalpha(x):
    for i in x:
        try:
            int(i)
            return False
        except ValueError:
            continue
    return True

def valid_assignment(x):
    l = [i.strip() for i in x.split("=")]
    if len(l) == 2:
        if all_isalpha(l[0]):
            if l[1].isdigit():
                return l
            else:
                if l[1] in valid_var:
                    l[1] = valid_var[l[1]]
                else:
                    print("Unknown variable")
                    return False
        else:
            print("Invalid identifier")
            return False
    else:
        return False

valid_var = {}

while True:
    try:
        user_input = input()
        if "=" in user_input:
            c = valid_assignment(user_input)
            if c:
                valid_var[c[0]] = c[1]

        elif user_input.startswith('/'):
            if user_input == "/exit":
                print("Bye!")
                break
            elif user_input == "/help":
                print("The program calculates the sum of numbers")
                continue
            # else:
            #     print("Unknown command")
        elif "+" in user_input or "-" in user_input:
            list_user_oper = user_input.split(' ')
            out_list = []
            for i in list_user_oper:
                if i in valid_var:
                    out_list.append(valid_var[i])
                else:
                    out_list.append(i)

            print(exec(''.join(out_list)))
    except:
        pass

# def n(znak, digit):
#     if "-" in znak:
#         if len(znak) % 2 == 0:
#             return int(digit)
#         else:
#             return int(digit) * -1
#     return digit
#
#
# while True:
#     try:
#         z = input()
#         if z.startswith('/'):
#             if z == "/exit":
#                 print("Bye!")
#                 break
#             elif z == "/help":
#                 print("The program calculates the sum of numbers")
#                 continue
#             else:
#                 print("Unknown command")
#         elif z == '':
#             continue
#         else:
#             print(eval(z))
#             # y = z.split()
#             # print(sum([n(i, j) for i, j in y]))
#             continue
#     except:
#         print("Invalid expression")
