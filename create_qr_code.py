import qrcode
img = qrcode.make("https://simulation.almostaphysicist.com/",error_correction=qrcode.constants.ERROR_CORRECT_H)
img.save("public/qr_high_error_tol.png")