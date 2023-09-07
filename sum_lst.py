# Create a software program (in any language you wish) which contains a function / method which
# computes the sum of a list / array of numbers (integers, whatever you want) given as a parameter and
# returns the result. Commit the resulting file(s). If your language is a compiled language (i.e., one in
# which the source code is compiled into a different, binary format) then only commit the source code
# file.


def sum_lst(lst):
    return sum(lst)

# print(sum_lst([1,1,1]))

# Extend the software program to add a function / method which computes the product (multiplication)
# of all of a list / array of numbers given as a parameter and returns the result. Commit the result. The
# new function / method may be in the same file as part 1’s function / method, or a new file, but this
# will be a second commit to the repository

def mul_lst(lst):
    if len(lst) == 0:
        return 0
    total = 1
    for x in lst:
        total = x * total

    return total


# print(mul_lst([1,2,3]))