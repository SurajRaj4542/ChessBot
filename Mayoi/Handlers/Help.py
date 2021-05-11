from ..Handlers.__init__ import *

@app.on_message(filters.command(['help','help@AW_Chessbot']))
async def startMain(client,msg):
    await msg.reply(Strings.HELP_TEXT)
