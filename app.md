
Schedule in crontab format

Every day at midnight:
0 0 * * * /usr/bin/python3 /home/tenzin_tsegyal/crontab/app.py > log.txt 2>&1 &

Every Sunday at 10:00pm
0 22 * * SUN /usr/bin/python3 /home/tenzin_tsegyal/crontab/app.py > log.txt 2>&1 &


At 8:00am on the 25th in every 3rd month 
0 8 25 */3 * /usr/bin/python3 /home/tenzin_tsegyal/crontab/app.py > log.txt 2>&1 &


Steps:

1) Deploy VM (deployed on GCP since I ran out of Azure credits)

2) run sudo apt-get update in the VM

3) run crontab-h to check if crontab is already installed

4) run select-editor and select nano

5) run git clone to open API

6) cd into the cloned git repository

7) run nano app.py to make any edits to the python code

8) run crontab -e

9) in crontab -e write the time, date, and the path of the script for each schedule
    ex. (0 0 * * * /usr/bin/python3 /home/tenzin_tsegyal/crontab/app.py > log.txt 2>&1 &)

10) pres ctrl+O and ctrl+X to save and close out of crontab

11) run systemctl status cron to check if crontab worked properly
        a) Additionally you can run ls -l in the home directory then,
            run nano log.txt to see if there are any errors in your python file

12) if there are no errors, cd into the crontab repository and do ls -l to check for new txt files 