#!/usr/bin/env python
# coding: utf-8

# # Makefile generator for chirpstack platform 

# In[95]:


from pathlib import Path
import os
import datetime


# In[109]:


# Variables

destination = "Afnic"
root = destination + "-" + str(datetime.datetime.now()).split(" ")[0] + "-certificates/"

net_id = "000000"

app_server_ip = "51.91.79.176"
join_server_ip = app_server_ip
net_server_ip = "51.178.80.199"

app_server_hosts = ["127.0.0.1","localhost", app_server_ip]
join_server_hosts = app_server_hosts.copy()
net_server_hosts = ["127.0.0.1","localhost", net_server_ip]
roaming_server_hosts = net_server_hosts.copy()
# Appending join server domains

join_server_domains = []

for i in join_server_domains:
    join_server_hosts.append(i)
    
roaming_server_domain = net_id+".netid.iotreg.net"
roaming_server_hosts.append(roaming_server_domain)


# In[110]:


def list_to_string(list):
    return_string = "["
    for i in list:
        return_string += "\""
        return_string += i
        return_string += "\""
        return_string += ","
    return return_string[:-1]+"]"


# In[111]:


# Creating system folders

Path("certificates/config").mkdir(parents=True, exist_ok=True) 
Path("certificates/certs").mkdir(parents=True, exist_ok=True) 


# In[112]:


# Generating Application Server - Server Certificate
Path(root+"config/application-server/api/server").mkdir(parents=True, exist_ok=True) 

filename = root+"config/application-server/api/server/certificate.json"
file_content ='{\n\t"CN" : "TSP-Application-Server",\n\t"host": '+ list_to_string(app_server_hosts) + ',\n\t"key": {\n\t\t"algo": "rsa",\n\t\t"size": 2048\n\t}\n}'

app_server_file = open(filename, 'w')
app_server_file.write(file_content)
app_server_file.close()

print("Written : \n" + file_content + "\n to \n" + filename)


# In[113]:


# Generating Application Server - Client Certificate

Path(root+"config/application-server/api/client").mkdir(parents=True, exist_ok=True) 

filename = root+"config/application-server/api/client/certificate.json"
file_content ='{\n\t"CN" : "'+ net_id+'",\n\t"host": '+ list_to_string(net_server_hosts) + ',\n\t"key": {\n\t\t"algo": "rsa",\n\t\t"size": 2048\n\t}\n}'

app_server_file = open(filename, 'w')
app_server_file.write(file_content)
app_server_file.close()

print("Written : \n" + file_content + "\n to \n" + filename)


# In[114]:


# Generating Join Server - Server Certificate

Path(root+"config/application-server/join-api/server").mkdir(parents=True, exist_ok=True) 

filename = root+"config/application-server/join-api/server/certificate.json"
file_content ='{\n\t"CN" : "'+ "Afnic-AS-Join-API" +'",\n\t"host": '+ list_to_string(join_server_hosts) + ',\n\t"key": {\n\t\t"algo": "rsa",\n\t\t"size": 2048\n\t}\n}'

join_server_file = open(filename, 'w')
join_server_file.write(file_content)
join_server_file.close()

print("Written : \n" + file_content + "\n to \n" + filename)


# In[115]:


# Generating Join Server - Client Certificate

Path(root+"config/application-server/join-api/client").mkdir(parents=True, exist_ok=True) 

filename = root+"config/application-server/join-api/client/certificate.json"
file_content ='{\n\t"CN" : "'+ net_id +'",\n\t"host": '+ list_to_string(net_server_hosts) + ',\n\t"key": {\n\t\t"algo": "rsa",\n\t\t"size": 2048\n\t}\n}'

join_server_file = open(filename, 'w')
join_server_file.write(file_content)
join_server_file.close()

print("Written : \n" + file_content + "\n to \n" + filename)


# In[116]:


# Generating Network Server - Server Certificate

Path(root+"config/network-server/api/server").mkdir(parents=True, exist_ok=True) 

filename = root+"config/network-server/api/server/certificate.json"
file_content ='{\n\t"CN" : "'+ "Afnic-Network-Server" +'",\n\t"host": '+ list_to_string(net_server_hosts) + ',\n\t"key": {\n\t\t"algo": "rsa",\n\t\t"size": 2048\n\t}\n}'

net_server_file = open(filename, 'w')
net_server_file.write(file_content)
net_server_file.close()

print("Written : \n" + file_content + "\n to \n" + filename)


# In[117]:


# Generating Network Server - Client Certificate

Path(root+"config/network-server/api/client").mkdir(parents=True, exist_ok=True) 

filename = root+"config/network-server/api/client/certificate.json"
file_content ='{\n\t"CN" : "'+ "00000000-0000-0000-0000-000000000000" +'",\n\t"host": '+ list_to_string(app_server_hosts) + ',\n\t"key": {\n\t\t"algo": "rsa",\n\t\t"size": 2048\n\t}\n}'

net_server_file = open(filename, 'w')
net_server_file.write(file_content)
net_server_file.close()

print("Written : \n" + file_content + "\n to \n" + filename)


# In[118]:


# Generating Roaming Server - Server Certificate
roaming_path = root+"config/network-server/roaming/" + net_id

Path(roaming_path + "/server").mkdir(parents=True, exist_ok=True) 

filename = roaming_path + "/server/certificate.json"
file_content ='{\n\t"CN" : "'+ net_id +'",\n\t"host": '+ list_to_string(roaming_server_hosts) + ',\n\t"key": {\n\t\t"algo": "rsa",\n\t\t"size": 2048\n\t}\n}'

net_server_file = open(filename, 'w')
net_server_file.write(file_content)
net_server_file.close()

print("Written : \n" + file_content + "\n to \n" + filename)


# In[119]:


# Generating Roaming Server - Server Certificate

Path(roaming_path + "/client").mkdir(parents=True, exist_ok=True)

filename = roaming_path + "/client/certificate.json"
file_content ='{\n\t"CN" : "'+ net_id +'",\n\t"host": '+ '[\"\"]' + ',\n\t"key": {\n\t\t"algo": "rsa",\n\t\t"size": 2048\n\t}\n}'

net_server_file = open(filename, 'w')
net_server_file.write(file_content)
net_server_file.close()

print("Written : \n" + file_content + "\n to \n" + filename)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




