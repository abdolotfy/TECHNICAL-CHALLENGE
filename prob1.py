import os
import shutil
from PIL import Image
import csv

# Function to copy images from subfolders to a single folder
def copy_images(src_folder, dest_folder):
    for root, _, files in os.walk(src_folder):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
                src_path = os.path.join(root, file)
                dest_path = os.path.join(dest_folder, file)
                shutil.copy(src_path, dest_path)

# Function to process images and create a CSV report
def generate_image_report(image_folder, report_file):
    with open(report_file, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Image Name", "Image Size (bytes)", "Last Modification Date"])

        for filename in os.listdir(image_folder):
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
                image_path = os.path.join(image_folder, filename)
                image = Image.open(image_path)
                image_name = filename.split('-', 1)[-1]  # Discard prefix
                image_size = os.path.getsize(image_path)
                last_modification_date = os.path.getmtime(image_path)
                csv_writer.writerow([image_name, image_size, last_modification_date])

if __name__ == "__main__":
    # Define your source folder and destination folder
    source_folder = "C:\\Users\\HP\\Downloads\\dairies"
    destination_folder = "C:\\Users\\HP\\Documents\\task"

    report_file = "image_report.csv"

    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Copy images from subfolders to the destination folder
    copy_images(source_folder, destination_folder)

    # Generate the image report
    generate_image_report(destination_folder, report_file)

    print("Images copied to destination folder.")
    print(f"Image report saved as '{report_file}'")

