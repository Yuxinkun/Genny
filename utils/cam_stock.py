import tushare as ts
from tradingSystem.models import StockInfo
from random import randint, random, choice

my_token = '5e32fc5444690de433fdab31c3b5f479f6b2f74083c9186299f0b8fe'

pro = ts.pro_api(my_token)
# data = pro.stock_basic(exchange='', list_status='L', fileds='ts_code,symbol,name,area,industry,list_date')
data = pro.query('stock_basic', exchange='', list_status='L',
                 fileds='ts_code,symbol,name,area,industry,list_date,market')

cnt = 0

for row in data.iterrows():
    # try:
    exchange = ""
    ts_code = row[1]['ts_code']
    if row[1]['ts_code'].find('SH'):
        exchange = "上证"
    else:
        exchange = "深证"
    close_y = randint(5, 200)
    extend = choice([0.1, -0.1, 0.05, -0.05]) * random()
    open_t = close_y + close_y * extend
    stock = StockInfo(
        stock_id=row[1]['symbol'],
        stock_name=row[1]['name'],
        block=row[1]['market'],
        issuance_time=row[1]['list_date'],
        stock_type=exchange,
        closing_price_y=close_y,
        open_price_t=open_t,
        change_extent=extend
    )
    stock.save()
    cnt += 1
    print(cnt)
    # except Exception:
    #     print(Exception)

for row in data.iterrows():
    try:
        stock = StockInfo(
            stock_id=row[1]['symbol'],
            stock_name=row[1]['name'],
            stock_type=row[1]['market']
        )
        stock.save()
        cnt += 1
        print(cnt)
    except Exception:
        print(Exception)

for row in data.iterrows():
    exchange = ""
    ts_code = row[1]['ts_code']
    if row[1]['ts_code'].find('SH'):
        exchange = "上证"
    else:
        exchange = "深证"
    stock_id = row[1]['symbol']
    stock_name = row[1]['name']
    stock_type = row[1]['market']
    # stock = StockInfo.objects.get(stock_id=stock_id)
    print(stock_id, stock_name, ts_code, stock_type, exchange)
    # stock.stock_type = exchange
    # stock.block = stock_type


def main():
    # print(ts.get_today_all())
    df = ts.get_realtime_quotes('000581')  # Single stock symbol
    # data = pro.stock_basic(exchange='', list_status='L', fileds='ts_code,symbol,name,area,industry,list_date')
    data = pro.query('stock_basic', exchange='', list_status='L', fileds='ts_code,symbol,name,area,industry,list_data')

    for ts_code, symbol, name, area, industry, list_data in data['ts_code'], data['symbol'], data['name'], data['area'], \
                                                            data['industry'], data['list_data']:
        print(ts_code, symbol, name, area, industry, list_data)
    print(data)


sh_data = pro.query('stock_basic', exchange='SSE', list_status='L',
                 fileds='ts_code,symbol,name,area,industry,list_date,market')

sz_data = pro.query('stock_basic', exchange='SZSE', list_status='L',
                 fileds='ts_code,symbol,name,area,industry,list_date,market')

cnt = 0
for row in sh_data.iterrows():
    exchange = ""
    ts_code = row[1]['ts_code']
    if row[1]['ts_code'].find('SH') == -1:
        exchange = "深证"
    else:
        exchange = "上证"
    stock_id = row[1]['symbol']
    stock_name = row[1]['name']
    stock_type = row[1]['market']
    try:
        stock = StockInfo.objects.get(stock_id=stock_id)
        stock.stock_type='上证'
        stock.block = stock_type
        stock.save()
        cnt += 1
        print(cnt)
    except Exception:
        print(Exception)
    # stock = StockInfo.objects.get(stock_id=stock_id)
    # print(stock_id, stock_name, ts_code, stock_type, exchange)

cnt = 0
for row in sz_data.iterrows():
    exchange = ""
    ts_code = row[1]['ts_code']
    if row[1]['ts_code'].find('SH') == -1:
        exchange = "深证"
    else:
        exchange = "上证"
    stock_id = row[1]['symbol']
    stock_name = row[1]['name']
    stock_type = row[1]['market']
    try:
        stock = StockInfo.objects.get(stock_id=stock_id)
        stock.stock_type='深证'
        stock.block = stock_type
        stock.save()
        cnt += 1
        print(cnt)
    except Exception:
        print(Exception)


    # print(stock_id, stock_name, ts_code, stock_type, exchange)

if __name__ == '__main__':
    main()
