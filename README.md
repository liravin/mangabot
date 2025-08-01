Posts one image per day from all the images of the specified folder into your Discord channel

1. Configure Discord bot at https://discord.com/developers/applications
2. Copy `.env.example` and name it `.env`, then fill in the values
3. Set up cronjob for periodic execution, e.g. for daily execution at midnight: `0 */24 * * *  cd /home/raspi/mangabot && source .venv/bin/activate && python3 run.py`
