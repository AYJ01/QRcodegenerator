import qrcode
import numpy as np
data = input("Enter the URL : ")
qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data(data)
qr.make()
print("The shape of the QR image:", np.array(qr.get_matrix()).shape)
img = qr.make_image(fill_color="white", back_color="black")
img.save("site_inversed.png")
