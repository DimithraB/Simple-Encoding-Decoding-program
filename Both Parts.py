def Repeat():
    option = input('''\n Try again?(Y/N):''')                                           #asks if the user wants to try again
    if option=='Y':                                                                     #user can try again by typing 'Y'
        interface()
    else:
        exit()                                                                          #programme will be closed

def Encode():
    message     = input('Enter the messaage:')                                          #asks the user to prompt the message
    shift_value = int(input('Enter an integer in the range of 1-25:'))                  #asks the user to prompt a shift value
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    Answer = ''
    if shift_value>25 or shift_value<1:                                                 #checking whether the shift value is less than 25 or greater than 1
        print("Enter integers in range 1 to 25")
    else:
        for i in message:                      
            if i not in alphabet:
                Answer += i
            else:
                Answer += alphabet[(alphabet.index(i)+shift_value)%26]
        print(Answer)
    Repeat()

def Decode():
    message     = input('Enter the messaage:')
    shift_value = int(input('Enter an integer in the range of 1-25:'))
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    Answer = ''
    if shift_value>25 or shift_value<1:
        print("Enter integers in range 1 to 25")
    else:
        for i in message:
            if i not in alphabet:
                Answer += i
            else:
                Answer += alphabet[(alphabet.index(i)-shift_value)%26]
        print(Answer)
    Repeat()



def interface():
    select = input("--------MENU--------\n1)Encode = E\n2)Decode = D\n3)Quit   = Q\nSelect a letter:")        #user can decide to encode,decode or to quit
    if select == 'E':                                                                                         #user can select the relevent letter
        Encode()
    elif select == 'D':
        Decode()
    elif select == 'Q':
        exit()
    else:
        print('Invalid input, Please Try Again')                                                              #if the user entered an invalid input a message will be shown
        interface()
interface()
