
# Thanks to Sipak bro and Aryan.. 
# animation Idea by @NOOB_GUY_OP (Sipakisking) && @Hell boy_pikachu
# Made by @ROMANTIC_KILLER...and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# Porting in Mafia Userbot by @H1M4N5HU0P

import asyncio
import random
from telethon import events
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME, mafiaversion
from mafiabot.utils import admin_cmd, sudo_cmd
from telethon.tl.types import ChannelParticipantsAdmins

# ๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "BLAC-BOT"

# Thanks to Sipak bro and Raganork.. 
# animation Idea by @NOOB_GUY_OP (Sipakisking)
# Made by @ROMANTIC_KILLER...and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# alive.py for รรลฎ$HรณpBรศ

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

mafia = bot.uid

edit_time = 10
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/502d3b7372c1c395bba5a.mp4"
file2 = "https://telegra.ph/file/d938d8f4ecaf2d6e70d31.mp4"
file3 = "https://telegra.ph/file/52e33f519c5b932082298.mp4"
file4 = "https://telegra.ph/file/16f20e53ebab4474b7ea3.jpg"
""" =======================CONSTANTS====================== """
pm_caption = "  __**๐ฅ๐ฅBLAC-BOT ๐๐ ๐ธ๐๐๐๐ผ๐ฅ๐ฅ**__\n\n"

pm_caption += (
    f"                 ๐๐๐ธ๐๐๐ผโ๐\n**  ใ๐[{DEFAULTUSER}](tg://user?id={mafia})๐ใ**\n\n"
)

pm_caption += "๐ก๏ธTELETHON๐ก๏ธ : `1.15.0` \n\n"

pm_caption += f"๐๐๐ธ๐ฝ๐๐ธ๐น๐๐๐ : `{mafiaversion}`\n\n"

pm_caption += f"๐ฑSUDO๐ฑ            : `{sudou}`\n\n"

pm_caption += "๐CHANNEL๐๏ธ   : [แดแดษชษด](https://t.me/MafiaBot_Support)\n\n"

pm_caption += "๐CREATOR๐    : [Himanshu](https://t.me/H1M4N5HU0P)\n\n"

pm_caption += "๐คฉSUPPORTER๐คฉ    :[HellBoy](https://t.me/kraken_the_badass)\n\n"

pm_caption += "      [๐ฅREPO๐ฅ](https://github.com/H1M4N5HU0P/MAFIA-BOT) ๐น [๐License๐](https://github.com/H1M4N5HU0P/MAFIA-BOT/blob/main/LICENSE)"

# @command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()   
    
    on = await borg.send_file(alive.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(alive.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(alive.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(alive.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(alive.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(alive.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(alive.chat_id, ok5, file=file4)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(alive.chat_id, ok6, file=file1)

    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, caption=pm_caption)
    await alive.delete()
    
    
