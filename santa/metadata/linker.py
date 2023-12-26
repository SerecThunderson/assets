import os
import json

def update_json_files(new_base_url):
    for filename in os.listdir('.'):  # Current directory
        if filename.endswith('.json'):
            with open(filename, 'r') as file:
                data = json.load(file)
            
            # Extract the filename from the original URL
            original_url = data['image']
            filename_part = original_url.split('/')[-1]
            
            # Replace the URL
            new_url = new_base_url + filename_part
            data['image'] = new_url

            # Write the updated JSON back to the file
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)

# Example usage
new_base_url = 'https://raw.githubusercontent.com/SerecThunderson/assets/main/santa/assets/'  # Replace with your new base URL
update_json_files(new_base_url)
