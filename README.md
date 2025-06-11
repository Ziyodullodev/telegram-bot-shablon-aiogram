# Telegram Bot Template with Aiogram

This repository provides a template for building Telegram bots using the Aiogram framework in Python. It is designed to help you quickly start your bot development with a clean and modular structure.

## Features

- Asynchronous Telegram Bot API with Aiogram
- Modular code organization
- Database integration utilities
- Easy to extend with custom handlers and commands

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Ziyodullodev/telegram-bot-shablon-aiogram.git
   cd telegram-bot-shablon-aiogram
   ```

2. Create venv file
   ```
   python -m venv venv
   cp .env.example .env
   source venv/bin/activate
   pip install -r requirements.txt
   python src/main.py
   ```



## Configuration

Set your Telegram Bot Token in the environment or configuration file as needed.

## Running the Bot

Run the bot with:

```bash
python -m src.main
```

## Project Structure

- `src/` - Source files
  - `functions/` - Utility functions including database operations
  - `handlers/` - Bot command and message handlers
  - `main.py` - Bot entry point

## Contributing

Contributions are welcome! Feel free to fork and submit pull requests.

## License

MIT License

---

Happy bot building! 🚀
