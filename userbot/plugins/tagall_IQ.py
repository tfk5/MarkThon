from telethon import events
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="tagall"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "Tak was done for everyone"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, 100):
        mentions += f"[\u2063](tg://user?id={x.id})"
    await event.reply(mentions)
    await event.delete()
