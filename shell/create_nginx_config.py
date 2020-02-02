# coding:utf-8
import os

from jinja2 import Template

source_file = "./source.txt"
des_path = "/apps/soft/nginx/conf.d/vhost/"
upstream_path = "/apps/soft/nginx/conf.d/upstream/"
# upstream_path = "/"
upstream_name_prefix = ""
ns = ""
nsswitch = {
    "dev1": "qb-dev-1",
    "pms": "qb-dev-1",
    "dev2": "qb-dev-2",
    "dev3": "qb-dev-3",
    "dev4": "qb-dev-4",
    "dev5": "qb-dev-5",
    "dev6": "qb-dev-6",
    "sit1": "qb-qa-1",
    "sit2": "qb-qa-2",
    "sit3": "qb-qa-3",
    "sit4": "qb-qa-4",
    "sit5": "qb-qa-5",
    "sit6": "qb-qa-6",
}
ciphers = {
    "qianbaocard.com": 'ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-DSS-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-DSS-AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA:DHE-RSA-AES256-SHA:AES128-GCM-SHA256:AES256-GCM-SHA384:AES128:AES256:AES:DES-CBC3-SHA:HIGH:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!MD5:!PSK'

}


def parse_source_file():
    with open(source_file, 'r') as f:
        for line in f:
            if line.strip().endswith(".com"):
                domain = line.strip()
                ns = nsswitch.get(domain.split(".")[0].split("-")[-1])
                dirname = ".".join(line.strip().split(".")[-2:])
                fileDir = des_path + dirname
                upstream_pool_name = upstream_name_prefix + "_pool_" + ns
                project_name = upstream_name_prefix
                # 判断upstream是否有pool name
                create_upstream_file(domain, ns, upstream_pool_name, project_name)

                create_nginx_file(domain, fileDir, upstream_pool_name, dirname)

            else:
                upstream_name_prefix = line.strip()


def create_upstream_file(domain, ns, poolname, projectname):
    upstream_sour_file = upstream_path + projectname + "_upstream_" + ns + ".conf"
    upstream_file = upstream_path + projectname + "_upstream_" + ns + ".conf"
    if not os.path.isfile(upstream_file) and not os.path.isfile(upstream_sour_file):
        upstream_data = '''
upstream  {{poolname}}  { 
    server test.qianbao-inc.com;
}
        '''
        data = {
            "poolname": poolname
        }
        temp = Template(upstream_data)
        config_data = temp.render(data)
        # print(config_data)
        # print(upstream_sour_file)

        with open(upstream_file, "w") as f:
            f.write(config_data)
            print("Write success  upstream for %s" % upstream_file)
    else:
        print("%s is exists" % upstream_file)


def create_nginx_file(domain, filedir, poolName, dirname):
    nginx_file = filedir + "/" + domain + ".conf"
    if os.path.exists(filedir) and not os.path.isfile(nginx_file):

        file_data = '''
server {
    listen 80;
    listen 443;
    server_name {{ domain }};
    access_log /apps/logs/nginx/{{ domain }}-access.log main;
    error_log /apps/logs/nginx/{{ domain }}-error.log;

    ssl          on;
    ssl_certificate     /apps/soft/nginx/conf.d/cert/{{ dirname }}.pem;
    ssl_certificate_key /apps/soft/nginx/conf.d/cert/{{ dirname }}.key;
    ssl_session_timeout  5m;
    ssl_protocols SSLv3 TLSv1 TLSv1.1 TLSv1.2;
    ssl_ciphers {{ ciphers }};
    ssl_prefer_server_ciphers   on;

    set $remote_address "$proxy_add_x_forwarded_for";
    if ( $proxy_add_x_forwarded_for ~ "(.*)\,.*" ) {
        set $remote_address "$1";
    }
    location / {
        proxy_next_upstream http_502 http_504 error timeout invalid_header;
        index index.jsp index.htm index.html;
        proxy_pass http://{{ poolname }};
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $remote_address;
    }
}
        
        
        '''
        data = {
            "domain": domain,
            "dirname": dirname,
            "poolname": poolName,
            "ciphers": ciphers.get(dirname)
        }
        temp = Template(file_data)
        config_data = temp.render(data)
        # print(config_data)
        # print(nginx_file)
        with open(nginx_file, "w") as f:
            f.write(config_data)
            print("Write success for %s" % nginx_file)
    else:
        print("%s not exist！or %s is exists" % (filedir, nginx_file))


if __name__ == '__main__':
    parse_source_file()
