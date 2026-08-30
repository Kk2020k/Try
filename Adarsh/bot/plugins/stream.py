import os
import asyncio
from asyncio import TimeoutError
from urllib.parse import quote_plus

from pyrogram import filters, Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo,
)

from Adarsh.bot import StreamBot
from Adarsh.utils.database import Database
from Adarsh.utils.human_readable import humanbytes
from Adarsh.vars import Var
from Adarsh.utils.file_properties import (
    get_name,
    get_hash,
    get_media_file_size,
)


db = Database(Var.DATABASE_URL, Var.name)
pass_db = Database(
    Var.DATABASE_URL,
    "ag_passwords",
)

MY_PASS = os.environ.get("MY_PASS")


async def wait_for_password(
    client: Client,
    chat_id: int,
    timeout=90,
):
    try:
        response: Message = await client.listen(
            chat_id,
            filters=filters.text,
            timeout=timeout,
        )

        return response.text if response else None

    except TimeoutError:
        return None
