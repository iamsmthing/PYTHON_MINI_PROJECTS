import pyqrcode
import png

s =input("Enter the text you want to convert in to QR code:")
url = pyqrcode.create(s)
url.png('myqr1.png', scale = 10)
