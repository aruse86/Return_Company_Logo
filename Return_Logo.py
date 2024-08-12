from flask import Flask, request

app = Flask(__name__)

# Define a dictionary with some company names and logo URLs
company_logo_dict = \
    {
        'meta': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Meta_Platforms_Inc._logo.svg/1280px-Meta_Platforms_Inc._logo.svg.png',
        'alphabet': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Alphabet_Inc_Logo_2015.svg/220px-Alphabet_Inc_Logo_2015.svg.png',
        'linkedin': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/LinkedIn_2021.svg/200px-LinkedIn_2021.svg.png',
        'apple': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Apple_logo_black.svg/90px-Apple_logo_black.svg.png',
        'cisco': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Cisco_logo_blue_2016.svg/220px-Cisco_logo_blue_2016.svg.png',
        'citadel': 'https://upload.wikimedia.org/wikipedia/commons/6/66/Citadel_Securities_logo.jpg',
        'intel': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Intel_logo_2023.svg/200px-Intel_logo_2023.svg.png',
        'tesla': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Tesla_Motors.svg/279px-Tesla_Motors.svg.png',
        'spotify': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/2024_Spotify_Logo.svg/512px-2024_Spotify_Logo.svg.png'
    }


@app.route('/company_logo', methods=['POST'])
def company_info():
    # Get the JSON data from the request
    data = request.get_json()

    # Extract the company name from the JSON data
    company_name = data.get('company_name').lower()

    if not company_name:
        return 'Company name is required.', 400

    info = company_logo_dict.get(company_name)

    if info:
        return info
    
    return 'Company not found.', 404


if __name__ == '__main__':
    app.run(port=5000, debug=True)  # Start Flask API Server
