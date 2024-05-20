volume_text = "Vol. 35 (2024)"

# Find the index of the space character after "Vol."
space_index = volume_text.find(' ')

# Extract the volume number
if space_index != -1:
    volume_number = volume_text[space_index+1 : volume_text.find(' ', space_index+1)].strip()
    print("Volume:", volume_number)
else:
    print("Volume number not found.")
