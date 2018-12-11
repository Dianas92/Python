import xml.etree.ElementTree as ET

def read_files(name):
    tree = ET.parse(name)
    root = tree.getroot()
    text = ''
    for items in root.iterfind('channel/item/description'):
        text += items.text + ' '
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
    sort_list = sorted(word_value.items(), key=l, reverse=True)
    count = 1
    top_10 = {}
    for word in sort_list:
        top_10[count] = word
        count += 1
        if count == 11:
            break
    return top_10


file_name = 'newsafr.xml'

top_10 = sort_top(count_word(read_files(file_name)))
for i in top_10.values():
    print (i[1], ': ', i[0])
