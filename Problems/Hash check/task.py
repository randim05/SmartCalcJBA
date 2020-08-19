# write your code here
try:
    hash(some_object)
    print("Hashable")
except:
    print("Not hashable")

# if isinstance(some_object, colletions.abc.Hashable):
#     print("Hashable")
# else:
#     print("Not hashable")