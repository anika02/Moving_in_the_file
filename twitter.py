import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl


def moving_in_file(js):
    """
    This is recursion which allow us to move in JSON file
    and find information what we want
    """
    print("\n" + '-' * 20)
    count = 1
    it_is_dict = False
    if type(js) == list:
        if len(js) == 0:
            return js
        for i in js:
            if type(i) == dict:
                lst = []
                it_is_dict = True
                for j in i:
                    # print(j, type(i[j]), type(i[j]) == list, type(i[j]) == dict)
                    if (type(i[j]) == list) or (type(i[j]) == dict):
                        lst.append(j)
                    else:
                        # print("GHFTJTJJTJGKGKJGFK")
                        lst.append((j, i[j]))
                print(count, lst)
                print()
                count += 1
        if it_is_dict:
            while True:
                number = input("Виберіть список ввівши номер списка (число, що стоїть зліва від нього): ")
                try:
                    number = int(number)
                except:
                    pass
                if (type(number) == int) and (0 < number <= len(lst)):
                    return moving_in_file(js[number-1])
        else:
            return js
    elif type(js) == dict:
        for i in js:
            print(i)
        while True:
            key1 = input("Введіть правильно назву вибраного Вами пункту із запропунованих: ")
            if key1 in js:
                break
        return moving_in_file(js[key1])
    else:
        return js


# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print('')
acct = input('Enter Twitter Account:')
if (len(acct) > 0):
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '5'})
    # print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()

    js = json.loads(data)
    try:
        print(moving_in_file(js))
    except:
        print("Введіть правильну назву акаунту!")