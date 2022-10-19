from http import client
from skpy import Skype
from datetime import *
import re
import gspread
from oauth2client.service_account import ServiceAccountCredentials
list_user = { "live:.cid.a821106b3f180f97": "Quangnd1", "live:.cid.6f77ed61558db69": "V.anh", "live:.cid.eccff1ee01674be4": "Hoàn", "live:.cid.154c2e3316abbe42": "Quangnd0", "live:.cid.fcd17658776516e8": "Đạt", "live:minhdz2612": "Minh", "live:maytinhhuugiai": "Huy", "live:.cid.7b4731d55e5dea1c": "Thịnh", "live:bff4e847288cf939": "Lê Văn Hưng", "live:.cid.b594fc7b5970aa0d": "Phạm Quang Anh", "live:.cid.200aa59940c71a73": "Huy Trần", "live:b7c3ac2e7e329d51": "A.Huy", "live:.cid.fe2091fd5a44b92": "Thi", "manhnd.dti": "A.mạnh", "live:.cid.5498c54b35e01186": "V.Huy", "live:.cid.37617356a8747fc4": "HuyBu", "live:.cid.b81a24a561b43f1a": "Phương", "live:.cid.7c2f78584abceb6a": "Duy", "live:.cid.e6d8d6c10f7c6b3f": "Hiền", "live:lam.pn_1": "Lâm"  }

def get_row(id):
    i = 1
    # print(wks.get("A" + str(i))[-1][-1])
    while(1):
        try:
            if(wks.get("A" + str(i))[-1][-1] == list_user[id]):
                return i
        except:
            return i
        i = i + 1

scopes = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
creads = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scopes)
client = gspread.authorize(creads)

spreadsheet = client.open("test_oder")
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
wks = spreadsheet.worksheet("thang 10")

today_date = date.today()
index = 0
while(1):
    try:
        # print(wks.get(chr(65 + index) + "1")[-1][-1])
        if(wks.get(chr(65 + index) + "1")[-1][-1] == (str(today_date.day) +"/"+ str(today_date.month))):
            break
    except:
        wks.update(chr(index+65) + "1", str(today_date.day) +"/"+ str(today_date.month))
        break
    index = index + 1
add_col = chr(index+65)
print(add_col)

for i in megs:
    if(today_date.month == i.time.month and today_date.day == i.time.day and today_date.year == i.time.year):
        if(re.search(".{1,}\:.{1,}\+.{1,}\+.{1,}", i.content)):
            print("Dat Ho")
            print(contacts[i.userId].name)
            print(i.plain)
            print()
        elif(re.search(".{1,}\+.{1,}\+.{1,}\(.{1,}\)", i.content)):
            print("Dat Ho")
            print(contacts[i.userId].name)
            print(i.plain)
            print()
        elif(re.search(".{1,}\+.{1,}\+.{1,}", i.content)):
            print("Chinh Chu")
            wks.update(add_col + str(get_row(i.userId)), i.plain)
            print(i.plain)





# wks.update('O1', 'thinv0' )

# if(wks.get("O1")[0][0] == "thinv0"):
#     print("dfsdfsd")

# print(get_row("manhnd.dti"))
