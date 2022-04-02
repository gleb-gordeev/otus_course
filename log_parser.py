import argparse
import os
import re
import json
from collections import defaultdict

parser = argparse.ArgumentParser(description='Process access.log')
parser.add_argument('-f', dest='file', action='store', help='Path to logfile')
args = parser.parse_args()
dict_ip = defaultdict(
    lambda: {
        "GET": 0,
        "POST": 0,
        "PUT": 0,
        "DELETE": 0,
        "HEAD": 0,
        'CONNECT': 0,
        'OPTIONS': 0,
        'TRACE': 0,
    })
top_res = {}
top_ip = defaultdict(lambda: 0)

if os.path.isdir(args.file):
    for i in os.listdir(args.file):
        if i[-4:] != '.log':
            continue
        with open(args.file + i) as file:
            line_count = 0
            for line in file:
                ip_match = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
                date_gr = re.search(r"\[\d{1,2}/\w{2,3}/\d{4}:\d{1,2}:\d{1,2}:\d{1,2} \+\d{1,4}]", line)
                url_gr = re.search(r"\"http[^ ]+\"", line)
                res = line.split(' ')[-1]
                if date_gr is not None:
                    date = date_gr.group()
                if url_gr is not None:
                    url = url_gr.group()
                else:
                    url = ''
                if ip_match is not None:
                    ip = ip_match.group()
                    method = re.search(
                        r"\] \"(POST|GET|PUT|DELETE|HEAD|CONNECT|OPTIONS|TRACE)", line
                    )
                    if method is not None:
                        line_count += 1
                        dict_ip[ip][method.group(1)] += 1
                        top_ip[ip] += 1
                    if len(top_res) < 3:
                        top_res[ip + date + url + method.group(1) + res] = int(res)
                    else:
                        if min(top_res.values()) < int(res):
                            top_res.pop(min(top_res, key=top_res.get))
                            top_res[ip + ' ' + date + ' ' + url + ' ' + method.group(1) + ' ' + res] = int(res)
        sorted_ip = sorted(top_ip.items(), key=lambda x: x[1])[-3:]
        print(
            json.dumps(dict_ip, indent=4),
            '\nLog Name: ' + i,
            '\nTop 3 Slowed response:\n', *top_res.keys(),
            '\nTop 3 IP:', *sorted_ip[::-1],
            '\nTotal lines:', line_count)
        with open(f'{i}.json', 'w') as outfile:
            json.dump(dict_ip, outfile)
else:
    with open(args.file) as file:
        line_count = 0
        for line in file:
            ip_match = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
            date_gr = re.search(
                r"\[\d{1,2}/\w{2,3}/\d{4}:\d{1,2}:\d{1,2}:\d{1,2} \+\d{1,4}]", line)
            url_gr = re.search(r"\"http[^ ]+\"", line)
            res = line.split(' ')[-1]
            if date_gr is not None:
                date = date_gr.group()
            if url_gr is not None:
                url = url_gr.group()
            else:
                url = ''
            if ip_match is not None:
                ip = ip_match.group()
                method = re.search(r"\] \"(POST|GET|PUT|DELETE|HEAD|CONNECT|OPTIONS|TRACE)", line)
                if method is not None:
                    line_count += 1
                    dict_ip[ip][method.group(1)] += 1
                    top_ip[ip] += 1
                if len(top_res) < 3:
                    top_res[ip + date + url + method.group(1) + res] = int(res)
                else:
                    if min(top_res.values()) < int(res):
                        top_res.pop(min(top_res, key=top_res.get))
                        top_res[ip + ' ' + date + ' ' + url + ' ' + method.group(1) + ' ' + res] = int(res)
        sorted_ip = sorted(top_ip.items(), key=lambda x: x[1])[-3:]
        print(
            json.dumps(dict_ip, indent=4),
            '\nTop 3 Slowed response:\n', *top_res.keys(),
            '\nTop 3 IP:', *sorted_ip[::-1],
            '\nTotal lines:', line_count)
        with open('data1.json', 'w') as outfile:
            json.dump(dict_ip, outfile)
