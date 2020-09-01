ui = input()
if ui.startswith(')'):
    print("ERROR")
elif (ui.count("(") - ui.count(")")) != 0:
    print("ERROR")
elif ui.endswith("("):
    print("ERROR")
else:
    print("OK")
