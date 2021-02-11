import urllib.request
"""
1300133 --> 1代表深证，0代表上海，300133股票代码
20200523 --> 日期
"""
url = "http://quotes.money.163.com/service/chddata.html?code=1300133&end=20200523&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP"
path = "/study_code/Day_20/download/华策影视2020.csv"
urllib.request.urlretrieve(url, path)
