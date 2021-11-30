#!/usr/bin/env python
# coding: utf-8

# In[20]:


import base64
import argparse
from getpass import getpass
import logging
import requests
import json
import texttable as tt
import urllib3 as ur
ur.disable_warnings()

def get_method_call():
    cluster= "aiqum.demo.netapp.com"
    
    """Get particular no of events"""
    url = "https://10.216.51.73/api/management-server/events"
    print(url)
    response = requests.get(url, verify=False)
    
    return response.json()


if __name__ == "__main__":
    logging.basicConfig(
    level=logging.INFO,
     format="[%(asctime)s] [%(levelname)5s] [%(module)s:%(lineno)s] %(message)s",
     )
    ARGS = parse_args()
    base64string = base64.encodestring(
     ('%s:%s' %
     (ARGS.api_user, ARGS.api_pass)).encode()).decode().replace('\n', '')
    headers = {
     'authorization': "Basic %s" % base64string,
     'content-type': "application/json",
     'accept': "application/json"
     }
    disp_vol(ARGS.cluster, ARGS.svm_name, headers)


#post a file multipart form data


# In[ ]:





# In[ ]:




