import qrcode


# birinci yöntem
code = qrcode.make("https://www.linkedin.com/in/erg%C3%BCl%C3%BC-bozkurt-82345323b/?lipi=urn%3Ali%3Apage%3Ad_flagship3_feed%3Bxrkpld0oS3C%2BIlav3HzsMg%3D%3D")
code.save("Try/resim.png")

# ikinci yöntem
code = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=8,
    border=1
)
code.add_data("https://www.linkedin.com/in/erg%C3%BCl%C3%BC-bozkurt-82345323b/?lipi=urn%3Ali%3Apage%3Ad_flagship3_feed%3Bxrkpld0oS3C%2BIlav3HzsMg%3D%3D")
code.make(fit=True)

image = code.make_image(fill_color = "black", back_color="white")
image.save("Try/resim2.png")