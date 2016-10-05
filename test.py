from docker import Client

eng_list = []
eng_active = []
lh = True


def create_new():
    pass


def list_container():
    pass


def connect():
    def show():
        if len(eng_list) < 0:
            print('No docker-engine  connected ')
        else:
            print('List of Engine are:')
            j = 1
            for i in eng_list:
                print(j, 'Name', ['name'], '\nDescription', i['description'], 'Connected to ', i['con'])
                j += 1

    def acivate():
        show()
        x = input('Engine want to active (seprated by comma)').split(',')
        for i in x:
            if int(i) <= len(eng_list):
                eng_active.append(int(i))

    def new():
        name = str(input('Enter name :'))
        disc = str(input('Enter Description:'))
        while True or lh == False:
            s = str(input('want to connect to this system [Y/N]'))
            if s == 'Y' or s == 'y':
                con = 'unix://var/run/docker.sock'
                ''.lh = False
                break
            elif s == 'N' or s == 'n':
                con = str(input('Enter docker address'))
                break
        try:
            eng_list.append({'name': name, 'description': disc, 'socket': Client(base_url=con), 'con': con})
            eng_list[len(eng_list) - 1]['socket'].containers()
        except ConnectionError:
            print("Unable to connect", con, "\ncheck confection and try again")
            new()


def menu():
    def e():
        print('\nPlease Select correct option')
        menu()

    print('''1)Connect/Modify to docker-engine\n2) Create New Container  \n3)List Container ''')
    try:
        r = int(input('Enter your choice'))
    except ValueError:
        e()
    except KeyboardInterrupt:
        print('Byee.....')
    else:
        if r == 1:
            connect()
        elif r == 2:
            create_new()
        elif r == 3:
            list_container()
        else:
            e()


menu()
