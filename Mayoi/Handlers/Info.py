from ..Handlers.__init__ import *

@app.on_message(filters.command(['info','info@AW_Chessbot']))
async def info(client,msg):
    id = msg.from_user.id
    userInfo = await client.get_chat(id)
    strength = showstrength(id)
    rank = ranking(id)
    
    name = userInfo.first_name
    bio = userInfo.bio
    group = msg.chat.title if msg.chat.title != None else 'Private Chat'
    username = userInfo.username if userInfo.username != None else f'[‌‌{name}](tg://user?id={id})'
    pic = await client.get_profile_photos(id,limit=1)
    pic = pic[0].file_id if pic else 'noPic.jpg'
    
    await msg.reply_photo(photo=pic,
                             caption=Strings.INFO_TEXT.format(name=name,username=username,
                                                        id=id,strength=strength,rank=rank,
                                                    bio=bio, group=group))

