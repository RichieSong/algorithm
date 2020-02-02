import time
from random import randint, random

method = ["OPTION", "POST", "GET"]
url = [" test.wk.qianbao-inc.com ", " abc.wk.qianbao-inc.com ", " loan1.wk.qianbao-inc.com ",
       " testloan1.wk.qianbao-inc.com "]
uri = ["GET /loan/sms/getImage.do?mobile=15311250924&0.20714812065558386 HTTP/1.1 200 ",
       "GET /loan/sms/abc.do?mobile=15311250924&0.20714812065558386 HTTP/1.1 200 ",
       "GET /loan/songm/getImageCode.do?mobile=15311250924&0.20714812065558386 HTTP/1.1 200 ",
       "GET /loan/bbb/getCode.do?mobile=15311250924&0.20714812065558386 HTTP/1.1 200 "]
log = "/tmp/access1.log"
log1 = "/tmp/access.log"
# print(line)
count = 0
while True:
    line = "{{ngin}} 172.28." \
           + str(randint(66, 255)) \
           + "." \
           + str(randint(66, 255)) \
           + " - - [" \
           + str(randint(19, 30)) \
           + "/Jun/2018:" \
           + str(randint(1, 23)) \
           + ":" \
           + str(randint(10, 59)) \
           + ":51 -0400] " \
           + method[randint(0, 2)] \
           + url[randint(0, 3)] \
           + uri[randint(0, 3)] \
           + str(randint(300, 900)) \
           + " " \
           + str(random()) \
           + " /loan/sms/getImageCode.do?mobile=15311250924&0.20714812065558386 98 " \
           + "http://testloan1.wk.qianbao-inc.com/cash_loan/views/login.html?rand=0.23136301237305612" \
           + " Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1  -" + " JSESSIONID=- 'upstream_addr: 172.28.137.139:8080' 'ups_resp_time: " \
           + str(random()) \
           + "' 'request_time: 0.030' upstream_status: 200"

    with open(log, "a+") as f:
        count += 1
        print(count, line)
        f.write(line + "\n")
        time.sleep(0.5)
    # with open(log1, "a+") as f:
    #     count += 1
    #     print(count, line)
    #     f.write(line + "\n")
    #     time.sleep(0.1)
