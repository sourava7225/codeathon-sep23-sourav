#Write a program to sort a string according to the frequency of character and return the final string

def sortString(s):
    # Write your code here
    freq = {}
    for i in s:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    res = ""
    for i in freq:
        res += i[0] * i[1]
    return res

print(sortString("hello world"))