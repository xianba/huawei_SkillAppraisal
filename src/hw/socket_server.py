#-*- coding: utf-8 -*-
"""
说明：考试工程文件，清不要修改该文件
      使用方法请阅读“python考试工程补充说明”
"""

import sys
import socket
import constants
from demo import OlympicsMedalSystem


# 该函数为考试工程函数，用于考生调试使用，请不要修改该程序
def socketServer(callback_fun):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the port
    server_address = ('127.0.0.1', 5555)
    print >>sys.stderr, 'starting up on %s port %s' % server_address
    sock.bind(server_address)
    
    try:
        while True:
            print >>sys.stderr, '\nwaiting to receive message'
            data, addr = sock.recvfrom(4096)

            print >>sys.stderr, "received cmd: %s"%(data)
            
            if data:
                ret = callback_fun(data)
                print >>sys.stderr, ret
                if ret:
                    sock.sendto(ret.encode('utf-8'), addr)

    finally:
        sock.close()


# 格式化错误码
def format_output(error_code):
    return error_code

#格式化国家奖牌榜
def format_country(ret, country_list):
    s = u'\n国家       金牌 银牌 铜牌 排名\n'
    for country in country_list:
        s += '%-10s %-4d %-4d %-4d %d\n' \
             % (country.get('country'),
                country.get('gold'),
                country.get('silver'),
                country.get('bronze'),
                country.get('ranking'))
    return s

Olympics = None

#程序入口，携带入参input_cmd，该参数为字符串类型
def cmd_console(input_cmd):
    args = input_cmd.split()
    cmd = args[0]

    if cmd == "r":
        if len(args) > 1:
            return constants.E001
        return format_output(Olympics.init())
    elif cmd == "i":
        if len(args) != 6:
            return constants.E001
        try:
            time = int(args[1])
            country = str(args[2])
            player = str(args[3])
            subject = int(args[4])
            medal = int(args[5])
        except:
            return constants.E001
        return format_output(Olympics.input_medal_record(time, country, player, subject, medal))
    elif cmd == "c":
        if len(args) != 4:
            return constants.E001
        try:
            time = int(args[1])
            player = str(args[2])
            subject = int(args[3])
        except:
            return constants.E001
        return format_output(Olympics.cancel_medal_record(time, player, subject))
    elif cmd == "qc":
        if len(args) != 1:
            return constants.E001
        ret, info = Olympics.query_country_medal_rankings()
        s = None
        if isinstance(info, list) and ret == constants.S003:
            s = format_country(ret, info)
        else:
            s = format_output(ret)
        return s
    else:
        return format_output(constants.E001)


if __name__ == "__main__":
    Olympics = OlympicsMedalSystem()
    socketServer(cmd_console)
