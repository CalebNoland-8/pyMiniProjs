import json, hashlib, getpass, os, time, pyperclip, sys
from cryptography.fernet import Fernet, MultiFernet



def register_new_user():
    username = input("Username: ")
    password = getpass.getpass(prompt='Master password: ')

    m = hashlib.sha256
    hashed_password = m(password.encode('utf-8')).hexdigest()

    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'user_data.json')

    with open (file_path, 'w') as foo:
        user_data = {'username': username, 'master_password': hashed_password}
        json.dump(user_data, foo)

def user_login():
    login = False

    username = input("Username: ")
    password = getpass.getpass(prompt='Master password: ')

    m = hashlib.sha256
    hashed_password = m(password.encode('utf-8')).hexdigest()

    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'user_data.json')

    with open(file_path, "r") as f:
        data = json.load(f)

    if data['username'] == username and data['master_password'] == hashed_password:
        login = True

    return login  

def add_password(key):
    website = input("Enter website: ")
    username = input("Enter username(or N/A): ")
    password = getpass.getpass(prompt="Enter password: ")

    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'user_passwords.json')

    message = password.encode('utf-8')

    with open(file_path, "r") as f:
        data = json.load(f)

    token = key.encrypt(message)

    data.append({'website': website, 'username': username, 'password': token.decode('utf-8')})

    with open (file_path, 'w') as foo:
        json.dump(data, foo)


def retrieve_password(key):

    website = input("Enter website: ")

    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'user_passwords.json')

    with open(file_path, 'r') as foo:
        data = json.load(foo)

    for x in range(len(data)):
        if data[x]['website'] == website:
            message = data[x]['password']
            decoded_message = key.decrypt(message.encode('utf-8'))
            decoded_message = decoded_message.decode()

            print(f'\nUsername: {data[x]['username']}\nPassword: {decoded_message}')
            pyperclip.copy(decoded_message)
            print('Password Copied to Clipboard')
            break
    else:
        print("Website Does Not Exist")

def delete_password():
    website = input("Enter website: ")

    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'user_passwords.json')

    with open(file_path, 'r') as foo:
        data = json.load(foo)

    for x in range(len(data)):
        if data[x]['website'] == website:
            confirm = input(f'{website} was found. Confirm Deletion [Y/N]')

            if confirm.lower() == 'y':
                
                data.pop(x)

                with open (file_path, 'w') as foo:
                    json.dump(data, foo)

                print('\nSuccessfully Deleted')

                break
            elif confirm.lower() == 'n':

                print('Deletion Cancelled')

                break
            else:

                print('Enter Valid Input')
    else:

        print("Website Does Not Exist")

def view_saved_websites():

    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'user_passwords.json')

    with open(file_path, 'r') as foo:
        data = json.load(foo)

    print('Loading Websites...\n')

    time.sleep(1)

    for x in range(len(data)):
        print(data[x]['website'])
        time.sleep(.2)


def generate_key():
    #key = 
    #return key
    pass


def main():
    #For key just generate it once and export to .key file

    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'master_key.key')

    if os.path.exists(file_path) and os.path.getsize(file_path) != 0:
        with open(file_path, 'rb') as foo:
            
            key = foo.read()
    else:

        key = Fernet.generate_key()

        with open(file_path, 'wb') as foo:

            foo.write(key)


    f = Fernet(key)
    
    while True:

        print('1. Register\n2. Login\n3. Quit')
        user_selection =  int(input('Enter your choice: '))

        if user_selection == 1:
            register_new_user()
        elif user_selection == 2:
            if user_login() == True:
                print('\n[+] Login Successful')
                while True:
                    print('\n1. Add Password\n2. Retrieve Password\n3. View Saved Websites\n4. Delete Password\n5. Quit')

                    second_user_selection = int(input('Enter your choice: '))

                    if second_user_selection == 1:
                        add_password(f)
                    elif second_user_selection ==2:
                        retrieve_password(f)
                    elif second_user_selection == 3:
                        view_saved_websites()
                    elif second_user_selection == 4:
                        delete_password()
                    elif second_user_selection == 5:
                        break
                    else:
                        print('\nInput Invalid, Try Again\n')

            else:
                print('Username or Password did not match')
        elif user_selection == 3:
            break
        else:
            print('\nInput Invalid, Try Again\n')

if __name__ == '__main__':
    main()