import qrcode
from PIL import Image, ImageOps

def generate_qr_code(data, icon_path, output_path):
    # Create the QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=1,
    )

    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code
    qr_image = qr.make_image(fill_color="black", back_color="white")

    # Open the custom icon image with transparency
    icon = Image.open(icon_path).convert("RGBA")

    # Resize the icon to fit the QR code
    icon = icon.resize((qr_image.size[0] // 4, qr_image.size[1] // 4), Image.ANTIALIAS)

    # Set the alpha (transparency) value for the icon
    alpha = 150  # Adjust this value (0 to 255) to control the transparency
    icon.putalpha(alpha)

    # Calculate the position to center the icon in the QR code
    icon_position = ((qr_image.size[0] - icon.size[0]) // 2, (qr_image.size[1] - icon.size[1]) // 2)

    # Create a new image with alpha channel (transparency)
    result = Image.new("RGBA", qr_image.size, (255, 255, 255, 0))

    # Paste the QR code onto the new image
    result.paste(qr_image, (0, 0))

    # Paste the icon onto the new image, using alpha_composite to preserve transparency
    result.paste(icon, icon_position, icon)

    # Save the final image in PNG format
    result.save(output_path, format="PNG")

def main():
    data_to_encode = "https://www.youtube.com"
    custom_icon_path = r"J:\python\qrcode\QR-code-langind-page\CI_icon.png"
    output_image_path = r"J:\python\qrcode\QR-code-langind-page\output\output.png"

    generate_qr_code(data_to_encode, custom_icon_path, output_image_path)

if __name__ == "__main__":
    main()
