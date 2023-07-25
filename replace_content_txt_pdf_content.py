import os
import shutil
import re
import PyPDF2

def find_and_replace_text_in_file(file_path, search_text, replace_text):
    with open(file_path, 'r') as file:
        content = file.read()
    updated_content = content.replace(search_text, replace_text)
    with open(file_path, 'w') as file:
        file.write(updated_content)

def main():
    root_folder = "path/to/root/folder"  # Replace with the path to your root folder
    reference_folder = "path/to/reference/folder"  # Replace with the path to your reference folder

    for subfolder in os.listdir(root_folder):
        subfolder_path = os.path.join(root_folder, subfolder)

        if not os.path.isdir(subfolder_path):
            continue

        # Get the first five letters of the sub-folder name
        new_subfolder_name = subfolder[:5]

        # Rename the sub-folder with the new name
        new_subfolder_path = os.path.join(root_folder, new_subfolder_name)
        os.rename(subfolder_path, new_subfolder_path)

        # Find the txt file and process its content
        txt_file_path = os.path.join(new_subfolder_path, "file.txt")

        if os.path.exists(txt_file_path):
            with open(txt_file_path, 'r') as txt_file:
                lines = txt_file.readlines()

            # Find the line starting with "enable spot list: "
            for i, line in enumerate(lines):
                if line.startswith("enable spot list: "):
                    pdf_file_path = os.path.join(reference_folder, f"{new_subfolder_name}.pdf")
                    if os.path.exists(pdf_file_path):
                        with open(pdf_file_path, 'rb') as pdf_file:
                            pdf_reader = PyPDF2.PdfReader(pdf_file)
                            pdf_text = pdf_reader.pages[0].extract_text()

                        # Extract the line starting with "enable spot list: " from the PDF
                        pdf_search_text = re.search(r"enable spot list: (.+)", pdf_text)
                        if pdf_search_text:
                            pdf_enable_spot_list = pdf_search_text.group(1).strip()
                            lines[i] = f"enable spot list: {pdf_enable_spot_list}\n"

                        # Find and replace the line starting with "additional spot list: "
                        pdf_search_additional_spot = re.search(r"additional spot list: (.+)", pdf_text)
                        if pdf_search_additional_spot:
                            pdf_additional_spot_list = pdf_search_additional_spot.group(1).strip()
                            find_and_replace_text_in_file(txt_file_path, "additional spot list:", f"additional spot list: {pdf_additional_spot_list}")

            # Update the txt file with the modified lines
            with open(txt_file_path, 'w') as txt_file:
                txt_file.writelines(lines)

if __name__ == "__main__":
    main()
