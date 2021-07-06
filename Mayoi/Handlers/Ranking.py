import asyncio
from bson.son import SON
from ..Handlers.__init__ import *


async def mention(userid):
    user = await client.get_chat(userid)
    return user.first_name


@app.on_message(filters.command(['ranking','ranking@AW_ChessBot']))
async def ranking(client:Client,msg:Message):
    pipeline = [{"$sort":SON([("strength",-1)])}]
    sortedUsers = list(Users.aggregate(pipeline))
 

    top =  await asyncio.gather(*[mention(user['_id']) for user in sortedUsers[:10]])
    text = "Top User"
    for user in top:
        text += f'\n{user}'

    await msg.reply(text)