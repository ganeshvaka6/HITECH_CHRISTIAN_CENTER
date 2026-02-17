
import qrcode

APP_BASE_URL = "https://hitech-seat-booking.onrender.com"

endpoint = "/"
full_url = f"{APP_BASE_URL.rstrip('/')}{endpoint}"

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(full_url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("qr_code.png")

print("QR code generated for:", full_url)
