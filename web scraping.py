import requests
from bs4 import BeautifulSoup

def get_full_body_text(url): 
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status() 

        soup = BeautifulSoup(response.text, 'html.parser')
        
        body = soup.find('body')

        if not body:
            return "there is no body"

        for element in body(['script', 'style', 'noscript', 'header', 'footer', 'nav', 'aside']):
            element.decompose()

        full_body_text = body.get_text(separator='\n', strip=True)
        
        return full_body_text

    except Exception as e:
        return f"  error: {e}"


target_url = 'https://flatandvilla.com/%D8%A7%D9%84%D8%B4%D9%8A%D8%AE-%D8%B2%D8%A7%D9%8A%D8%AF/%D9%85%D9%88%D9%84-%D8%B0%D8%A7-%D9%83%D9%88%D8%B1/' 

text = get_full_body_text(target_url)

print(text)
