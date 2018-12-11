import json
import chardet

def read_files(name):
 
    with open(name, 'rb') as jsonfile:
        data = jsonfile.read()
        result = chardet.detect(data)
        data = data.decode(result['encoding'])
        data = json.loads(data) 
        text = ''
        for items in data['rss']['channel']['items']:
           text += ' ' + items['description']
        return text

def count_word(text):
    
    to_list = text.lower().split(' ')
    word_value = {}
    for word in to_list: 
        if len(word) > 6:
            if word in word_value:
                word_value[word] += 1
            else:
                word_value[word] = 1
    return word_value 
  
 
def sort_top(word_value):
   
    l = lambda word_value: word_value[1]
    sort_list = sorted(word_value.items(), key = l, reverse = True)
    count = 1
    top_10 = {}
    for word in sort_list:
        top_10[count] = word        
        count += 1        
        if count == 11:
            break
    return top_10

name = 'newsafr.json'
top_10 = sort_top(count_word(read_files(name)))
for i in top_10.values():
  print (i[1], ': ', i[0])
  

