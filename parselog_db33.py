from parse_tools import *
import sys
#key: (ip,country), value: frequency
ip_country_dict = {} 

print sys.argv

f = open('dbpedia33_34_swdf.log','r')

'''
The plan is to use DirWalker to yield line of log in each file
'''
for line in f:
#    print "******"
#    print line
#    print "******"
    
    fields = getLogLineBNF_DBpedia33().parseString(line)
    (haship,country) = fields['hashIP'],fields['country']
    if ip_country_dict.has_key((haship, country)):
        ip_country_dict[(haship,country)] += 1
    else:
        ip_country_dict[(haship,country)] = 1

print 'total:',sum(ip_country_dict.values())

for k,v in ip_country_dict.items():
    print k, v
    
    #for k,v in fields.items():
        #print k,":",v
        