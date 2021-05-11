from ..Handlers.__init__ import *

@app.on_message(filters.command(['help','help@AW_ChessBot']))
async def startMain(client,msg):
    await msg.reply(Strings.HELP_TEXT)
