# news-discord-bot
Простой новостной бот Discord, который получает новостные статьи с помощью API и отвечает на них с помощью подсказок, сгенерированных искусственным интеллектом благодаря OpenAI API.

**Установка:**

Клонируйте репозиторий куда вам нужно:
```
git clone https://github.com/pref6/news-discord-bot.git
```
Установите зависимости из requirements.txt:
```
pip install -r requirements.txt
```

**Настройка:**

Замените ```YOUR_OPENAI_API_KEY``` на ваш ключ API OpenAI.

Замените ```YOUR_DISCORD_TOKEN``` на токен вашего бота Discord.

Установите ID канала, куда бот будет отправлять новости в ```CHANNEL_ID```.

Установите в словаре ```params``` ваш API от NewsAPI и установите нужную страну.

**Ссылки на сервисы:**

https://newsapi.org

https://platform.openai.com/docs/api-reference

https://discord.com/developers/docs/intro

**Использование:**

Запустите бота:
```
python3 news-discord-bot.py
```
