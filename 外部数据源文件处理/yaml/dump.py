#将python中的数据写到yaml文件中

import yaml
with open("demo3.yml","w") as f:
    yaml.dump(data={'c': [1, 2, 2], 'd': 888},stream=f)