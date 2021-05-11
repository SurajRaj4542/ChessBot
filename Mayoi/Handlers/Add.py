from ..Handlers.__init__ import *

@app.on_message(filters.command(['add','add@AW_Chessbot']))
async def strength(client,msg):
    if msg.from_user.id in Strings.SUDO_USERS:
        user = await getUserId(client,msg)
        strength = addstrength(user[0])
        text = f"""<b>User: {user[1]} got {strength} Strength.</b>"""
        await msg.reply(text)
    else:
        await msg.reply('<b>Fuck off, you no Sudo User</b>')
