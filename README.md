# :flags: lil_insta_scraper
lil_insta_scraper is an instagram scraper in python. It allows you to grab some informations about an account (mail, phone, biography, followers count, following count, profile picture). You can see and download profile pictures in a quite high quality. The informations you scrapped can be exported as a folder and a text file. 
# :wrench: Installation
```bash
git clone https://github.com/TheSaltMaker/lil_insta_scraper.git
cd lil_insta_scraper/
python3 -m pip install -r requirements.txt
```
# :triangular_ruler: Usage
You simply use arguments as `-s` for your sessionID (check it next) and `-t` for your target username or `-f` to loook for at least 2 targets. 
# :pushpin: exemple
If you want to scrap informations about one account:
```bash
python3 lil_insta_scraper/lil_insta_scraper.py -s 123456%abcd -t a_taget_name
```
If you have a list of accounts, you can do a simple list like:
```
username1
username2
usernameN
```
You can you an other option: 
```bash
python3 lil_insta_scraper/lil_insta_scraper.py -s 123456%abcd -f your_file_name.txt
```
# :red_circle: Important note
When you download a profile picture, export infos or both, they will be saved in your current directory!
# :page_with_curl: how to have your session ID 
To have your sesssion ID you have to log in on instagram with your browser. You have to `Inspect element` and go in `storage`. Now you can see a category named `cookies` within instagram url. You go on it and you can see a table with the `sessionid`. 

![alt text](https://github.com/TheSaltMaker/lil_insta_scraper/blob/master/lil_insta_scraper_sessionid.png?raw=true)
# :exclamation: Disclaimer
I'm not responsible of what you do with this script !
# :speech_balloon: Contact me
If you want to talk with me, you may find me on discord `SCP-343#2349` (I have may changed my name) or on Twitter `@MathsBreaking`.
