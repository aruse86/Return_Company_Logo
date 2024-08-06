from flask import Flask, request
import requests

app = Flask(__name__)


@app.route('/get_company_logo', methods=['POST'])
def get_company_info():
    # Extract the company name from the request body
    company_name = request.data.decode('utf-8')

    if not company_name:
        return 'Company name is required.', 400

    # URL of the Return_Logo service Flask app
    company_logo_url = 'http://127.0.0.1:5001/company_logo'

    # Send a POST request to the Return_Logo service with the company name
    response = requests.post(company_logo_url, json={'company_name': company_name})

    if response.status_code == 200:
        return response.text
    else:
        return response.text, response.status_code


if __name__ == '__main__':
    app.run(port=5000, debug=True)  # Run on port 5000
