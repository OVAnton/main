import re
import csv
from pprint import pprint

obj = re.compile(r'(?P<ip>\d+\.\d+\.\d+\.\d+)( - - \[)(?P<datetime>[\s\S]+)......\] '
                 r'\"(?P<metod>[A-Z]+) (?P<request>[\S]*) (?P<protocol>[\S]+)["] (?P<code>\d+) '
                 r'(?P<sendbytes>\d+) ["](?P<refere>[\S]*)["] ["](?P<useragent>[\S]*)([\S\s]+) (?P<ip_d>\d+\.\d+\.\d+\.\d+)')


def load_log(path):
    with open('csv_log.csv', 'w', newline='', encoding="windows-1251") as csv_f:
        writer = csv.writer(csv_f)
        header = ('IP', 'Date', 'Metod', 'Reques', 'Protocol', 'Code', 'Sendbytes', 'User', 'IP_Des')
        writer.writerow(header)
        with open('./nginx.log', mode="r", encoding="utf-8") as log_f:
            for line in log_f:
                line = line.strip()
                try:
                    pars = obj.match(line)
                    data_sample = (pars.group("ip"), pars.group("datetime"), pars.group("metod"), pars.group("request"),
                    pars.group("protocol"), pars.group("code"), pars.group("sendbytes"), pars.group("useragent"), pars.group("ip_d"))
                    writer.writerow(data_sample)
                except:
                    pass

def main():
    load_log("nginx_access.log")

if __name__ == '__main__':
    main()
