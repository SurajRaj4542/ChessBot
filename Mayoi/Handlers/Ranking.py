import asyncio
from ..Handlers.__init__ import *


async def mention(userid, client):
    user = await client.get_chat(userid)
    return (user.id, user.first_name)

@app.on_message(filters.command(['ranking','ranking@AW_ChessBot']))
async def ranking(client:Client,msg:Message): 
    sortedUsers = await getSorted()

    top =  await asyncio.gather(*[mention(user['_id'], client) for user in sortedUsers[:10]])
    text = "<b>&gt;&gt;<u> <a href=\"https://t.me/JOINCHESSWORLD\">Top 10 Players</u></b></a>\n"
    for user in top:
        for userdb in sortedUsers:
            if user[0] == userdb['_id']:
                text += f'\n<b>‣</b> {userdb["strength"]} - {user[1]}'
                break

    await msg.reply(text, disable_web_page_preview=True)
