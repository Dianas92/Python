import requests
import os
import json
from pprint import pprint

token = 'ed1271af9e8883f7a7c2cefbfddfcbc61563029666c487b2f71a5227cce0d1b533c4af4c5b888633c06ae'
user_id = '171691064'
print('Получаем список друзей пользователя')

params = {'access_token':token,'user_id': user_id, 'v': '5.92'}

friend_list = requests.get('https://api.vk.com/method/friends.get', params).json()['response']['items']

friends=''
for number in friend_list:
  friends = friends + str(number) + ','


print('Получаем список групп пользователя')
params = {'access_token':token,'user_id': '171691064', 'v': '5.92'}
group_list = requests.get('https://api.vk.com/method/groups.get', params).json()['response']['items']

print('Обработка результатов')

records = []


for number in group_list:
  params = {'group_id': number, 'access_token': token,'user_ids': friends, 'v': '5.92'}
  answer = requests.get('https://api.vk.com/method/groups.isMember', params).json()['response'] 
 
  params = {'access_token':token,'group_id': number, 'v': '5.92'}
  group_name = requests.get('https://api.vk.com/method/groups.getById', params).json()['response'][0]['name']
  
  
  print('.')
  users_in_group = 0
  for line in answer:
    if line['member'] == 1:
      users_in_group += 1
 
  if users_in_group == 0:
    params = {'access_token':token,'group_id': number, 'fields':'members_count', 'v': '5.92'}
    members_count = requests.get('https://api.vk.com/method/groups.getById', params).json()['response'][0]['members_count']
    records.append({'name':group_name,'gid':number,'members_count':members_count})

with open('groups.json', 'w') as outfile:
  json.dump(records, outfile)
print('Программа завершила работу, результаты можно увидеть в файле groups.json')
