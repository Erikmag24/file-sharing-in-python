import requests

# Set the path to your file for uploading
file_path = 'your_file_path.txt'

# Make a POST request to upload the file to Transfer.sh
response = requests.post('https://transfer.sh/', files={'file': open(file_path, 'rb')})

# Check if the request was successful
if response.status_code == 200:
    # Extract the sharing link from the response
    share_link = response.content.decode('utf-8')
    print(f"File uploaded successfully. Sharing link: {share_link}")
else:
    print("An error occurred while uploading the file.")
