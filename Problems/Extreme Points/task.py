# The following line creates a dictionary from the input. Do not modify it, please
test_dict = json.loads(input())

# # Work with the 'test_dict'
# min = test_dict[]
# max = 0
# for i in test_dict:
#     if test_dict[i] < max:
#         min = test_dict[i]
#     if test_dict[i] > max:
a = min(test_dict.values())
b = max(test_dict.values())
def po(x):
    for i in test_dict:
        if test_dict[i] == x:
            return i
x = po(a)
y = po(b)
print("min: " + x)
print("max: " + y)