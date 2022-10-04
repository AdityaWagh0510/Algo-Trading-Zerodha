from kiteconnect import KiteConnect
from kiteconnect import KiteTicker
from datetime import datetime,timedelta


if __name__=='__main__':

    api_key = "Enter_Api_Key_Here"
    api_secret = "Enter_Api_Secret_Here"
    kite = KiteConnect(api_key=api_key)
    
    access_token=""
    
    now = datetime.now()
    c_date=  now.strftime("%Y-%m-%d")
    f_date=""
    with open('access_token.txt','r') as ak:
        f_date=ak.readline()[0:10]

    if f_date==c_date:
        with open('access_token.txt') as ak:
            access_token=ak.readline()[10:42]
            print(access_token)
    else:
            print(kite.login_url())
            request_toke=input("Enter request token") 
            data = kite.generate_session(request_toke, api_secret=api_secret)          
            with open('access_token.txt','w') as ak:
                ak.write(c_date)
                ak.write(data['access_token'])
                access_token=data['access_token']

    kite.set_access_token(access_token)
