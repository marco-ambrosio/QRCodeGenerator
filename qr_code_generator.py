from tkinter import simpledialog
import qrcode
import sys


answer = simpledialog.askstring("Inserire URL", "Inserire URL da convertire in QR Code")
if answer is not None:
    qr = qrcode.make(answer)
    qr.save("qrcode.png")
sys.exit(0)