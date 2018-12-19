import requests
from pprint import pprint

token = 'ed1271af9e8883f7a7c2cefbfddfcbc61563029666c487b2f71a5227cce0d1b533c4af4c5b888633c06ae'
params = {'access_token':token,'user_id': '171691064', 'v': '5.92'}

friend_list = requests.get('https://api.vk.com/method/friends.get', params).json()['response']['items']

friends=''
for number in friend_list:
  friends = friends + str(number) + ','

#print(friends)
print('')

params = {'access_token':token,'user_id': '171691064', 'v': '5.92'}
group_list = requests.get('https://api.vk.com/method/groups.get', params).json()['response']['items']
#print(group_list)
print('')

for number in group_list:
  params = {'group_id': number, 'access_token': token,'user_ids': friends, 'v': '5.92'}
  answer = requests.get('https://api.vk.com/method/groups.isMember', params).json()['response']
  
  print('В группе '+str(number)+' состоят:')
  for line in answer:
    if line['member'] == 1:
      print(line['user_id'])

