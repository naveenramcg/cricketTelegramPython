import cricBuzz
import conf
import telegramBot
import time

cricket = telegramBot.telegram_bot()
message1 = "Your Cricket Updates are Ready. To start reply '\start'"
cricket.send_message(message1, conf.telegram_chat_id)
while True:
    q = cricket.get_index()
    message1 = cricket.user_response(q)
    print(message1)
    if message1 == '\start':
        cricket.send_message(cricBuzz.get_matches() + '\nReply with number to know the live score', conf.telegram_chat_id)
        r = cricket.get_index()
        message2 = cricket.user_response(r)
        cricket.send_score(message2)
    else:
        continue
        #if message2 == '\close':
           # continue
      #  else:
       #     try:
        #        cricket.send_message(cricBuzz.get_score(message2), conf.telegram_chat_id)
         #   except Exception as e:
          #      cricket.send_message("Invalid Reply",conf.telegram_chat_id)


