#!/usr/bin/env python
# coding: utf-8

# In[5]:


try:
    import logging
    from netapp_ontap import HostConnection, NetAppRestError, config, utils
    from netapp_ontap.resources import Volume
    import webbrowser
    import requests#pulling web request with bs4
    import json#reads/exports json
    import string
    import getpass#Password hide
    import openpyxl#excel edit
    import logging
    from netapp_ontap import HostConnection, NetAppRestError, config, utils
    from netapp_ontap.resources import Volume
    
except:
    insta=input ("You are currently missing 1 or more packages. Type yes to install all missing packages on this machine or no to exit the script\n")
    if insta=="yes" or insta=="Yes" or insta=="install":
        import pip
        pip.main(['install', 'netapp_ontap'])
        pip.main(['install', 'requests'])
        pip.main(['install', 'netapp_ontap.resources'])
        pip.main(['install', 'webbrowser'])
        pip.main(['install', 'requests'])
        pip.main(['install', 'json'])
        pip.main(['install', 'string'])
        pip.main(['install', 'getpass'])

        import webbrowser
        import requests#pulling web request with bs4
        import json#reads/exports json
        import string
        import getpass#Password hide
        import openpyxl#excel edit
        import logging
        from netapp_ontap import HostConnection, NetAppRestError, config, utils
        from netapp_ontap.resources import Volume
    else:
        print("Closing program")
        os._exit(1)
        
        
        
logging.basicConfig(level=logging.DEBUG)
config.CONNECTION = HostConnection('aiqum.demo.netapp.com/api/management-server/events', username='admin', password='Netapp1!', verify=False)

# Set the DEBUG flag to 1
utils.DEBUG = 1

# this API call will fail with a 404
try:
    volume = Volume(uuid="1", name='does_not_exist')
    volume.get()
except NetAppRestError:
    print('We got an expected exception')


# In[ ]:




