from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_og_tags():
    # Get the URL from the query parameter
    url = request.args.get('url')

    # Define the proxy URL
    proxy_url = 'http://20.204.212.45:3129'

    # Set up the proxy
    proxy = {
        'http': proxy_url,
        'https': proxy_url
    }

    # Make a request to the URL
    response = requests.get(url, proxies=proxy)
    response.raise_for_status()

    # Create a BeautifulSoup object
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all meta tags with property starting with 'og:'
    og_tags = soup.find_all('meta', property=lambda x: x and x.startswith('og:'))

    # Extract the content attribute from the og tags
    og_data = {tag['property'][3:]: tag['content'] for tag in og_tags}

    return jsonify(og_data)

    # return "hello"

# if __name__ == '__main__':
#     app.run()
