class script(object):
    START_TXT = """<b>𝗛𝗲𝘆 {}, <i>{}</i>
    
𝗜'𝗺 𝗮 𝗿𝗼𝗯𝘂𝘀𝘁 𝗠𝗼𝘃𝗶𝗲𝘀 & 𝗦𝗲𝗿𝗶𝗲𝘀 𝗣𝗿𝗼𝘃𝗶𝗱𝗲𝗿 𝗕𝗼𝘁! 🤖 𝗬𝗼𝘂 𝗰𝗮𝗻 𝗚𝗲𝘁 𝗮𝗻𝘆 𝗳𝗶𝗹𝗺, 𝘀𝗲𝗿𝗶𝗲𝘀, 𝗼𝗿 𝗮𝗻𝗶𝗺𝗲 𝗳𝗿𝗼𝗺 𝗺𝗲. 𝗜𝘁'𝘀 𝘀𝘂𝗽𝗲𝗿 𝗲𝗮𝘀𝘆 𝘁𝗼 𝘂𝘀𝗲 – 𝗷𝘂𝘀𝘁 𝗷𝗼𝗶𝗻 𝗺𝘆 𝘂𝗽𝗱𝗮𝘁𝗲𝘀 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 𝗮𝗻𝗱 𝗺𝗼𝘃𝗶𝗲 𝗴𝗿𝗼𝘂𝗽. 𝗧𝗵𝗲𝗻, 𝘀𝗵𝗼𝗼𝘁 𝗺𝗲 𝗮 𝗺𝗲𝘀𝘀𝗮𝗴𝗲, 𝗽𝗲𝗿𝘀𝗼𝗻𝗮𝗹𝗹𝘆 𝗼𝗿 𝗶𝗻 𝘁𝗵𝗲 𝗺𝗼𝘃𝗶𝗲 𝗴𝗿𝗼𝘂𝗽, 𝘄𝗶𝘁𝗵 𝘁𝗵𝗲 𝗻𝗮𝗺𝗲𝘀 𝗼𝗳 𝘁𝗵𝗲 𝗺𝗼𝘃𝗶𝗲𝘀, 𝘀𝗲𝗿𝗶𝗲𝘀, 𝗼𝗿 𝗮𝗻𝗶𝗺𝗲 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁 𝗶𝗻 𝘁𝗵𝗲 𝗰𝗼𝗿𝗿𝗲𝗰𝘁 𝗳𝗼𝗿𝗺𝗮𝘁. 𝗘𝗮𝘀𝘆, 𝗿𝗶𝗴𝗵𝘁? 🎬🍿
</b>"""

    MY_ABOUT_TXT = """<b>★ 𝗦𝗲𝗿𝘃𝗲𝗿: <a href=https://www.heroku.com>𝗛𝗲𝗿𝗼𝗸𝘂!</a>
★ 𝗟𝗶𝗯𝗿𝗮𝗿𝘆: <a href=https://pyrogram.org>𝗣𝘆𝗿𝗼𝗴𝗿𝗮𝗺!</a>
★ 𝗗𝗮𝘁𝗮𝗯𝗮𝘀𝗲: <a href=https://www.mongodb.com>𝗠𝗼𝗻𝗴𝗼𝗗𝗕!</a>
★ 𝗟𝗮𝗻𝗴𝘂𝗮𝗴𝗲: <a href=https://www.python.org>𝗣𝘆𝘁𝗵𝗼𝗻!</a></b>"""

    MY_OWNER_TXT = """<b>★ 𝗡𝗮𝗺𝗲: 𝗩𝗲𝗻𝗼𝗺 𝗦𝘁𝗼𝗻𝗲!
★ 𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲: @IAmVenomStone
★ 𝗨𝗽𝗱𝗮𝘁𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹: @VenomStoneNetwork</b>"""

    STATUS_TXT = """<b>◈ 𝗧𝗼𝘁𝗮𝗹 𝗙𝗶𝗹𝗲𝘀: <code>{}</code>
◈ 𝗧𝗼𝘁𝗮𝗹 𝗨𝘀𝗲𝗿𝘀: <code>{}</code>
◈ 𝗧𝗼𝘁𝗮𝗹 𝗖𝗵𝗮𝘁𝘀: <code>{}</code>
◈ 𝗨𝘀𝗲𝗱 𝗦𝘁𝗼𝗿𝗮𝗴𝗲: <code>{}</code>
◈ 𝗙𝗿𝗲𝗲 𝗦𝘁𝗼𝗿𝗮𝗴𝗲: <code>{}</code>
◈ 𝗕𝗼𝘁 𝗨𝗽𝘁𝗶𝗺𝗲: <code>{}</code></b>"""

    NEW_GROUP_TXT = """<b>#𝗡𝗲𝘄𝗚𝗿𝗼𝘂𝗽

▪ 𝗧𝗶𝘁𝗹𝗲 - {}
▪ 𝗜𝗗 - <code>{}</code>
▪ 𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲 - {}
▪ 𝗧𝗼𝘁𝗮𝗹 - <code>{}</code></b>"""

    NEW_USER_TXT = """<b>#𝗡𝗲𝘄𝗨𝘀𝗲𝗿

★ 𝗡𝗮𝗺𝗲: {}
★ 𝗜𝗗: <code>{}</code></b>"""

    NO_RESULT_TXT = """<b>#NoResult
★ Group Name: {}
★ Group ID: <code>{}</code>
★ Name: {}

★ Message: {}</b>"""

    REQUEST_TXT = """★ Name: {}
★ ID: <code>{}</code>

★ Message: {}"""

    NOT_FILE_TXT = """👋 Hello {},

I can't find the <b>{}</b> in my database! 🥲

👉 Google Search and check your spelling is correct.
👉 Please read the Instructions to get better results.
👉 Or not been released yet."""
    
    EARN_TXT = """<b>ʜᴏᴡ ᴛᴏ ᴇᴀʀɴ ꜰʀᴏᴍ ᴛʜɪs ʙᴏᴛ

➥ ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴇᴀʀɴ ᴍᴏɴᴇʏ ʙʏ ᴜsɪɴɢ ᴛʜɪꜱ ʙᴏᴛ.

» sᴛᴇᴘ 1:- ғɪʀsᴛ ʏᴏᴜ ʜᴀᴠᴇ ᴛᴏ ᴀᴅᴅ ᴛʜɪs ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴡɪᴛʜ ᴀᴅᴍɪɴ ᴘᴇʀᴍɪssɪᴏɴ.

» sᴛᴇᴘ 2:- ᴍᴀᴋᴇ ᴀᴄᴄᴏᴜɴᴛ ᴏɴ <a href=https://onepagelink.in/ref/infinity07>onepagelink.in</a> [ ʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴜsᴇ ᴏᴛʜᴇʀ sʜᴏʀᴛɴᴇʀ ᴡᴇʙsɪᴛᴇ ]

» sᴛᴇᴘ 3:- ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴇʟᴏᴡ ɢɪᴠᴇɴ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ sʜᴏʀᴛɴᴇʀ ᴡɪᴛʜ ᴛʜɪs ʙᴏᴛ.

➥ ᴛʜɪꜱ ʙᴏᴛ ɪs ꜰʀᴇᴇ ꜰᴏʀ ᴀʟʟ, ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘs ғᴏʀ ꜰʀᴇᴇ ᴏꜰ ᴄᴏꜱᴛ.</b>"""

    HOW_TXT = """<b>ʜᴏᴡ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ᴏᴡɴ sʜᴏʀᴛɴᴇʀ ‼️

➥ ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ᴏᴡɴ sʜᴏʀᴛɴᴇʀ ᴛʜᴇɴ ᴊᴜsᴛ sᴇɴᴅ ᴛʜᴇ ɢɪᴠᴇɴ ᴅᴇᴛᴀɪʟs ɪɴ ᴄᴏʀʀᴇᴄᴛ ꜰᴏʀᴍᴀᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ

➥ ғᴏʀᴍᴀᴛ ↓↓↓

<code>/set_shortlink sʜᴏʀᴛɴᴇʀ sɪᴛᴇ sʜᴏʀᴛɴᴇʀ ᴀᴘɪ</code>

➥ ᴇxᴀᴍᴘʟᴇ ↓↓↓

<code>/set_shortlink onepagelink.in f646357aa129cfbd7eb59bcba428096ab54ca950</code>

➥ ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴄʜᴇᴄᴋ ᴡʜɪᴄʜ sʜᴏʀᴛᴇɴᴇʀ ʏᴏᴜ ʜᴀᴠᴇ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛʜᴇɴ sᴇɴᴅ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴛʜᴇ ɢʀᴏᴜᴘ /get_shortlink

📝 ɴᴏᴛᴇ:- ʏᴏᴜ sʜᴏᴜʟᴅ ɴᴏᴛ ʙᴇ ᴀɴ ᴀɴᴏɴʏᴍᴏᴜs ᴀᴅᴍɪɴ ɪɴ ɢʀᴏᴜᴘ. sᴇɴᴅ ᴄᴏᴍᴍᴀɴᴅ ᴡɪᴛʜᴏᴜᴛ ʙᴇɪɴɢ ᴀɴ ᴀɴᴏɴʏᴍᴜs ᴀᴅᴍɪɴ.</b>"""

    IMDB_TEMPLATE = """✅ I Found: <code>{query}</code>

🏷 Title: <a href={url}>{title}</a>
🎭 Genres: {genres}
📆 Year: <a href={url}/releaseinfo>{year}</a>
🌟 Rating: <a href={url}/ratings>{rating} / 10</a>
☀️ Languages: {languages}
📀 RunTime: {runtime} Minutes

🗣 Requested by: {message.from_user.mention}
©️ Powered by: <b>{message.chat.title}</b>"""

    FILE_CAPTION = """<i>{file_name}</i>

🚫 ᴘʟᴇᴀsᴇ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ᴄʟᴏsᴇ ʙᴜᴛᴛᴏɴ ɪꜰ ʏᴏᴜ ʜᴀᴠᴇ sᴇᴇɴ ᴛʜᴇ ᴍᴏᴠɪᴇ 🚫"""

    WELCOME_TEXT = """👋 𝗚𝗿𝗲𝗲𝘁𝗶𝗻𝗴𝘀, {mention}! 𝗦𝘁𝗲𝗽 𝗶𝗻𝘁𝗼 𝘁𝗵𝗲 𝗲𝗻𝗰𝗵𝗮𝗻𝘁𝗶𝗻𝗴 𝘄𝗼𝗿𝗹𝗱 𝗼𝗳 {title} 𝗴𝗿𝗼𝘂𝗽! 💞 𝗘𝘅𝗰𝗶𝘁𝗲𝗺𝗲𝗻𝘁 𝗮𝗻𝗱 𝗰𝗮𝗺𝗮𝗿𝗮𝗱𝗲𝗿𝗶𝗲 𝗮𝘄𝗮𝗶𝘁 𝘆𝗼𝘂! 🚀✨"""

    HELP_TXT = """<b>🔹 𝗦𝗲𝗮𝗿𝗰𝗵 𝗠𝗼𝘃𝗶𝗲 𝘄𝗶𝘁𝗵 𝗖𝗼𝗿𝗿𝗲𝗰𝘁 𝗦𝗽𝗲𝗹𝗹𝗶𝗻𝗴:
› 𝗮𝘃𝗮𝘁𝗮𝗿 𝟮𝟬𝟬𝟵 ✅
› 𝗮𝘃𝗮𝘁𝗮𝗿 𝗵𝗶𝗻𝗱𝗶 ✅
› 𝗮𝘃𝗮𝘁𝗮𝗿 𝗺𝗼𝘃𝗶𝗲 ❌
› 𝗮𝘃𝗮𝘁𝗮𝗿 𝗵𝗶𝗻𝗱𝗶 𝗱𝘂𝗯𝗯𝗲𝗱 ❌

🔹 𝗦𝗲𝗮𝗿𝗰𝗵 𝗪𝗲𝗯 𝗦𝗲𝗿𝗶𝗲𝘀 𝗶𝗻 𝗧𝗵𝗶𝘀 𝗙𝗼𝗿𝗺𝗮𝘁:
› 𝘃𝗶𝗸𝗶𝗻𝗴𝘀 𝗦𝟬𝟭 ✅
› 𝘃𝗶𝗸𝗶𝗻𝗴𝘀 𝗦𝟬𝟭𝗘𝟬𝟭 ✅
› 𝘃𝗶𝗸𝗶𝗻𝗴𝘀 𝗦𝟬𝟭 𝗵𝗶𝗻𝗱𝗶 ✅
› 𝘃𝗶𝗸𝗶𝗻𝗴𝘀 𝗦𝟬𝟭 𝗵𝗶𝗻𝗱𝗶 𝗱𝘂𝗯𝗯𝗲𝗱 ❌
› 𝘃𝗶𝗸𝗶𝗻𝗴𝘀 𝘀𝗲𝗮𝘀𝗼𝗻 𝟭 ❌
› 𝘃𝗶𝗸𝗶𝗻𝗴𝘀 𝘄𝗲𝗯 𝘀𝗲𝗿𝗶𝗲𝘀 ❌</b>"""
    
    ADMIN_COMMAND_TXT = """<b>Here are the admin commands for the bot:

/index_channels - Check the number of added index channel IDs 📊
/stats - Get bot status ℹ️
/delete - Delete files using a query 🗑️
/delete_all - Delete all indexed files 🚮
/broadcast - Send a message to all bot users 📢
/grp_broadcast - Broadcast a message to all groups 🌐
/pin_broadcast - Send a pinned message to all bot users 📌
/pin_grp_broadcast - Send a pinned message to all groups 📌
/restart - Restart the bot 🔄
/leave - Make the bot leave a particular group 🚪
/unban_grp - Enable a group ✅
/ban_grp - Disable a group ❌
/ban_user - Ban a user from the bot 🚫
/unban_user - Unban a user from the bot ✅
/users - Get details of all users 🧑‍💻
/chats - Get details of all groups 🌐
/invite_link - Generate an invite link 🔗
/index - Index bot-accessible channels 📑
/add_premium - Add a user to the premium list 💎
/remove_premium - Remove a user from the premium list 💔</b>"""
    
    USER_COMMAND_TXT = """<b>Here are some commands for users to navigate the bot:

/start - Check if the bot is alive 🤖
/settings - Customize group settings as you wish ⚙️
/set_template - Set a custom IMDb template 🌟
/set_caption - Personalize the bot files' caption 📝
/set_shortlink - Admins can set a custom shortlink 🔗
/get_custom_settings - Retrieve your group settings details 📊
/set_welcome - Craft a warm welcome message for new members 👋
/set_tutorial - Set a custom tutorial link in the result page button 📘
/id - Check your group or channel ID 🆔
/my_plan - Review your plan details 📆
/plans - Explore available plan details 💡</b>"""

    SOURCE_TXT = """<b>𝗡𝗢𝗧𝗘:

⚠️ 𝗧𝗵𝗶𝘀 𝗕𝗼𝘁 𝗶𝘀 𝗡𝗼𝘁 𝗮𝗻 𝗢𝗽𝗲𝗻 𝗦𝗼𝘂𝗿𝗰𝗲 𝗣𝗿𝗼𝗷𝗲𝗰𝘁! 𝗧𝗵𝗮𝗻𝗸𝘀 𝘁𝗼 𝗥𝗞_𝗕𝗼𝘁𝘇 (𝗥𝗶𝘀𝗵𝗶𝗸𝗲𝘀𝗵), 𝗠𝗞𝗡_𝗕𝗼𝘁𝘀 & 𝗘𝘃𝗮𝗹𝗺𝗮𝗿𝗶𝗮 𝗗𝗲𝘃𝘀 𝗳𝗼𝗿 𝘁𝗵𝗲 𝗕𝗮𝘀𝗲 𝗖𝗼𝗱𝗲𝘀. 𝗦𝗽𝗲𝗰𝗶𝗮𝗹 𝗧𝗵𝗮𝗻𝗸𝘀 𝘁𝗼 𝗠𝘆 𝗧𝗚 𝗙𝗿𝗶𝗲𝗻𝗱𝘀 𝘁𝗼𝗼.

𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗱 𝗯𝘆 @VenomStoneNetwork👨‍💻</b>"""
