from telethon import TelegramClient, events
from telethon.tl.types import DocumentAttributeAnimated, DocumentAttributeImageSize, DocumentAttributeVideo
import uuid
import os
from gif_creator import *

api_id = int(input('api_id: '))
api_hash = input('api_hash: ')
bot_token = input('bot_token: ')

client = TelegramClient('sticker-creator-bot', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage())
async def sticker_creator(event):
    given_text = event.message.text
    if given_text is None or given_text == "/start": return
    output_gif_path = uuid.uuid4().hex + ".gif"
    create_text_gif(text=given_text,
                    output_gif_path=output_gif_path,
                    size=720,
                    bg_color=(0, 0, 0),
                    text_color=(255, 0, 0),
                    font_size=150,
                    duration=150
                    )
    await event.reply(attributes=[
        # DocumentAttributeAnimated(),
        # DocumentAttributeVideo(duration=100, w=1000, h=1000, nosound=True, round_message=True)
    ]
        , file=output_gif_path)
    os.remove(output_gif_path)

client.start()
client.run_until_disconnected()