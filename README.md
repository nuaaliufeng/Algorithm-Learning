# Algorithm-Learning

~~~PYTHON
# api https://api.github.com/repos/nuaaliufeng/Algorithm-Learning

# web_page https://github.com/nuaaliufeng/Algorithm-Learning

import requests
import webbrowser
import time

api = 'https://api.github.com/repos/nuaaliufeng/Algorithm-Learning'
web_page = 'https://github.com/nuaaliufeng/Algorithm-Learning'
last_update = None
all_info = requests.get(api).json()
cur_update = all_info['updated_at']
print(cur_update)

while True:
    all_info = requests.get(api).json()
	cur_update = all_info['updated_at']
    if not last_update:
        last_update = cur_update
    if last_update < cur_update:
    	webbrowser.open(web_page)
	time.sleep(600)
~~~





    if last_update < cur_update:
        webbrowser.open(web_page)
    time.sleep(600)
