import telepot
import time
isExit = False
class Manager():
    def __init__(self):
        self.bot = telepot.Bot('5251122654:AAEnM8PegZmsw2DErB_9VnhWi094kfZt0YA')
        self.run()

    def handle(self, msg):
        content_type, chat_type, self.chat_id = telepot.glance(msg)
        if(content_type != 'text'):
            sendMessage(chat_id, 'I cant understant your message')
            return
        content = msg['text']
        if (content == 'exit'):
            self.CloseBot()

    def CloseBot(self):
        self.bot.sendMessage(self.chat_id, '----종료합니다----')
        global isExit
        isExit = True

    def run(self):
        print(self.bot.getMe())
        self.bot.message_loop(self.handle)

if __name__ == "__main__":
    print('Listening')
    MM = Manager()
    try:
        while(isExit == False):
            time.sleep(10)
        print("봇을 종료합니다")
    except:
        print("End the program")