from PIL import Image, ImageFilter
import os

# 1. Open an image
def open_image():
    global img

    path = input("Enter image path (JPEG/PNG): ").strip().strip('"')

    try:
        img = Image.open(path).convert("RGB")
        print("\nImage opened successfully!")
        print("Image size:", img.size)
        print("Image format:", Image.open(path).format)

    except FileNotFoundError:
        print("Error: Image file not found!")

    except Exception as e:
        print("Error opening image:", e)


# 2. Convert image to grayscale using RGB values
def convert_grayscale():
    global img

    if img is None:
        print("Please open an image first!")
        return

    width, height = img.size
    pixels = img.load()

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            # Calculate grayscale intensity
            gray = int(0.299 * r + 0.587 * g + 0.114 * b)

            pixels[x, y] = (gray, gray, gray)

    print("Grayscale conversion completed!")


# 3. Convert image to black and white using thresholding
def convert_threshold():
    global img

    if img is None:
        print("Please open an image first!")
        return

    try:
        threshold = int(input("Enter threshold value (0-255): "))

        if not 0 <= threshold <= 255:
            print("Threshold must be between 0 and 255!")
            return

        width, height = img.size
        pixels = img.load()

        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]

                # Calculate pixel brightness
                gray = int(0.299 * r + 0.587 * g + 0.114 * b)

                if gray >= threshold:
                    pixels[x, y] = (255, 255, 255)
                else:
                    pixels[x, y] = (0, 0, 0)

        print("Black and white thresholding completed!")

    except ValueError:
        print("Please enter a valid integer!")


# 4. Apply a simple blur filter
def apply_blur():
    global img

    if img is None:
        print("Please open an image first!")
        return

    img = img.filter(ImageFilter.BLUR)
    print("Blur filter applied successfully!")


# 5. Display image
def display_image():
    if img is None:
        print("Please open an image first!")
        return

    img.show()


# 6. Save processed image
def save_image():
    if img is None:
        print("Please open an image first!")
        return

    path = input(
        "Enter output filename (e.g., output.png): "
    ).strip().strip('"')

    if not path:
        print("Filename cannot be empty!")
        return

    try:
        # Ensure the output has a supported extension
        extension = os.path.splitext(path)[1].lower()

        if extension not in (".png", ".jpg", ".jpeg"):
            print("Use a .png, .jpg, or .jpeg filename!")
            return

        img.save(path)
        print("Image saved successfully at:", os.path.abspath(path))

    except Exception as e:
        print("Error saving image:", e)


# 7. Main menu
img = None

def main():
    while True:
        print("\n====== IMAGE PROCESSING MINI-TOOL ======")
        print("1. Open Image")
        print("2. Convert to Grayscale")
        print("3. Black and White Thresholding")
        print("4. Apply Blur Filter")
        print("5. Display Image")
        print("6. Save Processed Image")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            open_image()

        elif choice == "2":
            convert_grayscale()

        elif choice == "3":
            convert_threshold()

        elif choice == "4":
            apply_blur()

        elif choice == "5":
            display_image()

        elif choice == "6":
            save_image()

        elif choice == "7":
            print("Exiting Image Processing Mini-Tool. Goodbye!")
            break

        else:
            print("Invalid choice! Please select 1-7.")


if __name__ == "__main__":
    main()

