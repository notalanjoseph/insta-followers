# Instagram non Followers😠


This is a python script that uses selenium to log into your account to display the list of people who you follow but don't follow you back on Instagram using automation.

## Requirements

- Python 3.6 or higher
- Flask 2.3.3 or higher
- selenium 3.141.0 or higher
- webdriver_manager 4.0.0 or higher

## Installation

- Clone this repository or download the zip file (main branch).
- Install the required packages using `pip install -r requirements.txt`.

## Usage

- Run the script using `python app.py`. An MS Edge page will open up local server.
- Enter the credentials `username`, `password`, `no.of followers` & `no.of following` and press "find".
- Wait for the script to log into your Instagram account, navigate to your profile page and execute the iteration.
- The list of usernames(with links) who don't follow you back will be displayed in the web page.

## Disclaimer

- This script is for educational purposes only and is not affiliated with Instagram or any other third-party service. Use it at your own risk and respect the Instagram terms of service.
- Social media websites like Instagram keeps changing their div ordering and class names, so this script may not be future proof.
