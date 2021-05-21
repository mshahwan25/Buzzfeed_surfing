from bs4 import BeautifulSoup
import requests

def get_weather():
    r = requests.get('https://www.timeanddate.com/weather/egypt/cairo/ext')
    cont = r.content
    soup = BeautifulSoup(cont,'lxml')
    txt = soup.get_text()

    txt_start = txt.find('Currently:')
    txt_end = len(txt)
    ntxt = txt[txt_start:txt_end]
    ntxt_end = ntxt.find('(')-2
    ftxt = ntxt[0:ntxt_end]
    ftxt = ftxt.replace('\xa0','')
    return (ftxt)
    

if __name__ == '__main__':
    print (get_weather())