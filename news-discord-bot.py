# Нужные библиотеки.
import discord
import schedule
import asyncio
import requests
import openai

# Брать ключ здесь https://platform.openai.com/docs/api-reference
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Токен дискорд бота https://discord.com/developers/docs/intro
CLIENT_TOKEN = 'YOUR_DISCORD_TOKEN'

# ID канала, куда бот будет отправлять новости.
CHANNEL_ID = "CHANNEL_ID"

url = "https://newsapi.org/v2/top-headlines"
params = {
# Параметры стараны можно узнать здесь https://newsapi.org/docs/endpoints/top-headlines
    "country": "ru",
# Получить API новостного источника здесь https://newsapi.org
    "apiKey": "YOUR_NEWS_API_KEY"
}

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

latest_url = ""

def get_latest_article():
    global latest_article
    response = requests.get(url, params=params)
    articles = response.json()['articles']
    latest_article = articles[0]
    return latest_article

async def send_article():
    global latest_url
    latest_article = get_latest_article()
    if latest_article['url'] != latest_url:
        channel = await client.fetch_channel(CHANNEL_ID)
        message = f"Новая статья: {latest_article['title']} - {latest_article['url']}"
        await channel.send(message)
        latest_url = latest_article['url']
        response_text = f'\n {message}'

        # Изменение промта для AI.
        prompt = "Придумай саркастический ответ на эту новостную статью " + response_text
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=60,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        sarcastic_response = response.choices[0].text.strip()
        if sarcastic_response:
            await channel.send(sarcastic_response)
    else:
        return 'Обновлений не найдено.'

@client.event
async def on_ready():
    print('Бот активен.')
    schedule.every(10).minutes.do(send_article)

    while True:
        await send_article()
        # Ждет 10 минут между отправкой новостей.
        await asyncio.sleep(10*60)

client.run(CLIENT_TOKEN)