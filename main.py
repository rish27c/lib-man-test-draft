try:
    print('Initializing...', flush=True, end='')
    import os
    print('Done')
except:
    print("Failed!\nError: Incorrect python execution. Python lacks basic processes.", flush=True)
    input()
    exit(1)
try:
    print('Stabilizing...', flush=True, end='')
    from time import sleep as wait
    print('Done!')
except:
    print('Failed!\nError!\nWarning! Python lacks basic functionality.', flush=True)
    input()
    os.sys.exit(1)
print('Activating...Done!', flush=True)
try:
    print('Importing mysql...', flush=True, end='')
    import mysql.connector
    print('Done!')
except:
    print('Error!\nlibman->Error: Unable to import.', flush=True)
    try:
        print('Attempting Patch #1...', end='', flush=True)
        os.system('pip install mysql-connector-python')
        os.system('pip3 install mysql-connector-python')
        import mysql.connector
        print('Done', flush=True)
    except:
        print('\nUnable to Patch.\nlibman->Fallback::Re-attempting patch #2', flush=True)
        os.system('pip uninstall mysql-connector-python')
        os.system('pip uninstall mysql')
        os.system('pip uninstall mysql-client')
        os.system('pip install mysql-connector-python')
        os.system('pip3 uninstall mysql-connector-python')
        os.system('pip3 uninstall mysql')
        os.system('pip3 uninstall mysql-client')
        os.system('pip3 install mysql-connector-python')
        print('Patch #2 Protocol Completion Confirmed...', flush=True)
        try:
            print('Re-attempting import..', flush=True)
            import mysql.connector
            print('Imported mysql-connector', flush=True)
        except:
            print('libman->Callback:return::Unable to import module "mysql-connector"\n\t\tManually install mysql-connector-python in your system.', flush=True)
            wait(5)
            os.sys.exit(1)
try:
    print('libman->Calling:: libdir')
    import libdir
except:
    print('libman->Error: Incomplete lib-manage file detected.')
    wait(5)
    os.sys.exit(1)

def printf(word:Any):
    print(word, flush=True, end='')

def run():
    err=0
    while err<2:
        try:
            printf('Checking for pre-existing data...\n')
            with open(os.path.join(os.path.dirname(__file__), "lib-host.blib"), 'r') as file:
                printf('Data found!\n')
            data=libdir.load_data()
            user=data[0]
            host=data[1]
            password=data[2]
            passt=data[3]
            if password=='#None*~':
                password=''
            if passt=='False':
                passt=False
            else:
                passt=True
            break
        except:
            try:
                libdir.new_data()
                err+=1
            except:
                printf('Fallback->Error: "No response from libdir protocols."\n')
                error=True
                err=2
    if err!=2:
        printf('Data-processing protocol completion confirmed.\n')
    else:
        printf('libman->libdir:Error::"Invalid data-processing protocol."\n')
        wait(5)
        os.sys.exit(1)
    try:
        printf('Building mysql connection...\n')
        mybd=mysql.connector.connect(user=user, host=host, password=password, database='libtest')
    except:
        try:
            mydb=mysql.connector.connect(user=user, host=host, password=password)
            cur=mydb.cursor()
            cur.execute('CREATE DATABASE libtest')
            mydb=mysql.connector.connect(user=user, host=host, password=password, database='libtest')
        except:
            printf('libdir->libman:Error::"Unable to stabilize connection with sql-database."\n\tCalling rescue-mode...\n')