#!/usr/bin/python3

#print(ord('A'))
#print(chr(65))

#numbers = [1, 2, 3, 4, 5]
#letters = list(map(lambda n: chr(n), numbers))


# message = 'Write Text: '
# converted = [ord(char) for char in message]

# print(converted)


# decoded = [chr(number) for number in converted]
# message = "".join(decoded)
# print(message)


# CM input is a string
# CM output is a list of numbers

def EncodeMessage( message ):
    return [ord(char) for char in message]
    
    
    

# CM input is a list of numbers
# CM output is a string

def DecodeMessage( encoded ):
    decoded = [chr(number) for number in encoded]
    return "".join(decoded)
    
Test = 'abc'

numbers = EncodeMessage(Test)
print(numbers)

message = DecodeMessage(numbers)
print(message)