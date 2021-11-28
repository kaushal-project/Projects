# 

import qrcode
import image
import os

qr = qrcode.QRCode(
    version= 15, # 15 means the version of the qr code (higher the number bigger the code image, and complicated picture)
    box_size = 10, # size of the box where qr code will be displayed
    border = 5, # it is the white part of image -- border in all 4 sides with white color
)


# Taking Input
name = input("Name :- ")
email = input("Email :- ")
dob = input("DOB (DD-MM-YYYY) :- ")
mobile = input("Mobile Number :- ")
address = input("Address :- ")

# Data
data = f"Name :- {name}\nEmail :- {email}\nDOB :- {dob}\nMobile-Number :- {mobile}\nAddress :- {address}"

# 
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill="black",back_color="white")
outputDir = os.getcwd() + "/qrCodeGenerator/output/img-qrcode.png"
img.save(outputDir)
