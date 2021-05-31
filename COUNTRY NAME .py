import requests
base_url='http://restcountries.eu/rest/v2/all'# base_url is a obj which is used to dump a url 
resp=requests.get(base_url)#resp is a obj which is used to get a request from the url 
data=resp.json()# data is also a obj which is used to display the url in json format 
print(data)
for country in data:# used to clear view 
    print(country['name'],country['capital'],country['population'])# this commond is used to print only the country names 
'''print("what is your name")
username=input()
print("what is your country")
usercountry=input()
for country in data:
     if(country['name'].upper() ==usercountry.upper()):#UPPER KEYWORD IS USED TO RETRIVE THE INFORMATION FROM THE SITE BECASUE THE SITE CONTAINS CASE SENSITIVE SO WHILE USING COUNTRY NAME WE CAN USE UPPER CASE 
         print('nice to meet you,{}!!!'.format(username))
         print('i like your country {},especially your capital {}'.format(usercountry,country['capital']))
         print('your country population  is {}'.format(country['population']))
         print('neighbour countries are ')
         print(country['borders'])

         for neighbour in country['borders']:
             code=requests.get('http://restcountries.eu/rest/v2/alpha/{}'.format(neighbour)).json()
             print(code['name'])'''
