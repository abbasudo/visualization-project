import os
import glob
import pandas as pd

def get_csv_previews(folder_path="data"):
    """
    Scans a folder for CSV files and returns a Markdown string 
    containing the filename, header, and first 5 rows of each.
    """
    
    # Construct the search path (e.g., "data/*.csv")
    search_path = os.path.join(folder_path, "*.csv")
    csv_files = glob.glob(search_path)
    
    markdown_output = ""
    
    if not csv_files:
        return f"No CSV files found in directory: '{folder_path}'"

    for file_path in csv_files:
        try:
            # Get just the filename for the header
            filename = os.path.basename(file_path)
            
            # Read header + first 5 rows
            df = pd.read_csv(file_path, nrows=5)
            
            # Format the entry
            markdown_output += f"### File: `{filename}`\n\n"
            
            # Convert DataFrame to Markdown table
            # index=False removes the generic 0,1,2,3 row numbers
            markdown_output += df.to_markdown(index=False)
            
            # Add a separator between files
            markdown_output += "\n\n---\n\n"
            
        except Exception as e:
            markdown_output += f"### File: `{filename}`\n\n"
            markdown_output += f"> **Error reading file:** {str(e)}\n\n---\n\n"

    return markdown_output

# --- Usage ---
if __name__ == "__main__":
    # Ensure the directory exists to avoid errors during testing
    if not os.path.exists("data"):
        os.makedirs("data")
        print("Created 'data' folder. Please put some CSV files in it and run again.")
    else:
        # Generate the text
        ai_context_text = get_csv_previews("data")
        
        # Print to console (or you could write this to a .txt file)
        print(ai_context_text)