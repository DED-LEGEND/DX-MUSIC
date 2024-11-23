#
# Copyright (C) 2024 by THE-VIP-BOY-OP@Github, < https://github.com/THE-VIP-BOY-OP >.
#
# This file is part of < https://github.com/THE-VIP-BOY-OP/VIP-MUSIC > project,
# and is released under the MIT License.
# Please see < https://github.com/THE-VIP-BOY-OP/VIP-MUSIC/blob/master/LICENSE >
#
# All rights reserved.

from config import LOG, LOG_GROUP_ID
from VIPMUSIC import app
from VIPMUSIC.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "ᴘʀɪᴠᴀᴛᴇ ɢʀᴏᴜᴘ"

        logger_text = f"""
**{app.mention} 𝐏𝐋𝐀𝐘 𝐋𝐎𝐆 𝐃𝐗๛𝐋𝐔𝐂𝐊𝐘**

**𝐂𝐇𝐀𝐓 𝐈𝐃  :** `{message.chat.id}`
**𝐂𝐇𝐀𝐓 𝐍𝐀𝐌𝐄 :** {message.chat.title}
**𝐂𝐇𝐀𝐓 𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄 :** {chatusername}

**𝐔𝐒𝐄𝐑 𝐈𝐃 :** `{message.from_user.id}`
**𝐍𝐀𝐌𝐄 :** {message.from_user.mention}
**𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄 :** @{message.from_user.username}

**𝐐𝐔𝐄𝐑𝐘 :** {message.text.split(None, 1)[1]}
**𝐒𝐓𝐑𝐄𝐀𝐌𝐓𝐘𝐏𝐒 :** {streamtype}"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    chat_id=LOG_GROUP_ID,
                    text=logger_text,
                    disable_web_page_preview=True,
                )
            except Exception as e:
                print(e)
        return
