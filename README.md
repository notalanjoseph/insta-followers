# Instagram non Followers ┗|｀O′|┛


This is a python script that uses selenium to log into your account to display the list of people who you follow but don't follow you back on Instagram using automation.

## Requirements

- Python 3.6 or higher
- Microsoft Edge 90.0.0 or higher
- Internet connection

## Installation

- Clone this repository or download the zip file (main branch).
```bash
git clone https://github.com/notalanjoseph/insta-non-followers/tree/main
```
- Change directory to insta-non-followers.
```bash
cd insta-non-followers
```
- Install the python dependencies using `pip` or `pip3`.
```bash
pip install -r requirements.txt
```

## Usage

- Run the script using `python app.py`. An MS Edge page will open up local server.
- Enter the credentials `username`, `password`, `no.of followers` & `no.of following` and press "Find".
- Wait for the script to log into your Instagram account, navigate to your profile page and execute the iteration.
- The list of usernames(with links) who don't follow you back will be displayed in the web page.

## Disclaimer

- This script is for educational purposes only and is not affiliated with Instagram or any other third-party service. Use it at your own risk and respect the Instagram terms of service.
- Social media websites like Instagram keeps changing their div ordering and class names, so this script may not be future proof.
