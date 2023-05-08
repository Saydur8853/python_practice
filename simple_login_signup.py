print ('Create an account now')

username = input('Enter username: ')
password = input('Enter password: ')

print('Your account has been created successfully')
print('Login now!')

valid_username = input('Enter username: ')
valid_password = input('Enter password: ')

if username == valid_username and password == valid_password :
    print('Logged in successfully')
else:
    print('Invalid credentials')