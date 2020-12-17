"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No Name set yet. [Mark .](t.me/i_M_5)"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("𖥳︙ MarkThon\n"
                     "𖥳︙ Version: 7.7.7\n"
                     "𖥳︙ Created By: [DEV](https://t.me/i_M_5) || [CH MarkThon](https://t.me/MarkThon1)\n"
                     "𖥳︙ BOT ORDERS : No thing\n"
                     "𖥳︙ The Files : [Here](https://t.me/MarkThon1)\n"
                     "𖥳︙ Source link ♻️ : [Here](https://heroku.com/deploy?template=https://github.com/tfk5/MarkThon)\n"
                    f"𖥳︙ The owner : {DEFAULTUSER}\n")
