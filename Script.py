class script(object):
    START_TXT = """<b>𝗛𝗲𝘆 {}, <i>{}</i>
    
𝟭. 𝗦𝗲𝗮𝗿𝗰𝗵 𝗠𝗼𝘃𝗶𝗲 𝗡𝗮𝗺𝗲 𝘄𝗶𝘁𝗵 𝗖𝗼𝗿𝗿𝗲𝗰𝘁 𝗦𝗽𝗲𝗹𝗹𝗶𝗻𝗴:
●✅ 𝗮𝘃𝗮𝘁𝗮𝗿 𝟮𝟬𝟬𝟵
●✅ 𝗮𝘃𝗮𝘁𝗮𝗿 𝗵𝗶𝗻𝗱𝗶
●❌ 𝗮𝘃𝗮𝘁𝗮𝗿 𝗺𝗼𝘃𝗶𝗲
●❌ 𝗮𝘃𝗮𝘁𝗮𝗿 𝗵𝗶𝗻𝗱𝗶 𝗱𝘂𝗯𝗯𝗲𝗱

𝟮. 𝗦𝗲𝗮𝗿𝗰𝗵 𝗪𝗲𝗯 𝗦𝗲𝗿𝗶𝗲𝘀 𝗶𝗻 𝗧𝗵𝗶𝘀 𝗙𝗼𝗿𝗺𝗮𝘁:
●✅ 𝘃𝗶𝗸𝗶𝗻𝗴𝘀 𝗦𝟬𝟭
●✅ 𝘃𝗶𝗸𝗶𝗻𝗴𝘀 𝗦𝟬𝟭𝗘𝟬𝟭
●✅ 𝘃𝗶𝗸𝗶𝗻𝗴𝘀 𝗦𝟬𝟭 𝗵𝗶𝗻𝗱𝗶
●❌ 𝘃𝗶𝗸𝗶𝗻𝗴𝘀 𝗦𝟬𝟭 𝗵𝗶𝗻𝗱𝗶 𝗱𝘂𝗯𝗯𝗲𝗱
●❌ 𝘃𝗶𝗸𝗶𝗻𝗴𝘀 𝘀𝗲𝗮𝘀𝗼𝗻 𝟭
●❌ 𝘃𝗶𝗸𝗶𝗻𝗴𝘀 𝘄𝗲𝗯 𝘀𝗲𝗿𝗶𝗲𝘀

𝟯. 𝗔𝘃𝗼𝗶𝗱 𝗨𝘀𝗶𝗻𝗴 𝗪𝗼𝗿𝗱𝘀 𝗟𝗶𝗸𝗲 𝗦𝗲𝗮𝘀𝗼𝗻𝘀/𝗘𝗽𝗶𝘀𝗼𝗱𝗲𝘀/𝗦𝗲𝗿𝗶𝗲𝘀/𝗗𝘂𝗯𝗯𝗲𝗱/𝗠𝗼𝘃𝗶𝗲𝘀/𝗦𝗲𝗻𝗱/𝗛𝗗, 𝗲𝘁𝗰.</b>"""

    MY_ABOUT_TXT = """<b>★ 𝗦𝗲𝗿𝘃𝗲𝗿: <a href=https://www.heroku.com>𝗛𝗲𝗿𝗼𝗸𝘂!</a>
★ 𝗟𝗶𝗯𝗿𝗮𝗿𝘆: <a href=https://pyrogram.org>𝗣𝘆𝗿𝗼𝗴𝗿𝗮𝗺!</a>
★ 𝗗𝗮𝘁𝗮𝗯𝗮𝘀𝗲: <a href=https://www.mongodb.com>𝗠𝗼𝗻𝗴𝗼𝗗𝗕!</a>
★ 𝗟𝗮𝗻𝗴𝘂𝗮𝗴𝗲: <a href=https://www.python.org>𝗣𝘆𝘁𝗵𝗼𝗻!</a></b>"""

    MY_OWNER_TXT = """<b>★ 𝗡𝗮𝗺𝗲: 𝗩𝗲𝗻𝗼𝗺 𝗦𝘁𝗼𝗻𝗲!
★ 𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲: @VenomMoviesBot
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

    NO_RESULT_TXT = """<b>#𝗡𝗼𝗥𝗲𝘀𝘂𝗹𝘁
★ 𝗚𝗿𝗼𝘂𝗽 𝗡𝗮𝗺𝗲: {}
★ 𝗚𝗿𝗼𝘂𝗽 𝗜𝗗: <code>{}</code>
★ 𝗡𝗮𝗺𝗲: {}

★ 𝗠𝗲𝘀𝘀𝗮𝗴𝗲: {}</b>"""

    REQUEST_TXT = """<b>★ 𝗡𝗮𝗺𝗲: {}
★ 𝗜𝗗: <code>{}</code>

★ 𝗠𝗲𝘀𝘀𝗮𝗴𝗲: {}</b>"""

    NOT_FILE_TXT = """👋 𝗚𝗿𝗲𝗲𝘁𝗶𝗻𝗴𝘀 {},

𝗢𝗼𝗽𝘀𝗶𝗲! 🥲 𝗖𝗼𝘂𝗹𝗱𝗻'𝘁 𝗹𝗼𝗰𝗮𝘁𝗲 𝘁𝗵𝗲 <b>{}</b> 𝗶𝗻 𝗺𝘆 𝗱𝗮𝘁𝗮𝗯𝗮𝘀𝗲.

👉 𝗗𝗶𝘃𝗲 𝗶𝗻𝘁𝗼 𝗚𝗼𝗼𝗴𝗹𝗲, 𝗰𝗿𝗼𝘀𝘀-𝗰𝗵𝗲𝗰𝗸 𝘁𝗵𝗼𝘀𝗲 𝘀𝗽𝗲𝗹𝗹𝗶𝗻𝗴𝘀.
👉 𝗚𝗹𝗮𝗻𝗰𝗲 𝗮𝘁 𝘁𝗵𝗲 𝗶𝗻𝘀𝘁𝗿𝘂𝗰𝘁𝗶𝗼𝗻𝘀 𝗳𝗼𝗿 𝘀𝗼𝗺𝗲 𝘄𝗶𝘇𝗮𝗿𝗱𝗹𝘆 𝘁𝗶𝗽𝘀.
👉 𝗣𝗲𝗿𝗵𝗮𝗽𝘀 𝗶𝘁'𝘀 𝗯𝗲𝗶𝗻𝗴 𝗰𝗼𝘆 – 𝗻𝗼𝘁 𝗿𝗲𝗹𝗲𝗮𝘀𝗲𝗱 𝘆𝗲𝘁! 🕵️‍♂️✨"""
    
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

    IMDB_TEMPLATE = """✅ 𝐕𝐨𝐢𝐥à! 𝐈 𝐃𝐢𝐬𝐜𝐨𝐯𝐞𝐫𝐞𝐝 <code>{query}</code>

🏷 𝐓𝐢𝐭𝐥𝐞:  <a href={url}>{title}</a>
🎭 𝐆𝐞𝐧𝐫𝐞𝐬: {genres}
📆 𝐘𝐞𝐚𝐫: <a href={url}/releaseinfo>{year}</a>
🌟 𝐑𝐚𝐭𝐢𝐧𝐠: <a href={url}/ratings>{rating} / 10</a>
☀️ 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞𝐬: {languages}
📀 𝐑𝐮𝐧𝐓𝐢𝐦𝐞: {runtime} Minutes

🗣 𝐒𝐮𝐦𝐦𝐨𝐧𝐞𝐝 𝐛𝐲: {message.from_user.mention}
©️ 𝐄𝐦𝐩𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲: <b>{message.chat.title}</b>"""

    FILE_CAPTION = """<b>{file_name}
    
🔰 Main Channel: @VenomStoneNetwok</b>"""

    WELCOME_TEXT = """👋 𝗚𝗿𝗲𝗲𝘁𝗶𝗻𝗴𝘀, {mention}! 𝗦𝘁𝗲𝗽 𝗶𝗻𝘁𝗼 𝘁𝗵𝗲 𝗲𝗻𝗰𝗵𝗮𝗻𝘁𝗶𝗻𝗴 𝘄𝗼𝗿𝗹𝗱 𝗼𝗳 {title} 𝗴𝗿𝗼𝘂𝗽! 💞 𝗘𝘅𝗰𝗶𝘁𝗲𝗺𝗲𝗻𝘁 𝗮𝗻𝗱 𝗰𝗮𝗺𝗮𝗿𝗮𝗱𝗲𝗿𝗶𝗲 𝗮𝘄𝗮𝗶𝘁 𝘆𝗼𝘂! 🚀✨"""

    HELP_TXT = """<b>𝗪𝗮𝘁𝗰𝗵 𝘁𝗵𝗲 𝘁𝘂𝘁𝗼𝗿𝗶𝗮𝗹 𝘃𝗶𝗱𝗲𝗼 𝗮𝗻𝗱 𝘂𝗻𝗱𝗲𝗿𝘀𝘁𝗮𝗻𝗱 𝗵𝗼𝘄 𝘁𝗼 𝗱𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝗮𝗻𝘆 𝗺𝗼𝘃𝗶𝗲 𝗼𝗿 𝘀𝗲𝗿𝗶𝗲𝘀 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁 𝘂𝘀𝗶𝗻𝗴 𝘁𝗵𝗶𝘀 𝗯𝗼𝘁. 🎥🤖

● 𝗧𝘂𝘁𝗼𝗿𝗶𝗮𝗹 𝗩𝘂𝗱𝗲𝗼 𝗟𝗶𝗻𝗸: https://t.me/VenomStoneMovies/2430

𝗠𝘂𝘀𝘁 𝘄𝗮𝘁𝗰𝗵 𝘁𝗵𝗶𝘀 𝘁𝘂𝘁𝗼𝗿𝗶𝗮𝗹 𝘃𝗶𝗱𝗲𝗼!  👆🏻</b>"""
    
    ADMIN_COMMAND_TXT = """<b>𝗛𝗲𝗿𝗲 𝗮𝗿𝗲 𝘁𝗵𝗲 𝗮𝗱𝗺𝗶𝗻 𝗰𝗼𝗺𝗺𝗮𝗻𝗱𝘀 𝗳𝗼𝗿 𝘁𝗵𝗲 𝗯𝗼𝘁:

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
/remove_premium - Remove a user from the premium list 💔
/settings - Customize group settings as you wish ⚙️
/set_template - Set a custom IMDb template 🌟
/set_caption - Personalize the bot files' caption 📝
/set_shortlink - Admins can set a custom shortlink 🔗
/get_custom_settings - Retrieve your group settings details 📊
/set_welcome - Craft a warm welcome message for new members 👋
/set_tutorial - Set a custom tutorial link in the result page button 📘
/id - Check your group or channel ID 🆔</b>"""
    
    USER_COMMAND_TXT = """<b>𝗛𝗲𝗿𝗲 𝗮𝗿𝗲 𝘀𝗼𝗺𝗲 𝗰𝗼𝗺𝗺𝗮𝗻𝗱𝘀 𝗳𝗼𝗿 𝘂𝘀𝗲𝗿𝘀 𝘁𝗼 𝗻𝗮𝘃𝗶𝗴𝗮𝘁𝗲 𝘁𝗵𝗲 𝗯𝗼𝘁:

/start - 𝗖𝗵𝗲𝗰𝗸 𝗶𝗳 𝘁𝗵𝗲 𝗯𝗼𝘁 𝗶𝘀 𝗮𝗹𝗶𝘃𝗲 🤖
/my_plan - 𝗥𝗲𝘃𝗶𝗲𝘄 𝘆𝗼𝘂𝗿 𝗽𝗹𝗮𝗻 𝗱𝗲𝘁𝗮𝗶𝗹𝘀 📆
/plans - 𝗘𝘅𝗽𝗹𝗼𝗿𝗲 𝗮𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 𝗽𝗹𝗮𝗻 𝗱𝗲𝘁𝗮𝗶𝗹𝘀 💡</b>"""

    SOURCE_TXT = """<b>𝗡𝗢𝗧𝗘:

⚠️ 𝗧𝗵𝗶𝘀 𝗕𝗼𝘁 𝗶𝘀 𝗡𝗼𝘁 𝗮𝗻 𝗢𝗽𝗲𝗻 𝗦𝗼𝘂𝗿𝗰𝗲 𝗣𝗿𝗼𝗷𝗲𝗰𝘁! 

𝗧𝗵𝗮𝗻𝗸𝘀 𝘁𝗼 𝗥𝗞_𝗕𝗼𝘁𝘇 (𝗥𝗶𝘀𝗵𝗶𝗸𝗲𝘀𝗵), 𝗠𝗞𝗡_𝗕𝗼𝘁𝘀 & 𝗘𝘃𝗮𝗹𝗺𝗮𝗿𝗶𝗮 𝗗𝗲𝘃𝘀 𝗳𝗼𝗿 𝘁𝗵𝗲 𝗕𝗮𝘀𝗲 𝗖𝗼𝗱𝗲𝘀. 

𝗦𝗽𝗲𝗰𝗶𝗮𝗹 𝗧𝗵𝗮𝗻𝗸𝘀 𝘁𝗼 𝗠𝘆 𝗧𝗚 𝗙𝗿𝗶𝗲𝗻𝗱𝘀 𝘁𝗼𝗼.

𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗱 𝗯𝘆 @VenomStoneNetwork👨‍💻</b>"""
