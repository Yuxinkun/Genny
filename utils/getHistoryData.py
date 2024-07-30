import tushare as ts
import numpy as np
import time
def getHistoryData(t):
    pro = ts.pro_api('5e32fc5444690de433fdab31c3b5f479f6b2f74083c9186299f0b8fe')
    strt = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    strt = strt.split("-")

    df = pro.daily(ts_code=t, start_date='20190101', end_date=strt[0] + strt[1] + strt[2])
    print(df)

    res = np.array(df)
    res = res[:,[1,2,5,4,3]]#日期，开盘，最高，最低,收盘
    res = res.tolist()


    return res
print(getHistoryData("000001.SZ"))

# print(getHistoryData("000002.SH"))
