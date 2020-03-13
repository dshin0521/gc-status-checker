# Green Card Application Status Checker

Check your Green Card status in periodic manner.
Or check other applications nearby you to check what their statuses are. 
 
status_checker.py
------
Periodically check your application statuses and get notified by email if there's any update. 

**Usage**
* Configure username and password of desirable Gmail account that you want to send email with
* Configure sender/receiver email address; sender's email address should match with that of Gmail account you configured earlier.
* Configure application numbers.
* Configure frequency of API call.

```
Example cron setup:

schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
```


nearby_status_checker.py
------
Check nearby applications to see/count their statuses.

**Usage**
* Configure what type of application you want to check (e.g. 'I-485')
* Configure application number and counts 

```
Example setup:

get_statuses('I-485', 'MSC1234567890', 3)

will check statuses of 'MSC1234567890', 'MSC1234567889', 'MSC1234567888'.
```

## Disclaimer
Please use with caution and DO NOT spam USCIS server as your IP address will be blocked by their rate-limiter.
I do not hold any accountability/liability per misusage of the script.
