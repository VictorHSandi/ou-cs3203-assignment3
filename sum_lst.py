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

# Extend the software program again to add a main method (or whatever equivalent in your programming
# language of choice is) which allows a user to enter numbers and then calls both of the functions/methods
# above and prints the result from each one (the sum and product of the numbers). Commit the result.
# Push all three commits to the Github repository

def main():
    lst = []
    num = input("Enter a number to start a list:\n    ")
    while num.isdigit():
        lst.append(int(num))
        num = input("Enter a number to start a list or enter any non-number to exit:\n    ")
    print("The sum of the list is: " + str(sum_lst(lst)))
    print("The product of the list is: " + str(mul_lst(lst)))

if __name__ == "__main__":
    main()


# Create a new branch named part5 on the HEAD of the default branch (e.g., main). In your code, add
# a new function / method which takes a list / array of numbers and returns a list / array of numbers
# which are the same numbers given as the argument to the function / method but in reverse order.
# Commit the result on your new branch

def rev_lst(lst):
    copy = lst.copy()
    copy.reverse()
    return copy

# print(rev_lst([1,2,3,4,5]))