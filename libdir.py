import os
from time import sleep as wait
try:
    print('Collecting libraries...', flush=True)
    from getpass import getpass
except:
    print('libman->Error: Unable to get basic functionality, "getpass" from python modular.', flush=True)
    input()
    os.sys.exit(1)
try:
    print('Re-collecting libraries...', flush=True)
    import libED
except:
    print('libdir->Error: Incomplete lib-manage file detected.')
    input()
    os.sys.exit(1)
def new_data(error:bool=False):
    try:
        if error==False:
            with open(os.path.join(os.path.dirname(__file__), "lib-host.blib"), 'r') as file:
                print('Failure! Database already exists.')
            ans=input('Want to re-initiate sql?[y/n]')
            if ans.lower()=='y':
                print('\rDeleting existing data...', end='', flush=True)
                os.remove(os.path.join(os.path.dirname(__file__), "lib-host.blib"))
                print('\rRe-initiating protocols...', flush=True)
                new_data()
            elif ans.lower()=='n':
                print('Cancelling...')
            else:
                print('Unknown read string.\nCancelling...')
        else:
            print('Initiating fallback...')
            wait(3)
            print('Cleaning corrupt data...')
            os.remove(os.path.join(os.path.dirname(__file__), "lib-host.blib"))
            raise Exception
    except:
        if bool==True:
            print('Stablizing protocol completed.\n\tnew-user protocol -force /0\nStarting new-user protocol...')
        else:
            print('No pre-loaded data found. Initiating new-user protocol...')
        user=input('user: ')
        host=input('host: ')
        password=getpass('password>>')
        if password=='':
            print('Filling default data')
            password='#None*~'
        passt=input('Password Toggle? 1. True(True) 2. False\n\tlib-help->For "True", you have to enter password everytime you perform high-authority tasks.\n[Option:]')
        if passt=='2':
            passt='False'
            print('Toggle: False')
        elif passt=='1':
            passt='True'
            print('Toggle: True')
            wait(2)
        elif '2' in passt:
            passt='False'
            print('Not correct sequence.\nFollowing conditional protocol...\tToggle: False')
            wait(2)
        else:
            passt='True'
            print('Not correct sequence.\nFollowing default protocol...\tToggle: False')
            wait(2)
        print('\rLoading...', end='', flush=True)
        wait(1)
        print('\rEncrypting data...', end='', flush='')
        wait(1)
        print('\rEncrypting user...', end='', flush='')
        wait(1)
        user=libED.libcrypt(user, 'encrypt', security_level=3)
        wait(1)
        print('\rEncrypting host...', end='', flush='')
        wait(1)
        host=libED.libcrypt(host, 'encrypt', security_level=3)
        wait(1)
        print('\rEncrypting password...', end='', flush='')
        wait(1)
        password=libED.libcrypt(password, 'encrypt', security_level=4)
        wait(1)
        print('\rCompiling encrypted data...', end='', flush='')
        wait(1)
        passt=libED.libcrypt(passt, 'encrypt', security_level=3)
        wait(1)
        print('\rStoring encrypted data...  ', end='', flush='')
        wait(1)
        print('Done!')
        wait(1)
        print('\rProcessing data...', end='', flush=True)
        wait(1)
        print('\rCompressing data...12%', end='', flush=True)
        wait(1)
        user=libED.compresser(user)
        wait(1)
        print('\rCompressing data...24%', end='', flush=True)
        wait(1)
        host=libED.compresser(host)
        wait(1)
        print('\rCompressing data...56%', end='', flush=True)
        wait(1)
        password=libED.compresser(password)
        wait(1)
        print('\rCompressing data...78%', end='', flush=True)
        wait(1)
        passt=libED.compresser(passt)
        wait(1)
        print('\rCompressing data...98%', end='', flush=True)
        wait(1)
        print('\rCompressing data...99%', end='', flush=True)
        wait(1)
        print('\rCompressing data...100%', end='', flush=True)
        wait(1)
        print('\rCompressing data...Completed!', end='\n', flush=True)
        with open(os.path.join(os.path.dirname(__file__), "lib-host.blib"), 'w') as file:
            file.write(f'{user}\n{host}\n{password}\n{passt}')

def load_data():
    try:
        with open(os.path.join(os.path.dirname(__file__), "lib-host.blib"), 'r') as file:
            data=file.read()
            try:
                data=data.split('\n')
                print('Fetching data...', flush=True)
                user=data[0]
                host=data[1]
                password=data[2]
                passt=data[3]
                print('\rDecoding data...22%', flush=True, end='')
                wait(1)
                user=libED.decompresser(user)
                user=libED.libcrypt(user, 'decrypt', security_level=3)
                wait(1)
                print('\rDecoding data...44%', flush=True, end='')
                wait(1)
                host=libED.decompresser(host)
                host=libED.libcrypt(host, 'decrypt', security_level=3)
                wait(1)
                print('\rDecoding data...72%', flush=True, end='')
                wait(1)
                password=libED.decompresser(password)
                password=libED.libcrypt(password, 'decrypt', security_level=4)
                wait(1)
                print('\rDecoding data...89%', flush=True, end='')
                wait(1)
                passt=libED.decompresser(passt)
                passt=libED.libcrypt(passt, 'decrypt', security_level=3)
                wait(1)
                print('\rDecoding data...99%', flush=True, end='')
                wait(1)
                print('\rProcess:Decoding data...Completed!', end='\n', flush=True)
                return [user, host, password, passt]
            except:
                print('libdir->Error::"Unable to load data. Failure response from data-processing protocol."')
                raise Exception
    except:
        new_data(True)