import qrcode
import qrcode.image.svg
import os

# pip install qrcode

fileName="URLs.txt"

exportDirectory="folderName"

with open(fileName) as f:
    URLs = [line.rstrip() for line in f]


if not os.path.exists(exportDirectory):
    os.makedirs(exportDirectory)

for url in URLs:
    img = qrcode.make(url, image_factory = qrcode.image.svg.SvgImage)

    filepath = exportDirectory + "/" + url.split("storeCode=",1)[1] + '.svg'

    with open(filepath, 'wb') as qr:
        img.save(filepath)
