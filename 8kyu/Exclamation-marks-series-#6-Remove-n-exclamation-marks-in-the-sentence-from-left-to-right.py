# Description:
#
# Remove n exclamation marks in the sentence from left to right. n is positive
# integer.
# Examples
#
# remove("Hi!",1) === "Hi"
# remove("Hi!",100) === "Hi"
# remove("Hi!!!",1) === "Hi!!"
# remove("Hi!!!",100) === "Hi"
# remove("!Hi",1) === "Hi"
# remove("!Hi!",1) === "Hi!"
# remove("!Hi!",100) === "Hi"
# remove("!!!Hi !!hi!!! !hi",1) === "!!Hi !!hi!!! !hi"
# remove("!!!Hi !!hi!!! !hi",3) === "Hi !!hi!!! !hi"
# remove("!!!Hi !!hi!!! !hi",5) === "Hi hi!!! !hi"
# remove("!!!Hi !!hi!!! !hi",100) === "Hi hi hi"


def remove(st, n):
    return st.replace("!", "", n)


if __name__ == '__main__':
    print(remove("!Hi!", 1))


# Best solutions:


def remove(s, n):
    liste=[]
    k=1
    for i in range(len(s)):
            if s[i]=="!" and k<=n:
                k+=1
            else:
                liste.append(s[i])
    return "".join(liste)


def remove(s, n):
    return ''.join(s.split('!', n))
