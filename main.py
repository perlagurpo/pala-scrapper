import requests
from bs4 import BeautifulSoup
import pandas as pd

# List of keywords to search
keywords = ["best web designer in japan", "another keyword", "yet another keyword"]

# Initialize empty lists to store data
data = []

# Loop through each keyword
for keyword in keywords:
    # Construct the search URL
    search_url = f"https://www.google.com/search?q={keyword}"

    # Send a GET request to Google
    response = requests.get(search_url)
    
    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find relevant search results
    search_results = soup.find_all("div", class_="tF2Cxc")
    
    print(f"Keyword: {keyword}")
    
    # Extract data from search results
    for result in search_results:
        website_url = result.a['href']
        
        # Visit the website URL to extract detailed information
        try:
            website_response = requests.get(website_url)
            website_soup = BeautifulSoup(website_response.content, 'html.parser')
            
            # Extract copyright text, email address, and phone number from the contact page
            copyright_text = "Not available"
            email_address = "Not available"
            phone_number = "Not available"
            
            # Add your code here to extract the copyright, email, and phone information
            # from the website_soup. This would depend on the structure of the website.
            
            # Store data in a dictionary
            entry = {
                "Website URL": website_url,
                "Copyright Text": copyright_text,
                "Email Address": email_address,
                "Phone Number": phone_number
            }
            data.append(entry)
            
            print(f"Website URL: {website_url}")
            print(f"Copyright Text: {copyright_text}")
            print(f"Email Address: {email_address}")
            print(f"Phone Number: {phone_number}")
            print()  # Add an empty line for readability
            
        except Exception as e:
            print(f"Error accessing {website_url}: {e}")
            continue

# Convert data to a pandas DataFrame
df = pd.DataFrame(data)

# Filter for websites with copyright before 2020
df_filtered = df[df["Copyright Text"].str.contains("2020", regex=False) == False]

# Save DataFrame to an Excel file
df_filtered.to_excel("web_design_leads_filtered.xlsx", index=False)
