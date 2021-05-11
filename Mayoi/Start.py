from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup,CallbackQuery 
from config import Strings
from Helpers.MongoDB import saveNewUser

startButtons = [[InlineKeyboardButton('Help & Commands',callback_data='Help'),]]
startButtons += [[InlineKeyboardButton('About',callback_data='About'),
                InlineKeyboardButton('Updates',callback_data='Updates'),]]
StartMarkup = InlineKeyboardMarkup(inline_keyboard=startButtons)

GoBack = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton('Back',callback_data='Back'),]])


async def start(client,msg):
     if msg.chat.type == 'private':
         await msg.reply_animation(animation='https://i.pinimg.com/originals/47/b7/32/47b732bdcc3f9e92844bf3c7853316c1.gif', caption=Strings.START_TEXT,
          parse_mode='html', reply_markup=StartMarkup)

         await saveNewUser(message=msg)

     else:
         groupButtons = [[InlineKeyboardButton(text='STOP IT get some help',url='https://t.me/AW_ChessBot?start=start')]]
         startGroup = InlineKeyboardMarkup(inline_keyboard=groupButtons)

         await msg.reply_animation(animation='https://telegra.ph/file/4f4bbe776a235f13ab602.mp4', caption=Strings.GROUP_START_TEXT,
          reply_markup=startGroup, parse_mode='html') 


async def startCallbacks(client, query):
    if query.data=="Help":
       await query.edit_message_text(Strings.HELP_TEXT,reply_markup=GoBack)

    elif query.data=="About":
        await query.edit_message_text(Strings.ABOUT_TEXT,reply_markup=GoBack)
    
    elif query.data=="Updates":
        await query.edit_message_text(Strings.UPDATES_TEXT,reply_markup=GoBack)
    
    elif query.data=="Back":
        await query.edit_message_text(Strings.START_TEXT,reply_markup=StartMarkup)              
