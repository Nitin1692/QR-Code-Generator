import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=4,
    border=4,
)
qr.add_data('https://drive.google.com/file/d/1JcRan6rLFJYfMGC6Gbwv_MRnEVGw7713/view?usp=sharing')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("QR_Code.png")