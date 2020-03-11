alphabet    = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'   #alphabet
shift_value = 0

message     = input('Enter the messaage:')                             #asks the user to prompt the message
shift_value = int(input('Enter an integer in the range of 1-25:'))     #asks the user to prompt a shift value

for i in message:
    if i in alphabet:
        x = alphabet.index(i)
        print(alphabet[x+shift_value], end='')
    else:
        print(i,end='')







