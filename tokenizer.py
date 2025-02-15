import re
import pprint


with open("the-verdict.txt","r",encoding="utf-8") as f:
    raw_text = f.read()

# print(len(raw_text))
# print(raw_text[:30])

split_text = re.split(r'([.,:;?_!"()\']|--|\s)',raw_text)
preprocesssed = [i for i in split_text if i.strip()]
# print(preprocesssed[:30])
print(len(preprocesssed))

all_words = sorted(set(preprocesssed))

print(len(all_words))

vocab = {token:integer for token,integer in enumerate(all_words)}

for i, item in enumerate(vocab.items()):
    print(item)
    if  i >20:
        break