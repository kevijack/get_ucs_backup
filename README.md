# get_ucs_backup
Sample Python code which leverages ucsmsdk to automate backup of a selected Cisco UCS Domain.
The code includes references to modules:  ucsmsdk, os and sys
Can be called with or without arguments. 

  Without arguments - you will be prompted for fqdn/ip, backup type, account name, password, path and filename.
  Alternatively, you can supply ALL of the required arguments to further automate the backup request.
  
    d: domain name or IP of UCS Fabric Interconnect
    u: username
    s: password
    b: backup type [fullstate][config-logical][config-system][config-all]
    p: local path
    f: local filename 
  
  Example:  
  python3 get_ucs_backup.py d:myucsdomain.mycompany.com u:ucsadmin p:mypassword b:fullstate p:/users/myaccount/downloads/ f:ucs-backup.xml
  
