# The moving in the JSON file

The moving in JSON file is a Python modules for moving in the JSON file from Twitter.


## Important

You must print your keys in **hidden.py**


## Usage

```python
import urllib.request, urllib.parse, urllib.error
connection = urllib.request.urlopen(url, context=ctx)
data = connection.read().decode()

import json
js = json.loads(data)

import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
```

## Conclusion

With this modules we can move in file by printing the item where we want go to. For helping us this modules prints all possible items and we just must choose one of them.

## Example

>Enter Twitter Account:`@Ann00000000`\
>\
>--------------------\
>users\
>next_cursor\
>next_cursor_str\
>previous_cursor\
>previous_cursor_str\
>total_count\
>Введіть правильно назву вибраного Вами пункту із запропунованих: `users`\
>\
>--------------------\
>1 [('id', 3351638), ('id_str', '3351638'), ('name', '방탄소년단'), ('screen_name', 'BTS_twt'), ('location', ''), ('description', 'Hi! We are BTS!!'), ('url', 'https://t.co/BP79N8Xkk'), ('followers_count', 24137453), ('friends_count', 131)]\
>\
>2 [('id', 10290729929267238), ('id_str', '10290729929267238'), ('name', 'Ужасные мемы'), ('screen_name', 'so_mad_so_funny'), ('location', ''), ('description', 'кекнутый'), ('url', 'https://t.co/LFKBn8pdt'), ('followers_count', 321303), ('friends_count', 4)]\
>\
>Виберіть список ввівши номер списка (число, що стоїть зліва від нього): `1`\
>\
>--------------------\
>id\
>id_str\
>name\
>screen_name\
>location\
>description\
>url\
>followers_count\
>friends_count\
>Введіть правильно назву вибраного Вами пункту із запропунованих: `friends_count`\
>\
>--------------------\
>**131**