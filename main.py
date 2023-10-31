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
        print('Menu')
        print('-' * 13)
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        menuOption = int(input('Please enter an option: '))
        if menuOption == 1:
            passwordDecoded = input('Please enter your password to encode: ')
            passwordEncoded = encode(passwordDecoded)
            print('Your password has been encoded and stored!')
        if menuOption == 2:
            print(f'The encoded password is {passwordEncoded}, and the original password is.')
        if menuOption == 3:
            break
