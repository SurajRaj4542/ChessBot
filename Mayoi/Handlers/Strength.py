from ..Handlers.__init__ import *

@app.on_message(filters.command(['strength','strength@AW_Chessbot']))
async def fstrength(client,msg):
    user = await getUserid(client,msg)
    userstrength = showstrength(user[0])
    text = f"User {user[1]}'s strength is {userstrength}"
    await msg.reply_text(text)

