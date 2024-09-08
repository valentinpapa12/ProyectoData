import requests

print(requests.get("http://127.0.0.1:8000/get_word_count/hulu/the").json())