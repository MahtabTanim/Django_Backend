from urllib.request import urlopen

with urlopen('http://localhost:3000/lyrics/') as response:
    data = response.read()
    encoding = response.headers.get_content_charset()
    string = data.decode(encoding)

print(string)