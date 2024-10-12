import qrcode
from qrcode.image.pil import PilImage
from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener la URL y los colores desde las variables de entorno
url = os.getenv("URL")
fill_color = os.getenv("FILL_COLOR", "black")  # Color del QR
back_color = os.getenv("BACK_COLOR", "white")  # Color de fondo
fileName = os.getenv("FILE_NAME")

# Crear un objeto QRCode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border= 3,
)

# Agregar la URL al objeto QRCode
qr.add_data(url)
qr.make(fit=True)

# Generar el código QR en formato PNG con colores personalizados
img = qr.make_image(image_factory=PilImage, fill_color=fill_color, back_color=back_color)

# Especificar la ruta de guardado
ruta_guardado = f"./{fileName}.png"

# Guardar el archivo PNG
with open(ruta_guardado, "wb") as f:
    img.save(f)