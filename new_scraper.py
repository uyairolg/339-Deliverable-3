import os
import csv

# Define the path to the 'meets' directory
meets_dir = 'meets'

def open_csv_files_in_meets():
    # Get all CSV files in the 'meets' directory
    csv_files = [f for f in os.listdir(meets_dir) if f.endswith('.csv')]
    
    for csv_file in csv_files:
        csv_file_path = os.path.join(meets_dir, csv_file)
        try:
            # Open and read the CSV file
            with open(csv_file_path, mode='r', encoding='utf-8') as file:
                reader = csv.reader(file)
                rows = list(reader)
                
                # Extract metadata from the first few lines
                meet_name = rows[0][0]
                meet_date = rows[1][0]
                meet_url = rows[2][0]
                meet_comments = ""
                for i in range(0,len(rows[3])):
                    meet_comments=meet_comments+rows[3][i]
                # Start reading team results from row 6 onwards
                team_results = rows[7:]  # Team place, name, and score
                individual_results = []
                for i in range(0,len(rows)-1):
                    if (len(rows[i])==8):
                        individual_results.append(rows[i+1])

                # Create HTML page with the metadata and results
                page = f"""
<!DOCTYPE html>
<html lang="en">
    <head><!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{meet_name}</title>
  <link rel="stylesheet" href="css/style.css">
    </head>
    <body>
        <header>
        <h1><a href="{meet_url}">{meet_name}</a></h1>
        <nav>
           <ul>
             <li> <a href = '../index.html'>Home</a></li>
             <li> <a href = '../gallery.html'>Gallery</a></li>
            </ul>
            </nav>
        </header>
        <main>
        <div class="info">
            <div>Date: {meet_date}</div>
            <div>Comments: {meet_comments}</div>
        </div>
        <h2>Team Results</h2>
        <table class = "team_results">
            <tr><th>Place</th><th>Team</th><th>Score</th></tr>
    """

                # Loop through the team results and add them to the HTML table
                for row in team_results:
                    if len(row) == 3:  # Ensure valid row with 3 columns
                        place, team, score = row
                        page += f"<tr><td>{place}</td><td>{team}</td><td>{score}</td></tr>"
                
                page += """
        </table>

        <h2>Individual Results</h2>
        <table class="indiv_results">
            <tr><th>Place</th><th>Name</th><th>Grade</th><th>Time</th><th>Picture</th><th>Team</th></tr>
    """
                
                # Loop through the individual results and add them to the HTML table
                for row in individual_results:
                    place=row[0]
                    grade=row[1]
                    name=row[2]
                    athlink=row[3]
                    time=row[4]
                    team=row[5]
                    team_link=row[6]
                    pro_pic=row[7]
                    
                    page += f"""<tr>
                        <td>{place}</td>
                        <td>{name}</td>
                        <td>{grade}</td>
                      
                        <td>{time}</td>
                        
                        <td><img width = 100 src= "../AthleteImages/{pro_pic}" alt = "{name}"></td> 
                        <td> {team}</td>
                    
                        </tr>"""
                
                page += """
        </table>
        </main>
    </body>
</html>
"""
                # Generate the output HTML file path (same name as CSV but with .html extension)
                output_html = os.path.join(meets_dir, os.path.splitext(csv_file)[0] + '_results.html')
                
                # Write the HTML content to the file
                with open(output_html, 'w', encoding='utf-8') as output_file:
                    output_file.write(page)
                
                print(f"Created HTML file: {output_html}")
        
        except Exception as e:
            print(f"Error processing the file {csv_file}: {e}")

# Call the function to process all CSV files in the 'meets' directory
open_csv_files_in_meets()




def generate_index_html(directory='.'):
    # List all .html files in the given directory
    html_files = [f for f in os.listdir(meets_dir) if f.endswith('.html')]

    # Create the content for the index HTML page
    page_content = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <link rel="stylesheet" href="css/style.css">
    
    
    
    </head>
    <body>




        <h1>List of HTML Files</h1>
        <ul>
    """
    
    # Add each HTML file as a list item with a link
    for html_file in html_files:
        html_file = html_file.strip()
        page_content += f'<li><a href=meets/{html_file}>{html_file}</a></li>\n'
    
    page_content += """
        </ul>
    </body>
</html>
"""
    
    # Write the index.html file
    output_html = os.path.join(directory, 'index.html')
    with open(output_html, 'w', encoding='utf-8') as file:
        file.write(page_content)
    
    print(f"Created index file: {output_html}")

# Call the function to generate the index.html file
generate_index_html()
