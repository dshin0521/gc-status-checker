# Green Card Application Status Checker

## Usage
* Configure username and password to desirable Gmail account that you want to send email with
* Configure sender/receiver email address; sender's email address should match with that of Gmail account you configured earlier.
* Configure frequency and application numbers.

```
Example cron setup:

schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
```

## Disclaimer
Please use with caution and DO NOT spam USCIS server as your IP address will be blocked by their rate-limiter.
I do not hold any accountability/liability per misusage of the script.
