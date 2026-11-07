# SERBIA DISCOVERED — MVP prototype 0.1

This is a starter prototype, not a live deployed Telegram bot.

## Included
- Telegram bot (`bot.py`) with an "Open excursion" Web App button.
- Mini App (`webapp/index.html`) with a map, four demo stops, GPS proximity detection, manual stop selection, Google Maps directions and local progress.
- Stop content and coordinates are demo data and must be checked on site before public use.
- Audio files are not included yet.

## What Margarita needs to do
1. In Telegram, open the official BotFather account and create a bot using `/newbot`.
2. Copy the bot token. Do not send the token in chat or publish it.
3. Host the `webapp` folder at a public HTTPS address (GPS requires HTTPS).
4. Set `BOT_TOKEN` and `WEBAPP_URL` as environment variables on the server.
5. Install dependencies from `requirements.txt` and run `python bot.py`.

## Local run
Python 3.10+:
```bash
pip install -r requirements.txt
export BOT_TOKEN="YOUR_TOKEN"
export WEBAPP_URL="https://YOUR-HTTPS-HOST/index.html"
python bot.py
```

Windows PowerShell:
```powershell
$env:BOT_TOKEN="YOUR_TOKEN"
$env:WEBAPP_URL="https://YOUR-HTTPS-HOST/index.html"
python bot.py
```

## Important limitations of this prototype
- Telegram Mini App must remain open in the foreground for dependable GPS polling.
- It does not promise background GPS while Telegram is minimized or the screen is locked.
- Browser GPS accuracy varies; a 50 m radius is a target setting, not a guarantee.
- Progress currently uses browser localStorage on this device; it is not yet synced to a server or linked to a purchase.
- Map tiles require internet. Offline maps and offline media packaging are not implemented yet.
- Coordinates are preliminary. Confirm each trigger point on location before testing.
- For production: add server-side user/progress storage, admin panel, activation codes, media hosting, offline cache, privacy notice and robust GPS trigger logic.