import os

# Define the header and footer signatures to search for
HEADER = b"ENter Header"
FOOTER = b"Enter Footer here"

# Define the path to the .dd image file
IMAGE_PATH = "path/to/img"

# Define the output directory for the carved files
OUTPUT_DIR = "path/to/output/dir"

# Open the .dd image file in binary mode
with open(IMAGE_PATH, "rb") as f:
    # Read the entire contents of the file
    data = f.read()

# Find all occurrences of the header and footer signatures in the data
matches = []
header_pos = data.find(HEADER)
footer_pos = data.find(FOOTER)
while header_pos != -1 and footer_pos != -1:
    # If the footer comes before the header, skip to the next footer
    if footer_pos < header_pos:
        footer_pos = data.find(FOOTER, footer_pos + len(FOOTER))
        continue
    
    # Add the current header and footer positions to the list of matches
    matches.append((header_pos, footer_pos + len(FOOTER)))
    
    # Search for the next header and footer positions
    header_pos = data.find(HEADER, footer_pos + len(FOOTER))
    footer_pos = data.find(FOOTER, footer_pos + len(FOOTER))
    print(header_pos)
# Carve the files from the data based on the matched positions
for i, match in enumerate(matches):
    print(match)
    # Extract the file data from the matched positions
    file_data = data[match[0]:match[1]]
    
    # Define the output file path for the carved file
    output_path = os.path.join(OUTPUT_DIR, f"file_{i}")
    
    # Write the carved file data to the output file
    with open(output_path, "wb") as f:
        f.write(file_data)
