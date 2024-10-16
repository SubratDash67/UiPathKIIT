from PIL import Image
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import ImageFormatter
import io


def convert_python_to_jpeg(python_file_path, output_image_path):
    # Read the Python file
    with open(python_file_path, "r") as file:
        code = file.read()

    # Use Pygments to apply syntax highlighting and create an image
    formatter = ImageFormatter(
        font_name="Consolas", font_size=18, line_numbers=True, style="material"
    )
    data = highlight(code, PythonLexer(), formatter)

    # Convert the image data to a Pillow Image object
    image = Image.open(io.BytesIO(data))

    # Calculate the aspect ratio to resize the image properly
    aspect_ratio = image.width / image.height
    new_width = 1920
    new_height = int(new_width / aspect_ratio)

    # Resize the image to HD resolution (1920x1080) while maintaining aspect ratio
    hd_image = image.resize((new_width, new_height), Image.LANCZOS)

    # Save the image as a JPEG file
    hd_image.save(output_image_path, "JPEG", quality=95)


if __name__ == "__main__":
    # Specify the path to the Python file and the output JPEG file
    python_file_path = "trading_system.py"  # Change this to your Python file path
    output_image_path = "example3.jpg"  # Change this to your desired output path

    convert_python_to_jpeg(python_file_path, output_image_path)
    print(f"Python file {python_file_path} has been converted to {output_image_path}")
