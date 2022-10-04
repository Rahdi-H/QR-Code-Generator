import qrcode
from PIL import Image

img = qrcode.make('WWW.google.com')
img.save('qrcodetest.png')