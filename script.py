#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import requests
import re
import json
# import urllib
# import urllib2

################################################################################
## Latency (<service>_time)
## Dependencies API vs Services (<service>_status)

################################################################################
## Prioridades       ## Prioridades
# 1000 = 1           # 1= leve
# 1500 = Regular     # 2= moderado
# thrd_bad = Ruim    # 3= grave

################################################################################
### Prioridades VS services

### + Ticket
# api_ticket_hbase=3
# api_ticket_nifi=3
# api_ticket_inventi=3
# api_ticket_tibco=3
# api_ticket_hive=2
# api_ticket_srv4=2
# api_ticket_srv5=2

### + Stock
# api_stock_hbase=3
# api_stock_nifi=3
# api_stock_inventi=3
# api_stock_tibco=3
# api_stock_hive=2
# api_stock_gold=2

### + History
# api_history_hbase=3
# api_history_nifi=3
# api_history_inventi=3
# api_history_tibco=3
# api_history_hive=2
# api_history_srv4=2
# api_history_srv5=2
################################################################################

thrd_good = 1000
thrd_regular = 1500
thrd_bad = 2000

# ## ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ## hbase_url
hbase_url = 'https://api.biggylabs.com/v2/heartbeat/hbase'
hbase_request_content = requests.get(hbase_url).content
hbase_time = re.search(r'\d{1,5}\.?\d{0,5}', hbase_request_content, re.I)
hbase_time = int(hbase_time.group())
print hbase_time
if ( hbase_time < thrd_good ):
    hbase_status = 1
    print hbase_status
elif ( hbase_time > thrd_good ) and ( hbase_time > thrd_bad ):
    hbase_status = 2
    print hbase_status
else:
    hbase_status = 3
    print hbase_status

# ## ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ## nifi
nifi_url = 'https://api.biggylabs.com/v2/heartbeat/hbase'
nifi_request_content = requests.get(nifi_url).content
nifi_time = re.search(r'\d{1,5}\.?\d{0,5}', nifi_request_content, re.I)
nifi_time = int(nifi_time.group())
print nifi_time
if ( nifi_time < thrd_good ):
    nifi_status = 1
    print nifi_status
elif ( nifi_time > thrd_good ) and ( nifi_time > thrd_bad ):
    nifi_status = 2
    print nifi_status
else:
    nifi_status = 3
    print nifi_status

# ## ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ## inventi
inventi_url = 'https://api.biggylabs.com/v2/heartbeat/hbase'
inventi_request_content = requests.get(inventi_url).content
inventi_time = re.search(r'\d{1,5}\.?\d{0,5}', inventi_request_content, re.I)
inventi_time = int(inventi_time.group())
print inventi_time
if ( inventi_time < thrd_good ):
    inventi_status = 1
    print inventi_status
elif ( inventi_time > thrd_good ) and ( inventi_time > thrd_bad ):
    inventi_status = 3
    print inventi_status
else:
    inventi_status = 3
    print inventi_status

# ## ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ## tibco
tibco_url = 'https://api.biggylabs.com/v2/heartbeat/hbase'
tibco_request_content = requests.get(tibco_url).content
tibco_time = re.search(r'\d{1,5}\.?\d{0,5}', tibco_request_content, re.I)
tibco_time = int(tibco_time.group())
print tibco_time
if ( tibco_time < thrd_good ):
    tibco_status = 1
    print tibco_status
elif ( tibco_time > thrd_good ) and ( tibco_time > thrd_bad ):
    tibco_status = 2
    print tibco_status
else:
    tibco_status = 3
    print tibco_status

# ## ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ## hive
hive_url = 'https://api.biggylabs.com/v2/heartbeat/hbase'
hive_request_content = requests.get(hive_url).content
hive_time = re.search(r'\d{1,5}\.?\d{0,5}', hive_request_content, re.I)
hive_time = int(hive_time.group())
print hive_time
if ( hive_time < thrd_good ):
    hive_status = 1
    print hive_status
elif ( hive_time > thrd_good ) and ( hive_time > thrd_bad ):
    hive_status = 2
    print hive_status
else:
    hive_status = 3
    print hive_status

# ## ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ## gold
gold_url = 'https://api.biggylabs.com/v2/heartbeat/hbase'
gold_request_content = requests.get(gold_url).content
gold_time = re.search(r'\d{1,5}\.?\d{0,5}', gold_request_content, re.I)
gold_time = int(gold_time.group())
print gold_time
if ( gold_time < thrd_good ):
    gold_status = 1
    print gold_status
elif ( gold_time > thrd_good ) and ( gold_time > thrd_bad ):
    gold_status = 2
    print gold_status
else:
    gold_status = 3
    print gold_status

# ## ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ## srv4
srv4_url = 'https://api.biggylabs.com/v2/heartbeat/hbase'
srv4_request_content = requests.get(srv4_url).content
srv4_time = re.search(r'\d{1,5}\.?\d{0,5}', srv4_request_content, re.I)
srv4_time = int(srv4_time.group())
print srv4_time
if ( srv4_time < thrd_good ):
    srv4_status = 1
    print srv4_status
elif ( srv4_time > thrd_good ) and ( srv4_time > thrd_bad ):
    srv4_status = 2
    print srv4_status
else:
    srv4_status = 3
    print srv4_status

# ## ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ## srv5
srv5_url = 'https://api.biggylabs.com/v2/heartbeat/hbase'
srv5_request_content = requests.get(srv5_url).content
srv5_time = re.search(r'\d{1,5}\.?\d{0,5}', srv5_request_content, re.I)
srv5_time = int(srv5_time.group())
print srv5_time
if ( srv5_time < thrd_good ):
    srv5_status = 1
    print srv5_status
elif ( srv5_time > thrd_good ) and ( srv5_time > thrd_bad ):
    srv5_status = 2
    print srv5_status
else:
    srv5_status = 3
    print srv5_status

# ## ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ## history
def history():
    if ( hbase_time > thrd_bad ) or ( nifi_time > thrd_bad  ) or ( inventi_time > thrd_bad  ) or ( tibco_time > thrd_bad  ):
        status_history = 3
        return status_history
        print "Api sale-history aprensenta instabilidade de nivel:", status_history

    elif ( hbase_time >= thrd_regular ) or ( nifi_time >= thrd_regular ) or ( inventi_time >= thrd_regular ) or ( tibco_time >= thrd_regular ):
        status_history = 2
        return status_history
        print "Api sale-history aprensenta instabilidade de nivel:", status_history

    elif ( hive_time >= thrd_regular ) or ( srv4_time >= thrd_regular ) or ( srv5_time >= thrd_regular ):
        status_history = 2
        return status_history
        print "Api sale-history aprensenta instabilidade de nivel:", status_history

    else:
        status_history = 1
        return status_history
        print "Api sale-history com status OK. Status:", status_history

# ## ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ## stock
def stock():
    if ( hbase_time > thrd_bad ) or ( nifi_time > thrd_bad ) or ( inventi_time > thrd_bad ) or ( tibco_time > thrd_bad ):
        status_stock = 3
        return status_stock
        print "Api sale-stock aprensenta instabilidade de nivel:", status_stock

    elif ( hbase_time >= thrd_regular ) or ( nifi_time >= thrd_regular ) or ( inventi_time >= thrd_regular ) or ( tibco_time >= thrd_regular ):
        status_stock = 2
        return status_stock
        print "Api sale-stock aprensenta instabilidade de nivel:", status_stock

    elif ( hive_time >= thrd_regular  ) or ( gold_time >= thrd_regular ):
        status_stock = 2
        return status_stock
        print "Api sale-stock aprensenta instabilidade de nivel:", status_stock

    else:
        status_stock = 1
        return status_stock
        print "Api sale-stock com status OK. Status:", status_stock

# ## ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ## ticket
def ticket():
    if ( hbase_time > thrd_bad ) or ( nifi_time > thrd_bad ) or ( inventi_time > thrd_bad ) or ( tibco_time > thrd_bad ):
        status_ticket = 3
        return status_ticket
        print "Api sale-ticket aprensenta instabilidade de nivel:", status_ticket

    elif ( hbase_time >= thrd_regular  ) or ( nifi_time >= thrd_regular  ) or ( inventi_time >= thrd_regular  ) or ( tibco_time >= thrd_regular  ):
        status_ticket = 2
        return status_ticket
        print "Api sale-ticket aprensenta instabilidade de nivel:", status_ticket

    elif ( hive_time >= thrd_regular  ) or ( srv4_time >= thrd_regular  ) or ( srv5_time >= thrd_regular  ):
        status_ticket = 2
        return status_ticket
        print "Api sale-ticket aprensenta instabilidade de nivel:", status_ticket

    else:
        status_ticket = 1
        return status_ticket
        print "Api sale-ticket com status OK. Status:", status_ticket


# request post http://elasticsearch/status_apis/ -d json_status

# url = "http://localhost:9200/dolphin_api_log/status"
def post():
    json_status = "{"+\
    "'date':"+ str(1515778632) +","+\
    "'hbase_time':"+ str(hbase_time) +","+\
    "'hbase_status':"+ str(hbase_status) +","+\
    "'nifi_time':"+ str(nifi_time) +","+\
    "'nifi_status':"+ str(nifi_status) +","+\
    "'hive_time':"+ str(hive_time) +","+\
    "'hive_status':"+ str(hive_status) +","+\
    "'gold_time':"+ str(gold_time) +","+\
    "'gold_status':"+ str(gold_status) +","+\
    "'tibco_time':"+ str(tibco_time) +","+\
    "'tibco_status':"+ str(tibco_status) +","+\
    "'srv4_time':"+ str(srv4_time) +","+\
    "'srv4_status':"+ str(srv4_status) +","+\
    "'srv5_time':"+ str(srv5_time) +","+\
    "'srv5_status':"+ str(srv5_status) +","+\
    "'store_status':"+ str(0) +","+\
    "'product-catalog_status':"+ str(0) +","+\
    "'product-where-to-buy_status':"+ str(0) +","+\
    "'price_status':"+ str(0) +","+\
    "'sale-integration_status':"+ str(0) +","+\
    "'marketing-structure_status':"+ str(0) +","+\
    "'supplier_status':"+ str(0) +","+\
    "'pgc-patrol_status':"+ str(0) +","+\
    "'fiscal-xml-list_status':"+ str(0) +","+\
    "'fiscal-xml-consult_status':"+ str(0) +","+\
    "'sale-integration-sumary_status':"+ str(0) +","+\
    "'sale-ticket_status':"+ str(ticket()) + \
    "}"
    response = requests.post("http://localhost:9200/capa/folha/dado", json=json_status)
    print response

def main():
    history()
    ticket()
    stock()
    post()

main()

