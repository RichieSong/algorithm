# coding:utf-8
import requests

# 项目名  域名前缀
projects = {

    "bizaccount_cbiz_endday": "cbiz-endday",
    "bizaccount_biz_endday": "biz-endday",
    "biz_quartz_job": "biz-quartz",
    "bizaccount_interface": "bizapi",
    "qbauth_qbcard_auth": "pms",
    "sharding_admin_sfzf": "sharding-admin-sfzf",
    "bizaccount_cbiz_quartz_job": "cbiz-quartz"

}
ns = [
    "qb-dev-1",
    "qb-dev-2",
    "qb-dev-3",
    "qb-dev-4",
    "qb-dev-5",
    "qb-dev-6",
    "qb-qa-1",
    "qb-qa-2",
    "qb-qa-3",
    "qb-qa-4",
    "qb-qa-5",
    "qb-qa-6",
]


def req():
    for k, v in projects.items():
        for n in ns:
            data = {
                "domainPrefix": v,
                "firstDomain": "qianbaocard.com",
                "projectName": k,
                "nameSpace": n,
                "locPath": "/"
            }
            ret = requests.post(url="http://nginx-dev.qianbao-inc.com/nginx/api/addvhost", json=data)
            if ret.status_code != 200:
                print(ret.json())
            else:
                print(ret.json())


if __name__ == '__main__':
    req()
