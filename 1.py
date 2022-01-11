import vk_api
import requests
import time
import random

token = '62bb013572eb9e024cdc08326dbac39fd8373f1fe10c42aeba343efd96cf28eb0481531d3e5bf2e364278'
vk = vk_api.VkApi(token=token)
vk.get_api()
token1 = 'ece8ae033870d648bae5bdefeee4cb5e4b97725bd5ca478b070bf7fb0192aee355f110b90f4565fc0cc36'

doc = ['doc-209773117_628178389', 'doc-209773117_628178397', 'doc-209773117_628178401', 'doc-209773117_628178411', 'doc-209773117_628178419']

_id =  1#int(input('Введите ID беседы\n>>>'))

# for i in range(1,6):
#     try:
#         a = vk.method("docs.getUploadServer", {'group_id':209773117})
#         b = requests.post(a['upload_url'], files={'file': open(f'{i}.gif', 'rb')}).json()
#         c = vk.method('docs.save', {'file': b['file']})
#         d = "doc{}_{}".format(c['doc']["owner_id"], c['doc']["id"])
#         doc.append(d)
#         time.sleep(5)
#     except vk_api.exceptions.Captcha as captcha:
#         captcha.sid # Получение sid
#         print(captcha.get_url()) # Получить ссылку на изображение капчи
#         captcha.get_image() # Получить изображение капчи (jpg)
#         captcha.try_again(input())

text = '😀 😃 😄 😁 😆 😅 😂 🤣 😇 😉 😊 🙂 🙃 ☺ 😋 😌 😍 🥰 😘 😗 😙 😚 🥲 🤪 😜 😝 😛 🤑 😎 🤓 🥸 🧐 🤠 🥳 🤗 🤡 😏 😶 😐 😑 😒 🙄 🤨 🤔 🤫 🤭 🤥 😳 😞 😟 😠 😡 🤬 😔 😕 🙁 ☹ 😬 🥺 😣 😖 😫 😩 🥱 😤 😮‍💨 😮 😱 😨 😰 😯 😦 😧 😢 😥 😪 🤤 😓 😭 🤩 😵 😵‍💫 🥴 😲 🤯 🤐 😷 🤕 🤒 🤮 🤢 🤧 🥵 🥶 😶‍🌫️ 😴 💤 😈 👿 👹 👺 💩 👻 💀 ☠ 👽 🤖 🎃 😺 😸 😹 😻 😼 😽 🙀 😿 😾 👐 🤲 🙌 👏 🙏 🤝 👍 👎 👊 ✊ 🤛 🤜 🤞 ✌ 🤘 🤟 👌 🤌 🤏 👈 👉 👆 👇 ☝ ✋ 🤚 🖐 🖖 👋 🤙 💪 🦾 🖕 ✍ 🤳 💅 🦵 🦿 🦶 👄 🦷 👅 👂 🦻 👃 👁 👀 🧠 🫀 🫁 🦴 👤 👥 🗣 🫂 👶 👧 🧒 👦 👩 🧑 👨 👩‍🦱 🧑‍🦱 👨‍🦱 👩‍🦰 🧑‍🦰 👨‍🦰 👱‍♀️ 👱 '

vk = vk_api.VkApi(token=token1)
vk._auth_token()
vk.get_api()

##for i in doc:   
##vk.method("messages.send", {"peer_id": '2000000001', "message": "TEST NAHUY", "attachment": f'{doc[0]},{doc[2]}', "random_id": 0})
##time.sleep(2)

def raid(_id):
    while True:
        try:
            text0 = text.split(' ')
            random.shuffle(text0)
            text0 = ' '.join(text0)
            vk.method('messages.send', {'peer_id': 2000000000+_id,
                                        'message':text0+х'[dko_05|&#8300]',
                                        'attachment': ','.join(random.sample(doc, 3)),
                                        'random_id':0})
            time.sleep(random.uniform(0.1, 1))
        except vk_api.exceptions.ApiError as err:
            print(err)
            time.strftime('Время: %H:%M')
            time.sleep(120)
            print('Возобновление...')
        
##vk.method('messages.send', {'peer_id': 2000000000+_id,
##                            'message': 'Произошла критическая ошибка. Запускаю аварийный модуль',
##                            'random_id':0})


time.sleep(5)

vk.method('messages.send', {'peer_id': 2000000000+_id,
                            'message': 'RAID BOT ACTIVATED',
                            'random_id':0})

time.sleep(5)

for i in range(10, 0, -1):
    vk.method('messages.send', {'peer_id': 2000000000+_id,
                                'message': f'{i}',
                                'random_id':0})
    time.sleep(1)


raid(_id)
