# -*-encode:utf-8-*-

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

#import logging

#logging.basicConfig(
    #filename='log.txt',
    #level=logging.DEBUG,
    #format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

mainAdmin = 820586182
#<////Admin Load\\\\\>
Admintxt = open("admins.txt", "r")
AdminRead = Admintxt.read()
Adminsstr = AdminRead.split(",")
Admins = []
for adminn in Adminsstr:
    try:
        Admins.append(int(adminn))
    except:
        pass
Admintxt.close()
#<\\\\\\Admin Load/////>
#<//////Banlist Load\\\\\>
banltxt = open("banlist.txt", "r")
banlRead = banltxt.read()
banstr = banlRead.split(",")
banlist = []
for ban in banstr:
    try:
        banlist.append(int(ban))
    except:
        pass
banltxt.close()
#<\\\\\Banlist Load//////>
Users = []

Utxt = open("Users.txt")
URead = Utxt.readlines()
for i in URead:
    i1 = i.strip()
    i2 = i1.split(",")
    if "" in i2:
        i2.remove("")
    Users.append(i2)
Utxt.close()

foshs = ["کص", "کون", "کسکش", "جنده", "حروم", "حرام", "کیر", "کثکش", "شسبیصرثقشرص", "سیبشسرشرسشز",]
updater = Updater("1271177685:AAGbrlfKnwiQ_w8XTS5CGXe1dG1RHNWpAE4", use_context=True)
dp = updater.dispatcher
##################################################################################################
ueximode = False

def start(update, context):
    global ueximode
    for a in range(0, len(Users)):
        if int(Users[a][3]) == update.message.chat.id:
            ueximode = True
            break
        else:
            ueximode = False
    if ueximode == False:
        for i in range(0, len(Users)+1):
            try:
                x = Users[i][0]
                pass
            except:
                Users.append([str(i+1), update.message.from_user.first_name, update.message.from_user.username, update.message.chat.id])
        Utxt = open("Users.txt", "w")
        writetxt = ""
        for i in Users:
            for b in i:
                writetxt += str(b) + ","
            writetxt += "\n"
        Utxt.write(writetxt)
        Utxt.close()
    if update.message.chat.id in banlist:
        update.message.reply_text("شما از ربات بن شده اید.")
    elif (update.message.chat in Admins) or update.message.chat.id == mainAdmin:
        pass
    else:
        update.message.reply_text("سلام خیلی خوش اومدین😄🌹\nلطفا پیامتون رو بفرستید تا بدست ادمین ها برسونم.")
        context.bot.forward_message(mainAdmin, update.message.chat.id, update.message.message_id)
        context.bot.send_message(mainAdmin, text=f"new user~> {update.message.from_user.username}\nchatid~> {update.message.chat.id}")
        try:
            for admin in Admins:
                context.bot.forward_message(admin, update.message.chat.id, update.message.message_id)
                context.bot.send_message(admin, text=f"new user~> {update.message.from_user.username}\nchatid~> {update.message.chat.id}")
        except:
            pass

def help(update, context):
    if (update.message.chat.id in Admins) or update.message.chat.id == mainAdmin:
        update.message.reply_text("/start - Start Bot\n/ping - Check Bot\n/addadmin ChatId - Add Admin\n/remadmin ChatId - Remove Admin\n/ban ChatId - Ban Users\n/unban ChatId - Unban Users\n/Users - Show UserList\n/help - Get Help", quote=True)
    elif update.message.chat.id in banlist:
        update.message.reply_text("شما از ربات بن شده اید.", quote=True)
    else:
        update.message.reply_text("سلام خیلی خوش اومدین😄🌹\nلطفا پیامتون رو بفرستید تا بدست ادمین ها برسونم.", quote=True)

def ping(update, context):
    update.message.reply_text("Bot is Online", quote=True)

def sendUsers(update, context):
    userShow = ""
    for user in Users:
        userShow += f"👇🏻User {user[0]}👇🏻\n Name: {user[1]}\n UserName: @{user[2]}\n Number Id: {user[3]}\n---------------------------\n"

    update.message.reply_text(text=userShow, quote=True)
##########################################################################
#</////////////////////Admin defs\\\\\\\\\\\\\\\\\>
def admin(update, context):#*********def Check Admins
    if update.message.chat.id in Admins:
        update.message.reply_text("شما ادمین هستید :)", quote=True)
    else:
        update.message.reply_text("شما ادمین نیستید :,(", quote=True)

def addAdmin(update, context):#*******def add admin
    if(update.message.chat.id == mainAdmin):
        newAdmin = context.args[0]
        writetxt = ""
        Admins.append(int(newAdmin))
        addadminn = open("admins.txt", "w")
        for i in Admins:
            writetxt+=(str(i) + ",")
        addadminn.write(writetxt)
        addadminn.close()
        update.message.reply_text(f"new admin: {newAdmin}", quote=True)
        context.bot.send_message(newAdmin, "شما به لیست ادمین ها اضافه شدید.")
    else:
        update.message.reply_text("شما ادمین اصلی نیستید.")

def remAdmin(update, context):#*******def remove admin
    if (update.message.chat.id == mainAdmin):
        RemAdmin = context.args[0]
        writetxt = ""
        Admins.remove(int(RemAdmin))
        addadminn = open("admins.txt", "w")
        for i in Admins:
            writetxt += (str(i) + ",")
        addadminn.write(writetxt)
        addadminn.close()
        update.message.reply_text(f"Admin Removed: {RemAdmin}", quote=True)
    else:
        update.message.reply_text("شما ادمین اصلی نیستید.")

def addban(update, context):
    #replied_to_text = update._effective_message.reply_to_message.text  # payam daryaft shode az reply
    #if replied_to_text != None:
        #banid = replied_to_text.split("= ")[-1]
        #banlist.append(int(banid))
        #file = open("banlist.txt", "w")
        #file.write(str(banid) + ",")
        #file.close()
        #update.message.reply_text(f"کاربر {banid}از ربات بن شد ")
    #else:
    if (update.message.chat.id in Admins) or (update.message.chat.id == mainAdmin):
        banid = context.args[0]
        banlist.append(int(banid))
        file = open("banlist.txt", "w")
        file.write(str(banid) + ",")
        file.close()
        update.message.reply_text(f"کاربر {banid}از ربات بن شد ", quote=True)

def unban(update, context):
    writetxt = ""
    unbanid = context.args[0]
    banlist.remove(int(unbanid))
    for i in banlist:
        writetxt += str(i) + ","
    file = open("banlist.txt", "w")
    file.write(writetxt)
    file.close()
    update.message.reply_text(f"کاربر{unbanid} از لیست بن درآمد. ", quote=True)
#<\\\\\\\\\\\\\\\\\\\\\\\\\\\\Admin defs/////////////////////////////////>

#<////////////////////////////Messages defs\\\\\\\\\\\\\\\\\\\\\\\\\\\\>
def getMessage(update, context):#*******************Get Message from User
    text = f'{update.message.text}\n \nusername~> @{update.message.chat.username}\n chat_id = {update.message.chat.id}\n برای ارسال جواب این پیام را ریپلای کنید.'
    for fosh in foshs:
        if fosh in update.message.text:
            foshMode = True
            break
        else:
            foshMode = False
    if update.message.chat.id in banlist:
        banMode = True
    else:
        banMode = False
    if banMode == True:
        update.message.reply_text("شما از ربات بن شده اید.", quote=True)
    elif foshMode == True:
        update.message.reply_text("پیام شما حاوی کلمات نامناسب است.", quote=True)
        context.bot.forward_message(mainAdmin, update.message.chat.id, update.message.message_id)
        context.bot.send_message(mainAdmin, text)
    else:
        for admin in Admins:
            context.bot.forward_message(admin, update.message.chat.id, update.message.message_id)
            context.bot.send_message(admin, text)
        update.message.reply_text("پیام شما ارسال شد.", quote=True)

def sendAnswer(update, context):#******************Send Answer to User
    if update.message.text != "/ban":
        replied_to_text = update._effective_message.reply_to_message.text #payam daryaft shode az reply
        print(update._effective_message.reply_to_message)
        replied_to_text2 = replied_to_text.split("= ")[-1]
        context.bot.send_message(replied_to_text2, update.message.text)
        update.message.reply_text("پیام به کاربر ارسال شد.", quote=True)
#<\\\\\\\\\\\\\\\\\\\\\\\\\\Messages defs/////////////>
def sdoc(update, context):
    if update.message.chat.id in Admins:
        doc = open("Users.txt","rb")
        context.bot.send_document(update.message.chat.id, doc)
        doc.close()
#<//////////////////////////Handlers\\\\\\\\\\\\\\\\>
dp.add_handler(CommandHandler("start", start))#*****start Command
dp.add_handler(CommandHandler("ping", ping))#*****Check Bot
dp.add_handler(CommandHandler("admin", admin))#*****Check Admins Command
dp.add_handler(CommandHandler("help", help))#****get help
dp.add_handler(MessageHandler(Filters.text & ~Filters.user(Admins), getMessage))#*****Get message MessageHandler
dp.add_handler(MessageHandler(Filters.text & Filters.user(Admins) & Filters.reply, sendAnswer))#*****Send Answer MessageHandler
dp.add_handler(CommandHandler("addadmin", addAdmin))#******add admin
dp.add_handler(CommandHandler("remadmin", remAdmin))#****remove admin
dp.add_handler(CommandHandler("ban", addban))#*****add ban
dp.add_handler(CommandHandler("unban", unban))#****unban
dp.add_handler(CommandHandler("Users", sendUsers))
dp.add_handler(CommandHandler("getusers", sdoc))
#<\\\\\\\\\\\\\\\\\\\\\\\\\\Handlers///////////////>

updater.start_polling()
updater.idle()

#{'message_id': 1338, 'date': 1594652277, 'chat': {'id': 820586182, 'type': 'private', 'username': 'DeadBot811', 'first_name': '\u206a\u206c\u206e\u206e\u206e\u206e', 'last_name': '\u206a\u206c\u206e\u206e\u206e\u206e'}, 'forward_from': {'id': 991650296, 'first_name': 'Alikoli', 'is_bot': False, 'language_code': 'en'}, 'forward_date': 1594652276, 'text': '/pong', 'entities': [{'type': 'bot_command', 'offset': 0, 'length': 5}], 'caption_entities': [], 'photo': [], 'new_chat_members': [], 'new_chat_photo': [], 'delete_chat_photo': False, 'group_chat_created': False, 'supergroup_chat_created': False, 'channel_chat_created': False, 'from': {'id': 1132634913, 'first_name': 'Clash ac', 'is_bot': True, 'username': 'Clashphishbot'}}
