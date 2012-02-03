from parse_tools import *
import sys
from log_util import *
import log_util

#key: (ip,country), value: frequency
ip_country_dict = {} 

#print sys.argv

#f = open(sys.argv[1],'r')

'''
The plan is to use DirWalker to yield line of log in each file
'''

import sys

w = DirWalker(sys.argv[1], sys.argv[2])
ip_country_dict = {} 
for fields in w:
    if sys.argv[2] == log_util.DB33_34_SWDF:
        (ip, country) = fields['hashIP'], fields['country']
    elif sys.argv[2] == log_util.DB36:
        (ip, country) = fields['ipAddr'], "N/A"
        
    
    if ip_country_dict.has_key((ip, country)):
        ip_country_dict[(ip, country)] += 1
    else:
        ip_country_dict[(ip, country)] = 1

print 'total:', sum(ip_country_dict.values())

for k, v in ip_country_dict.items():
    print k, v

        