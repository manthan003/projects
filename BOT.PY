import requests
jokes=input()
'''for joke in jokes:'''
base_url='https://api.telegram.org/bot1796419872:AAFJqFy-PoulAuPlQDqhDPn1wTTbB6A-8tM/sendMessage?chat_id=-594504706&text="{}"'.format(jokes)
requests.get(base_url)
