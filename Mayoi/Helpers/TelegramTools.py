async def getUserId(client,msg):
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
