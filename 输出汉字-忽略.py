#encoding=utf-8

import json

list_words = ['你','我','他']
print(list_words)
#无法正常显示汉字
print(str(list_words).decode('string_escape'))
#正常显示汉字
list_words_result=json.dumps(list_words,encoding='utf-8',ensure_ascii=False)
print(list_words_result)