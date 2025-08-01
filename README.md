Posts one image per day from all the images of the specified folder into your Discord channel

1. Create your Discord bot at https://discord.com/developers/applications
2. In terminal in project directory: `source .venv/bin/activate`
3. `pip install --upgrade pip && pip install -r requirements.txt`
4. Copy `.env.example` and name it `.env`, then fill in the values
5. Set up cronjob for periodic execution, e.g. for daily execution at midnight: 

```bash
crontab -e # open cronjob editor

# add a line like this:
# 0 */24 * * *  cd /home/raspi/mangabot && source .venv/bin/activate && python3 run.py" >> cr

crontab -l # save
```

This best runs on a remote server or a raspberry pi or similar. 
