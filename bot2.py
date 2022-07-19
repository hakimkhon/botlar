from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
import requests
from bs4 import BeautifulSoup

BTN_BOMDOD, BTN_PESHIN, BTN_ASR, BTN_SHOM, BTN_XUFTON, BTN_HUDUD, BTN_XIZMAT = ( '🌒 Bomdod', '🌗 Peshin', '🌖 Asr', '🌘 Shom', '🌑 Xufton', '♻️ Hududni uzgartirish', 'Boshlash') 

btn_vaqtlar = ReplyKeyboardMarkup([
    [
        BTN_BOMDOD, BTN_PESHIN, BTN_ASR
    ],
    [
        BTN_SHOM, BTN_XUFTON
    ],
    [
        BTN_HUDUD
    ]
], resize_keyboard=True)

btn_xizmat = ReplyKeyboardMarkup([
    [
        BTN_XIZMAT
    ]
], resize_keyboard=True, one_time_keyboard=True)


btn_xududlar = [
    [
        InlineKeyboardButton('Namangan', callback_data='namangan'),
        InlineKeyboardButton('Andijon', callback_data='andijon'),
        InlineKeyboardButton("Farg'ona", callback_data="fargona"),
        InlineKeyboardButton("Toshkent", callback_data="toshkent"),
    ],
    [
        InlineKeyboardButton('Sirdaryo', callback_data='guliston'),
        InlineKeyboardButton('Jizzax', callback_data='jizzax'),
        InlineKeyboardButton("Samarqand", callback_data="samarqand"),
        InlineKeyboardButton("Navoiy", callback_data="navoiy"),
    ],
    [
        InlineKeyboardButton('Qashqadaryo', callback_data='qarshi'),
        InlineKeyboardButton('Surxandaryo', callback_data='termiz'),
        InlineKeyboardButton("Buxoro", callback_data="buxoro"),
        InlineKeyboardButton("Xorazm", callback_data="urganch"),
    ],
    [
        InlineKeyboardButton("Qoraqalpog'iston", callback_data='nukus'),
        InlineKeyboardButton('Toshkent viloyati', callback_data='yangiyol'),
    ],    
]

STETE_REGION = 1,
STETE_TIME = 2,
STETE_OTHER = 3,
STETE_OTHER_2 = 4,
manzil = list()

def xududni_uzgartirish(xudud):
    print('xududni_uzgartirish: ', xudud)
    print('manzil[0]: ', manzil[len(manzil)-1])
    print('manzil: ', manzil)
    manzillar = f'https://namozvaqti.uz/shahar/{xudud}'
    r = requests.get(manzillar)
    s = BeautifulSoup(r.text, 'html.parser')
    t = s.find_all(class_='time')
    return t

def bomdod(update, context):
    qqq = manzil[len(manzil)-1]
    # print('qqq: ', qqq)
    vaqt = xududni_uzgartirish(qqq)
    # print('bomdod: ', vaqt)
    # print('bomdod: ', vaqt.text)
    # print('bomdod: ', vaqt[0].text)
    update.message.reply_html(f'<b>{qqq.capitalize()}</b> vaqti bilan Bomdod {vaqt[0].text} da', reply_markup = btn_vaqtlar)
def peshin(update, context):
    qqq = manzil[len(manzil)-1]
    vaqt = xududni_uzgartirish(qqq)
    update.message.reply_html(f'<b>{qqq.capitalize()}</b> vaqti bilan Peshin {vaqt[2].text} da', reply_markup = btn_vaqtlar)
def asr(update, context):
    qqq = manzil[len(manzil)-1]
    vaqt = xududni_uzgartirish(qqq)
    update.message.reply_html(f'<b>{qqq.capitalize()}</b> vaqti bilan Asr {vaqt[3].text} da', reply_markup = btn_vaqtlar)
def shom(update, context):
    qqq = manzil[len(manzil)-1]
    vaqt = xududni_uzgartirish(qqq)
    update.message.reply_html(f'<b>{qqq.capitalize()}</b> vaqti bilan Shom {vaqt[4].text} da', reply_markup = btn_vaqtlar)
def xufton(update, context):
    qqq = manzil[len(manzil)-1]
    vaqt = xududni_uzgartirish(qqq)
    update.message.reply_html(f'<b>{qqq.capitalize()}</b> vaqti bilan Xufton  {vaqt[5].text} da', reply_markup = btn_vaqtlar)

def almashtirish(update, context):
    manzil.clear()
    print('listni bushatish: ', manzil)
    update.message.reply_html('<b>Hududlar</b>dan birini tanlang', reply_markup = InlineKeyboardMarkup(btn_xududlar))
    update.message.reply_html('Yoki <b>Bot</b>ni qayta ishga tushiring', reply_markup = btn_xizmat)
    return STETE_OTHER

def boshqa(update, context):
    update.message.delete()
    update.message.reply_text(
        f'Bu xizmat hali oxiriga yetmagan! Iltimos mavjud xizmatlardan foydalanib turing!', reply_markup = btn_vaqtlar
    )
    return STETE_OTHER

def inline_callback(update, context):
    query = update.callback_query
    query.message.delete()
    query.message.reply_html(
        text=f'Siz <b>{query.data.capitalize()}</b> hududini tanladingiz, endi namoz vaqtlaridan birini tanlang!', 
        reply_markup = btn_vaqtlar
    )
    xudud = f'{query.data}'
    manzil.append(f'{xudud}')
    print('inline_callback: ',xudud)
    xududni_uzgartirish(xudud)
    return STETE_TIME

def inline_call(update, context):
    query = update.callback_query
    query.message.delete()
    query.message.reply_html(
        text=f'Siz <b>{query.data.capitalize()}</b> hududini tanladingiz, endi namoz vaqtlaridan birini tanlang!', 
        reply_markup = btn_vaqtlar
    )
    xudud = f'{query.data}'
    manzil.append(f'{xudud}')
    print('inline_callback: ',xudud)
    xududni_uzgartirish(xudud)
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
                MessageHandler(Filters.regex('^('+BTN_HUDUD+')$'), almashtirish),
                MessageHandler(Filters.regex('^('+BTN_XIZMAT+')$'), boshqa),

            ], 
            STETE_OTHER:[
                CallbackQueryHandler(inline_call),
            ],
            # STETE_OTHER_2:[
            #     MessageHandler(Filters.regex('^('+BTN_XIZMAT+')$'), boshqa),
            # ]          
        },
    )

    mydispatcher.add_handler(conv_handler)
    updater.start_polling(skip_updates=True)
    updater.idle()

if __name__ == '__main__':
    main()