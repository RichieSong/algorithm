#coding:utf-8
import re
line="""{{nginx}} 172.28.66.186 - - [19/Jun/2018:23:17:51 -0400] GET testloan1.wk.qianbao-inc.com "GET /loan/sms/getImageCode.do?mobile=15311250924&0.20714812065558386 HTTP/1.1" 200 358 0.030 /loan/sms/getImageCode.do?mobile=15311250924&0.20714812065558386 98 "http://testloan1.wk.qianbao-inc.com/cash_loan/views/login.html?rand=0.23136301237305612" "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"  "-" JSESSIONID=- 'upstream_addr: 172.28.137.139:8080' 'ups_resp_time: 0.030' 'request_time: 0.030' upstream_status: 200"""

c=line.split(" ")
i=0
for v in c:
    print(i,v)
    i+=1

import datetime
t1=datetime.datetime.today()
print(t1)
