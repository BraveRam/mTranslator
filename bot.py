import googletrans
from googletrans import LANGCODES as lang, Translator
import telebot 
from telebot.types import *
import pymongo
from pymongo import MongoClient
from mtranslate import translate
from gtts import gTTS

client = MongoClient("mongodb+srv://really651:K4vSnRMEsZhqsTqS@cluster0.pxc2foz.mongodb.net/?retryWrites=true&w=majority")

# Select the database and collection
db = client["Newdb"]
collection = db["Mycollection"]

bot = telebot.TeleBot("5801051594:AAHsFpufFnlndKl-HsRht_2FD3AVx7A954g")

def lang1(message):
	langs = [key for key in lang]
	btn = []
	for i in range(12):
		btn.append(InlineKeyboardButton(langs[i].title(), callback_data = lang[langs[i]])) 
	markup = InlineKeyboardMarkup(row_width = 4)
	oro = InlineKeyboardButton(text ="Oromo", callback_data ="om")
	k1 = InlineKeyboardButton(text ="Cebuano", callback_data ="ceb")
	k2 = InlineKeyboardButton(text ="Chichewa", callback_data = "ny")
	k3 = InlineKeyboardButton(text = "Chinese (Simplified)", callback_data ="zh-cn")
	k = InlineKeyboardButton(text ="🔜Next", callback_data ="next1")
	k5 = InlineKeyboardButton(text ="⛔Close", callback_data ="close")
	markup.add(*btn)
	markup.add(oro, k1, k2, k3)
	markup.add(k5, k)
	return markup

def lang2(message):
	langs = [key for key in lang]
	btn = []
	for i in range(15, 30):
		btn.append(InlineKeyboardButton(langs[i].title(), callback_data = lang[langs[i]]))
	markup2 = InlineKeyboardMarkup(row_width = 3)
	k = InlineKeyboardButton(text ="🔙Back", callback_data ="back1")
	k1 = InlineKeyboardButton(text ="🔙Next", callback_data ="next2")		
	markup2.add(*btn)
	markup2.add(k, k1)
	return markup2

def lang3(message):
	langs = [key for key in lang]
	btn = []
	for i in range(30, 45):
		btn.append(InlineKeyboardButton(langs[i].title(), callback_data = lang[langs[i]]))
	markup3 = InlineKeyboardMarkup(row_width = 3)
	k = InlineKeyboardButton(text ="🔙Back", callback_data ="back2")
	k1 = InlineKeyboardButton(text ="🔜Next", callback_data ="next3")		
	markup3.add(*btn)
	markup3.add(k, k1)
	return markup3

def lang4(message):
	langs = [key for key in lang]
	btn = []
	for i in range(45, 60):
		btn.append(InlineKeyboardButton(langs[i].title(), callback_data = lang[langs[i]]))
	markup4 = InlineKeyboardMarkup(row_width = 3)
	k = InlineKeyboardButton(text ="🔙Back", callback_data ="back3")
	k1 = InlineKeyboardButton(text ="🔜Next", callback_data ="next4")		
	markup4.add(*btn)
	markup4.add(k, k1)
	return markup4

def lang5(message):
	langs = [key for key in lang]
	btn = []
	for i in range(60, 75):
		btn.append(InlineKeyboardButton(langs[i].title(), callback_data = lang[langs[i]]))
	markup5 = InlineKeyboardMarkup(row_width = 3)
	k = InlineKeyboardButton(text ="🔙Back", callback_data ="back4")
	k1 = InlineKeyboardButton(text ="🔜Next", callback_data ="next5")		
	markup5.add(*btn)
	markup5.add(k, k1)
	return markup5

def lang6(message):
	langs = [key for key in lang]
	btn = []
	for i in range(75, 90):
		btn.append(InlineKeyboardButton(langs[i].title(), callback_data = lang[langs[i]]))
	markup6 = InlineKeyboardMarkup(row_width = 3)
	k = InlineKeyboardButton(text ="🔙Back", callback_data ="back5")
	k1 = InlineKeyboardButton(text ="🔜Next", callback_data ="next6")		
	markup6.add(*btn)
	markup6.add(k, k1)
	return markup6

def lang7(message):
	langs = [key for key in lang]
	btn = []
	for i in range(90, 106):
		btn.append(InlineKeyboardButton(langs[i].title(), callback_data = lang[langs[i]]))
	markup7 = InlineKeyboardMarkup(row_width = 4)
	k = InlineKeyboardButton(text ="🔙Back", callback_data ="back6")
	markup7.add(*btn)
	markup7.add(k)
	return markup7

keyboard = InlineKeyboardMarkup()
t = InlineKeyboardButton(text ="☑️Subscribe To The Channel", url="https://t.me/oro_tech_tips")
t1 = InlineKeyboardButton(text ="🔔Share The Bot", url="https://t.me/share/url?url=t.me/Oromotranslatorbot")
keyboard.add(t)
keyboard.add(t1)

@bot.message_handler(commands=["start"], chat_types=["private"])
def start(message):
		ids = message.from_user.id
		users= collection.find_one({"user_id": ids})
		if users:
			bot.send_message(message.chat.id, f"✋{message.from_user.first_name} Baga Nagaan Dhuftan. Ani Bootii Afaan barbaaddan gara Afaan feetaniitti isiniif jijjiiruudha. <b>Afaan Oromoo</b> dabalatee jechuudha.\nSirreefama Afaanii jijjiiruuf /set kan jedhu cuqaasaa! Amma barreeffama barbaaddan anatti ergaa🔍", parse_mode = "html", reply_markup = keyboard)
		else:
			collection.insert_one({"user_id": ids, "lang": "om"})
			bot.send_message(message.chat.id, f"✋{message.from_user.first_name} Baga Nagaan Dhuftan. Ani Bootii Afaan barbaaddan gara Afaan feetaniitti isiniif jijjiiruudha. <b>Afaan Oromoo</b> dabalatee jechuudha.\nSirreefama Afaanii jijjiiruuf /set kan jedhu cuqaasaa! Amma barreeffama barbaaddan anatti ergaa🔍", parse_mode ="html", reply_markup = keyboard)

@bot.inline_handler(lambda query: True)
def a(message):
	if len(message.query) ==0:
		r8 = InlineQueryResultArticle("99", "Barreeffama barressaa....", InputTextMessageContent("Barreeffama barbaaddan inline mode irratti barreessitanii gara afaan birootti jijjiiruu dandeessu▼"), description ="Maaloo barreeffama afaan barbaaddanii bareessaa...", thumb_url="https://t.me/Oro_tech_tips/336")
		bot.answer_inline_query(message.id, [r8])
		return
	else:
		try:
			t = translate(message.query, "om")
			r1 = InlineQueryResultArticle("1", "🇪🇹Afaan Oromoo", InputTextMessageContent(t), description = t,  thumb_url="https://t.me/Oro_tech_tips/336")
			t = translate(message.query, "en")
			r2 = InlineQueryResultArticle("2", "🇬🇧English",InputTextMessageContent(t), description = t,  thumb_url="https://t.me/Oro_tech_tips/336")
			t = translate(message.query, "am")
			r3 = InlineQueryResultArticle("3", "🇪🇹Amharic", InputTextMessageContent(t), description = t,  thumb_url="https://t.me/Oro_tech_tips/336")			
			bot.answer_inline_query(message.id, [r1, r2, r3])
		except:
			pass


@bot.message_handler(commands=["set"], chat_types=["private"])
def set(message):
	bot.send_message(message.chat.id, "💡Maaloo Afaan Keessan Filadhaa💾", reply_markup = lang1(message))

@bot.message_handler(commands =["tts"])
def ttss(message):
	bot.reply_to(message, "<b>🎙Barreeffama barbaaddan barreessaatii ergaa😉\n🎧Gara sagaleetti jijjiireen isiniif erga!</b>", parse_mode ="html")
	bot.register_next_step_handler(message, text)

def text(message):
      a= bot.send_message(message.chat.id, "🔄Xiqqoo eegaa...")
      text = message.text
      to_speech = gTTS(text=text)
      to_speech.save('result.mp3')
      with open('result.mp3','rb') as file:
          bot.send_voice(message.chat.id,voice=file, reply_to_message_id = message.message_id, caption ="<b>Generated by @OromoTranslatorBot</b>", parse_mode ="html")
          bot.delete_message(message.chat.id, a.id)
          return

@bot.message_handler(commands = ["stats"])
def sats(message):
	users = list(collection.find())
	count = len(users)
	if message.chat.id == 1365625365:
		bot.send_message(message.chat.id, f"Total Users: {count}")

help ="""
🤖Bootiin kun afaan barbaaddan gara afaan birootti salphaatti kan hiikudha!

🎙Akkasumas barreefama gara sagaleetti jijjiiruu ni danda'a✅

👌Keessattuu bootiin kun Barattootaaf baay'ee tokko barbaachisaadha.

🌍Sirreeffama Afaanii jijjiiruuf /set jedhu cuqaasaa👏

🕹Barreeffama gara sagaleetti jijjiiruuf /tts kan jedhu cuqaasaa💡

🔑Kanaafuu isinis link Bootii kana Namoota biroof akka ergitaniif isin gaafanna🙏

🥰Yeroo Gaarii isiniif haa ta\'u🥰
"""

@bot.message_handler(commands = ["about"])
def maker(message):
	bot.send_message(message.chat.id, help, reply_markup = keyboard)

channels = ["@oro_tech_tips"]

def check(message):
	for i in channels:
		sub = bot.get_chat_member(i, message.from_user.id)
		if sub.status == "left":
			return False 
	return True 

@bot.message_handler(commands =["feedback"])
def feedback(message):
	if len(message.text.split(" "))  == 1:
		bot.send_message(message.chat.id, "💡Yaada kennuuf fakkeenya kanaan kenni👇\n<code>/feedback Bootii baay\'ee bareedaadha.</code>", parse_mode ="html")
		return 
	else:
		a = message.text.split(maxsplit = 1)[1]
		bot.send_message(message.chat.id, "Yaada keessaniif, Galatoomaa!")
		bot.send_message(1365625365, f"📝Yaada Namootaa📝\n\n✏️User Id: {message.from_user.id}\n📑First Name: {message.from_user.first_name}\n🗞Username: @{message.from_user.username}\n🗒Yaada: {a}")

@bot.message_handler(commands =["broadcast"])
def new(message):
	if message.chat.id == 1365625365:
		bot.send_message(message.chat.id, "📥Send me a message to be sent to users!")
		bot.register_next_step_handler(message, photo)

failed = 0
success = 0

def photo(message):
	users = collection.find({})
	for i in users:
		a = i["user_id"]
		try:
			if message.content_type =="photo":
				fileID = message.photo[-1].file_id
				file_info = bot.get_file(fileID)
				downloaded_file = bot.download_file(file_info.file_path)
				if message.caption:
					bot.send_photo(a, downloaded_file, caption =message.caption)
					success+=1							
		except:
			pass
	
@bot.message_handler(commands =["sent"])
def check_sent(message):
	bot.send_message(message.chat.id, f"😄Sent to {success} users")
						
@bot.message_handler(func = lambda message: True)
def str1(message):
	sub = check(message)
	a = collection.find({"user_id": message.chat.id})
	for i in a:
	   langs = i["lang"]
	   text = message.text
	   translated_text = translate(text, langs)
	   if sub == True:
	   	bot.send_message(message.chat.id, f"{translated_text}\n\n<b>@{bot.get_me().username}</b>", parse_mode ="html")
	   else:
	   	key = InlineKeyboardMarkup()
	   	k1 = InlineKeyboardButton(text ="♻️Join Channel♻️", url="t.me/oro_tech_tips")
	   	key.add(k1)
	   	bot.send_message(message.chat.id, f"⚠️{message.chat.first_name} Bot Kana Fayyadamuun dura Channel keenya Join godhuu qabdu!\n👌San booda fayyadamuu dandeessu", reply_markup = key)
    
@bot.callback_query_handler(lambda callback:True)
def callback(callback):
	id = callback.from_user.id
	if callback.data =="next1":
		bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id, reply_markup = lang2(callback))
	elif callback.data =="back1":
		bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id, reply_markup = lang1(callback))
	elif callback.data =="next2":
		bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id, reply_markup = lang3(callback))
	elif callback.data =="next3":
		bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id, reply_markup = lang4(callback))
	elif callback.data =="next4":
		bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id, reply_markup = lang5(callback))
	elif callback.data =="next5":
		bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id, reply_markup = lang6(callback))
	elif callback.data =="next6":
		bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id, reply_markup = lang7(callback))
	elif callback.data =="back6":
		bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id, reply_markup = lang6(callback))
	elif callback.data =="back5":
		bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id, reply_markup = lang5(callback))
	elif callback.data =="back4":
		bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id, reply_markup = lang4(callback))
	elif callback.data =="back3":
		bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id, reply_markup = lang3(callback))
	elif callback.data =="back2":
		bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id, reply_markup = lang2(callback))
	elif callback.data =="close":
		bot.delete_message(callback.message.chat.id, callback.message.message_id)
		bot.send_message(callback.message.chat.id, f"✋{callback.from_user.first_name} Baga Nagaan Dhuftan. Ani Bootii Afaan barbaaddan gara Afaan feetaniitti isiniif jijjiiruudha. <b>Afaan Oromoo</b> dabalatee jechuudha.\nSirreefama Afaanii jijjiiruuf /set kan jedhu cuqaasaa! Amma barreeffama barbaaddan anatti ergaa🔍", parse_mode ="html")
	elif callback.data =="om":
		bot.delete_message(callback.message.chat.id, callback.message.message_id)
		collection.update_one({'user_id': id}, {'$set': {'lang': "om"}})
		bot.send_message(callback.message.chat.id, f"⚙️Sirreeffamni Afaan keessanii gara Afaan <b>Oromoo</b> tti jijjiirameera.", parse_mode = "html")
	else:
		for i in lang.items():
			if callback.data == i[1]:
				collection.update_one({'user_id': id}, {'$set': {'lang': callback.data}})
				bot.delete_message(callback.message.chat.id, callback.message.message_id)
				bot.send_message(callback.message.chat.id, f"⚙️Sirreeffamni Afaan keessanii gara Afaan <b>{i[0].title()}</b> tti jijjiirameera.", parse_mode = "html")
				
				
print("Successfully Started")
bot.infinity_polling()
			
