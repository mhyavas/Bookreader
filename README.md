# Bookreader
Slicing sentences of a book according to dots and pushing those sentences to Discord hourly. Sentences are limited with 280 charcters and users can push to Twitter with a No-code platform.

In the same directory, the book should be in book.txt file.

In config.py file, dicord channel and token values should be filled before starting.

I use crontab for running the code every hour.

crontab setup:

0 * * * * python dc_bot.py >> cron.log 2>&1
