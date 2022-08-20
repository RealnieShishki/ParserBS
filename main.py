from bs4 import BeautifulSoup
import requests
import json


def news():
        url = 'https://yandex.ru/news/'

        headers = {'authority': 'yandex.ru',
        'method': 'GET',
        'path': '/news/',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ru,en;q=0.9',
        'cache-control':'max-age=0',
        'cookie': 'news_lang=ru; nc=tips=1645736385060%3Bfavorites-button:1; yandexuid=5009530751608547766; is_gdpr=0; _ym_uid=1608548197632927107; mda=0; gdpr=0; yandex_login=Superstar-ul; font_loaded=YSv1; my=YwA=; yuidss=5009530751608547766; ymex=1950196266.yrts.1634836266; is_gdpr_b=CPnbRhDmUCgC; y360w.xpnd.11057946=0; L=XQBJYQlrU01ybFcFf10ARGcGd2VucWABGjgZDkcnFiARRiMr.1652363122.14975.345713.010780fe5ce63a892b5b1de0b6d3c147; skid=5337375131653237137; _ym_d=1656154643; _ym_isad=2; amcuid=6551666911660503633; i=/UF7uhyLP6P2xSpxRutrh4WQ8DjrWwX9Uyq0hlihJKKnDGfOTimzoQYziuVHp5FRBOWxrbt0yFT3efyTR0VBwUFXclU=; Session_id=3:1660540877.5.0.1610293898848:ko90sA:85.1.2:1|11057946.42069224.2.2:42069224|3:10256781.477015.afzgM6VDnA42KG1aN48vKyp4HM0; sessionid2=3:1660540877.5.0.1610293898848:ko90sA:85.1.2:1.499:1|11057946.42069224.2.2:42069224|3:10256781.568515.Egu0U3VIzc1xbWfcwYxsJzEuThE; sae=0:62D674B4-F10D-4195-856C-FB6BBE3E7BA4:p:22.7.3.822:w:d:RU:20200918; ys=svt.1#def_bro.1#ead.2FECB7CF#wprid.1660565307727169-10453937191763969145-sas3-1045-8f5-sas-l7-balancer-8080-BAL-1476#ybzcc.ru#newsca.native_cache; _yasc=uAW/yU2DmXjL045vfl5y/gXx9CqWLm3g+OxqFd3TlkMgfmI/8Ba0K9N9Sg6stH8kY7Y=; yabs-frequency=/5/5m0c03mt-cBK1EHY/9cwmS9K00005I402/; yp=1660648185.uc.ru#1660648185.duc.ru#1666372267.cld.2360929#1967723122.udn.cDpTdXBlcnN0YXItdWw%3D#1667224590.stltp.serp_bk-map_1_1635688590#1660574385.gpauto.54_265182:48_275146:140:1:1660567185#1661145676.mcv.0#1661145676.mcl.2odd7o#1661145676.szm.1:1920x1080:1920x964; cycada=vvlJDYlhzZFfHA/PqmNdyNslHlEpBx3sof2EZGMuFWQ=',
        'device-memory': '8',
        'downlink': '4.9',
        'dpr': '1',
        'ect': '4g',
        'referer': 'https://www.yandex.ru/clck/jsredir?from=yandex.ru;suggest;browser&text=',
        'rtt': '150',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Yandex";v="22"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "Windows",
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.167 YaBrowser/22.7.3.822 Yowser/2.5 Safari/537.36',
        'viewport-width': '1920'
        }

        response = requests.get(url=url, headers=headers)

        soup = BeautifulSoup(response.text, 'html.parser')

        big_body = soup.find_all('section')

        result = {}
        text = []
        time = []
        agent = []
        for n1 in big_body[0]:
            n2 = n1.find_all('div', class_='mg-card__annotation')
            times = n1.find_all('span', class_='mg-card-source__time')
            agents = n1.find_all('a', class_='mg-card__source-link')
            for n3 in n2:
                text.append(n3.text)
            for t in times:
                time.append(t.text)
            for a in agents:
                agent.append(a.text)

        for i in range(5):
            result[time[i]] = text[i] + ' // ' + agent[i]


        return result

