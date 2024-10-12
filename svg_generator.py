import qrcode
from qrcode.image.svg import SvgImage
from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener la URL desde las variables de entorno
url = os.getenv("URL")

# Crear un objeto QRCode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Agregar la URL al objeto QRCode
qr.add_data(url)
qr.make(fit=True)

# Generar el código QR en formato SVG
img = qr.make_image(image_factory=SvgImage)

fileName = os.getenv("fileName")

# Especificar la ruta de guardado
ruta_guardado = f"./{fileName}.svg"

ruta_escritorio = os.path.join(os.path.expanduser("~"), "Desktop")

# Guardar el archivo SVG
with open(ruta_guardado, "wb") as f:
    img.save(f)
