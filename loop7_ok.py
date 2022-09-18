import requests
import os
import os.path
import json

from json_tricks import dump


# a = 0
# b = 1
# c = 10

a = 0
b = 1
c = 10

# https://pse.kominfo.go.id/home/pse-domestik 18 september 2022 = 1028 pages, daftar ke 1 dari 10 total 10273
# 1	MAKE THE MOOVE	ns1.siteground.net	Sektor Perdagangan	BETTER DAYS AHEAD	2022-09-16
# ...
# 10	MEDIA HARIAN GARUT	hariangarut.com	Sektor Teknologi Informasi dan Komunikasi	GARUT DIGITAL MULTIMEDIA	2022-09-15


# jsonfile = 'response_pse_1-250_ok.json'
# jsonfile = 'response_pse_251-500_ok.json'
# jsonfile = 'response_pse_501-750_ok.json'
# jsonfile = 'response_pse_751-1000_ok.json'
# jsonfile = 'response_pse_1001-1028_ok.json'
# jsonfile = 'response_pse_1-1028_ok.json'

# jsonfile = 'response_pse_lokal_dihentikan_sementara1-5_ok.json'
jsonfile = 'response_pse_asing_dihentikan_sementara1-2_ok.json'


if os.path.exists(jsonfile):
    os.remove(jsonfile)
    print("The old file has been deleted successfully")
else:
    print("The old file does not exist!")


# for i in range(3):  
#     print(a)
#     a = a + 1

json_begin = '['
json_end = ']'


# url kominfo
# https://pse.kominfo.go.id/home/pse-domestik
# https://pse.kominfo.go.id/home/pse-asing

# https://pse.kominfo.go.id/static/json-static/LOKAL_TERDAFTAR/0.json?page[page]=1&page[limit]=10&filter[search_term]=
# https://pse.kominfo.go.id/static/json-static/LOKAL_DIHENTIKAN_SEMENTARA/0.json?page[page]=1&page[limit]=10&filter[search_term]=
# https://pse.kominfo.go.id/static/json-static/LOKAL_DICABUT/0.json?page[page]=1&page[limit]=10&filter[search_term]=

# https://pse.kominfo.go.id/static/json-static/ASING_TERDAFTAR/0.json?page[page]=1&page[limit]=10&filter[search_term]=
# https://pse.kominfo.go.id/static/json-static/ASING_DIHENTIKAN_SEMENTARA/0.json?page[page]=1&page[limit]=10&filter[search_term]=
# https://pse.kominfo.go.id/static/json-static/ASING_DICABUT/0.json?page[page]=1&page[limit]=10&filter[search_term]=

# https://pse.kominfo.go.id/static/json-static/LOKAL_TERDAFTAR/{}.json?page[page]={}&page[limit]={}&filter[search_term]=


with open(jsonfile, 'a') as outfile:
    outfile.write(json_begin)

    # for j in range(253):  
    for j in range(2):  
        # url = 'https://pse.kominfo.go.id/static/json-static/LOKAL_TERDAFTAR/{}.json?page[page]={}&page[limit]={}&filter[search_term]='.format(a,b,c)
        # url = 'https://pse.kominfo.go.id/static/json-static/LOKAL_DIHENTIKAN_SEMENTARA/{}.json?page[page]={}&page[limit]={}&filter[search_term]='.format(a,b,c)
        # url = 'https://pse.kominfo.go.id/static/json-static/LOKAL_DICABUT/{}.json?page[page]={}&page[limit]={}&filter[search_term]='.format(a,b,c)

        # url = 'https://pse.kominfo.go.id/static/json-static/ASING_TERDAFTAR/{}.json?page[page]={}&page[limit]={}&filter[search_term]='.format(a,b,c)
        url = 'https://pse.kominfo.go.id/static/json-static/ASING_DIHENTIKAN_SEMENTARA/{}.json?page[page]={}&page[limit]={}&filter[search_term]='.format(a,b,c)
        # url = 'https://pse.kominfo.go.id/static/json-static/ASING_DICABUT/{}.json?page[page]={}&page[limit]={}&filter[search_term]='.format(a,b,c)
        

        cookies = {
            '_5ec80': 'http://10.0.2.107:80',
            'TS019ac7c3': '016b270e6f886bc637c4a4d6f89b7dbb07afaaf49e4992d0159c8a88c7b0dc70bc556f0d57bf998b02a43ba73d349090a5fb22b2f22fdd44a81a3883e099ed500c42b658ad',
        }

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'en-US,en;q=0.9,id;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            # Requests sorts cookies= alphabetically
            # 'Cookie': '_5ec80=http://10.0.2.107:80; TS019ac7c3=016b270e6f886bc637c4a4d6f89b7dbb07afaaf49e4992d0159c8a88c7b0dc70bc556f0d57bf998b02a43ba73d349090a5fb22b2f22fdd44a81a3883e099ed500c42b658ad',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
        }

        response = requests.get(url, cookies=cookies, headers=headers)

        jr = response.json()
        # print(jr)

        # with open('response2.json','w') as responseFile:
        #     dump(jr,responseFile)
        
        # with open('response1-3.json','a') as responseFile:
        #     dump(jr,responseFile)   
                
        files = os.listdir(os.curdir)       

        # for f in files:

            # extension = os.path.splitext(f)[1][1:]
            # base = os.path.splitext(f)[0]
            # name = f

            # data = {
            #     "file_name" : name,
            #     "extension" : extension,
            #     "base_name" : base
            # }

        json.dump(jr, outfile)        
        outfile.write(',')        
           
        
        # print(url)
        a = a + 1
        b = b + 1

    # delete (',') in the end of for loop
    outfile.seek(outfile.tell() - 1, os.SEEK_SET)
    outfile.truncate()
    
    outfile.write(json_end)


