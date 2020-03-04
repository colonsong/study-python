import datetime

import loguru
import requests

def main():
    # 下載加權指數成分股暨市值比重資料網頁
    resp = requests.get('https://www.taifex.com.tw/cht/9/futuresQADetail')
    # 從 HTTP / HTTPS 回應狀態碼判斷是否下載成功
    if resp.status_code != 200:
        loguru.logger.error('RESP: status code is not 200')
    # 執行到這裡，resp 裡存放的就是 HTTPS 回應，裡面包含回應的標頭和內容主體等資訊
    loguru.logger.success('RESP: success')

if __name__ == '__main__':
    loguru.logger.add(
        f'{datetime.date.today():%Y%m%d}.log',
        rotation='1 day',
        retention='7 days',
        level='DEBUG'
    )
    main()