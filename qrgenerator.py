import qrcode

#website link
url_link = "https://aquakeepers.business.site"

#generating empty qr code
qr = qrcode.QRCode(version=5,
                   box_size=10,
                   border=3)
#adding link to qr
qr.add_data(url_link)
qr.make(fit=True)
img = qr.make_image()

#saving qr code to img file
img.save('new_qrLink.png')