import requests as r
from bs4 import BeautifulSoup as bs
from time import sleep as sl
from os import system as cmd;cmd('clear')
r = r.Session()

url = 'https://tools.tracemyip.org/search--isp/pt+telkom+indonesia'
ua = {'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 9; Ubuntu Citah/20.4)'}

num = []
ak = []

def scr(bres):
    for i in bres.findAll('a',href=True):
        if '/lookup/' in str(i):
           print(i.text)

def nscr(v):
    for i in v.findAll('span',class_='tsTxt14 sModPrW'):
        print(i.text)
        num.append(i.text)


def main():
    if len(num) == 0:
       nscr(bs(r.get(url=url,headers=ua).text,'html.parser'))

    n = 1
    while True:
          if len(ak) == 0 and n == 1:
            print('pertama')
            scr(bs(r.get(url=url,headers=ua).text,'html.parser'))
          else:
              print(f'LOOP ke {n}')
              for nu in num:
                 if nu != num[-1]:
                    if len(ak) != 0 and int(nu) > int(ak[0]):
                       print('next two')
                       #url2 = f'https://tools.tracemyip.org/search--isp/pt+telkom+indonesia:-v-:gTr={nu}&gNr=50'
                       #scr(bs(r.get(url=url2,headers=ua).text,'html.parser'))
                    elif len(ak) == 0:
                        print('next')
                        #url2 = f'https://tools.tracemyip.org/search--isp/pt+telkom+indonesia:-v-:gTr={nu}&gNr=50'
                        #scr(bs(r.get(url=url2,headers=ua).text,'html.parser'))
 
                 else:
                     print(nu,'done')
                     url2 = f'https://tools.tracemyip.org/search--isp/pt+telkom+indonesia:-v-:gTr={nu}&gNr=50'
                     rs = bs(r.get(url=url2,headers=ua).text,'html.parser')
                     scr(rs)
                     if len(ak) == 0:
                        ak.append(num[-1]);num.clear()
                        nscr(rs)
                        main()
                        
                     else:
                         ak.clear()
                         ak.append(num[-1]);num.clear()
                         nscr(rs)
                         main()
                
          n+=1


main()
