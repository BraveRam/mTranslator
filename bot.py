import googletrans, requests
from googletrans import LANGCODES, Translator
import telebot 
from telebot import custom_filters
from telebot.types import *
import pymongo
from pymongo import MongoClient
from mtranslate import translate
from gtts import gTTS
import time

client = MongoClient("mongodb+srv://really651:gSPMW6u9WuStXIwD@cluster0.pxc2foz.mongodb.net/?retryWrites=true&w=majority")

db = client["Newdb"]
collection = db["Mycollection"]

bot = telebot.TeleBot("5801051594:AAFs_wJHPH91qzgGVratn4lTjIAWPa-DsOo")

keyboard = InlineKeyboardMarkup()
t = InlineKeyboardButton(text ="☑️Subscribe To The Channel", url="https://t.me/oro_tech_tipz")
t1 = InlineKeyboardButton(text ="🔄Inline Here", switch_inline_query_current_chat="How are you?")
t2 = InlineKeyboardButton(text ="🔂Inline Another Chat", switch_inline_query="How are you?")
keyboard.add(t1)
keyboard.add(t2)
keyboard.add(t)

def translate_photo(message):
    b = bot.reply_to(message,"<i>Maaloo xiqqoo eegaa....:-)</i>", parse_mode="html")
    file_info = bot.get_file(message.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)    
    api_key = 'K81164834388957'
    url = 'https://api.ocr.space/parse/image'
    payload = {
        'apikey': api_key,
        'language': 'eng',
        'isOverlayRequired': False
    }
    files = {
        'filename': ('image.jpg', downloaded_file, 'image/jpeg')
    }
    response = requests.post(url, data=payload, files=files)
    if response.status_code == 200:
        response_data = response.json()
        if response_data['IsErroredOnProcessing']:
            error_message = response_data['ErrorMessage']
            bot.send_message(message.chat.id, 'Error: An error occured - please try again.')
        else:
            extracted_text = response_data['ParsedResults'][0]['ParsedText']
            bot.delete_message(message.chat.id, b.id)
            a = collection.find({"user_id": message.chat.id})
            for i in a:
              langs = i["lang"]
              text = extracted_text
              translated_text = translate(text, langs)
              bot.reply_to(message, translated_text)
    else:
        bot.send_message(message.chat.id, 'Error: An error occured - please try again.')


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
		r8 = InlineQueryResultArticle("99", "Barreeffama barressaa....", InputTextMessageContent("Barreeffama barbaaddan inline mode irratti barreessitanii gara afaan birootti jijjiiruu dandeessu▼"), description ="Maaloo barreeffama afaan barbaaddanii barreessaa...", thumbnail_url="https://t.me/Oro_tech_tipz/336")
		bot.answer_inline_query(message.id, [r8])
		return
	else:
		try:
			t = translate(message.query, "om")
			r1 = InlineQueryResultArticle("1", "🇪🇹Afaan Oromoo", InputTextMessageContent(t), description = t,  thumbnail_url="https://t.me/Oro_tech_tipz/336")
			t = translate(message.query, "en")
			r2 = InlineQueryResultArticle("2", "🇬🇧English",InputTextMessageContent(t), description = t,  thumbnail_url="https://t.me/Oro_tech_tipz/336")
			t = translate(message.query, "am")
			r3 = InlineQueryResultArticle("3", "🇪🇹Amharic", InputTextMessageContent(t), description = t,  thumbnail_url="https://t.me/Oro_tech_tipz/336")
			t = translate(message.query, "hi")
			r4 = InlineQueryResultArticle("4", "🇮🇳Hindi", InputTextMessageContent(t), description = t,  thumbnail_url="https://t.me/Oro_tech_tipz/336")			
			bot.answer_inline_query(message.id, [r1, r2, r3, r4])
		except:
			pass

def keyboards():
    btn = []
    keyboard = ReplyKeyboardMarkup(row_width=2)
    keyboard.add("Oromic:om")
    langs = [lang for lang in LANGCODES]
    for i in range(150):
        try:
            btn.append(KeyboardButton(text=langs[i].title()+":"+LANGCODES[langs[i]]))
        except:
            break
    keyboard.add(*btn)
    keyboard.add("Return To Home")
    return keyboard 

@bot.message_handler(commands=["set"], chat_types=["private"])
def set(message):
	bot.set_state(message.from_user.id, "choose", message.chat.id)
	return bot.send_message(message.chat.id, "💡Maaloo Afaan Keessan Filadhaa💾", reply_markup = keyboards())
	
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

🌍Sirreeffama Afaanii jijjiiruuf /set jedhu cuqaasaa👏

🕹Barreeffama gara sagaleetti jijjiiruuf /tts kan jedhu cuqaasaa💡

🔑Kanaafuu isinis link Bootii kana Namoota biroof akka ergitaniif isin gaafanna🙏

🥰Yeroo Gaarii isiniif haa ta\'u🥰
"""

@bot.message_handler(commands = ["about"])
def maker(message):
	bot.send_message(message.chat.id, help, reply_markup = keyboard)

channels = ["@oro_tech_tipz"]

def check(message):
	for i in channels:
		sub = bot.get_chat_member(i, message.from_user.id)
		if sub.status == "left":
			return False 
	return True 

@bot.message_handler(commands =["feedback"])
def feedback(message):
	if len(message.text.split(" "))  == 1:
		bot.send_message(message.chat.id, "💡Yaada kennuuf fakkeenya kanaan kenni👇\n<code>/feedback bot kana jaalladheen jira😍</code>", parse_mode ="html")
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
		time.sleep(0.5)
		a = i["user_id"]
		try:
			if message.content_type =="photo":
				fileID = message.photo[-1].file_id
				file_info = bot.get_file(fileID)
				downloaded_file = bot.download_file(file_info.file_path)
				if message.caption:
					bot.send_photo(a, downloaded_file, caption =message.caption)
					success+=1					
		except Exception as e:
			print(e)
			pass
	
@bot.message_handler(commands =["sent"])
def check_sent(message):
	bot.send_message(message.chat.id, f"😄Sent to {success} users")

@bot.message_handler(func=lambda message: True, state="choose")
def handle_choose(message):
    if message.text == "Return To Home":
        bot.delete_state(message.from_user.id, message.chat.id)
        bot.send_message(message.chat.id, "📎Share & Support Us✨", reply_markup = ReplyKeyboardRemove())
        return bot.send_message(message.chat.id, f"✋{message.from_user.first_name} Baga Nagaan Dhuftan. Ani Bootii Afaan barbaaddan gara Afaan feetaniitti isiniif jijjiiruudha. <b>Afaan Oromoo</b> dabalatee jechuudha.\nSirreefama Afaanii jijjiiruuf /set kan jedhu cuqaasaa! Amma barreeffama barbaaddan anatti ergaa🔍", parse_mode ="html", reply_markup = keyboard)
    else:
        try:
            langs = message.text.split(":")[0]
            lang = message.text.split(":")[1]
            if lang == "om":
            	collection.update_one({"user_id": message.chat.id}, {"$set": {"lang": "om"}})
            	bot.delete_state(message.from_user.id, message.chat.id)
            	return bot.send_message(message.chat.id, "🔄Sirreeffamni Afaan keessanii gara Afaan Oromoo tti jijjiirameera!", reply_markup=ReplyKeyboardRemove())
            else:
            	pass
            for i in LANGCODES:              
                if lang == LANGCODES[i]:
                    collection.update_one({"user_id": message.chat.id}, {"$set": {"lang": lang}})
                    bot.delete_state(message.from_user.id, message.chat.id)
                    return bot.send_message(message.chat.id, "🔄Sirreeffamni Afaan keessanii gara Afaan {} tti jijjiirameera!".format(langs), reply_markup=ReplyKeyboardRemove())
            return bot.send_message(message.chat.id, "💡Maaloo Afaan Keessan Filadhaa💾", reply_markup=keyboards())
        except Exception as e:
            #bot.send_message(message.chat.id, e)
            return bot.send_message(message.chat.id, "💡Maaloo Afaan Keessan Filadhaa💾", reply_markup=keyboards())

@bot.message_handler(content_types=["photo"])
def str1_photo(message):
	sub = check(message)
	if sub == True:
	  bot.send_chat_action(message.chat.id, "typing")
	  translate_photo(message)
	else:
	  key = InlineKeyboardMarkup()
	  k1 = InlineKeyboardButton(text ="♻️Join Channel♻️", url="t.me/oro_tech_tipz")
	  key.add(k1)
	  bot.send_message(message.chat.id, f"⚠️{message.chat.first_name} Bot Kana Fayyadamuun dura Channel keenya Join gochuu qabdu!\n👌San booda fayyadamuu dandeessu", reply_markup = key)
				
@bot.message_handler(func = lambda message: True)
def str1(message):
	sub = check(message)
	a = collection.find({"user_id": message.chat.id})
	for i in a:
	   langs = i["lang"]
	   text = message.text
	   translated_text = translate(text, langs)
	   if sub == True:
	   	bot.send_chat_action(message.chat.id, "typing")
	   	bot.reply_to(message, "<b>{}</b>".format(translated_text), parse_mode ="html")
	   else:
	   	key = InlineKeyboardMarkup()
	   	k1 = InlineKeyboardButton(text ="♻️Join Channel♻️", url="t.me/oro_tech_tipz")
	   	key.add(k1)
	   	bot.send_message(message.chat.id, f"⚠️{message.chat.first_name} Bot Kana Fayyadamuun dura Channel keenya Join gochuu qabdu!\n👌San booda fayyadamuu dandeessu", reply_markup = key)
				
bot.add_custom_filter(custom_filters.StateFilter(bot))
print("Successfully Started")
bot.infinity_polling()
			
