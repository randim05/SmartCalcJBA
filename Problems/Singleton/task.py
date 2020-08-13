# Truthy values
one = 1
non_empty_string = "singleton"

# Falsy values
zero = 0
empty_list = []

# NoneType
none_obj = None

# Truthy values
one = bool(1)
non_empty_string = bool("singleton")

# Falsy values
zero = bool(0)
empty_list = bool([])

# NoneType
# none_obj = bool(None)

one is True
non_empty_string is True
zero is False
empty_list is False
# none_obj is False

# bool(one)
# bool(non_empty_string)
# bool(zero)
# bool(empty_list)
# bool(none_obj)
#
# bool(1)
# bool("singleton")
# bool(0)
# bool([])
# bool(None)
#
# bool(1) is True
# bool("singleton") is True
# bool(0) is False
# bool([]) is False
# bool(None) is False