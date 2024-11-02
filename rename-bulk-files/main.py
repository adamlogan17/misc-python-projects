import os

def capitalize_and_add_spaces(folder_path):
    # Iterate over all files in the specified folder
    for filename in os.listdir(folder_path):
        # Construct the full file path
        old_file_path = os.path.join(folder_path, filename)
        
        # Check if the path is a file
        if os.path.isfile(old_file_path):
            # Split the filename into name and extension
            name, extension = os.path.splitext(filename)
            
            # Replace underscores with spaces and convert to title case
            new_name = name.replace('_', ' ').title()
            
            # Combine the new name with the original extension
            new_filename = new_name + extension
            
            # Construct the new file path
            # new_file_path = os.path.join(folder_path, new_filename)
            
            # Rename the file
            # os.rename(old_file_path, new_file_path)
            print(f"Renamed '{filename}' to '{new_filename}'")
            
# Specify the folder path
folder_path = 'C:/Users/adam2/Documents/The Boys/EPUB'

# Call the function to rename files
# capitalize_and_add_spaces(folder_path)

def rename_files_to_match_pdfs(src_folder, dest_folder):
    # List all PDF files in the source folder
    pdf_files = [f for f in os.listdir(src_folder) if f.lower().endswith('.pdf')]
    
    # Strip extensions and make a list of the base names
    base_names = [os.path.splitext(pdf)[0] for pdf in pdf_files]
    
    # List all files in the destination folder
    dest_files = os.listdir(dest_folder)
    
    # Check if the number of files match
    if len(base_names) != len(dest_files):
        print("The number of files in the destination folder does not match the number of PDF files in the source folder.")
        return
    
    # Iterate over the destination files and rename them
    for i, dest_filename in enumerate(dest_files):
        old_dest_file_path = os.path.join(dest_folder, dest_filename)
        
        if os.path.isfile(old_dest_file_path):
            # Split the destination file to get its extension
            _, extension = os.path.splitext(dest_filename)
            
            # Construct the new filename using the corresponding PDF base name and the original extension
            new_dest_filename = base_names[i] + extension
            # new_dest_file_path = os.path.join(dest_folder, new_dest_filename)
            
            # Rename the file in the destination folder
            # os.rename(old_dest_file_path, new_dest_file_path)
            print(f"Renamed '{dest_filename}' to '{new_dest_filename}'")

# Specify the source and destination folder paths
src_folder = 'C:/Users/adam2/Documents/The Boys/PDF'
dest_folder = 'C:/Users/adam2/Documents/The Boys/EPUB'

# Call the function to rename files in the destination folder
rename_files_to_match_pdfs(src_folder, dest_folder)
