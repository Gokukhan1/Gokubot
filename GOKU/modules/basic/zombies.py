import html

from pyrogram import Client, enums, filters
from pyrogram.types import Message

from GOKU.helper.basic import edit_or_reply
from GOKU.helper.parser import mention_html, mention_markdown
from GOKU.modules.help import *

@Client.on_message(filters.command(["zombies"], ".") & filters.me)

async def kickdel_cmd(client: Client, message: Message):
    # Send initial message indicating action
    edit_message = await edit_or_reply(message, "<b>Kicking deleted accounts...</b>")
    
    # Fetch all members and kick deleted accounts
    deleted_members = [
        await message.chat.kick_member(member.user.id, int(time()) + 31)
        for member in await message.chat.get_members()
        if member.user.is_deleted
    ]
    
    # Update message with result
    await edit_message.edit(f"<b>Successfully kicked {len(deleted_members)} deleted account(s).</b>")
    
