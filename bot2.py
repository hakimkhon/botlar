from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
import requests
from bs4 import BeautifulSoup

BTN_BOMDOD, BTN_PESHIN, BTN_ASR, BTN_SHOM, BTN_XUFTON, BTN_HUDUD = ( '🌒 Bomdod', '🌗 Peshin', '🌖 Asr', '🌘 Shom', '🌑 Xufton', '♻️ Hududni almashtirish') 

btn_vaqtlar = ReplyKeyboardMarkup([
    [
        BTN_BOMDOD, BTN_PESHIN, BTN_ASR
    ],
    [
        BTN_SHOM, BTN_XUFTON, BTN_HUDUD
    ]
], resize_keyboard=True)

STETE_REGION = 1,
STETE_TIME = 2,

def xududni_uzgartirish(xudud):
    print('uzg: ', xudud)
    manzil = f'https://namozvaqti.uz/shahar/{xudud}'
    r = requests.get(manzil)
    s = BeautifulSoup(r.text, 'html.parser')
    vaqt = s.find_all(class_='time')
    return vaqt

btn_xududlar = [
    [
        InlineKeyboardButton('Namangan', callback_data='namangan'),
        InlineKeyboardButton('Andijon', callback_data='andijon'),
        InlineKeyboardButton("Farg'ona", callback_data="fargona"),
        InlineKeyboardButton("Toshkent", callback_data="toshkent"),
    ],
    [
        InlineKeyboardButton('Sirdaryo', callback_data='sirdaryo'),
        InlineKeyboardButton('Jizzax', callback_data='jizzax'),
        InlineKeyboardButton("Samarqand", callback_data="samarqand"),
        InlineKeyboardButton("Navoiy", callback_data="navoiy"),
    ],
    [
        InlineKeyboardButton('Qashqadaryo', callback_data='qashqadaryo'),
        InlineKeyboardButton('Surxandaryo', callback_data='surxondaryo'),
        InlineKeyboardButton("Buxoro", callback_data="buxoro"),
        InlineKeyboardButton("Xorazm", callback_data="xorazm"),
    ],
    [
        InlineKeyboardButton("Qoraqalpog'iston", callback_data='qoraqalpogistonrespublikasi'),
        InlineKeyboardButton('Toshkent viloyati', callback_data='toshkent'),
    ],    
]
 
def bomdod(update, context):
    query = update.callback_query
    print(query)
    print(update)
    # vaqt = xududni_uzgartirish(query.data)
    # print('bom: ',xudud)
    # update.message.reply_html(f'Bomdod vaqti: {vaqt[0].text} ⏰', reply_markup = btn_vaqtlar)
def peshin(update, context):
    vaqt = xududni_uzgartirish()
    update.message.reply_html(f'Peshin vaqti: {vaqt[2].text} ⏰', reply_markup = btn_vaqtlar)
def asr(update, context):
    vaqt = xududni_uzgartirish()
    update.message.reply_html(f'Asr vaqti: {vaqt[3].text} ⏰', reply_markup = btn_vaqtlar)
def shom(update, context):
    vaqt = xududni_uzgartirish()
    update.message.reply_html(f'Shom vaqti: {vaqt[4].text} ⏰', reply_markup = btn_vaqtlar)
def xufton(update, context):
    vaqt = xududni_uzgartirish()
    update.message.reply_html(f'Xufton vaqti: {vaqt[5].text} ⏰', reply_markup = btn_vaqtlar)

def almashtirish(update, context):
    update.message.reply(reply_markup = InlineKeyboardMarkup(btn_xududlar))
    return STETE_REGION

def inline_callback(update, context):
    query = update.callback_query
    query.message.delete()
    query.message.reply_html(
        text=f'Siz <b>{query.data}</b> hududini tanladingiz, endi namoz vaqtlaridan birini tanlang!', 
        reply_markup = btn_vaqtlar
    )
    xudud = f'{query.data}'
    print('inl: ',xudud)
    xududni_uzgartirish(xudud)
    # bomdod(xudud)
    return STETE_TIME

def start(update, context):
    update.message.reply_html('Assalomu alaykum <b>{}.</b> Sizga qaysi hududning <b>namoz vaqtlari</b> kerak? quyidagilardan birini tanlang! 👇'.format(update.message.from_user.first_name), reply_markup = InlineKeyboardMarkup(btn_xududlar))
    return STETE_REGION

def main():
    updater = Updater('5441641304:AAFpYVAkpm9b1UdjHrCjXB_5quEZ0IhYh8U', use_context=True)
    mydispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        fallbacks=[MessageHandler(Filters.text, start)],
        states={
            STETE_REGION:[
                CallbackQueryHandler(inline_callback),
            ],
            STETE_TIME:[
                MessageHandler(Filters.regex('^('+BTN_BOMDOD+')$'), bomdod),
                MessageHandler(Filters.regex('^('+BTN_PESHIN+')$'), peshin),
                MessageHandler(Filters.regex('^('+BTN_ASR+')$'), asr),
                MessageHandler(Filters.regex('^('+BTN_SHOM+')$'), shom),
                MessageHandler(Filters.regex('^('+BTN_XUFTON+')$'), xufton),
            ],           
        },
    )

    mydispatcher.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()