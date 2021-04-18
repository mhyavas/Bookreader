# Bookreader
Slicing sentences of a book and push the sentences to discord.

In config.py file, dicord channel and token values should be filled before starting.

I use crontab for run the code every hour.

crontab setup:

0 * * * * python dc_bot.py >> cron.log 2>&1
