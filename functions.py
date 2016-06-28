# this function take list arguments
def print_two(*args):
    arg1, arg2 = args
    print "arg1: {} arg2: {}".format(arg1, arg2)

# THe first function is too unclear so we
# can rewrite it with better parameter def'ns
def print_two_again(arg1, arg2):
    print "arg1: {} arg2: {}".format(arg1, arg2)

def print_one(arg1):
    print "arg1: {}".format(arg1)

def print_none():
    print "I got nothin"


print_two(2, 3)
print_two_again("Joe", "Seidel")
print_one(3)
print_none()
