import os
import glob

# Define the HTML template as a multi-line string
page_template = """
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Athletic.net</title>
    </head>
    <body>
        <h1>{meet_name}</h1>
        <div class="team_results">
        {results}
        </div>
    </body>
</html>
"""

# Template for each result entry
result_template = """
<div class="result">
    <div>{place}</div>
    <div>{team}</div>
    <div>{score}</div>
</div>
"""

def open_csv_files_in_meets():
    # Define the path to the 'meets' directory
    meets_dir = 'meets'  # Adjust this to your actual directory
    
    # Use glob to find all .csv files in the 'meets' directory
    csv_files = glob.glob(os.path.join(meets_dir, '*.csv'))
    
    # Iterate over each .csv file found
    for csv_file in csv_files:
        try:
            # Open the CSV file manually
            with open(csv_file, mode='r', encoding='utf-8') as file:
                lines = file.readlines()
                
                # The first line should be the meet name
                meet_name = lines[0].strip()
                
                # Start processing the rest of the CSV after skipping the header rows
                results_html = ""
                for line in lines[4:]:  # Skip first 4 lines assuming the actual data starts from line 5
                    # Split the line by commas
                    fields = line.strip().split(',')
                    
                    # Check if we have exactly 3 fields (place, team, score), otherwise skip the line
                    if len(fields) == 3:
                        place, team, score = fields
                        # Replace placeholders with actual data
                        result_html = result_template.format(place=place, team=team, score=score)
                        results_html += result_html
                    else:
                        print(f"Skipping invalid row in {csv_file}: {line}")
            
            # Replace the meet name and results in the HTML template
            final_page = page_template.format(meet_name=meet_name, results=results_html)
            
            # Define the output HTML file path
            base_name = os.path.splitext(csv_file)[0]  # Remove the .csv extension
            html_file = f"{base_name}.html"
            
            # Write the generated HTML to a new file
            with open(html_file, mode='w', encoding='utf-8') as output_file:
                output_file.write(final_page)
            
            print(f"Created HTML file: {html_file}")
        
        except Exception as e:
            print(f"Error processing file {csv_file}: {e}")

# Calling the function to open and process CSV files
open_csv_files_in_meets()
