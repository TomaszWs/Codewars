# Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates and the paperwork has 'm' pages.

# Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0.
# Example:

# n= 5, m=5: 25
# n=-5, m=5:  0

# My solution

def paperwork(n, m):
    # Happy Coding! ^_^
    if n < 0 or m < 0:
        return 0
    else:
        blank_pages = n*m
        return blank_pages
n=int(input())
m=int(input())
print(paperwork(n,m))

# Best practices
def paperwork(n, m):
    return n * m if n > 0 and m > 0 else 0

def paperwork(n, m):
    if m<0 or n<0:
        return 0
    else:
        return n*m