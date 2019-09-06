#!/usr/bin/env python2
# -*- conding: UTF-8 -*-
import os
import commands
import re

while 1:
    prompt = "\
        \n#########################\
        \n# Please Input Network! #\
        \n# e.g.  172.28.14.0/24  #\
        \n#########################\
        \n\
        \n                Please: "
    while 1:
        n_net = raw_input(prompt)
        #    n_net_match = re.match('(10|172|192).\d{1,3}.\d{1,3}.0/\d{1,2}', n_net)
        n_net_match = re.match('\d{1,3}.\d{1,3}.\d{1,3}.0/\d{1,2}', n_net)
        if n_net == "":
            print
            "           Format error, e.g. 172.28.14.0/24"
        elif n_net_match == None:
            print
            "           Format error, e.g. 172.28.14.0/24"
        else:
            if n_net[:6] == '10.6.2':
                w_net = '117.121.18.0/24'
            elif n_net[:6] == '10.2.1':
                w_net = '211.154.165.0/24'
            elif n_net[:6] == '10.2.2':
                w_net = '211.154.161.0/24'
            elif n_net[:6] == '10.2.3':
                w_net = '211.154.162.0/24'
            elif n_net[:6] == '10.2.5':
                w_net = '115.182.20.0/24'
            else:
                w_net = 0
            break
    '''
    (rpmstate, rpmoutput) = commands.getstatusoutput("rpm -q nmap")
    if rpmstate != 0:
        commands.getoutput("yum install nmap -y")
    '''

    pattern = re.compile(r'\w{1,3}\.\w{1,3}\.\w{1,3}\.\w{1,3}')


    def split_s(a_list):
        pattern = re.compile(r'\s')
        split_n = pattern.split(a_list)
        return split_n


    def split_point(a_ip):
        pattern = re.compile(r'\.')
        split_ip = pattern.split(a_ip)
        return split_ip


    def total_list(a_net):
        net_len = a_net[:len(a_net) - 4]
        total_list = []
        for i in range(1, 255):
            net_len_i = net_len + str(i)
            total_list.append(net_len_i)
        return total_list


    def available_list(a_net):
        active_list = []
        nmap = os.popen("nmap -n -sP " + a_net)
        nmap_ip = nmap.read()
        nmap.close()
        split_ip = split_s(nmap_ip)
        for i in split_ip:
            match = pattern.match(i)
            if match:
                active_list.append(match.group())
        total_ip_list = total_list(a_net)
        for ip in active_list:
            if ip in total_ip_list:
                total_ip_list.remove(ip)
        return total_ip_list


    n_available_list = available_list(n_net)
    if w_net != 0:
        w_available_list = available_list(w_net)


    def ip_3list(a_net):
        ip_3list = []
        match = re.match('(10|172|192).\d{1,3}.\d{1,3}.0/\d{1,2}', a_net)
        if match == None:
            a_list = w_available_list
        else:
            a_list = n_available_list
        for ip in a_list:
            ip_3 = split_point(ip)[3]
            ip_3list.append(ip_3)
        return ip_3list


    def ip_012(a_net):
        ip_012 = split_point(a_net)[0] + '.' + split_point(a_net)[1] + '.' + split_point(a_net)[2] + '.'
        return ip_012


    if w_net != 0:
        pair_list = []
        w_ip_3list = ip_3list(w_net)
        w_ip_012 = ip_012(w_net)
        for n_ip in n_available_list:
            n_ip_3 = split_point(n_ip)[3]
            if n_ip_3 in w_ip_3list:
                pair_list.append(n_ip + "  <= Pair =>  " + w_ip_012 + n_ip_3)

        pair_6list = []
        for pair_ip in pair_list:
            ip_6 = split_point(pair_ip)[6]
            pair_6list.append(ip_6)

        n_no_pair_list = []
        w_no_pair_list = []
        for nnn in n_available_list:
            nnn3 = split_point(nnn)[3]
            if nnn3 in pair_6list:
                continue
            else:
                n_no_pair_list.append(nnn)
        for www in w_available_list:
            www3 = split_point(www)[3]
            if www3 in pair_6list:
                continue
            else:
                w_no_pair_list.append(www)
        print
        "\n============ Pair IP ============="
        for pip in pair_list:
            print
            pip
        print
        "                                        Summary: %s" % len(pair_list)
        print
        "\n=========== No Pair NIP ==========="
        for nnpip in n_no_pair_list:
            print
            nnpip
        print
        "                  Summary: %s" % len(n_no_pair_list)
        print
        "\n=========== No Pair WIP ==========="
        for wnpip in w_no_pair_list:
            print
            wnpip
        print
        "                  Summary: %s" % len(w_no_pair_list)
        # os.system("pause")
    else:
        for final_n in n_available_list:
            print
            final_n
        print
        "                  Summary: %s" % len(n_available_list)
        # os.system("pause")
