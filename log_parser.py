import argparse
import os
import re
import json
from collections import defaultdict

parser = argparse.ArgumentParser(description='Process access.log')
parser.add_argument('-f', dest='file', action='store', help='Path to logfile')
args = parser.parse_args()

if os.path.isdir(args.file):
    for i in os.listdir(args.file):
        if i[-4:] != '.log':
            continue

        top_res = []
        top_ip = defaultdict(lambda: 0)
        line_count = defaultdict(
            lambda: {
                "GET": 0,
                "POST": 0,
                "PUT": 0,
                "DELETE": 0,
                "HEAD": 0,
                'CONNECT': 0,
                'OPTIONS': 0,
                'TRACE': 0,
            }
        )
        result_dump = {}

        with open(args.file + i) as file:
            for line in file:
                ip_match = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
                date_gr = re.search(
                    r"\[\d{1,2}/\w{2,3}/\d{4}:\d{1,2}:\d{1,2}:\d{1,2} \+\d{1,4}]", line
                )
                url_gr = re.search(r"\"http[^ ]+\"", line)
                res = line.split(' ')[-1]
                if date_gr is not None:
                    date = date_gr.group()
                if url_gr is not None:
                    url = url_gr.group()
                else:
                    url = '-'
                if ip_match is not None:
                    ip = ip_match.group()
                    method = re.search(
                        r"\] \"(POST|GET|PUT|DELETE|HEAD|CONNECT|OPTIONS|TRACE)", line
                    )
                    if method is not None:
                        line_count[''][method.group(1)] += 1
                        top_ip[ip] += 1
                    if len(top_res) < 3:
                        res_line = {
                            'ip': ip,
                            'date': date,
                            'method': method.group(1),
                            'url': method.group(1),
                            'duration': int(res),
                        }
                        top_res.append(res_line)
                    else:
                        if min(top_res, key=lambda x: x['duration'])['duration'] < int(res):
                            for p in range(len(top_res)):
                                if (
                                    top_res[p]['duration']
                                    == min(top_res, key=lambda x: x['duration'])['duration']
                                ):
                                    del top_res[p]
                                    break
                            res_line = {
                                'ip': ip,
                                'date': date,
                                'method': method.group(1),
                                'url': method.group(1),
                                'duration': int(res),
                            }
                            top_res.append(res_line)
        sorted_ip = sorted(top_ip.items(), key=lambda x: x[1])[-3:]
        print(
            '\nLog Name: ' + i,
            '\nTop 3 IP:',
            *sorted_ip[::-1],
            '\nTop 3 longest response:\n',
            *top_res,
            '\nTotal requests:\n',
            line_count[''],
            '\n',
            sum(line_count[''].values()),
        )
        result_dump = {
            'top_ips': dict(sorted_ip[::-1]),
            'top_longest': list(top_res),
            "total_stat": line_count[''],
            "total_requests": sum(line_count[''].values()),
        }
        with open(f'{i[:-4]}.json', 'w') as outfile:
            json.dump(result_dump, outfile, indent=4)

else:
    top_res = []
    top_ip = defaultdict(lambda: 0)
    line_count = defaultdict(
        lambda: {
            "GET": 0,
            "POST": 0,
            "PUT": 0,
            "DELETE": 0,
            "HEAD": 0,
            'CONNECT': 0,
            'OPTIONS': 0,
            'TRACE': 0,
        }
    )
    result_dump = {}
    with open(args.file) as file:
        for line in file:
            ip_match = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
            date_gr = re.search(
                r"\[\d{1,2}/\w{2,3}/\d{4}:\d{1,2}:\d{1,2}:\d{1,2} \+\d{1,4}]", line
            )
            url_gr = re.search(r"\"http[^ ]+\"", line)
            res = line.split(' ')[-1]
            if date_gr is not None:
                date = date_gr.group()
            if url_gr is not None:
                url = url_gr.group()
            else:
                url = '-'
            if ip_match is not None:
                ip = ip_match.group()
                method = re.search(r"\] \"(POST|GET|PUT|DELETE|HEAD|CONNECT|OPTIONS|TRACE)", line)
                if method is not None:
                    line_count[''][method.group(1)] += 1
                    top_ip[ip] += 1
                if len(top_res) < 3:
                    res_line = {
                        'ip': ip,
                        'date': date,
                        'method': method.group(1),
                        'url': method.group(1),
                        'duration': int(res),
                    }
                    top_res.append(res_line)
                else:
                    if min(top_res, key=lambda x: x['duration'])['duration'] < int(res):
                        for p in range(len(top_res)):
                            if (
                                top_res[p]['duration']
                                == min(top_res, key=lambda x: x['duration'])['duration']
                            ):
                                del top_res[p]
                                break
                        res_line = {
                            'ip': ip,
                            'date': date,
                            'method': method.group(1),
                            'url': method.group(1),
                            'duration': int(res),
                        }
                        top_res.append(res_line)
        sorted_ip = sorted(top_ip.items(), key=lambda x: x[1])[-3:]
        print(
            '\nTop 3 IP:',
            *sorted_ip[::-1],
            '\nTop 3 longest response:\n',
            *top_res,
            '\nTotal requests:\n',
            line_count[''],
            '\n',
            sum(line_count[''].values()),
        )
        result_dump = {
            'top_ips': dict(sorted_ip[::-1]),
            'top_longest': list(top_res),
            "total_stat": line_count[''],
            "total_requests": sum(line_count[''].values()),
        }
        with open(f'data.json', 'w') as outfile:
            json.dump(result_dump, outfile, indent=4)
