#
# Copyright (C) 2026 by Kanha-Team@Github, < https://github.com/Kanha-Team>.
# This file is part of < https://github.com/Kanha-Team/KanhaClone > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Kanha-Team/KanhaClone/blob/main/LICENSE >
#
# All rights reserved.
#

from pyrogram import Client, filters
from pyrogram.types import Message

from config import BANNED_USERS
from KanhaClone.core.call import Kanha
from KanhaClone.cplugin.utils.decorators.admins import AdminRightsCheck
from KanhaClone.misc import db
from KanhaClone.utils.database import set_loop
from KanhaClone.utils.inline import close_markup


@Client.on_message(
    filters.command(
        ["end", "stop", "cend", "cstop"],
        prefixes=["/", "!", "%", ",", "", ".", "@", "#"],
    )
    & filters.group
    & ~BANNED_USERS
)
@AdminRightsCheck  # <-- Ab ye Clone Owner/Sudo ko allow karega
async def stop_music(cli, message: Message, _, chat_id):
    if len(message.command) != 1:
        return

    # Stream Stop Karega
    await Kanha.stop_stream(chat_id)

    # Loop Reset Karega
    await set_loop(chat_id, 0)

    try:
        db[chat_id] = []
    except:
        pass

    await message.reply_text(
        _["admin_5"].format(message.from_user.mention), reply_markup=close_markup(_)
    )
