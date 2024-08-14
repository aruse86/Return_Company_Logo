# Return_Company_Logo
This microservice returns a company logo url when a company name is given.

Flask is the framework used to create this microservice. In order to use this
microservice, please follow the steps outlined below:

1)  If Python 3 is not installed, install the latest release from
    https://www.python.org/downloads/windows/

2)  If Pip (Pip is the recommended tool for installing Python packages)
    is not installed on your computer, install Pip from
    https://pip.pypa.io/en/stable/installation/

3)  The Flask application will need to run in a virtual environment so install
    one using the following command in a terminal (or command prompt)
    `pip install pipenv`

4)  Install Dependencies
    `pip install -r requirements.txt`

5) To run the microservice, open the directory where the microservice files Return_Logo.py,
   Request_Logo.py, and Test_Script.py are located in your preferred IDE.
   `python Return_Logo.py`

6) Open Test_Script.py and edit the company name in the payload variable (it is initially set to
    'meta', then click run. The microservice will return a result in the terminal window.
