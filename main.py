from pyrogram import Client, filters
from config import Strings
from Mayoi.Start import start, startCallbacks
from Helpers.MongoDB import addstrength, showstrength, ranking

app = Client(
    "mayoi",
    api_id = 1639263,
    api_hash = "bb491a5c6b6ab5cd510325d474908d49",
    bot_token="1652690019:AAHontptuFFuolfhNPO91H8hws1s2bWmaDg"
)

async def getUserid(client,msg):
    if msg.reply_to_message:
        userid = msg.reply_to_message.from_user.id
        name = f"""{msg.reply_to_message.from_user.first_name}"""
        return (userid,name)
    else:
        username = msg.text.split(' ')[1:][0] if msg.text.split(' ')[1:] != [] else None
        if not username:
            return (msg.from_user.id,msg.from_user.first_name)
            username = username.strip('@')

        user = await client.get_chat(username)
        name = f"""{user.first_name}"""
        userid = user.id 
        return (userid,name)

        


@app.on_message(filters.command(['help','help@AW_Chessbot']))
async def startMain(client,msg):
    await msg.reply(Strings.HELP_TEXT,parse_mode='html')


@app.on_message(filters.command(['start','start@AW_Chessbot']))
async def startMain(client,msg):
    await start(client,msg)


@app.on_message(filters.command(['info','info@AW_Chessbot']))
async def info(client,msg):
    id = msg.from_user.id
    userInfo = await client.get_chat(id)
    fnostrength = showstrength(id)
    rankuwu = ranking(id)
    
    name = userInfo.first_name
    bio = userInfo.bio
    group = msg.chat.title
    username = userInfo.username if userInfo.username != None else f'[‌‌{name}](tg://user?id={id})'
    pic = client.get_profile_photos(id,limit=1)
    pic = pic[0].file_id if pic else 'noPic.jpeg'
    
    await msg.reply_photo(photo=pic, caption=Strings.INFO_TEXT.format(name=name,username=username,id=id,strength=fnostrength,rank=rankuwu,bio=bio, group=group),
                        parse_mode='html')

    

@app.on_callback_query()
async def callback_query_handler(client, query):
    await startCallbacks(client,query)


@app.on_message(filters.command(['add','add@AW_Chessbot']))
async def strength(client,msg):

    if msg.from_user.id in Strings.SUDO_USERS:
        user = await getUserid(client,msg)
        strength = addstrength(user[0])
        text = f"""<b>User: {user[1]} got {strength} Strength.</b>"""
        await msg.reply(text)
    
    else:
        await msg.reply('<b>Fuck off, you no Sudo User</b>')


@app.on_message(filters.command(['strength','strength@AW_Chessbot']))
async def fstrength(client,msg):
    user = await getUserid(client,msg)
    userstrength = showstrength(user[0])
    text = f"User {user[1]}'s strength is {userstrength}"
    await msg.reply_text(text)

    

app.run()
