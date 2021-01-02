# api https://api.github.com/repos/nuaaliufeng/Algorithm-Learning
# web_page https://github.com/nuaaliufeng/Algorithm-Learning

import requests

api = 'https://api.github.com/repos/nuaaliufeng/Algorithm-Learning'
last_update = None
all_info = requests.get(api).json()
cur_update = all_info['updated_at']
print(cur_update)

# if last_update < cur_update:
#     open(webpage)
