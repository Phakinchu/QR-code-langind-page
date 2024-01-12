import qrcode

def generate_qr_code(text, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

if __name__ == "__main__":
    text_to_encode = "S/N: FG10E0TB21900043\n Exp Date:5 ปี นับจากวันรับมอบพัสดุ\nContract Info:อุปกรณ์ชำรุดแจ้ง 095-956-8396 หรือ หมายเลข 9960 (ITIL กฟภ.) "
    output_filename = "J:\python\qrcode\QR-code-langind-page\output\output.png"

    generate_qr_code(text_to_encode, output_filename)
    print(f"QR code saved as {output_filename}")
