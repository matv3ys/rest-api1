from requests import get, post, put, delete

print(delete('http://localhost:5000/api/users/9').json())