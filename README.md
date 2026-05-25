# Mindful Balance Telegram Bot

Telegram bot: @mindfulbalance_bot  
Booking contact: @irina_sexologist_coach  
Website: https://mindfulbalance.online

## Files

- `bot.py` — main Telegram bot code
- `requirements.txt` — Python dependencies
- `.env.example` — example environment variable
- `render.yaml` — optional Render configuration

## How to run locally

1. Install Python 3.11+
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set the token:

Windows PowerShell:
```powershell
$env:BOT_TOKEN="YOUR_TOKEN_FROM_BOTFATHER"
python bot.py
```

macOS/Linux:
```bash
export BOT_TOKEN="YOUR_TOKEN_FROM_BOTFATHER"
python bot.py
```

## How to deploy on Render

1. Create a GitHub repository and upload these files.
2. Go to https://render.com
3. New → Background Worker
4. Connect your GitHub repository.
5. Build command:

```bash
pip install -r requirements.txt
```

6. Start command:

```bash
python bot.py
```

7. Add Environment Variable:

Key:
```bash
BOT_TOKEN
```

Value:
```bash
YOUR_TOKEN_FROM_BOTFATHER
```

8. Click Deploy.

## Important

Do not paste your real BotFather token into public code or screenshots.