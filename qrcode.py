import qrcode

# Create The variable to store the information
data = "Pavitra"

# Encode The Data
img = qrcode.make(data)

# Save the QR Code
img.save("QRCode.jpg")