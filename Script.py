class script(object):
    START_TXT = """<b>HELLO {},
MY NAME IS <a href=https://t.me/{}>{}</a>, I AM A âĄ POWERFUL AUTOFILTER BOT âĄ. HERE YOU CAN GET ALL MOVIES\n\nWORK FOR @SS_Movie_Club
MANAGED BY @SS_ADMIN_308_bot</b>"""
    HELP_TXT = """<b>đ·đŽđ {}
HERE IS THE HELP FOR MY COMMANDS.</b>"""
    FEATURES_TXT = """<b>đ·đŽđ {}
HERE IS THE ALL FEATURES.</b>
âź Auto Filter
âź Manual Filter
âź IMDB
âź Welcome Message
âź Admin Commands
âź Broadcast
âź Index
âź IMDB search
âź Inline Search
âź Random pics
âź ids and User info
âź Stats, Users, Chats, Ban, Unban, Leave, Disable, Channel
âź Spelling Check Feature
âź Youtube Video , Song , Thumbnail Download.
âź Image Edit
âź Google Translator
âź Telegraph
âź Games
âź Sticker ID Generator
âź Text Message URL
âź URL Shorter
âź File to Link
âź Image Editor"""
    ABOUT_TXT = """<b>âź MY NAME: {}
âź CREATOR: <a href=https://t.me/Salvin_308>SALVIN</a>
âź LIBRARY: PYROGRAM
âź LANGUAGE: PYTHON 3
âź DATA BASE: MONGO DB
âź BOT SERVER: HEROKU
âź BOT SUPPORT CHAT:</b> <a href=https://t.me/SS_ADMIN_308_bot>SS Admin Chat Bot</a></b>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>
âșâș <b>Donation</b>
âȘŒ <b>You Can Donate Any Amount You Have đł. 
<b>âââââââââá Payment Methods áâââââââââ
âź GooglePay
âź Paytm
âź Phonepe
_Contact Me For Know About The Payment Info_
ââââââââââââá <a href=https://t.me/SS_ADMIN_308_bot><b>SALVIN</b></a> áââââââââââââ
âșâș <b>Paid Promotion</b>
âȘŒ <b>Contact Me With You Content Which You Want To Promote . 
<b>âââââââââá Payment Methods áâââââââââ
âź GooglePay
âź Paytm
âź Phonepe
_Contact Me With You Content AND KNOW ABOUT THE PAYMENT INFO_
ââââââââââââá <a href=https://t.me/SS_ADMIN_308_bot><b>SALVIN</b></a> áââââââââââââ"""
    PROMOTION_TXT = """<b>ă Paid Promotion ă</b>
âȘŒ <b>Contact Me With You Content Which You Want To Promote . 
<b>âââââââââá Payment Methods áâââââââââ
âź GooglePay
âź Paytm
âź Phonepe
_Contact Me With You Content Which You Want To Promote_
ââââââââââââá <a href=https://t.me/SS_ADMIN_308_bot><b>SALVIN</b></a> áââââââââââââ""" 
    FILE_TXT = """â€ HELP: FILE STORE MODULE../
<b>BY USING THIS MODULE YOU CAN STORE FILES IN MY DATABASE AND I WILL GIVE YOU A PERMANENT LINK TO ACCESS THE SAVED FILES. IF YOU WANT TO ADD FILES FROM A PUBLIC CHANNEL SEND THE FILW LINK ONLY OR YOU WANT TO ADD FILES FROM A PRIVATE CHANNEL YOU MUST MAKE ME ADMIN ON THE CHANNEL TO ACCESS FILES...//</b>
âȘŒ Commands and Usage âș
âȘ /plink âșâș <b>REPLY TO ANY MEDIA TO GET LINK.</b>
âȘ /pbatch âșâș <b>USE YOUR MEDIA LINK WITH THIS COMMAND.</b>
âȘ /batch âșâș <b>TO CREATE LINK FOR MULTIPLE FILES.</b>
âȘŒ Example âș
<code>/batch https://t.me/SS_OTT_Channel/5 https://t.me/SS_OTT_Channel/8</code>
đČđđŽđłđžđđ âșâș <a href=https://t.me/movie_club_308><b>SS MOVIE CLUB</b></a>"""
    WHOIS_TXT ="""<b>WHO IS MODULE</b>
Note:- Give a user details
âą/whois :-give a user full details"""
    FUN_TXT ="""<b>GáŽáŽáŽs</b> 
    
<b>âĄ JUST SOME KIND OF FUN THING'S âĄ</b>
 
đŁ. /dice - ROLE THE DICE
đ€. /Throw đđ /Dart - TO MAKE DART 
3. /Runs - SOME RAMDOM DIALOGUES
4. /Goal or /Shoot - TO MAKE A GOAL OR SHOOT
5. /luck or /cownd - SPIN AND TRY YOUR LUCK"""

    MANUELFILTER_TXT = """Help: <b>Filters</b>
- Filter is the feature were users can set automated replies for a particular keyword and SANTO  will respond whenever a keyword is found the message
<b>NOTE:</b>
1. SANTO should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.
<b>Commands and Usage:</b>
âą /filter - <code>add a filter in chat</code>
âą /filters - <code>list all the filters of a chat</code>
âą /del - <code>delete a specific filter in chat</code>
âą /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    SONG_TXT = """<b>đđŸđœđ¶ đłđŸđđœđ»đŸđ°đł đŒđŸđłđđ»đŽ</b>
<b>SONGE DOWNLOAD MODULE, FOR THOSE WHO LOVE MUSIC. YOU CAN USE THIS FEATUE FOR DOWNLOAD ANY SONG WITH SUPER FAST SPEED./</b>
<b>đČđŸđŒđŒđ°đœđłđ</b>
âșâș  /song SONG NAME
WORK ONLY ON GROUP
CREDITS:- <a href=https://t.me/SS_Movie_Club</a>"""
    PIN_TXT ="""<b>PIN MODULE</b>
<b>PIN A MESSAGE../</b>
<b>ALL THE PIN RELATED COMMANDS CAN BE FOUND HERE::</b>
<b>đ COMMANDS AND USAGE đ</b>
â /pin :- TO PIN THE MESSAGE ON YOUR CHATS
â /unpin :- TO UNPIN THE CURREENT PINNED MESSAGE"""
    PASTE_TXT = """Help: <b>Paste</b>
Paste some texts or documents on a website!
<b>Commands and Usage:</b>
âą /paste [text] - paste the given text on Pasty
<b>NOTE:</b>
âą These commands works on both pm and group.
âą These commands can be used by any group member."""
    TTS_TXT = """Help: <b> TTS đ€ module:</b>
Translate text to speech
<b>Commands and Usage:</b>
âą /tts <text> : convert text to speech
<b>NOTE:</b>
âą IMDb should have admin privillage.
âą These commands works on both pm and group.
âą IMDb can translate texts to 200+ languages."""
    PINGS_TXT ="""<b>đ Ping:</b>
Helps you to know your ping đ¶đŒââïž
<b>Commands:</b>
âą /alive - To check you are alive.
âą /help - To get help.
âą /ping - To get your ping.
âą /bot_info - Bot Link.
<b>đčUsageđč :</b>
âą This commands can be used in pms and groups
âą This commands can be used buy everyone in the groups and bots pm
âą Share us for more features"""
    TELE_TXT = """<b>â«ïžHELP: TelegraphâȘïž</b>
Do as you wish with telegra.ph module!
</b>USAGE:</b>
đ€§ /telegraph - Send me Picture or Vide Under (5MB)
<b>NOTE:</b>
âą This Command Is Available in goups and pms
âą This Command Can be used by everyone"""

    PRIVATEBOT_TXT = """<b>Hello, I am Restarted. Now you can Search movies With Me</b>"""

    JSON_TXT ="""<b>JSON:</b>
Bot returns json for all replied messages with /json
<b>Features:</b>
Message Editting JSON
Pm Support
Group Support
<b>Note:</b>
Everyone can use this command , if spaming happens bot will automatically ban you from the group."""
    PURGE_TXT = """<b>Purge</b>
    
Delete A Lot Of Messages From Groups! 
    
 <b>ADMIN</b> 
â /purge :- Delete All Messages From The Replied To Message, To The Current Message"""
    BUTTON_TXT = """Help: <b>Buttons</b>
-Bot  Supports both url and alert inline buttons.
<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. SPIDY supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format
<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/movie_club)</code>
<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """<b>AUTO FILTER ON/OFF MODULE..</b>
<b>AUTO FILTER IS THE FEATURE TO FILTER AND SAVE THE FILES AUTOMATICALLY FROM CHANNEL TO GROUP. YOU CAN USE THE FOLLOWING COMMANDS TO ON AND OFF THE AUTOFILTER IN YOUR GROUP.../</b>
<b>đČđŸđŒđŒđ°đœđłđ :-
<b>âșâș /autofilter on - ENABLE AUTO FILTER IN THE GROUPS.</b>
<b>âșâș /autofilter off - DISABLED AUTO FILTER IN THE GROUPS.</b>
<b>âșâș /set_template - SET CUSTOM IMDB TEMPLETE FOR AUTO FILTER.</b>
<b>âșâș /get_template - GET CURRENT IMDB TEMPLETE OF AUTO FILTER.</b>
<b>đČđđŽđłđžđđ :- <a href=https://t.me/movie_club_308</a></b>"""
    CONNECTION_TXT = """Help: <b>Connections</b>
- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.
<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM
<b>Commands and Usage:</b>
âą /connect  - <code>connect a particular chat to your PM</code>
âą /disconnect  - <code>disconnect from a chat</code>
âą /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>
<b>NOTE:</b>
these are the extra features of AUTOFILTERBOT 
<b>Commands and Usage:</b>
âą /id - <code>get id of a specifed user.</code>
âą /info  - <code>get information about a user.</code>
âą /imdb  - <code>get the film information from IMDb source.</code>
âą /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>
<b>NOTE:</b>
This module only works for my admins
<b>Commands and Usage:</b>
âą /logs - <code>to get the rescent errors</code>
âą /stats - <code>to get status of files in db.</code>
âą /delete - <code>to delete a specific file from db.</code>
âą /users - <code>to get list of my users and ids.</code>
âą /chats - <code>to get list of the my chats and ids </code>
âą /leave  - <code>to leave from a chat.</code>
âą /disable  -  <code>do disable a chat.</code>
âą /ban_user  - <code>to ban a user.</code>
âą /unban_user  - <code>to unban a user.</code>
âą /channel - <code>to get list of total connected channels</code>
âą /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """<b>áâș TOTAL FILES: <code>{}</code></b>
<b>áâș TOTAL USERS: <code>{}</code></b>
<b>áâș TOTAL CHATS: <code>{}</code></b>
<b>áâș USED STORAGE: <code>{}</code></b>
<b>áâș FREE STORAGE: <code>{}</code></b>"""
    LOG_TEXT_G = """#New_Group
    
<b>áâș GROUP âȘŒ {}(<code>{}</code>)</b>
<b>áâș TOTAL MEMBERS âȘŒ <code>{}</code></b>
<b>áâș ADDED BY âȘŒ {}</b>
"""
    LOG_TEXT_P = """#New_User
    
<b>áâș ID - <code>{}</code></b>
<b>áâș NAME - {}</b>
"""
    REPORT_TXT = """â€ HELP: <code>Report Sended To My Admin</code> â ïž
đđđđ đđđđđđđ đđđđđ đąđđ đđ đđđđđđ đ đđđđđđđ đđ đ đđđđ đđ đđđ đđđđđđ đđ đđđ đđđđđđđđđđ đđđđđ. đłđđ'đ đđđđđđ đđđđ đđđđđđđ.
â€ Commands and Usage:
âȘ/report đđ @admins - đłđ đđŸđđđđ đș đđđŸđ đđ đđđŸ đșđœđđđđ (đđŸđđđ đđ đș đđŸđđđșđđŸ)."""

    share_text_TXT = """â€ đđđ„đ©: This Command Help you to Share Text. As Link
â€ Commands and Usage:
âȘ /share - đđđŸ đđđđ đŒđđđđșđđœ đđđđ đđđđ Text You Want to Share
âđ€đđșđđđđŸ:
<code>/share Hello Bro Sugmano</code>"""

    URLSHORT_TXT = """â€ đđđ„đ©: đŽđđ đđđđđđđŸđ
đđđđ đđđđđđđ đđđđđ đąđđ đđ đđđđđ đ đđđ 
â€ Commands and Usage:
âȘ /short: đđđŸ đđđđ đŒđđđđșđđœ đđđđ đđđđ đđđđ đđ đđŸđ đđđđđđŸđœ đđđđđ
âđ€đđșđđđđŸ:
<code>/short https://youtu.be/kB9TkCs8cX0</code>"""

    VIDEO_TXT ="""HELP TO DOWNLOAD VIDEOS FROM YOUTUBE.
âą đđŽđąđšđŠ
đ đ°đ¶ đđąđŻ đđ°đžđŻđ­đ°đąđ„ đđŻđș đđȘđ„đŠđ° đđłđ°đź đ đ°đ¶đ”đ¶đŁđŠ
How to Use
âą đđșđ±đŠ /video or /mp4 đđŻđ„ (https://youtu.be/kB9TkCs8cX0)
âą đđčđąđźđ±đ­đŠ:
<code>/mp4 https://youtu.be/kB9TkCs8cX0</code>
<code>/video https://youtu.be/kB9TkCs8cX0</code>"""

    ZOMBIES_TXT = """HELP YOU TO KICK USERS
<b>Kick incative members from group. Add me as admin with ban users permission in group.</b>
<b>Commands and Usage:</b>
âą /inkick - command with required arguments and i will kick members from group.
âą /instatus - to check current status of chat member from group.
âą /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
âą /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.
âą /dkick - to kick deleted accounts."""

    IMAGE_TXT = """â€ Help: IáŽáŽÉąáŽ
đđđđ đđđđđđđ đđđđđ đąđđ đđ đđđđ đđđđđ đđđđą đđđđđđą 
â€ Commands and Usage:
âȘ đ©đđđ đđŸđđœ đđŸ đș đđđșđđŸ đđ đŸđœđđ âš
đŹđșđœđŸ đ»đ <a href=https://t.me/SS_ADMIN_308_bot>SALVIN</a>"""

    STICKER_TXT = """YOU CAN USE THIS MODULE TO FIND ANY STICKER.
âą USAGE
To Get Sticker ID
 
  â­ How to use
 
â Reply To Any Sticker [/stickerid]"""

    YTTHUMB_TXT = """HELPS TO DOWNLOAD ANY YOUTUBE VIDEO THUMBNAIL
    
â­ How to use
đđșđ±đŠ /ytthumb đđŻđ„ đđȘđ„đŠđ° đđȘđŻđŹ
âą đđčđąđźđ±đ­đŠ
<code>/ytthumb https://youtu.be/UyzJ9KEoU0w</code>"""

    ABOOK_TXT = """â€ Help: đ đđœđđđ»đđđ
đđđ đđđ đđđđđđđ đ đżđłđ” đđđđ đđ đ đđđđđ đđđđ đ đđđ đđđđ đđđđđđđ âŻ
â€ Commands and Usage:
âȘ /audiobook: đ±đŸđđđ đđđđ đŒđđđđșđđœ đđ đșđđ đŻđŁđ„ đđ đđŸđđŸđđșđđŸ đđđŸ đșđđœđđ"""

    GTRANS_TXT = """â€ Help: đŠđđđđđŸ đłđđșđđđđșđđŸđ
đđđđ đđđđđđđ đđđđđ đąđđ đđ đđđđđđđđđ đ đđđĄđ đđ đșđđ đđđđđđđđđ đąđđ đ đđđ. đđđđ đđđđđđđ đ đđđđ đđ đđđđ đđ đđđ đđđđđ âŻ
â€ Commands and Usage:
âȘ/tr - đłđ đđđșđđđđșđđŸđ đđŸđđđ đđ đș đđđŸđŒđđżđŒ đđșđđđđșđđŸ
â€ đ­đđđŸ:
đ¶đđđđŸ đđđđđ /tr đđđ đđđđđđœ đđđŸđŒđđżđ đđđŸ đđșđđđđșđđŸ đŒđđœđŸ
âđ€đđșđđđđŸ: /đđ đđ
âą đŸđ = đ€đđđđđđ
âą đđ = đŹđșđđșđđșđđșđ
âą đđ = đ§đđđœđ"""

    RESTRIC_TXT = """â€ Help: MáŽáŽáŽ đ«
đđđđđ đđđ đđđ đđđđđđđđ đ đđđđđ đđđđđ đđđ đđđ đđ đđđđđđ đđđđđ đđđđđ đđđđ đđđđđđđđđđđą.
âȘ/ban: đłđ đ»đșđ đș đđđŸđ đżđđđ đđđŸ đđđđđ.
âȘ/unban: đłđ đđđ»đșđ đș đđđŸđ đđ đđđŸ đđđđđ.
âȘ/tban: đłđ đđŸđđđđđșđđđđ đ»đșđ đș đđđŸđ.
âȘ/mute: đłđ đđđđŸ đș đđđŸđ đđ đđđŸ đđđđđ.
âȘ/unmute: đłđ đđđđđđŸ đș đđđŸđ đđ đđđŸ đđđđđ.
âȘ/tmute: đłđ đđŸđđđđđșđđđđ đđđđŸ đș đđđŸđ.
â€ đ­đđđŸ:
đ¶đđđđŸ đđđđđ /tmute đđ /tban đđđ đđđđđđœ đđđŸđŒđđżđ đđđŸ đđđđŸ đđđđđ.
âđ€đđșđđđđŸ: /đđ»đșđ 2đœ đđ /đđđđđŸ 2đœ.
đžđđ đŒđșđ đđđŸ đđșđđđŸđ: đ/đ/đœ. 
 âą đ = đđđđđđŸđ
 âą đ = đđđđđ
 âą đœ = đœđșđđ"""
    CREATOR_REQUIRED = """â<b>You have To Be The Group Creator To Do That.</b>"""
      
    INPUT_REQUIRED = "â **Arguments Required**"
      
    KICKED = """âïž Successfully Kicked {} Members According To The Arguments Provided."""
      
    START_KICK = """đź Removing Inactive Members This May Take A While..."""
      
    ADMIN_REQUIRED = """â<b>I Want to be an admin in this group bye.. Add Me Again with all admin rights.</b>"""
      
    DKICK = """âïž Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """<b>Copying files from that Channel. Please Wait...</b>"""
      
    STATUS = """{}\n<b>Chat Member Status</b>**\n\n```<i>Recently``` - {}\n```Within Week``` - {}\n```Within Month``` - {}\n```Long Time Ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}</i>
"""
