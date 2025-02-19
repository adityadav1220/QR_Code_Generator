import qrcode
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

data = input("Please input the text or URL you want to generate a QR Code for:")

qr = qrcode.QRCode(version=4, box_size=15, border=2)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill="black", back_color="white")

file_name = "qr_code.png"
img.save(file_name)

plt.imshow(img, cmap="gray")
plt.axis("off")  # Hide axes
plt.title("Generated QR Code")
plt.show()

print("QR code generated successfully! Check qr_code.png")