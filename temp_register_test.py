import http.client
import json

conn = http.client.HTTPConnection('localhost', 8081)
payload = json.dumps({
    'username': 'testuser7',
    'email': 'test7@example.com',
    'password': 'password123',
    'mobileNumber': '1234567890'
})
headers = {
    'Content-Type': 'application/json'
}
conn.request('POST', '/api/auth/register', payload, headers)
r = conn.getresponse()
print(r.status, r.reason)
print(r.read().decode())
