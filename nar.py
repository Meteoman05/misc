import vk_api
import requests
import time

token = '' # https://vkhost.github.io/
vk = vk_api.VkApi(token=token)
vk.get_api()

vk.method('messages.send', {'peer_id': 2000000000+1,
                                'message': 'Сокращен',
                                'random_id':0})
