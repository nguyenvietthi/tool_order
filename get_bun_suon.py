from skpy import Skype
from datetime import *
import re

list_user = { "live:.cid.a821106b3f180f97": "Quangnd1", "live:.cid.6f77ed61558db69": "V.anh", "live:.cid.eccff1ee01674be4": "Hoàn", "live:.cid.154c2e3316abbe42": "Quangnd0", "live:.cid.fcd17658776516e8": "Đạt", "live:minhdz2612": "Minh", "live:maytinhhuugiai": "Huy", "live:.cid.7b4731d55e5dea1c": "Thịnh", "live:bff4e847288cf939": "Lê Văn Hưng", "live:.cid.b594fc7b5970aa0d": "Phạm Quang Anh", "live:.cid.200aa59940c71a73": "Huy Trần", "live:b7c3ac2e7e329d51": "A.Huy", "live:.cid.fe2091fd5a44b92": "Thi", "manhnd.dti": "A.mạnh", "live:.cid.5498c54b35e01186": "V.Huy", "live:.cid.37617356a8747fc4": "HuyBu", "live:.cid.b81a24a561b43f1a": "Phương", "live:.cid.7c2f78584abceb6a": "Duy", "live:.cid.e6d8d6c10f7c6b3f": "Hiền", "live:lam.pn_1": "Lâm"  }

sk = Skype("0366939260", "")

chat = sk.chats
contacts = sk.contacts
# userIds = ['live:.cid.a821106b3f180f97', 'live:.cid.6f77ed61558db69', 'live:.cid.eccff1ee01674be4', 'live:.cid.154c2e3316abbe42', 'live:.cid.fcd17658776516e8', 'live:minhdz2612', 'live:maytinhhuugiai', 'live:.cid.7b4731d55e5dea1c', 'live:bff4e847288cf939', 'live:.cid.b594fc7b5970aa0d', 'live:.cid.200aa59940c71a73', 'live:b7c3ac2e7e329d51', 'live:.cid.fe2091fd5a44b92', 'manhnd.dti', 'live:.cid.5498c54b35e01186', 'live:.cid.37617356a8747fc4', 'live:.cid.b81a24a561b43f1a', 'live:.cid.7c2f78584abceb6a', 'live:.cid.e6d8d6c10f7c6b3f', 'live:lam.pn_1']
# for i in userIds:
#     print(list_user[i])
#     print(i)
#     print()
# oder_group = chat.chat("19:f9436e25d3ca444392bf1a5156eba308@thread.skype") # TEST
oder_group = chat.chat("19:232a4474d06e465eaed75e93c2cbf27a@thread.skype") # dat com
megs = oder_group.getMsgs()


today_date = date.today()

list_order_user = dict()

for i in megs:
    if(today_date.month == i.time.month and today_date.day == i.time.day and today_date.year == i.time.year):
        if(re.search("\+", i.content) and (re.search("mọc", i.content) or re.search("dải", i.content) or re.search("giải", i.content) or re.search("sườn", i.content))):
            try:
                if(list_order_user[contacts[i.userId].name] != i.content):
                    list_order_user[contacts[i.userId].name] = list_order_user[contacts[i.userId].name] + ", "+ i.content  
            except KeyError:
                list_order_user[contacts[i.userId].name] = i.content  

# print(list_order_user)
total = 0
print("DATE:", today_date)
for order_user in list_order_user:
    content = list_order_user[order_user]
    content_remove_plus = content.replace("+", "")
    index_trash = content.find("<")
    # print(index_trash)
    if(index_trash != -1):
        content_remove = content[:index_trash]
    else:
        content_remove = content
    content_remove = content_remove.replace("\n", "")
    number_of_order = sum([int(s) for s in content_remove_plus.split() if s.isdigit()])
    total = total + number_of_order
    # print(number_of_order)
    print(order_user, end=": ")
    print(number_of_order, end=" \n\tContent: \"")
    print(content_remove, end = "\" \n")

print("\nTOTAL: ",total)
