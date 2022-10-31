# Welcome to my Reddit Savebot! 
This is a simple bot for those who want a solution for sending content from Reddit to Telegram without needing to crop watermarks off downloaded photos or download videos through third-party websites. 

To make it work, you only need to prepare 2 major things: 
- A Reddit application for OAuth2 to use Reddit's API.
    You can find an extensive tutorial for it here: https://github.com/reddit-archive/reddit/wiki/OAuth2
- And a Telegram bot.
    Tutorial for starting and basic stuff if you want to customize my bot for your needs: https://towardsdatascience.com/how-to-write-a-telegram-bot-with-python-8c08099057a8
    
With this, just follow requirements.txt to install necessary modules and enjoy! The script should be runnable both locally and online. If you're tight on storage for the videos, I can recommend shortening the interval in the schedule in line 73 (docs: https://schedule.readthedocs.io/en/stable/). Alternatively, I'm working on a way to skip storing videos in a folder altogether, so you can expect a patch in a few months!
