import qrcode

# Data to encode
data ="any name"
qrcode = qrcode.make(data)
# Save the QR code as an image file
qrcode.save("qrcode.png")
# Display the QR code   
print("QR code generated and saved as 'qrcode.png'.")



