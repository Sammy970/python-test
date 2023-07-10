from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_og_tags():
    # Get the URL from the query parameter
    url = request.args.get('url')

    # Make a request to the URL
    response = requests.get(url)
    response.raise_for_status()

    # Create a BeautifulSoup object
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all meta tags with property starting with 'og:'
    og_tags = soup.find_all('meta', property=lambda x: x and x.startswith('og:'))

    # Extract the content attribute from the og tags
    og_data = {tag['property'][3:]: tag['content'] for tag in og_tags}

    return jsonify(og_data)

# if __name__ == '__main__':
#     app.run()
