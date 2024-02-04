class script(object):
    START_TXT = """<b>𝗛𝗲𝘆 {}, <i>{}</i>
    
𝗜'𝗺 𝗮 𝗿𝗼𝗯𝘂𝘀𝘁 𝗠𝗼𝘃𝗶𝗲𝘀 & 𝗦𝗲𝗿𝗶𝗲𝘀 𝗣𝗿𝗼𝘃𝗶𝗱𝗲𝗿 𝗕𝗼𝘁! 🤖 𝗬𝗼𝘂 𝗰𝗮𝗻 𝗚𝗲𝘁 𝗮𝗻𝘆 𝗳𝗶𝗹𝗺, 𝘀𝗲𝗿𝗶𝗲𝘀, 𝗼𝗿 𝗮𝗻𝗶𝗺𝗲 𝗳𝗿𝗼𝗺 𝗺𝗲. 𝗜𝘁'𝘀 𝘀𝘂𝗽𝗲𝗿 𝗲𝗮𝘀𝘆 𝘁𝗼 𝘂𝘀𝗲 – 𝗷𝘂𝘀𝘁 𝗷𝗼𝗶𝗻 𝗺𝘆 𝘂𝗽𝗱𝗮𝘁𝗲𝘀 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 𝗮𝗻𝗱 𝗺𝗼𝘃𝗶𝗲 𝗴𝗿𝗼𝘂𝗽. 𝗧𝗵𝗲𝗻, 𝘀𝗵𝗼𝗼𝘁 𝗺𝗲 𝗮 𝗺𝗲𝘀𝘀𝗮𝗴𝗲, 𝗽𝗲𝗿𝘀𝗼𝗻𝗮𝗹𝗹𝘆 𝗼𝗿 𝗶𝗻 𝘁𝗵𝗲 𝗺𝗼𝘃𝗶𝗲 𝗴𝗿𝗼𝘂𝗽, 𝘄𝗶𝘁𝗵 𝘁𝗵𝗲 𝗻𝗮𝗺𝗲𝘀 𝗼𝗳 𝘁𝗵𝗲 𝗺𝗼𝘃𝗶𝗲𝘀, 𝘀𝗲𝗿𝗶𝗲𝘀, 𝗼𝗿 𝗮𝗻𝗶𝗺𝗲 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁 𝗶𝗻 𝘁𝗵𝗲 𝗰𝗼𝗿𝗿𝗲𝗰𝘁 𝗳𝗼𝗿𝗺𝗮𝘁. 𝗘𝗮𝘀𝘆, 𝗿𝗶𝗴𝗵𝘁? 🎬🍿</b>"""

    MY_ABOUT_TXT = """★ Server: <a href=https://www.heroku.com>Heroku</a>
★ Database: <a href=https://www.mongodb.com>MongoDB</a>
★ Language: <a href=https://www.python.org>Python</a>
★ Library: <a href=https://pyrogram.org>Pyrogram</a>"""

    MY_OWNER_TXT = """★ Name: RK Bots
★ Username: @Rk_botowner
★ Update Channel : @Rkbotz"""

    STATUS_TXT = """🗂 Total Files: <code>{}</code>
👤 Total Users: <code>{}</code>
👥 Total Chats: <code>{}</code>
✨ Used Storage: <code>{}</code>
🗳 Free Storage: <code>{}</code>
🚀 Bot Uptime: <code>{}</code>"""

    NEW_GROUP_TXT = """#NewGroup
Title - {}
ID - <code>{}</code>
Username - {}
Total - <code>{}</code>"""

    NEW_USER_TXT = """#NewUser
★ Name: {}
★ ID: <code>{}</code>"""

    NO_RESULT_TXT = """#NoResult
★ Group Name: {}
★ Group ID: <code>{}</code>
★ Name: {}

★ Message: {}"""

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

    WELCOME_TEXT = """👋 Hello {mention}, Welcome to {title} group! 💞"""

    HELP_TXT = """<b>Note - <spoiler>Try each command without any argument to see more details 😹</spoiler></b>"""
    
    ADMIN_COMMAND_TXT = """<b>Here is bot admin commands 👇

/index_channels - to check how many index channel id added
/stats - to get bot status
/delete - to delete files using query
/delete_all - to delete all indexed file
/broadcast - to send message to all bot users
/grp_broadcast - to send message to all groups
/pin_broadcast - to send message as pin to all bot users.
/pin_grp_broadcast - to send message as pin to all groups.
/restart - to restart bot
/leave - to leave your bot from particular group
/unban_grp - to enable group
/ban_grp - to disable group
/ban_user - to ban a users from bot
/unban_user - to unban a users from bot
/users - to get all users details
/chats - to get all groups
/invite_link - to generate invite link
/index - to index bot accessible channels
/add_premium - to add user in premium
/remove_premium - to remove user from premium</b>"""
    
    USER_COMMAND_TXT = """<b>Here is bot user commands 👇

/start - to check bot alive or not
/settings - to change group settings as your wish
/set_template - to set custom imdb template
/set_caption - to set custom bot files caption
/set_shortlink - group admin can set custom shortlink
/get_custom_settings - to get your group settings details
/set_welcome - to set custom new joined users welcome message for group
/set_tutorial - to set custom tutorial link in result page button
/id - to check group or channel id
/my_plan - to check your plan details
/plans - to get plan details</b>"""

    SOURCE_TXT = """<b>ʙᴏᴛ ɢɪᴛʜᴜʙ ʀᴇᴘᴏsɪᴛᴏʀʏ -

- ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ᴀɴ ᴏᴘᴇɴ ꜱᴏᴜʀᴄᴇ ᴘʀᴏᴊᴇᴄᴛ.

- ꜱᴏᴜʀᴄᴇ - <a href=https://github.com/Rishikesh-Sharma09/Auto-Filter-Bot>ʜᴇʀᴇ</a>

- ᴅᴇᴠʟᴏᴘᴇʀ - @Rkbotz"""
