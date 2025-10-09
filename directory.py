import os

# Create a new directory
os.mkdir("my_folder")
print("Directory 'my_folder' created.")

# List directories and files in the current path
print("Current directory contents:")
print(os.listdir())

# Rename the directory
os.rename("my_folder", "renamed_folder")
print("Directory renamed to 'renamed_folder'.")

# Delete the directory
os.rmdir("renamed_folder")
print("Directory 'renamed_folder' deleted.")
