from PIL import Image, ImageFilter
import sys
import os

# Check if command-line arguments were provided
if len(sys.argv) > 1:
    # Access the arguments starting from index 1
    # as the index 0 is the script name
    arguments = sys.argv[1:]

    # Process the arguments
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Specify the name of the new folder
    try:
        folder_name = f"{arguments[0]}"

    # Create the folder path by joining the current directory with the folder name
        folder_path = os.path.join(current_directory, folder_name)
        print("Bal")
        os.mkdir(folder_path)
        print("meh")
    except FileExistsError:
        print("Folder already exits.")

    # Specify the path and filename of the input JPG image
    # input_folder_path = "./Pokedex"
    # output_folder_path = "./new_pics"

    input_folder_path = f"{arguments[0]}"
    output_folder_path = f"{arguments[1]}"

    # Loop through all files in the folder
    for filename in os.listdir(input_folder_path):
        # Construct the full file path
        input_file_path = os.path.join(input_folder_path, filename)
        # string = f"{filename}"
        # substring = ".jpg"
        #
        # filename = string.rstrip(substring)

        output_file_path = os.path.join(output_folder_path, filename)

        input_image_path = f"{input_file_path}"

        # Specify the path and filename for the output PNG image
        # output_image_path = f"{output_file_path}"
        output_image_path = os.path.splitext(output_file_path)[0] + ".png"

        # Open the input image
        image = Image.open(input_image_path)

        # Convert the image to PNG format
        image.save(output_image_path, "png")

else:
    print("No command-line arguments provided.")
