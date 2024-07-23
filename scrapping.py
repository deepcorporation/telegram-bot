import requests
from bs4 import BeautifulSoup

# URL de la página web a scrapear
url = 'https://www.ejemplo.com/productos'

# Realizar la solicitud HTTP
response = requests.get(url)

# Verificar que la solicitud sea exitosa
if response.status_code == 200:
    # Parsear el contenido HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Encontrar todos los elementos de productos (suponiendo la estructura HTML)
    productos = soup.find_all('div', class_='producto')
    
    # Iterar sobre cada producto y extraer nombre y precio
    for producto in productos:
        nombre = producto.find('h2', class_='nombre-producto').text.strip()
        precio = producto.find('span', class_='precio').text.strip()
        
        print(f'Producto: {nombre}, Precio: {precio}')
else:
    print('Error al conectar con la página web')
