import vk_api
import requests
import time

token = 'd925108929cda3ce60c74fe23e57557a7c81b848e5b5de6e6e46c46591f51ea7c04fcd41ed589f4cb3c0d' # https://vkhost.github.io/
vk = vk_api.VkApi(token=token)
vk.get_api()


def main():
  vk.method('messages.send', {'peer_id': 2000000000+1,
                                  'message': 'Сокращённое время, КД 2-4. Чек закреп!',
                                  'random_id':0})
  time.sleep(3600)



while True:
  for i in range(9):  
    if time.gmtime()[3] == 5 + 2*i and time.gmtime()[4] == 45:
      main()
      break
  time.sleep(5)

