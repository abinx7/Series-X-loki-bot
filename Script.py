class script(object):
    START_TXT = """<b>𝖧𝖾𝗅𝗅𝗈 {},
ഈ ബോട്ട് Sᴇʀɪᴇs X ഗ്രൂപ്പിലേക്ക് ഉള്ളത് എന്ന് ഇനി വീണ്ടും വീണ്ടും പറയണോ??
അപ്പോ പിന്നെ എന്തിനാ വീണ്ടും വീണ്ടും സ്റ്റാർട്ട് കുത്തി കളിക്കാൻ വരുന്നേ... എന്തായാലും സ്റ്റാർട്ട് അടിച്ചതല്ലെ ഇനി ആ താഴെ കാണുന്ന നമ്മുടെ ഒഫീഷ്യൽ ചന്നെൽ കൂടി Subscribe ചെയ്തിട്ട് പൊക്കോ 😎😎</b>

"""
    HELP_TXT = """<b>𝖧𝖾𝗋𝖾 𝗂𝗌 𝗍𝗁𝖾 𝖴𝗌𝗎𝖺𝗅 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌:</b>
"""
    GTRANS_TXT = """<b>𝖳𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝗈𝗋</b>
- 𝖳𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝖾 𝗍𝖾𝗑𝗍𝗌 𝗍𝗈 𝖺 𝗌𝗉𝖾𝖼𝗂𝖿𝗂𝖼 𝗅𝖺𝗇𝗀𝗎𝖺𝗀𝖾!
<b>𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖺𝗇𝖽 𝖴𝗌𝖺𝗀𝖾:</b>
- /tr [language code][reply] - 𝖳𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝖾 𝗋𝖾𝗉𝗅𝗂𝖾𝖽 𝗆𝖾𝗌𝗌𝖺𝗀𝖾 𝗍𝗈 𝗌𝗉𝖾𝖼𝗂𝖿𝗂𝖼 𝗅𝖺𝗇𝗀𝗎𝖺𝗀𝖾.
"""
    PASTE_TXT = """<b>𝖯𝖺𝗌𝗍𝖾</b>
- 𝖯𝖺𝗌𝗍𝖾 𝗌𝗈𝗆𝖾 𝗍𝖾𝗑𝗍𝗌 𝗈𝗋 𝖽𝗈𝖼𝗎𝗆𝖾𝗇𝗍𝗌 𝗈𝗇 𝖺 𝗐𝖾𝖻𝗌𝗂𝗍𝖾!
<b>𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖺𝗇𝖽 𝖴𝗌𝖺𝗀𝖾:</b>
- /paste [text] - 𝖯𝖺𝗌𝗍𝖾 𝗍𝗁𝖾 𝗀𝗂𝗏𝖾𝗇 𝗍𝖾𝗑𝗍 𝗈𝗇 𝗉𝖺𝗌𝗍𝗒
- /paste [reply] - 𝖯𝖺𝗌𝗍𝖾 𝗍𝗁𝖾 𝗋𝖾𝗉𝗅𝗂𝖾𝖽 𝗍𝖾𝗑𝗍 𝗈𝗇 𝗉𝖺𝗌𝗍𝗒
"""
    STICK_TXT = """<b>𝖲𝗍𝗂𝖼𝗄𝖾𝗋 𝖨𝖣</b>
- 𝖳𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗂𝗌 𝗎𝗌𝖾𝖽 𝗍𝗈 𝗀𝖾𝗍 𝖺 𝖨𝖣 𝗈𝖿 𝖺𝗇 𝗌𝗍𝗂𝖼𝗄𝖾𝗋

<b>Command</b>
- /stickerid - 𝖦𝖾𝗍 𝖨𝖣
"""
    ABOUT_TXT = """
𝐌𝐲 𝐍𝐚𝐦𝐞 : {} 🐍

🦁 𝐂𝐫𝐞𝐚𝐭𝐨𝐫 : <a href=</a>🍷

🐍𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞 : 𝐏𝐲𝐭𝐡𝐨𝐧

🐍𝐋𝐢𝐛𝐫𝐚𝐫𝐲 : 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 𝐚𝐬𝐲𝐧𝐜𝐢𝐨 

🐍𝐒𝐞𝐫𝐯𝐞𝐫 : 𝐂𝐎𝐍𝐓𝐀𝐁𝐎

🐍𝐒𝐨𝐮𝐫𝐜𝐞 : <a href=https://t.me/kurachkanjiedukkatte/8>👉 𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞</a>
🐍𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞 : 𝐌𝐨𝐧𝐠𝐨𝐃𝐁

🐍𝐁𝐮𝐢𝐥𝐝 s𝐭𝐚𝐭𝐮𝐬 : 𝐕𝟑.𝟐 [𝐁𝐄𝐓𝐀]
"""
    SOURCE_TXT = """<b>DISCLAIMER NOTE‼️:</b>
    
<b>-  is an Open Source Project.</b> <code>All the files in this bot are freely available on the internet or posted by somebody else. This bot is indexing files which are already uploaded on Telegram for easy of searching, We respect all the copyright laws and works in compliance with DMCA and EUCD. If anything is against law please contact us so that it can be removed asap. It is forbidden to download, stream, reproduce, or by any means, share, or consume, content without explicit permission from the content creator or legal copyright holder. If you believe this bot is violating your intellectual property, contact the respective channels for removal. The Bot does not own any of these contents, it only index the files from telegram. </code>
- <b>Source - @FilmClubGroup </b>

<b>𝐃𝐄𝐕𝐒:</b>
- <a href=Club</a>  
"""
    TTS_TXT = """<b>TEXT TO SPEACH</b>
Simple Telegram Text-To-Speech Module.
It can use the following as speech synthesis engines:

Amazon's Polly engine
Google's TTS engine by way of the gTTS library
"""
    COVID_TXT = """<b><u>𝖢𝗈𝗏𝗂𝖽 19 𝗂𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇</u><b/>
𝖢𝗈𝗋𝗈𝗇𝖺 𝗂𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇 𝗈𝖿 𝗒𝗈𝗎𝗋 𝖼𝗈𝗎𝗇𝗍𝗋𝗒 / 𝖳𝗈 𝗄𝗇𝗈𝗐 𝗍𝗁𝖾 𝖼𝗈𝗏𝗂𝖽 𝗂𝗇𝖿𝗈 𝗈𝖿 𝖺𝗇𝗒 𝖼𝗈𝗎𝗇𝗍𝗋𝗒            
<b>𝖢𝗈𝗆𝗆𝖺𝗇𝖽:</b>
/covid [country name] - 𝖦𝖾𝗍 𝗂𝗇𝖿𝗈 𝖺𝖻𝗈𝗎𝗍 𝖼𝗈𝗏𝗂𝖽 𝖼𝖺𝗌𝖾𝗌 𝗂𝗇 𝗒𝗈𝗎𝗋 𝖼𝗈𝗎𝗇𝗍𝗋𝗒
<b>𝖴𝗌𝖺𝗀𝖾</b>
- 𝖢𝗈𝗎𝗅𝖽 𝖻𝖾 𝗎𝗌𝖾𝖽 𝗂𝗇 𝗉𝗆 𝖺𝗇𝖽 𝗀𝗋𝗈𝗎𝗉𝗌
    """
    BAN_TXT = """<b>𝖡𝖺𝗇𝗌:</b>
𝖲𝗈𝗆𝖾 𝗉𝖾𝗈𝗉𝗅𝖾 𝗇𝖾𝖾𝖽 𝗍𝗈 𝖻𝖾 𝗉𝗎𝖻𝗅𝗂𝖼𝗅𝗒 𝖻𝖺𝗇𝗇𝖾𝖽; 𝗌𝗉𝖺𝗆𝗆𝖾𝗋𝗌, 𝖺𝗇𝗇𝗈𝗒𝖺𝗇𝖼𝖾𝗌, 𝗈𝗋 𝗃𝗎𝗌𝗍 𝗍𝗋𝗈𝗅𝗅𝗌.  
𝖳𝗁𝗂𝗌 𝗆𝗈𝖽𝗎𝗅𝖾 𝖺𝗅𝗅𝗈𝗐𝗌 𝗒𝗈𝗎 𝗍𝗈 𝖽𝗈 𝗍𝗁𝖺𝗍 𝖾𝖺𝗌𝗂𝗅𝗒, 𝖻𝗒 𝖾𝗑𝗉𝗈𝗌𝗂𝗇𝗀 𝗌𝗈𝗆𝖾 𝖼𝗈𝗆𝗆𝗈𝗇 𝖺𝖼𝗍𝗂𝗈𝗇𝗌, 𝗌𝗈 𝖾𝗏𝖾𝗋𝗒𝗈𝗇𝖾 𝗐𝗂𝗅𝗅 𝗌𝖾𝖾!

<b>𝖠𝖽𝗆𝗂𝗇 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌:</b>
- /ban - 𝖡𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋
- /tban - 𝖳𝖾𝗆𝗉𝗈𝗋𝖺𝗋𝗂𝗅𝗒 𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋. 𝖤𝗑𝖺𝗆𝗉𝗅𝖾 𝗍𝗂𝗆𝖾 𝗏𝖺𝗅𝗎𝖾𝗌: 𝟦𝗆 = 𝟦 𝗆𝗂𝗇𝗎𝗍𝖾𝗌, 𝟥𝗁 = 𝟥 𝗁𝗈𝗎𝗋𝗌, 𝟨𝖽 = 𝟨 𝖽𝖺𝗒𝗌, 𝟧𝗐 = 𝟧 𝗐𝖾𝖾𝗄𝗌.
- /unban - 𝖴𝗇𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋

<b>𝖤𝗑𝖺𝗆𝗉𝗅𝖾𝗌:</b>
- 𝖡𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋 𝖿𝗈𝗋 𝗍𝗐𝗈 𝗁𝗈𝗎𝗋𝗌. 
-> /tban @𝗎𝗌𝖾𝗋𝗇𝖺𝗆𝖾 𝟤𝗁
"""
    PING_TXT= """<b>𝖯𝗂𝗇𝗀:</b>

𝖧𝖾𝗅𝗉𝗌 𝗒𝗈𝗎 𝗍𝗈 𝗄𝗇𝗈𝗐 𝗒𝗈𝗎𝗋 𝗉𝗂𝗇𝗀, 𝖨𝗇 𝗌𝗁𝗈𝗋𝗍-𝗍𝖾𝗋𝗆𝗌 '𝗆𝗌'.

<b>𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌:</b>

- /alive - 𝖳𝗈 𝖼𝗁𝖾𝖼𝗄 𝗐𝗁𝖾𝗍𝗁𝖾𝗋 𝗒𝗈𝗎 𝖺𝗋𝖾 𝖺𝗅𝗂𝗏𝖾
- /hi - 𝖭𝗈 𝗁𝗂, 𝖡𝗈𝗍 𝗁𝖺𝗍𝖾𝗌 𝗁𝗂
- /ping - 𝖳𝗈 𝖪𝗇𝗈𝗐 𝗒𝗈𝗎𝗋 𝗉𝗂𝗇𝗀 

<b>𝖴𝗌𝖺𝗀𝖾:</b>

• 𝖳𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝖼𝖺𝗇 𝖻𝖾 𝗎𝗌𝖾𝖽 𝗂𝗇 𝗉𝗆𝗌 𝖺𝗇𝖽 𝗀𝗋𝗈𝗎𝗉𝗌.
• 𝖳𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝖼𝖺𝗇 𝖻𝖾 𝗎𝗌𝖾𝖽 𝖻𝗎𝗒 𝖾𝗏𝖾𝗋𝗒𝗈𝗇𝖾 𝗂𝗇 𝗀𝗋𝗈𝗎𝗉𝗌 𝖺𝗇𝖽 𝖻𝗈𝗍𝗌 𝗉𝗆.
"""
    JSON_TXT = """<b>𝖩𝗌𝗈𝗇:</b>
𝖡𝗈𝗍 𝗋𝖾𝗍𝗎𝗋𝗇𝗌 𝗃𝗌𝗈𝗇 𝖿𝗈𝗋 𝖺𝗅𝗅 𝗋𝖾𝗉𝗅𝗂𝖾𝖽 𝗆𝖾𝗌𝗌𝖺𝗀𝖾𝗌 𝗐𝗂𝗍𝗁 /json. 
<b>𝖥𝖾𝖺𝗍𝗎𝗋𝖾𝗌:</b>
𝖬𝖾𝗌𝗌𝖺𝗀𝖾 𝖤𝖽𝗂𝗍𝗍𝗂𝗇𝗀 JSON
𝖯𝗆 𝖲𝗎𝗉𝗉𝗈𝗋𝗍 
𝖦𝗋𝗈𝗎𝗉 𝖲𝗎𝗉𝗉𝗈𝗋𝗍
"""
    FUN_TXT ="""<b>𝖥𝗎𝗇 𝖬𝗈𝖽𝗎𝗅𝖾𝗌</b> 
    
<b>🎲 𝖭𝗈𝗍𝗁𝗂𝗇𝗀 𝗆𝗎𝖼𝗁 𝗃𝗎𝗌𝗍 𝗌𝗈𝗆𝖾 𝖿𝗎𝗇 𝗌𝗍𝗎𝖿𝖿𝗌</b>
𝗍𝗋𝗒 𝗍𝗁𝖾𝗌𝖾 𝗈𝗎𝗍: 
𝟣. /dice - 𝖱𝗈𝗅𝗅 𝗍𝗁𝖾 𝖽𝗂𝖼𝖾
𝟤. /Throw 𝗈𝗋 /Dart - 𝖳𝗈 𝗍𝗁𝗋𝗈𝗐 𝖺 𝖽𝖺𝗋𝗍
3. /Runs - 𝖩𝗎𝗌𝗍 𝗌𝗈𝗆𝖾 𝗋𝖺𝗇𝖽𝗈𝗆 𝖽𝖺𝗂𝗅𝗈𝗎𝗀𝖾𝗌
4. /Goal or /Shoot - 𝖳𝗈 𝗀𝗈𝖺𝗅 𝗈𝗋 𝗌𝗁𝗈𝗈𝗍 𝖺 𝖻𝖺𝗅𝗅
"""
    PURGE_TXT ="""<b>𝖯𝗎𝗋𝗀𝖾</b>
- 𝖣𝖾𝗅𝖾𝗍𝖾 𝖺 𝗅𝗈𝗍𝗌 𝗈𝖿 𝗆𝖾𝗌𝗌𝖺𝗀𝖾𝗌 𝖿𝗋𝗈𝗆 𝖺 𝗀𝗋𝗈𝗎𝗉!
    
 <b>𝖠𝖽𝗆𝗂𝗇</b> 
◉ /purge :- 𝖣𝖾𝗅𝖾𝗍𝖾 𝖺𝗅𝗅 𝗆𝖾𝗌𝗌𝖺𝗀𝖾𝗌 𝖿𝗋𝗈𝗆 𝗍𝗁𝖾 𝗋𝖾𝗉𝗅𝗂𝖾𝖽 𝗆𝖾𝗌𝗌𝖺𝗀𝖾 𝗍𝗈, 𝖳𝗁𝖾 𝖼𝗎𝗋𝗋𝖾𝗇𝗍 𝗆𝖾𝗌𝗌𝖺𝗀𝖾
    """
    MANUELFILTER_TXT = """Help: <b>Filters</b>
    
- Filter is the feature were users can set automated replies for a particular keyword and Auto Filter will respond whenever a keyword is found the message

<b>NOTE:</b>

1. Auto Filter should have admin privillage.
2. Only admins can add filters in a chat.
3. Alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>

• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    
    SONG_TXT = """<b>𝖲𝗈𝗇𝗀 𝖣𝗈𝗐𝗇𝗅𝗈𝖺𝖽 𝖬𝗈𝖽𝗎𝗅𝖾</b>
- 𝖨𝖿 𝗒𝗈𝗎 𝗐𝖺𝗇𝗍 𝗍𝗈 𝖽𝗈𝗐𝗇𝗅𝗈𝖺𝖽 𝖺 𝗌𝗈𝗇𝗀, 𝖽𝗈𝗇'𝗍 𝗌𝖾𝖺𝗋𝖼𝗁 𝖿𝗈𝗋 𝗈𝗍𝗁𝖾𝗋 𝖻𝗈𝗍 𝗁𝖾𝗋𝖾 𝗂𝗌 𝗍𝗁𝖾 𝖺𝗅𝗅 𝗂𝗇 𝗈𝗇𝖾 𝖻𝗈𝗍
<b>𝖢𝗈𝗆𝗆𝖺𝗇𝖽</b>
- /song [Song Name] - 𝖳𝗈 𝗀𝖾𝗍 𝗍𝗁𝖾 𝗌𝗈𝗇𝗀
<b>Usage</b>
- 𝖢𝖺𝗇 𝖻𝖾 𝗎𝗌𝖾𝖽 𝖻𝗒 𝖾𝗏𝖾𝗋𝗒 𝗈𝗇𝖾
- 𝖶𝗈𝗋𝗄𝗌 𝗈𝗇𝗅𝗒 𝗂𝗇 𝖻𝗈𝗍𝗌 𝗉𝗆
<b>𝖡𝗎𝗀</b>
𝖲𝗈𝗆𝖾𝗍𝗂𝗆𝖾𝗌 𝗂𝗍 𝗐𝗂𝗅𝗅 𝗌𝗁𝗈𝗐 𝖺𝗇 𝖾𝗋𝗋𝗈𝗋!
"""
    MUTE_TXT = """<b>𝖬𝗎𝗍𝖾:</b>

𝖲𝗈𝗆𝖾 𝗉𝖾𝗈𝗉𝗅𝖾 𝗇𝖾𝖾𝖽 𝗍𝗈 𝖻𝖾 𝗉𝗎𝖻𝗅𝗂𝖼𝗅𝗒 Muted; 𝗌𝗉𝖺𝗆𝗆𝖾𝗋𝗌, 𝖺𝗇𝗇𝗈𝗒𝖺𝗇𝖼𝖾𝗌, 𝗈𝗋 𝗃𝗎𝗌𝗍 𝗍𝗋𝗈𝗅𝗅𝗌.  
𝖳𝗁𝗂𝗌 𝗆𝗈𝖽𝗎𝗅𝖾 𝖺𝗅𝗅𝗈𝗐𝗌 𝗒𝗈𝗎 𝗍𝗈 𝖽𝗈 𝗍𝗁𝖺𝗍 𝖾𝖺𝗌𝗂𝗅𝗒, 𝖻𝗒 𝖾𝗑𝗉𝗈𝗌𝗂𝗇𝗀 𝗌𝗈𝗆𝖾 𝖼𝗈𝗆𝗆𝗈𝗇 𝖺𝖼𝗍𝗂𝗈𝗇𝗌, 𝗌𝗈 𝖾𝗏𝖾𝗋𝗒𝗈𝗇𝖾 𝗐𝗂𝗅𝗅 𝗌𝖾𝖾!   

<b>🔞 𝖠𝖽𝗆𝗂𝗇 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌:</b>

- /mute - 𝖬𝗎𝗍𝖾 𝖠 𝖴𝗌𝖾𝗋 
- /tmute - 𝖳𝖾𝗆𝗉𝗈𝗋𝖺𝗋𝗂𝗅𝗒 𝖬𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋. 𝖤𝗑𝖺𝗆𝗉𝗅𝖾 𝗍𝗂𝗆𝖾 𝗏𝖺𝗅𝗎𝖾𝗌: 𝟦𝗆 = 𝟦 𝗆𝗂𝗇𝗎𝗍𝖾𝗌, 𝟥𝗁 = 𝟥 𝗁𝗈𝗎𝗋𝗌, 𝟨𝖽 = 𝟨 𝖽𝖺𝗒𝗌, 𝟧𝗐 = 𝟧 𝗐𝖾𝖾𝗄𝗌. 
- /unmute - 𝖴𝗇mute 𝖺 𝗎𝗌𝖾𝗋.  
𝖤𝗑𝖺𝗆𝗉𝗅𝖾𝗌:
- 𝖬𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋 𝖿𝗈𝗋 𝗍𝗐𝗈 𝗁𝗈𝗎𝗋𝗌. 
-> /tmute @𝗎𝗌𝖾𝗋𝗇𝖺𝗆𝖾 𝟤𝗁
"""
    CNTRY_TXT = """Use /Country (Country name)
- Get info about Country 
"""
    TRNT_TXT = """This feature will be added soon"""
    SHORT_TXT = """To Short your big urls
- Command /Short Link 
"""
    WEATHER_TXT = """Under development"""
    BUTTON_TXT = """Help: <b>𝖡𝗎𝗍𝗍𝗈𝗇𝗌</b>
Auto Filter 𝗌𝗎𝗉𝗉𝗈𝗋𝗍𝗌 𝖻𝗈𝗍𝗁 𝗎𝗋𝗅 𝖺𝗇𝖽 𝖺𝗅𝖾𝗋𝗍 𝗂𝗇𝗅𝗂𝗇𝖾 𝖻𝗎𝗍𝗍𝗈𝗇𝗌, 𝗇𝗈𝗐 𝗅𝖾𝗍𝗌 𝗌𝖾𝖾 𝗁𝗈𝗐 𝗍𝗈 𝗂𝗆𝗉𝗅𝖾𝗆𝖾𝗇𝗍 𝗂𝗍. 
<b>𝖭𝖡:</b>
𝟣. 𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝗐𝗂𝗅𝗅 𝗇𝗈𝗍 𝖺𝗅𝗅𝗈𝗐𝗌 𝗒𝗈𝗎 𝗍𝗈 𝗌𝖾𝗇𝖽 𝖻𝗎𝗍𝗍𝗈𝗇𝗌 𝗐𝗂𝗍𝗁𝗈𝗎𝗍 𝖺𝗇𝗒 𝖼𝗈𝗇𝗍𝖾𝗇𝗍, 𝗌𝗈 𝖼𝗈𝗇𝗍𝖾𝗇𝗍 𝗂𝗌 𝗆𝖺𝗇𝖽𝖺𝗍𝗈𝗋𝗒. 
𝟤. 𝖳𝗁𝗂𝗌 𝖻𝗈𝗍 𝗌𝗎𝗉𝗉𝗈𝗋𝗍𝗌 𝖻𝗎𝗍𝗍𝗈𝗇𝗌 𝗐𝗂𝗍𝗁 𝖺𝗇𝗒 𝗍𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝗆𝖾𝖽𝗂𝖺 𝗍𝗒𝗉𝖾. 
𝟥. 𝖡𝗎𝗍𝗍𝗈𝗇𝗌 𝗌𝗁𝗈𝗎𝗅𝖽 𝖻𝖾 𝗉𝗋𝗈𝗉𝖾𝗋𝗅𝗒 𝖿𝗈𝗋𝗆𝖺𝗍𝗍𝖾𝖽 𝖺𝗌 𝖻𝖾𝗅𝗈𝗐 𝗈𝗋 𝖾𝗅𝗌𝖾 𝗋𝖾𝗌𝗎𝗅𝗍 𝗐𝗂𝗅𝗅 𝖻𝖾 𝗆𝖺𝗅𝖿𝗈𝗋𝗆𝖾𝖽. 
<b>𝖴𝖱𝖫 𝖻𝗎𝗍𝗍𝗈𝗇𝗌:</b>
- 𝗌𝗂𝗇𝗀𝗅𝖾 𝖻𝗎𝗍𝗍𝗈𝗇 
<code>[𝖡𝗎𝗍𝗍𝗈𝗇](𝖻𝗎𝗍𝗍𝗈𝗇𝗎𝗋𝗅://𝗍.𝗆𝖾/FilmClub_Channel)</code>
- 𝖣𝗈𝗎𝖻𝗅𝖾 𝖻𝗎𝗍𝗍𝗈𝗇 
<code>[𝖡𝗎𝗍𝗍𝗈𝗇𝟣](𝖻𝗎𝗍𝗍𝗈𝗇𝗎𝗋𝗅://𝗍.𝗆𝖾/FilmClub_Channel)
[𝖡𝗎𝗍𝗍𝗈𝗇𝟤](𝖻𝗎𝗍𝗍𝗈𝗇𝗎𝗋𝗅://𝗍.𝗆𝖾/telegram)</code>
- 𝖣𝗈𝗎𝖻𝗅𝖾 𝖻𝗎𝗍𝗍𝗈𝗇𝗌 𝗂𝗇 𝖲𝖺𝗆𝖾 𝖱𝖺𝗐 
<code>[𝖡𝗎𝗍𝗍𝗈𝗇𝟣](𝖻𝗎𝗍𝗍𝗈𝗇𝗎𝗋𝗅://𝗍.𝗆𝖾/FilmClub_Channel)
[𝖡𝗎𝗍𝗍𝗈𝗇𝟤](𝖻𝗎𝗍𝗍𝗈𝗇𝗎𝗋𝗅://𝗍.𝗆𝖾/FilmClub_Channel:𝗌𝖺𝗆𝖾)</code>
<b>𝖠𝗅𝖾𝗋𝗍 𝖻𝗎𝗍𝗍𝗈𝗇𝗌:</b>
<code>[𝖡𝗎𝗍𝗍𝗈𝗇](𝖻𝗎𝗍𝗍𝗈𝗇𝖺𝗅𝖾𝗋𝗍:𝗍𝗁𝗂𝗌 𝗂𝗌 𝖺𝗇 𝖺𝗅𝖾𝗋𝗍!)</code>
"""
    AUTOFILTER_TXT = """<b>Auto Filter</b>
<b>𝖭𝗈𝗍𝖾:</b>
𝟣. 𝖬𝖺𝗄𝖾 𝗆𝖾 𝗍𝗁𝖾 𝖺𝖽𝗆𝗂𝗇 𝗈𝖿 𝗒𝗈𝗎𝗋 𝖼𝗁𝖺𝗇𝗇𝖾𝗅 𝗂𝖿 𝗂𝗍'𝗌 𝗉𝗋𝗂𝗏𝖺𝗍𝖾. 
𝟤. 𝗆𝖺𝗄𝖾 𝗌𝗎𝗋𝖾 𝗍𝗁𝖺𝗍 𝗒𝗈𝗎𝗋 𝖼𝗁𝖺𝗇𝗇𝖾𝗅 𝖽𝗈𝖾𝗌 𝗇𝗈𝗍 𝖼𝗈𝗇𝗍𝖺𝗂𝗇𝗌 𝖼𝖺𝗆 𝗋𝗂𝗉, 𝗉𝗈𝗋𝗇 𝖺𝗇𝖽 𝖿𝖺𝗄𝖾 𝖿𝗂𝗅𝖾𝗌. 
𝟥. 𝖥𝗈𝗋𝗐𝖺𝗋𝖽 𝗍𝗁𝖾 𝗅𝖺𝗌𝗍 𝗆𝖾𝗌𝗌𝖺𝗀𝖾 𝗍𝗈 𝗆𝖾 𝗐𝗂𝗍𝗁 𝗊𝗎𝗈𝗍𝖾𝗌.  𝖨'𝗅𝗅 𝖺𝖽𝖽 𝖺𝗅𝗅 𝗍𝗁𝖾 𝖿𝗂𝗅𝖾𝗌 𝗂𝗇 𝗍𝗁𝖺𝗍 𝖼𝗁𝖺𝗇𝗇𝖾𝗅 𝗍𝗈 𝗆𝗒 𝖽𝖻.
"""
    CONNECTION_TXT = """<b>𝖢𝗈𝗇𝗇𝖾𝖼𝗍𝗂𝗈𝗇𝗌</b>
𝖴𝗌𝖾𝖽 𝗍𝗈 𝖼𝗈𝗇𝗇𝖾𝖼𝗍 𝖻𝗈𝗍 𝗍𝗈 𝖯𝖬 𝗐𝗁𝗂𝖼𝗁 𝗅𝖾𝗍 𝗐𝗂𝗅𝗅 𝗒𝗈𝗎 𝗍𝗈 𝖾𝗑𝖾𝖼𝗎𝗍𝖾 𝖻𝗈𝗍𝗁 𝗇𝗈𝗋𝗆𝖺𝗅 𝖿𝗂𝗅𝗍𝖾𝗋 𝗋𝖾𝗅𝖺𝗍𝖾𝖽 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖺𝗇𝖽 𝗌𝗈𝗆𝖾 𝗈𝗍𝗁𝖾𝗋 𝗌𝖾𝗇𝗌𝗂𝗍𝗂𝗏𝖾 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝗋𝗂𝗀𝗁𝗍 𝖿𝗋𝗈𝗆 𝗍𝗁𝖾 𝖯𝖬 𝗍𝗁𝖺𝗍 𝗐𝗂𝗅𝗅 𝗋𝖾𝖿𝗅𝖾𝖼𝗍 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉 𝗐𝗁𝗂𝖼𝗁 𝗁𝖾𝗅𝗉𝗌 𝗒𝗈𝗎 𝗍𝗈 𝗄𝖾𝖾𝗉 𝗍𝗁𝖾 𝖿𝗂𝗅𝗍𝖾𝗋 𝖺𝖽𝖽𝗂𝗍𝗂𝗈𝗇𝗌 𝖺𝗇𝖽 𝗈𝗍𝗁𝖾𝗋 𝗌𝗍𝗎𝖿𝖿𝗌 𝗉𝗋𝗂𝗏𝖺𝗍𝖾 𝖺𝗇𝖽 𝗁𝖾𝗅𝗉𝗌 𝗍𝗈 𝗉𝗋𝖾𝗏𝖾𝗇𝗍 𝖿𝗅𝗈𝗈𝖽𝗂𝗇𝗀. 
𝖭𝖮𝖳𝖤:
𝟣. 𝖮𝗇𝗅𝗒 𝖺𝖽𝗆𝗂𝗇𝗌 𝖼𝖺𝗇 𝖺𝖽𝖽 𝖺 𝖼𝗈𝗇𝗇𝖾𝖼𝗍𝗂𝗈𝗇. 
𝟤. 𝖨𝗇 𝖺 𝖼𝗁𝖺𝗍 𝗒𝗈𝗎 𝖼𝖺𝗇 𝗌𝗂𝗆𝗉𝗅𝗒 𝗎𝗌𝖾 𝗍𝗁𝖾 /connect 𝖿𝗈𝗋 𝗌𝗍𝖺𝗋𝗍𝗂𝗇𝗀 𝖺 𝖼𝗈𝗇𝗇𝖾𝖼𝗍𝗂𝗈𝗇  
𝟥. 𝖨𝗇 𝖯𝖬 𝗒𝗈𝗎 𝗆𝗎𝗌𝗍 𝗌𝗉𝖾𝖼𝗂𝖿𝗒 𝖼𝗁𝖺𝗍 𝗂𝖽 𝗋𝗂𝗀𝗁𝗍 𝖺𝖿𝗍𝖾𝗋 𝗍𝗁𝖾 𝖼𝗈𝗆𝗆𝖺𝗇𝖽. 
𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖺𝗇𝖽 𝖴𝗌𝖺𝗀𝖾: 
/connect - 𝖼𝗈𝗇𝗇𝖾𝖼𝗍 𝖺 𝗉𝖺𝗋𝗍𝗂𝖼𝗎𝗅𝖺𝗋 𝖼𝗁𝖺𝗍 𝗍𝗈 𝗒𝗈𝗎𝗋 𝖯𝖬 
/disconnect  - 𝖽𝗂𝗌𝖼𝗈𝗇𝗇𝖾𝖼𝗍 𝖿𝗋𝗈𝗆 𝖺 𝖼𝗁𝖺𝗍 
/connections - 𝗅𝗂𝗌𝗍 𝖺𝗅𝗅 𝗒𝗈𝗎𝗋 𝖼𝗈𝗇𝗇𝖾𝖼𝗍𝗂𝗈𝗇𝗌

"""
    FILTER_TXT ="""𝖲𝖾𝗅𝖾𝖼𝗍 𝖺 𝖿𝗂𝗅𝗍𝖾𝗋 𝗍𝗒𝗉𝖾 𝖻𝖾𝗅𝗈𝗐:"""
    PIN_TXT = """<b>𝖯𝖨𝖭:</b>
𝖠𝗅𝗅 𝗍𝗁𝖾 𝗉𝗂𝗇 𝗋𝖾𝗅𝖺𝗍𝖾𝖽 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖼𝖺𝗇 𝖻𝖾 𝖿𝗈𝗎𝗇𝖽 𝗁𝖾𝗋𝖾; 𝗄𝖾𝖾𝗉 𝗒𝗈𝗎𝗋 𝖼𝗁𝖺𝗍 𝗎𝗉 𝗍𝗈 𝖽𝖺𝗍𝖾 𝗈𝗇 𝗍𝗁𝖾 𝗅𝖺𝗍𝖾𝗌𝗍 𝗇𝖾𝗐𝗌 𝗐𝗂𝗍𝗁 𝖺 𝗌𝗂𝗆𝗉𝗅𝖾 𝗉𝗂𝗇𝗇𝖾𝖽 𝗆𝖾𝗌𝗌𝖺𝗀𝖾!  

<b>𝖠𝖽𝗆𝗂𝗇 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌:</b> 
- /pin: 𝖯𝗂𝗇 𝗍𝗁𝖾 𝗆𝖾𝗌𝗌𝖺𝗀𝖾 𝗒𝗈𝗎 𝗋𝖾𝗉𝗅𝗂𝖾𝖽 𝗍𝗈 𝖬𝖾𝗌𝗌𝖺𝗀𝖾 𝗍𝗈 𝗌𝖾𝗇𝖽 𝖺 𝗇𝗈𝗍𝗂𝖿𝗂𝖼𝖺𝗍𝗂𝗈𝗇 𝗍𝗈 𝗀𝗋𝗈𝗎𝗉 𝗆𝖾𝗆𝖻𝖾𝗋𝗌. 
- /unpin: 𝖴𝗇𝗉𝗂𝗇 𝗍𝗁𝖾 𝖼𝗎𝗋𝗋𝖾𝗇𝗍 𝗉𝗂𝗇𝗇𝖾𝖽 𝗆𝖾𝗌𝗌𝖺𝗀𝖾. 𝖨𝖿 𝗎𝗌𝖾𝖽 𝖺𝗌 𝖺 𝗋𝖾𝗉𝗅𝗒, 𝗎𝗇𝗉𝗂𝗇𝗌 𝗍𝗁𝖾 𝗋𝖾𝗉𝗅𝗂𝖾𝖽 𝗍𝗈 𝗆𝖾𝗌𝗌𝖺𝗀𝖾.
"""
    TGRAPH_TXT ="""<b>𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗉𝗁</b>
𝖣𝗈 𝖺𝗌 𝗒𝗈𝗎 𝗐𝗂𝗌𝗁 𝗐𝗂𝗍𝗁 telegra.ph 𝗆𝗈𝖽𝗎𝗅𝖾!
<b>𝖴𝗌𝖺𝗀𝖾:</b>

- /telegraph - 𝖲𝖾𝗇𝖽 𝗆𝖾 𝖯𝗂𝖼𝗍𝗎𝗋𝖾 𝗈𝗋 𝖵𝗂𝖽𝖾 𝖴𝗇𝖽𝖾𝗋 (𝟧𝖬𝖡)

<b>𝖭𝖮𝖳𝖤:</b>
• 𝖲𝖺𝗄𝗎𝗋𝖺 𝗌𝗁𝗈𝗎𝗅𝖽 𝗁𝖺𝗏𝖾 𝖺𝖽𝗆𝗂𝗇 𝗉𝗋𝗂𝗏𝗂𝗅𝗅𝖺𝗀𝖾.
• 𝖳𝗁𝗂𝗌 𝖢𝗈𝗆𝗆𝖺𝗇𝖽 𝖨𝗌 𝖠𝗏𝖺𝗂𝗅𝖺𝖻𝗅𝖾 𝗂𝗇 𝗀𝗈𝗎𝗉𝗌 𝖺𝗇𝖽 𝗉𝗆𝗌
• 𝖳𝗁𝗂𝗌 𝖢𝗈𝗆𝗆𝖺𝗇𝖽 𝖢𝖺𝗇 𝖻𝖾 𝗎𝗌𝖾𝖽 𝖻𝗒 𝖾𝗏𝖾𝗋𝗒𝗈𝗇𝖾
"""
    IMBD_TXT ="""<b>Search</b>
- 𝖲𝖾𝖺𝗋𝖼𝗁 𝖿𝗂𝗅𝗆 𝖽𝖾𝗍𝖺𝗂𝗅𝗌 𝗐𝗂𝗍𝗁𝗈𝗎𝗍 𝗅𝖾𝖺𝗏𝗂𝗇𝗀 𝗍𝖾𝗅𝖾𝗀𝗋𝖺𝗆
- 𝖲𝖾𝖺𝗋𝖼𝗁 𝖺𝗇𝗒𝗍𝗁𝗂𝗇𝗀 𝗐𝗂𝗍𝗁𝗈𝗎𝗍 𝗅𝖾𝖺𝗏𝗂𝗇𝗀 𝗍𝖾𝗅𝖾𝗀𝗋𝖺𝗆
<b>U𝗌𝖺𝗀𝖾:</b>
- /imdb - 𝗀𝖾𝗍 𝗍𝗁𝖾 𝖿𝗂𝗅𝗆 𝗂𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇 𝖿𝗋𝗈𝗆 𝖨𝖬𝖣𝖻 𝗌𝗈𝗎𝗋𝖼𝖾
- /search - 𝗀𝖾𝗍 𝗍𝗁𝖾 𝖿𝗂𝗅𝗆 𝗂𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇 𝖿𝗋𝗈𝗆 𝗏𝖺𝗋𝗂𝗈𝗎𝗌 𝗌𝗈𝗎𝗋𝖼𝖾𝗌
"""
    INFO_TXT ="""<b>𝖨𝗇𝖿𝗈</b>
𝖦𝖾𝗍 𝗂𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇 𝖺𝖻𝗈𝗎𝗍 𝗌𝗈𝗆𝖾𝗍𝗁𝗂𝗇𝗀!
<b>𝖴𝗌𝖺𝗀𝖾:</b>
➥ /id - 𝗀𝖾𝗍 𝗍𝗁𝖾 𝗂𝖽 𝗈𝖿 𝖺 𝗌𝗉𝖾𝖼𝗂𝖿𝖾𝖽 𝗎𝗌𝖾𝗋
➥ /info - 𝗀𝖾𝗍 𝗍𝗁𝖾 𝗂𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇 𝖺𝖻𝗈𝗎𝗍 𝖺 𝗎𝗌𝖾𝗋
"""
    EXTRAMOD_TXT = """<b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of tessa

<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>
"""
    ADMIN_TXT = """
<b>🤖Bot Commands and Usage</b>

• /filter 𝗈𝗋 /add <code>𝖺𝖽𝖽 𝖺 𝖿𝗂𝗅𝗍𝖾𝗋</code>
• /filters 𝗈𝗋 /viewfilters <code>𝗅𝗂𝗌𝗍 𝖺𝗅𝗅 𝗍𝗁𝖾 𝖿𝗂𝗅𝗍𝖾𝗋𝗌 𝗈𝖿 𝖺 𝖼𝗁𝖺𝗍</code>
• /stop 𝗈𝗋 /del <code>𝖽𝖾𝗅𝖾𝗍𝖾 𝖺 𝗌𝗉𝖾𝖼𝗂𝖿𝗂𝖼 𝖿𝗂𝗅𝗍𝖾𝗋</code>
• /stopall 𝗈𝗋 /delall <code>𝖽𝖾𝗅𝖾𝗍𝖾 𝗍𝗁𝖾 𝗐𝗁𝗈𝗅𝖾 𝖿𝗂𝗅𝗍𝖾𝗋𝗌 𝗂𝗇 𝖺 𝖼𝗁𝖺𝗍</code>
• /imdb <code>𝗀𝖾𝗍 𝗍𝗁𝖾 𝖿𝗂𝗅𝗆 𝗂𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇 𝖿𝗋𝗈𝗆 𝖨𝖬𝖣𝖻 𝗌𝗈𝗎𝗋𝖼𝖾</code>
• /search <code>𝗀𝖾𝗍 𝗍𝗁𝖾 𝖿𝗂𝗅𝗆 𝗂𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇 𝖿𝗋𝗈𝗆 𝗏𝖺𝗋𝗂𝗈𝗎𝗌 𝗌𝗈𝗎𝗋𝖼𝖾𝗌</code>
• /purge <code>𝖣𝖾𝗅𝖾𝗍𝖾 𝖺𝗅𝗅 𝗆𝖾𝗌𝗌𝖺𝗀𝖾𝗌 Of Groups</code>
• /telegraph <code>𝖲𝖾𝗇𝖽 𝗆𝖾 𝖯𝗂𝖼𝗍𝗎𝗋𝖾 𝗈𝗋 𝖵𝗂𝖽𝖾 𝖴𝗇𝖽𝖾𝗋 (𝟧𝖬𝖡)</code>
• /pin <code>𝖯𝗂𝗇 𝗍𝗁𝖾 𝗆𝖾𝗌𝗌𝖺𝗀𝖾 𝗒𝗈𝗎 𝗋𝖾𝗉𝗅𝗂𝖾𝖽 𝗍𝗈 𝖬𝖾𝗌𝗌𝖺𝗀𝖾 𝗍𝗈 𝗌𝖾𝗇𝖽 𝖺 𝗇𝗈𝗍𝗂𝖿𝗂𝖼𝖺𝗍𝗂𝗈𝗇 𝗍𝗈 𝗀𝗋𝗈𝗎𝗉 𝗆𝖾𝗆𝖻𝖾𝗋𝗌</code>
• /unpin <code>𝖴𝗇𝗉𝗂𝗇 𝗍𝗁𝖾 𝖼𝗎𝗋𝗋𝖾𝗇𝗍 𝗉𝗂𝗇𝗇𝖾𝖽 𝗆𝖾𝗌𝗌𝖺𝗀𝖾</code>
• /id <code>𝗀𝖾𝗍 𝗍𝗁𝖾 𝗂𝖽 𝗈𝖿 𝖺 𝗌𝗉𝖾𝖼𝗂𝖿𝖾𝖽 𝗎𝗌𝖾𝗋</code>
• /info <code>𝗀𝖾𝗍 𝗍𝗁𝖾 𝗂𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇 𝖺𝖻𝗈𝗎𝗍 𝖺 𝗎𝗌𝖾𝗋</code>
• /covid [country name] <code>𝖦𝖾𝗍 𝗂𝗇𝖿𝗈 𝖺𝖻𝗈𝗎𝗍 𝖼𝗈𝗏𝗂𝖽 𝖼𝖺𝗌𝖾𝗌 𝗂𝗇 𝗒𝗈𝗎𝗋 𝖼𝗈𝗎𝗇𝗍𝗋𝗒</code>
• /song [Song Name] <code>𝖳𝗈 𝗀𝖾𝗍 𝗍𝗁𝖾 𝗌𝗈𝗇𝗀</code>
• /tr [language code][reply] <code>𝖳𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝖾 𝗋𝖾𝗉𝗅𝗂𝖾𝖽 𝗆𝖾𝗌𝗌𝖺𝗀𝖾 𝗍𝗈 𝗌𝗉𝖾𝖼𝗂𝖿𝗂𝖼 𝗅𝖺𝗇𝗀𝗎𝖺𝗀𝖾.</code>
• /Country (Country name) <code>Get info about Country</code>
• /stats <code>Get Activities Of Bots</code>
"""
    STATUS_TXT = """𝖳𝗈𝗍𝖺𝗅 𝖥𝗂𝗅𝖾𝗌: <code>{}</code>
𝖳𝗈𝗍𝖺𝗅 𝖬𝖾𝗆𝖻𝖾𝗋𝗌: <code>{}</code>
𝖳𝗈𝗍𝖺𝗅 𝖢𝗁𝖺𝗍𝗌: <code>{}</code>
𝖴𝗌𝖾𝖽 𝖲𝗍𝗈𝗋𝖺𝗀𝖾: <code>{}</code> 𝙼𝚒𝙱
"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
