from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a dictionary with some company names and logo URLs
company_logo_dict = \
    {
        'meta': 'https://www.google.com/url?q=https://en.wikipedia.org/wiki/Meta_Platforms%23/media/File:Meta_Platforms_Inc._logo.svg&sa=D&source=editors&ust=1722915372894048&usg=AOvVaw2D3N0lef9DSzWAkp3cKCPL',
        'alphabet': 'https://www.google.com/url?q=https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Alphabet_Inc_Logo_2015.svg/220px-Alphabet_Inc_Logo_2015.svg.png&sa=D&source=editors&ust=1722915372894432&usg=AOvVaw0wjV9sTewsZr7rHGCkXHJM',
        'linkedin': 'https://www.google.com/url?q=https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/LinkedIn_2021.svg/200px-LinkedIn_2021.svg.png&sa=D&source=editors&ust=1722915372894718&usg=AOvVaw2kKHsa1zg35zqGggHviNK0',
        'apple': 'https://www.google.com/url?q=https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Apple_logo_black.svg/90px-Apple_logo_black.svg.png&sa=D&source=editors&ust=1722915372894984&usg=AOvVaw1wSsh8LGdW35wupDh0xoCm',
        'cisco': 'https://www.google.com/url?q=https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Cisco_logo_blue_2016.svg/220px-Cisco_logo_blue_2016.svg.png&sa=D&source=editors&ust=1722915372895265&usg=AOvVaw3YhXqc9jyUoIwDpWl-6aa9',
        'citadel': 'https://www.google.com/url?q=https://upload.wikimedia.org/wikipedia/commons/6/66/Citadel_Securities_logo.jpg&sa=D&source=editors&ust=1722915372895474&usg=AOvVaw1FNsKUpp4dIIMCMUQdsZWL',
        'intel': 'https://www.google.com/url?q=https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Intel_logo_2023.svg/200px-Intel_logo_2023.svg.png&sa=D&source=editors&ust=1722915372895694&usg=AOvVaw0aO7fP7AfgK9wweRXCA5eO',
        'tesla': 'https://www.google.com/url?q=https://en.wikipedia.org/wiki/File:Tesla_Motors.svg&sa=D&source=editors&ust=1722915372895916&usg=AOvVaw2pHsoqf3BuGXA-QPj5nbVY',
        'spotify': 'https://www.google.com/url?q=https://en.wikipedia.org/wiki/File:2024_Spotify_Logo.svg&sa=D&source=editors&ust=1722915372896151&usg=AOvVaw3RQ2GzcPjA6DnPXT6LQzIQ'
    }


@app.route('/company_logo', methods=['POST'])
def company_info():
    # Get the JSON data from the request
    data = request.get_json()

    # Extract the company name from the JSON data
    company_name = data.get('company_name').lower()

    if not company_name:
        return 'Company name is required.', 400

    # Look up the company name in the dictionary
    info = company_logo_dict.get(company_name)

    if info:
        return info
    else:
        return 'Company not found.', 404


if __name__ == '__main__':
    app.run(port=5000, debug=True)  # Run on port 5000
