import requests
from bs4 import BeautifulSoup

class WebsiteScrapper:


    @classmethod
    def get_html_from_url(self, url):
        response = requests.get(
            url=f'http://{url}',
            
        )
        print(f'Status code: {response.status_code}')
        file_path = f'./files/html/GET__{url.replace("/","")}.txt'
        with open(file_path, 'w') as file:
            file.write(response.text)
        print(f'html response saved on {file_path}')
        return response.text
    
    @classmethod
    def get_footer_data_from_html(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        divs = soup.find_all('div')
        footer = soup.find_all('footer')
        footer = [f.text for f in footer if '©' in f.text]
        copy_rights = [div.text for div in divs if '©' in div.text ]
        if not copy_rights and not footer:
            raise Exception('Contact data not found')
        

        for text in footer + copy_rights:
            if '2023' in text:
                raise Exception('Already updated')
        
        for i in range(len(copy_rights)):
            copy_rights[i] = copy_rights[i].replace('\n', '')
        data = {
            'copyright': copy_rights,
            'footer': footer
        }
        return data
