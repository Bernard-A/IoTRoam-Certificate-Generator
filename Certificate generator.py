#!/usr/bin/env python
# coding: utf-8

# # Makefile generator for chirpstack platform 

# In[ ]:


from pathlib import Path
import os
import datetime


# In[ ]:


# Archiving old certificates
if os.path.isfile("certificates"):
    os.rename("certificates", "old-"+str(datetime.datetime.now()).split(" ")[0]+"-certificates")


# In[ ]:


# Variables

folder_destination = "Afnic"
entity = "Afnic"

# File Names
## Application Server Generic Name
app_server_generic_name = "Application Server " + entity
## Network Server Generic Name - Not Used - NetID used instead
net_server_generic_name = "Network Server " + entity
## Join Server Generic Name
join_server_generic_name = "Join Server " + entity
## Roaming Server Generic Name
roaming_server_generic_name = "Join Server " + entity

# Identifier
## Application Server Generic Identifier - Used in Chirpstack AS config
app_server_identifier = "00000000-0000-0000-0000-000000000000"
## NetID as provided by LoRa Alliance
net_id = "000000"

# Addresses
## Application Server IP Address
app_server_ip = "51.91.79.176"
## Network Server IP Address
net_server_ip = "51.178.80.199"
## Join Server IP Address
join_server_ip = app_server_ip

# Hostnames - Associated with certificates
## Application Server Hosts
app_server_hosts = ["127.0.0.1","localhost", app_server_ip]
## Join Server Hosts - default is Application Server Hosts + Additional JoinEUI names
join_server_hosts = app_server_hosts.copy()
## Network Server Hosts
net_server_hosts = ["127.0.0.1","localhost", net_server_ip]
## Roaming Server Hosts - default is Network Server Hosts + Additional NetID name
roaming_server_hosts = net_server_hosts.copy()

## Setting additional names for roaming interfaces

join_server_domains = []
for i in join_server_domains:
    join_server_hosts.append(i)
    
roaming_server_domain = net_id+".netid.iotreg.net"
roaming_server_hosts.append(roaming_server_domain)


# In[ ]:


def list_to_string(list):
    return_string = "["
    for i in list:
        return_string += "\""
        return_string += i
        return_string += "\""
        return_string += ","
    return return_string[:-1]+"]"


# In[ ]:


def configuration_string(CN, hosts, key_algo="rsa", key_size=2048):
    config = '{\n\t"CN" : "'+ CN + '",\n\t"hosts": '+ list_to_string(hosts) + ',\n\t"key": {\n\t\t"algo":" '+ key_algo +'",\n\t\t"size": ' +str(key_size)+'\n\t}\n}'
    return config


# In[ ]:


# Creating system folders

Path("certificates/config").mkdir(parents=True, exist_ok=True) 
Path("certificates/config").mkdir(parents=True, exist_ok=True) 


# In[ ]:


# Generating Application Server - Server Certificate
Path("certificates/config/application-server/api/server").mkdir(parents=True, exist_ok=True) 

filename = "certificates/config/application-server/api/server/certificate.json"
file_content = configuration_string(app_server_generic_name,app_server_hosts)

app_server_file = open(filename, 'w')
app_server_file.write(file_content)
app_server_file.close()

print("\nWritten : \n" + file_content + "\nto\n" + filename + "\n")


# In[ ]:


# Generating Application Server - Client Certificate

Path("certificates/config/application-server/api/client").mkdir(parents=True, exist_ok=True) 

filename = "certificates/config/application-server/api/client/certificate.json"
file_content = configuration_string(net_id,net_server_hosts)

app_server_file = open(filename, 'w')
app_server_file.write(file_content)
app_server_file.close()

print("\nWritten : \n" + file_content + "\nto\n" + filename + "\n")


# In[ ]:


# Generating Join Server - Server Certificate

Path("certificates/config/application-server/join-api/server").mkdir(parents=True, exist_ok=True) 

filename = "certificates/config/application-server/join-api/server/certificate.json"
file_content = configuration_string(join_server_generic_name,join_server_hosts)

join_server_file = open(filename, 'w')
join_server_file.write(file_content)
join_server_file.close()

print("\nWritten : \n" + file_content + "\nto\n" + filename + "\n")


# In[ ]:


# Generating Join Server - Client Certificate

Path("certificates/config/application-server/join-api/client").mkdir(parents=True, exist_ok=True) 

filename = "certificates/config/application-server/join-api/client/certificate.json"
file_content = configuration_string(net_id,net_server_hosts)

join_server_file = open(filename, 'w')
join_server_file.write(file_content)
join_server_file.close()

print("\nWritten : \n" + file_content + "\nto\n" + filename + "\n")


# In[ ]:


# Generating Network Server - Server Certificate

Path("certificates/config/network-server/api/server").mkdir(parents=True, exist_ok=True) 

filename = "certificates/config/network-server/api/server/certificate.json"
file_content = configuration_string(net_server_generic_name,net_server_hosts)

net_server_file = open(filename, 'w')
net_server_file.write(file_content)
net_server_file.close()

print("\nWritten : \n" + file_content + "\nto\n" + filename + "\n")


# In[ ]:


# Generating Network Server - Client Certificate

Path("certificates/config/network-server/api/client").mkdir(parents=True, exist_ok=True) 

filename = "certificates/config/network-server/api/client/certificate.json"
file_content = configuration_string(app_server_identifier,app_server_hosts)

net_server_file = open(filename, 'w')
net_server_file.write(file_content)
net_server_file.close()

print("\nWritten : \n" + file_content + "\nto\n" + filename + "\n")


# In[ ]:


# Generating Roaming Server - Server Certificate
roaming_path = "certificates/config/network-server/roaming/" + net_id

Path(roaming_path + "/server").mkdir(parents=True, exist_ok=True) 

filename = roaming_path + "/server/certificate.json"
file_content = configuration_string(net_id,roaming_server_hosts)

net_server_file = open(filename, 'w')
net_server_file.write(file_content)
net_server_file.close()

print("\nWritten : \n" + file_content + "\nto\n" + filename + "\n")


# In[ ]:


# Generating Roaming Server - Server Certificate

Path(roaming_path + "/client").mkdir(parents=True, exist_ok=True)

filename = roaming_path + "/client/certificate.json"
file_content = configuration_string(net_id,[""])

net_server_file = open(filename, 'w')
net_server_file.write(file_content)
net_server_file.close()

print("\nWritten : \n" + file_content + "\nto\n" + filename + "\n")


# In[ ]:


root = folder_destination + "-" + str(datetime.datetime.now()).split(" ")[0] + "-certificates/"
if not os.path.isfile(root):
    os.rename(root, root[:-1]+"-old")
os.rename("certificates", root)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




