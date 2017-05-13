#!/usr/bin/python3

bine1 = 0
bine2 = 0
e3 = 0
bine = list ()
start_namber = input ('Whot start namber do you whont')
st1 = int (start_namber)
start_namber = int (start_namber)
#e3 = start_namber
starter = 1
# dun = 0
print (starter)
while int (starter) < (start_namber):
    starter = starter * 2
    print (starter)
while True:
    if int(starter) > (start_namber) or int (starter) == (start_namber):
        #while int (starter) > int (start_namber):
        while starter > 1:
            starter = int (starter / 2)
            print (starter)

            if int(starter) < st1 or int (starter) == st1:
                bine. append ('1')
                
