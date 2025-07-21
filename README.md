# 🎬 MovieBot

**MovieBox** is a Telegram bot that recommends popular movies using the TMDB API. It supports inline navigation buttons, click limits, and persistent user state using PickleDB.

---

## 🚀 Features

- Get random movies with `/movie`
- Inline "Next Movie" button
- Limit to 3 clicks per user per session
- Persistent click tracking with PickleDB
- Fetches from a random TMDB page per session

---

## 📦 Requirements

- Python 3.7+
- `pyTelegramBotAPI`
- `pickledb`
- `requests`
- TMDB API token
- Telegram bot token

---

## 📥 Installation

```bash
git clone https://github.com/yourusername/moviebox.git
cd moviebox
pip install -r requirements.txt
```
create virtual environment:
```bash
virtualenv .venv
```

Install dependencies:
```bash
pip install -r requirements.txt
```
move .env.sample to .env file
```bash
mv .env.sample .env
```
Add your credentials:
```
TELEGRAM_BOT_TOKEN=your-telegram-bot-token
TMDB_API_TOKEN=your-tmdb-api-token
```
---
# 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

