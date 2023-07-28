import os

hosts_path = r'C:\Windows\System32\drivers\etc\hosts'
example_org = 'api.openai.com'
ip_address = '127.0.0.1'

option = input('Enter 1 to add api.openai.com to hosts or 2 to remove api.openai.com from hosts: ')

if option == '1':
    with open(hosts_path, 'r') as f:
        if example_org in f.read():
            print('api.openai.com already in hosts')
        else:
            with open(hosts_path, 'a') as f:
                f.write(f'{ip_address} {example_org}\n')
            print('successfully added api.openai.com to hosts')
elif option == '2':
    with open(hosts_path, 'r') as f:
        lines = f.readlines()
        found = False
        for i, line in enumerate(lines):
            if example_org in line:
                lines.pop(i)
                found = True
        if found:
            with open(hosts_path, 'w') as f:
                f.writelines(lines)
            print('successfully removed api.openai.com from hosts')
        else:
            print('there wasn\'t an api.openai.com instance in hosts')
else:
    print('Invalid option')