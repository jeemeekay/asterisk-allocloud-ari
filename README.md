# Requirements
 - Ubuntu 18.04 Bionic 64-bit Server
 - Internet access

# To run playbook on bare Ubuntu server (modify servers.ini with ip of Ubuntu server) 
ansible-playbook -i servers.ini deploy.yml 

# To deploy server via Vagrant 
vagrant up 

# TODO
Migrate python app to python3 to use asyncio 


