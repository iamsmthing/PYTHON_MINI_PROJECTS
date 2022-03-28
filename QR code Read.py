from pyzbar import pyzbar

from PIL import Image
URL=input("Enter the URL of the QR image to be decoded:")
image = Image.open(URL)

qr_code = pyzbar.decode(image)[0]

data= qr_code.data.decode("utf-8")
print("----")
print("The Secret Message is :",data)
print("----")