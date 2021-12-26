import glob
import os
import json
from acdh_tei_pyutils.tei import TeiReader
from tqdm import tqdm
files = glob.glob('./data/editions/*xml')
out_file = "./html/calendar.json"
data = []
for x in tqdm(files, total=len(files)):
    item = {}
    head, tail = os.path.split(x)
    doc = TeiReader(x)
    item['name'] = doc.any_xpath('//tei:title[@type="main"]/text()')[0]
    item['startDate'] = doc.any_xpath('//tei:title[@type="iso-date"]/text()')[0]
    item['id'] = tail.replace('.xml', '.html')
    data.append(item)

print(f"writing calendar data to {out_file}")
with open(out_file, 'w',  encoding='utf8') as f:
    json.dump(data, f, ensure_ascii=False)

