import requests
import os
import json

token = 'ed1271af9e8883f7a7c2cefbfddfcbc61563029666c487b2f71a5227cce0d1b533c4af4c5b888633c06ae'
user_id = '171691064'
file_name = 'groups.json'

def list_of_friends(token, user_id):
  try:
    params = {'access_token':token,'user_id': user_id, 'v': '5.92'}
    friend_list = requests.get('https://api.vk.com/method/friends.get', params).json()['response']['items']
  except:
    print('Не удалось получить список друзей пользователя')
  return(friend_list)

def split_list(in_list, number):
  out_list = []
  for i in range(int(len(in_list)/number+0.999)):
    out_list.append(in_list[i*number:(i+1)*number])
  return out_list

def list_to_string(in_list):
  new_string=''
  for number in in_list:
    new_string = new_string + str(number) + ','
  return(new_string)

def list_of_groups(token, user_id):
  try:
    params = {'access_token':token,'user_id': user_id, 'v': '5.92'}
    group_list = requests.get('https://api.vk.com/method/groups.get', params).json()['response']['items']
  except:
    print('Не удалось получить списокгрупп пользователя')
  return(group_list)

def friends_in_group(group_list, token, friends):
  new_group_list = []
  for number in group_list:
    print('.')

    try:
      params = {'group_id': number, 'access_token': token,'user_ids': friends, 'v': '5.92'}
      answer = requests.get('https://api.vk.com/method/groups.isMember', params).json()['response'] 
    except:
      print('Ошибка ответа сервера ВК')

    for line in answer:
      if line['member'] == 1:
        break
    else:
      new_group_list.append(number)
    
  return(new_group_list)

def make_result(in_list):
  numbers = list_to_string(in_list)
  records = []

  try:
    params = {'access_token':token,'group_ids': numbers, 'fields':'members_count', 'v': '5.92'}
    answer = requests.get('https://api.vk.com/method/groups.getById', params).json()['response']
  except:
    print('Не удалось получить информацию о группах')

  for line in answer:
    records.append({'name':line['name'],'gid':line['id'],'members_count':line['members_count']})
  return(records)

def write_to_file(file_name, records):
  try:
    with open(file_name, 'w') as outfile:
      json.dump(records, outfile)
    print('Программа завершила работу, результаты можно увидеть в файле groups.json')
  except:
    print('Не удалось записать файл с результатами')  

print('Получаем список друзей пользователя')
friend_list = split_list(list_of_friends(token, user_id), 500)

print('Получаем список групп пользователя')
groups_list = list_of_groups(token, user_id)

print('Обработка результатов')
for line in friend_list:
  friends = list_to_string(line)
  groups_list = friends_in_group(groups_list, token, friends)
records = make_result(groups_list)
write_to_file(file_name, records)
