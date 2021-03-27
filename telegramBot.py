import requests
import json
import conf
import cricBuzz

token = conf.telegram_bot_id
base = "https://api.telegram.org/"


class telegram_bot():
    def get_chat(self):
        url = base + token + "/getUpdates"
        r = requests.get(url)
        res = json.loads(r.content)
        q =(len(res['result']))
        #print(q-1)
        #text = res["result"][q-1]['channel_post']['text']
        #print(text)
        #print(res)
        return res

    def send_message(self, message, chat_id):
        url = base + token + "/sendMessage?chat_id=" + chat_id + "&text=" + message
        requests.get(url)

    def user_response(self, num):
        url = base + token + "/getUpdates"
        r = requests.get(url)
        res = json.loads(r.content)
        #q = (len(res['result']))
        # print(q-1)
        try:
            text = res["result"][num]['channel_post']['text']
            #print(text)
            #print(res)
            return text
        except Exception as e:
            self.user_response(num)
            return self.user_response(num)
            #return text

    def send_score(self, message2):
        try:
            self.send_message(cricBuzz.get_score(int(message2)), conf.telegram_chat_id)
        except Exception as e:
            self.send_message('the reply is invalid', conf.telegram_chat_id)


    def get_index(self):
        url = base + token + "/getUpdates"
        r = requests.get(url)
        res = json.loads(r.content)
        q = (len(res['result']))
        # print(q-1)
        return q
#a = telegram_bot()
#print(a.get_chat())
#num = a.get_q()
#print(num)
#a.send_message('Hello Naveen', conf.telegram_chat_id)
#print(a.get_index())
#print(a.user_response(a.get_index()))

