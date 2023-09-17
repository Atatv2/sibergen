import discord
import responses


async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message, str(message.author), str(message.channel))
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'MTE1MzAwOTAxODQ3OTA1ODk0NQ.GSg8Ex.1vo2TGv27SkpyFeqBoluLc_wi9O9hvyk8IunKI'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')


    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        
        print(f'{username} said: "{user_message}" in {channel}')

        p_message = user_message.lower()
        if "thock gen" in p_message:
            if channel == "🤖┃thock":
                await send_message(message, user_message, is_private=True)
            else:
                await send_message(message, user_message, is_private=False)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)
