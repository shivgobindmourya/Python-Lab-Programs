import traceback
import logging

# Configure error logging
logging.basicConfig(
    filename="error_log.txt",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Custom exception classes
class InvalidFileFormatError(Exception):
    pass

class EmptyFileError(Exception):
    pass


def parse_file(filename):
    file = None

    try:
        # Open the file
        file = open(filename, "r")

        print("\nReading file:", filename)

        # Read file contents
        data = file.read()

        # Check whether file is empty
        if not data.strip():
            raise EmptyFileError("The file is empty!")

        # Validate file format
        if not filename.endswith(".txt"):
            raise InvalidFileFormatError(
                "Only .txt files are supported!"
            )

        # Parse file contents
        lines = data.splitlines()

        print("\nFile parsed successfully!")
        print("Total lines:", len(lines))

        print("\nFile Contents:")
        for line_number, line in enumerate(lines, start=1):
            print(f"{line_number}: {line}")

    except FileNotFoundError:
        error = traceback.format_exc()
        logging.error("File not found:\n%s", error)
        print("Error: File does not exist!")

    except PermissionError:
        error = traceback.format_exc()
        logging.error("Permission denied:\n%s", error)
        print("Error: Permission denied!")

    except (InvalidFileFormatError, EmptyFileError) as e:
        error = traceback.format_exc()
        logging.error("File parsing error:\n%s", error)
        print("Parsing Error:", e)

    except Exception:
        error = traceback.format_exc()
        logging.error("Unexpected error:\n%s", error)
        print("An unexpected error occurred!")

    else:
        print("\nELSE: File processing completed successfully.")

    finally:
        if file is not None:
            file.close()
            print("\nFINALLY: File resource closed safely.")
        else:
            print("\nFINALLY: No file resource was opened.")


# Main program
if __name__ == "__main__":

    filename = input("Enter the file name: ")

    parse_file(filename)