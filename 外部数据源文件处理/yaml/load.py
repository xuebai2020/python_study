#将yaml数据文件读为python中的字典或列表

import yaml
'''
print(yaml.load("""
 - Hesperiidae
 - Papilionidae
 - Apatelodidae
 - Epiplemidae
 """,Loader=yaml.FullLoader))


print(yaml.load("""
 a: 1
 b: 2
 """,Loader=yaml.FullLoader))
'''
print(yaml.load(open("demo2.yml"), Loader=yaml.FullLoader))

