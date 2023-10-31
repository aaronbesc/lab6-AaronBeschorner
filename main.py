# Encode a password by adding +3 to each integer.
def encode(password):
    passwordList = list(password)
    for i in range(len(passwordList)):
        passwordList[i] = int(passwordList[i]) + 3
        if passwordList[i] > 9:
            passwordList[i] = passwordList[i] - 10
        passwordList[i] = str(passwordList[i])
    passwordList = ''.join(passwordList)
    return passwordList

if __name__ == '__main__':
    while True:
        # Menu options
        print('Menu')
        print('-' * 13)
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        # User selects an option
        menuOption = int(input('Please enter an option: '))
        # Encode method
        if menuOption == 1:
            passwordDecoded = input('Please enter your password to encode: ')
            passwordEncoded = encode(passwordDecoded)
            print('Your password has been encoded and stored!')
        # Encode and decode method
        if menuOption == 2:
            print(f'The encoded password is {passwordEncoded}, and the original password is.')
        # Exit the program
        if menuOption == 3:
            break
