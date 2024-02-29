import qrcode
from PIL import Image, ImageOps

def generate_qr_code_with_logo(data, icon_path, output_path):
    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=1,
    )
    qr.add_data(data)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white").convert('RGB')

    # Load the logo
    icon = Image.open(icon_path)
    icon_w, icon_h = icon.size

    # Calculate the size of the logo as a fraction of the QR code size
    factor = 4  # Example: logo size = 1/4 of the QR code size
    size_w = int(qr_image.size[0] / factor)
    size_h = int(qr_image.size[1] / factor)
    icon = icon.resize((size_w, size_h), Image.LANCZOS)

    # Calculate the position to place the logo
    pos_w = (qr_image.size[0] - size_w) // 2
    pos_h = (qr_image.size[1] - size_h) // 2

    # Create a clear space for the logo
    # Note: This simplistic approach clears a rectangle area. For more complex QR codes, you may need a more nuanced approach.
    clear_space = (pos_w, pos_h, pos_w + size_w, pos_h + size_h)
    clear_img = Image.new('RGB', (size_w, size_h), 'white')
    qr_image.paste(clear_img, clear_space)

    # Place the logo
    qr_image.paste(icon, (pos_w, pos_h), mask=icon)

    # Save the result
    qr_image.save(output_path, format="PNG")

def main():
    data_to_encode = "https://pea-phase2-sticker-information.glitch.me/?serialNumber=FGT60FTK23099B2G"
    custom_icon_path = r"J:\python\qrcode\QR-code-langind-page\CI_icon.png"
    output_image_path = r"J:\python\qrcode\QR-code-langind-page\output\output.png"

    generate_qr_code_with_logo(data_to_encode, custom_icon_path, output_image_path)

if __name__ == "__main__":
    main()
