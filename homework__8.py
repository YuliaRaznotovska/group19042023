user_login = input('Enter your login (only letters)  >> ')
user_password = input('Enter your password (only letters and numbers) >> ')

if user_login.isalpha() and user_password.isalnum():
    confirm_user_login = input('Confirm your login >> ')
    confirm_user_password = input('Confirm your password >> ')
    user_login_requirement = confirm_user_login == user_login
    user_password_requirement = confirm_user_password == user_password

    if user_login_requirement and user_password_requirement:
        first_successful_login = 'You are logged in'
        print(first_successful_login)

        teacher_whim = 'You are logged out due to a teacher\'s whim'
        print(teacher_whim)

        final_confirmation_login = input('Confirm your login again >> ')
        final_confirmation_password = input('Confirm your password again >> ')
        final_login_requirement = final_confirmation_login == user_login
        final_password_requirement = final_confirmation_password == user_password

        if final_login_requirement and final_password_requirement:
            second_successful_login = 'You are logged in'
            print(second_successful_login)
        else:
            print('Login and password do not match.')
    else:
        print('Login and password do not match.')
else:
    print('Invalid login or password.')
