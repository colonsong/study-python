import datetime

import chardet
import loguru
import pyquery
import requests
import os

import fractions

class Propotion:

    def __init__(self, sort, code, name, percent):

        self.Sort = int(sort)

        self.Code = code 
        
        self.Name = name 

        self.Percent = fractions.Fraction(percent[:-1])
    
    def __repr__(self):
        return (
            f'class Propotion {{ '
            f'Sort={self.Sort}, '
            f'Code={self.Code}, '
            f'Name={self.Name}, '
            f'Percent={float(self.Percent):4f}% '
            f'}}'
        )







def main():

    resp = requests.get('https://www.taifex.com.tw/cht/9/futuresQADetail')
    if resp.status_code != 200:
        loguru.logger.error('RESP: status code is not 200')
    loguru.logger.success('RESP: success')


    txt = None
    det = chardet.detect(resp.content)
    try:
        if det['confidence'] > 0.5:
            if det['encoding'] == 'big-5':
                txt = resp.content.decode('big5')
            else:
                txt = resp.content.decode(det['encoding'])
        else:
            txt = resp.content.decode('utf-8')
    except Exception as e:
        loguru.logger.error(e)

    if txt is None:
        return
    #loguru.logger.info(txt)# 成分股市值佔比清單

    proportions = []

    # 將下載回來的內容解析為 PyQuery 物件
    d = pyquery.PyQuery(txt)
    # 透過 CSS 選擇器取出所有表格行
    trs = list(d('table tr').items())
    
    # 去除標頭行（分析結果 1.）
    trs = trs[1:]

    for tr in trs:
        tds = list(tr('td').items())
        
        code = tds[1].text().strip()

        if code != '':
            sort = tds[1].text().strip()

            name = tds[2].text().strip()

            percent = tds[3].text().strip()

            proportions.append(Propotion(
                sort=sort,
                code=code,
                name=name,
                percent=percent

            ))


        #loguru.logger.info(code)
        proportions.sort(key=lambda proportion: proportion.Code)
        #loguru.logger.info(proportions)
        
        message = os.linesep.join([str(proportion) for proportion in proportions])
        loguru.logger.info('PROPORTIONS' + os.linesep + message)

if __name__ == '__main__':
    STARTED_TIME_STR = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    loguru.logger.add(
        f"log/{STARTED_TIME_STR}.log",
        rotation='1 day',
        retention='7 days',
        level='DEBUG'
    )
    main()