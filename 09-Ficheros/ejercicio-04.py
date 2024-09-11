from urllib import request
from urllib.error import URLError


def contar_palabras(url):
    try:
        with request.urlopen(url) as f:
            contenido = f.read()
    except URLError:
        print(f"La url {url} no existe")
    else:
        return len(contenido.split())


print(contar_palabras('https://www.gutenberg.org/files/2000/2000-0.txt'))
print(contar_palabras(
    "https://raw.githubusercontent.com/asalber/asalber.github.io/master/README.md"))
