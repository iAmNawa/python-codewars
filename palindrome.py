test_string = 'racecar'

def palindrome_checker(input):
    return input == input[::-1]

print(palindrome_checker(test_string))
