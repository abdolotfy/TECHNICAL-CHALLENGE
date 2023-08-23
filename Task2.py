import json

# Define the paths to input and output files
input_file_path = "C:\\Users\\HP\\Downloads\\problem2\\image1.txt"  # Replace with the actual path
output_file_path = "C:\\Users\\HP\\Documents\\JSON\\Task.py"    # Replace with the desired output path

# Read data from the input file
with open(input_file_path, "r") as input_file:
    data = input_file.readlines()

# Initialize the JSON structure
json_data = {
    "annotations": [
        {
            "result": []
        }
    ],
    "data": {
        "image": ""  # Placeholder for the image path (since there is no actual image)
    }
}

# Parse the data and add it to the JSON structure
for entry in data:
    parts = entry.strip().split()
    if len(parts) >= 5:
        # Keep the first number as is
        first_number = float(parts[0])

        # Start filling x from the second number, y from the third number,
        # width from the fourth number, and height from the fifth number
        x = float(parts[1]) * 88.77887
        y = float(parts[2]) * 44.00003
        width = float(parts[3]) * 100
        height = float(parts[4]) * 100

        annotation = {
            "image_rotation": 0,
            "value": {
                "x": x,
                "y": y,
                "width": width,
                "height": height,
                "rotation": 0,
                "rectanglelabels": ["object"]
            }
        }

        json_data["annotations"][0]["result"].append(annotation)



# Convert the JSON structure to a JSON string
json_string = json.dumps(json_data, indent=4)

# Write the JSON string to the output file
with open(output_file_path, "w") as output_file:
    output_file.write(json_string)

print(f"JSON data has been written to {output_file_path}")
