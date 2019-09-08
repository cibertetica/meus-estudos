s = 'aba'
n = int(input(f'Number of times to repeat {s}: '))

''' my original function
    s *= n
    new_s = s[:n + 1]
    a = new_s.count('a')
    return a
'''

# calculation to avoid memory error | got this on hackerrank discussions

def repeatedString(n, s):
    a = s.count('a')
    num = n // len(s) # integer division of the number of times the string should be repeated by the length of the string
    mod = n % len(s) # division rest of the number of times the string should be repeated by the length of the string
    count = a * num + s[:mod].count('a')
    return count 

print(repeatedString(n, s))