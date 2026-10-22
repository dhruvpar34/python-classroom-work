import qrcode

url = input("enter url of the website")
filename = input("enter the filename you want to save as :")

if not (filename.endswith(".png")):
    filename = filename + ".png"

img = qrcode.make(url)
img.save(filename)