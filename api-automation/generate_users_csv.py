import requests
import csv

def generate_csv_from_api():
    # 1. Define the target URL and Headers
    url = "https://reqres.in/api/users?page=2"
    
    # Add your API key
    headers = {
        "x-api-key": "YOUR_API_KEY" 
    }
    
    print(f"Fetching data from: {url}")
    
    # 2. Make the GET request AND pass the headers
    response = requests.get(url, headers=headers)
    
    # 3. Check if the request was successful
    if response.status_code == 200:
        users = response.json().get('data', [])
        
        csv_filename = "reqres_users_page2.csv"
        csv_headers = ["First Name", "Last Name", "Email"]
        
        # 4. Open a new CSV file and write the data
        with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(csv_headers)
            
            for user in users:
                writer.writerow([user['first_name'], user['last_name'], user['email']])
                
        print(f"✅ Success! {len(users)} user records have been saved to '{csv_filename}'.")
        
    else:
        print(f"❌ Failed to retrieve data. HTTP Status Code: {response.status_code}")
        print(f"Response message: {response.text}") # Added this so you can see the exact error if it fails!

if __name__ == "__main__":
    generate_csv_from_api()