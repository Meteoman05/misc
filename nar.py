import vk_api
import requests
import time

token = '' # https://vkhost.github.io/
vk = vk_api.VkApi(token=token)
vk.get_api()


def main():
  vk.method('messages.send', {'peer_id': 2000000000+1,
                                  'message': 'Сокращённое время, КД 2-4. Чек закреп!',
                                  'random_id':0})
  time.sleep(3600)



while True:
  
  if time.gmtime()[3] == 1 and time.gmtime()[4] == 30:
    main()
  elif time.gmtime()[3] == 3 and time.gmtime()[4] == 0:
    main()
  elif time.gmtime()[3] == 4 and time.gmtime()[4] == 30:
    main()
  elif time.gmtime()[3] == 6 and time.gmtime()[4] == 0:
    main()
  elif time.gmtime()[3] == 7 and time.gmtime()[4] == 30:
    main()
  elif time.gmtime()[3] == 9 and time.gmtime()[4] == 0:
    main()
  elif time.gmtime()[3] == 10 and time.gmtime()[4] == 30:
    main()
  elif time.gmtime()[3] == 12 and time.gmtime()[4] == 0:
    main()
  elif time.gmtime()[3] == 13 and time.gmtime()[4] == 30:
    main()
  elif time.gmtime()[3] == 15 and time.gmtime()[4] == 0:
    main()
  elif time.gmtime()[3] == 16 and time.gmtime()[4] == 30:
    main()
  elif time.gmtime()[3] == 18 and time.gmtime()[4] == 0:
    main()
  elif time.gmtime()[3] == 19 and time.gmtime()[4] == 30:
    main()
  elif time.gmtime()[3] == 21 and time.gmtime()[4] == 0:
    main()
  elif time.gmtime()[3] == 22 and time.gmtime()[4] == 30:
    main()
  elif time.gmtime()[3] == 0 and time.gmtime()[4] == 0:
    main()
   else:
    sleep(5)
