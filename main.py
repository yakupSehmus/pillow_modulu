from PIL import Image, ImageFilter

image = Image.open("özil.jpg")

image.save("özil2.jpg")

image.rotate(180).save("özil3.jpg")#resmi döndürür

image.rotate(90).save("özil4.jpg")

image.convert(mode = "L").save("özil5.jpg")#siyah beyaz

degistir = (960, 600)

image.thumbnail(degistir)

image.save("özil6.jpg")#boyut ayarladık

image.filter(ImageFilter.GaussianBlur(5)).save("özil7.jpg")#blurlaştırdık

kırpılacak_alan = (100,0,950,600)
image2 = Image.open("fenerbahçe.jpg")
image2.crop(kırpılacak_alan).save("fenerbahçe2.jpg")#kırmak için
