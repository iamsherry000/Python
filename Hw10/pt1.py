# https://www.itread01.com/article/1533536621.html

import json
import pandas as pd


with open('pt1.json', 'r',encoding="utf8") as json_file:
  data = json_file.read()
  print(type(data))  # type(data) = 'str'
  result = json.loads(data)
  new_result = json.dumps(result,ensure_ascii=False) # 參考網上的方法，***ensure_ascii***設為False
  print (new_result)
  df = pd.json_normalize(result)
  df.to_csv("samplecsv.csv",index = None,encoding="utf_8_sig")