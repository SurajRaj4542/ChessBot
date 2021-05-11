from ..Handlers.__init__ import *

startButtons = [[InlineKeyboardButton('Help & Commands',callback_data='start|Help'),]]
startButtons += [[InlineKeyboardButton('About',callback_data='start|About'),
                InlineKeyboardButton('Updates',callback_data='start|Updates'),]]

backButton = [[InlineKeyboardButton('Back',callback_data='start|Back'),]]

updateButtons = [[InlineKeyboardButton(text='Updates Channel',url='https://t.me/AW_Updates')]]
updateButtons += [[InlineKeyboardButton('Back',callback_data='start|Back')]]
groupButtons = [[InlineKeyboardButton(text='STOP IT get some help',url='https://t.me/AW_ChessBot?start=start')]]

StartMarkup = InlineKeyboardMarkup(startButtons)
GroupMarkup = InlineKeyboardMarkup(groupButtons)
BackMarkup = InlineKeyboardMarkup(backButton)
UpdateMarkup = InlineKeyboardMarkup(updateButtons)

@app.on_message(filters.command('start','start@AW_ChessBot'))
async def start(client,msg):
     if msg.chat.type == 'private':
        await msg.reply_animation(animation='https://i.pinimg.com/originals/47/b7/32/47b732bdcc3f9e92844bf3c7853316c1.gif',
                                    caption=Strings.START_TEXT,
                                        reply_markup=StartMarkup)
        saveNewUser(msg)
     else:
        await msg.reply_animation(animation='https://telegra.ph/file/4f4bbe776a235f13ab602.mp4',
                                    caption=Strings.GROUP_START_TEXT,
                                      reply_markup=GroupMarkup) 


@app.on_callback_query(filters.create(lambda _,__,query: query.startswith('start|')))
async def startCallbacks(client, query):
    if query.data=="start|Help":
       await query.edit_message_text(Strings.HELP_TEXT,reply_markup=BackMarkup)

    elif query.data=="start|About":
        await query.edit_message_text(Strings.ABOUT_TEXT,reply_markup=BackMarkup)
    
    elif query.data=="start|Updates":
        await query.edit_message_text(Strings.UPDATES_TEXT,reply_markup=UpdateMarkup)
    
    elif query.data=="start|Back":
        await query.edit_message_text(Strings.START_TEXT,reply_markup=StartMarkup)              
