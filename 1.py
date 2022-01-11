import vk_api
import requests
import time
import random

token = 'Токен пользователя (для загрузки файлов на сервер)' # https://vkhost.github.io/
vk = vk_api.VkApi(token=token)
vk.get_api()
token1 = 'Токен сообщества, которое будет спамить'

doc = []

_id =  int(input('Введите ID беседы\n>>>'))

for i in range(1,6):
    try:
        a = vk.method("docs.getUploadServer", {'group_id':209773117})
        b = requests.post(a['upload_url'], files={'file': open(f'{i}.gif', 'rb')}).json()
        c = vk.method('docs.save', {'file': b['file']})
        d = "doc{}_{}".format(c['doc']["owner_id"], c['doc']["id"])
        doc.append(d)
        time.sleep(5)
    except vk_api.exceptions.Captcha as captcha:
        print(captcha.get_url()) # Получить ссылку на изображение капчи
        captcha.try_again(input('Введите капчу\n>>>'))

text = '😀 😃 😄 😁 😆 😅 😂 🤣 😇 😉 😊 🙂 🙃 ☺ 😋 😌 😍 🥰 😘 😗 😙 😚 🥲 🤪 😜 😝 😛 🤑 😎 🤓 🥸 🧐 🤠 🥳 🤗 🤡 😏 😶 😐 😑 😒 🙄 🤨 🤔 🤫 🤭 🤥 😳 😞 😟 😠 😡 🤬 😔 😕 🙁 ☹ 😬 🥺 😣 😖 😫 😩 🥱 😤 😮‍💨 😮 😱 😨 😰 😯 😦 😧 😢 😥 😪 🤤 😓 😭 🤩 😵 😵‍💫 🥴 😲 🤯 🤐 😷 🤕 🤒 🤮 🤢 🤧 🥵 🥶 😶‍🌫️ 😴 💤 😈 👿 👹 👺 💩 👻 💀 ☠ 👽 🤖 🎃 😺 😸 😹 😻 😼 😽 🙀 😿 😾 👐 🤲 🙌 👏 🙏 🤝 👍 👎 👊 ✊ 🤛 🤜 🤞 ✌ 🤘 🤟 👌 🤌 🤏 👈 👉 👆 👇 ☝ ✋ 🤚 🖐 🖖 👋 🤙 💪 🦾 🖕 ✍ 🤳 💅 🦵 🦿 🦶 👄 🦷 👅 👂 🦻 👃 👁 👀 🧠 🫀 🫁 🦴 👤 👥 🗣 🫂 👶 👧 🧒 👦 👩 🧑 👨 👩‍🦱 🧑‍🦱 👨‍🦱 👩‍🦰 🧑‍🦰 👨‍🦰 👱‍♀️ 👱 '

vk = vk_api.VkApi(token=token1)
vk._auth_token()
vk.get_api()

def raid(_id):
    vk.method('messages.send', {'peer_id': 2000000000+_id,
                                'message': 'RAID BOT ACTIVATED',
                                'random_id':0})
    time.sleep(5)

    for i in range(10, 0, -1):
        vk.method('messages.send', {'peer_id': 2000000000+_id,
                                    'message': f'{i}',
                                    'random_id':0})
        time.sleep(1)
    while True:
        try:
            text0 = text.split(' ')
            random.shuffle(text0)
            text0 = ' '.join(text0)
            vk.method('messages.send', {'peer_id': 2000000000+_id,
                                        'message':text0+,
                                        'attachment': ','.join(random.sample(doc, 3)),
                                        'random_id':0})
            time.sleep(random.uniform(0.1, 1))
        except vk_api.exceptions.ApiError as err:
            print(err)
            time.strftime('Время: %H:%M')
            time.sleep(120)
            print('Возобновление...')
        


raid(_id)
