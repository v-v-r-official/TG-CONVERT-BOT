import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import time
import pyrogram
from Tools.progress import progress_for_pyrogram
from translation import Translation


async def upload_video(c, m, send, media_location, thumb_image_path, duration, width, height):
      await send.edit(Translation.UPLOAD_START)
      update_channel = Config.UPDATE_CHANNEL
 if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked":
               await update.reply_text("🤭 Sorry Dude, You are **B A N N E D**. If you feel You are not guilty please contact @VKP_BOTS")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{update_channel} To Use Me")
            await update.reply_text(
                text="**Join My Updates Channel to use me & Enjoy the Free Service**",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="Join Our Updates Channel", url=f"https://t.me/{update_channel}")]
              ])
            )
            return
      c_time = time.time()
      if m.text == "/converttovideo":
         await c.send_video(
                chat_id=m.chat.id,
                video=media_location,
                duration=duration,
                width=width,
                height=height,
                supports_streaming=True,
                thumb=thumb_image_path,
                reply_to_message_id=m.reply_to_message.message_id,
                progress=progress_for_pyrogram,
                progress_args=(
                    "Upload Status:",
                    send,
                    c_time
                )
         )
      if m.text == "/converttofile":
         await c.send_document(
                chat_id=m.chat.id,
                document=media_location,
                thumb=thumb_image_path,
                reply_to_message_id=m.reply_to_message.message_id,
                progress=progress_for_pyrogram,
                progress_args=(
                    "Upload Status:",
                    send,
                    c_time
                )
         )
      try:
          os.remove(media_location)
      except:
          pass
      await send.edit(Translation.UPLOAD_COMPLETE)
      logger.info(f"{m.from_user.first_name}'s Task completed")
