from telegram.ext import * 
import logging

API_KEY= '8191505882:AAEanKawuSRlxHmt2PsCPaps-ED7FYchnAo'



async def start_com(update,context):
   await update.message.reply_text("enter any text to see the biggest in the world")

async def sendthepic_com(update,context):
   with open("karimo.jpg", 'rb') as photo:
    await update.message.reply_photo(photo=photo)

async def replytohim(update,context):
  await update.message.reply_text("nta ")
  with open("karimo.jpg",'rb') as photo :
   await update.message.reply_photo(photo=photo)

if __name__=="__main__":
  app = ApplicationBuilder().token(API_KEY).build()
  app.add_handler( CommandHandler('start',start_com))
  app.add_handlers(
    [
     
      CommandHandler('send_photo',sendthepic_com)
      ,MessageHandler(~filters.COMMAND & filters.TEXT , replytohim)
    ]
  )

  app.run_polling()
  