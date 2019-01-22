# CISCO UCS BACKUP
# Kevin Jackson
# v1.0



# ----------------------------------------------
# IMPORT UCSHANDLE FUNCTION FROM UCSMSDK MODULE
# ----------------------------------------------
try:
    from ucsmsdk.ucshandle import UcsHandle
    from ucsmsdk.utils.ucsbackup import backup_ucs
except ImportError:
    print ('     *** ERROR - Module UCSMSDK not available. Please install and restart.')


# ----------------------------------------------
# IMPORT OS MODULE
# ----------------------------------------------
try:
    import os
except ImportError:
    print ('     *** ERROR - Module OS not available. Please install and restart.')


# ----------------------------------------------
# IMPORT SYS MODULE
# ----------------------------------------------
try:
    import sys
except ImportError:
    print ('     *** ERROR - Module SYS not available. Please install and restart.')
    

    
# ----------------------------------------------
# DEFINE CLEAR SCREEN FUNCTION
# ----------------------------------------------
def cls():
    print ('\n'*50)


# ----------------------------------------------
# COMMAND LINE ARGUMENT HELP
# ----------------------------------------------
def args_help():
        print ('\n COMMAND LINE ARGUMENT HELP')
        print ('d=fqdn/ip of UCS domain')
        print ('u=username')
        print ('s=password')
        print ('b=backup type [fullstate][config-logical][config-system][config-all]')
        print ('p=local folder path')
        print ('f=local filename\n\n\n')



# ----------------------------------------------
# CLEAR SCREEN & DISPLAY HEADER
# ----------------------------------------------
cls()
print ('---------------------------------------------------')
print ('        C I S C O   U C S   B A C K U P \n')
print (' Utility will initiate a UCS backup of your choice ')
print (' on a selected UCS domain. \n')
print (' This should be done periodically and retained for ')
print (' possible system restoration')
print ('---------------------------------------------------\n\n\n')



# ----------------------------------------------
# CHECK COMMAND LINE ARGUMENTS
# Force all command line arguments to be present
# ----------------------------------------------
valid_args = False
if len(sys.argv) > 1:
    if len(sys.argv) == 7:
        print ('*** PARSING ARGUMENTS')
        
        for iLoop in range(1,len(sys.argv)):
            tArg = sys.argv[iLoop]
            if tArg[0:1] == 'd':
                ucs_name = tArg[2:len(tArg)]
                print ('UCS DOMAIN= ',ucs_name)
                
            elif tArg[0:1] == 'u':
                login_name = tArg[2:len(tArg)]
                print ('LOGIN NAME= ',login_name)
                
            elif tArg[0:1] == 's':
                password = tArg[2:len(tArg)]
                print ('PASSWORD=   ',password)
                
            elif tArg[0:1] == 'b':
                backup_selection = tArg[2:len(tArg)]
                print ('BACKUP TYPE=',backup_selection)
                
            elif tArg[0:1] == 'p':
                local_dcty = tArg[2:len(tArg)]
                print ('PATH=       ',local_dcty)
                
            elif tArg[0:1] == 'f':
                local_filename = tArg[2:len(tArg)]
                print ('FILENAME=   ',local_filename)
                
            else:
                print ('*** ERROR - Invalid argument supplied')
                print ('     Invalid Argument: ', tArg)
                args_help()
                exit()
            
        valid_args = True
        print ('\n')
        
    else:
        print ('*** ERROR - If arguments are supplied, then ALL arguments must be included.')
        args_help()
        exit()


# ----------------------------------------------
# GET UCS DOMAIN LOGIN CREDENTIALS
# ----------------------------------------------
if valid_args == False:
    ucs_name = input ("UCS Domain FQDN or IP: ")
    login_name = input("User/Admin account name: ")
    password = input("Password: ")


# ----------------------------------------------
# ATTEMPT TO LOGIN TO USE DOMAIN
# ----------------------------------------------
handle = UcsHandle(ucs_name, login_name, password)

try:
    print ('*** Logging in')
    handle.login()
    print ('*** Successfully Logged in \n')
except:
    print ('*** ERROR - UNABLE TO LOGIN\n\n\n')
    exit()

    
# ----------------------------------------------
# WHAT TYPE OF BACKUP SHOULD WE PERFORM
# ----------------------------------------------
if valid_args == False:
    backup_type = []
    backup_type.append('fullstate')
    backup_type.append('config-logical')
    backup_type.append('config-system')
    backup_type.append('config-all')

    print ('SELECT BACKUP TYPE')
    for iLoop in range(4):
        print (str(iLoop) + '. ' + backup_type[iLoop])

    backup_choice = 5
    while backup_choice > 3:
        backup_choice = input('Enter backup type: ')
        backup_choice = int(backup_choice)
    backup_selection = backup_type[backup_choice]
    print ('*** ' + backup_type[backup_choice].upper() + ' Selected\n\n')


# ----------------------------------------------
# WHERE SHOULD WE SAVE THE BACKUP LOCALLY
# ----------------------------------------------
if valid_args == False:
    while 1:
        local_dcty = input('Local directory to store backup: ')
        if os.path.isdir(local_dcty):
            print ('*** Verified Path: ' + local_dcty + '\n')
            break
        else:
            print ('*** Path could not be found.')


# ----------------------------------------------
# WHAT FILENAME SHOULD WE USE LOCALLY
# ----------------------------------------------
if valid_args == False:
    local_filename = input ('Local Filename: ')
    
    # WAS A FILE EXTENSION INCLUDED
    find_ext = local_filename.find(".")
    
    if find_ext > -1:
        # WAS THE INCLUDED EXTENSION .XML?
        if local_filename[len(local_filename)-4:len(local_filename)].lower() != ".xml":
            print ('***ERROR - FILENAME MUST END IN .XML\n\n\n')
            exit()
            
    #IF THERE'S NO EXTENSION, ADD .XML
    else:
        local_filename = local_filename + ".xml"



# ----------------------------------------------
# ----------------------------------------------
# GOOD TO GO - LETS GET A BACKUP
# ----------------------------------------------
# ----------------------------------------------

try:
    print ('*** Filename: ' + local_filename + '\n')
    print ('*** Requesting backup from UCS Domain ' + ucs_name + '\n')
    backup_ucs(handle, backup_selection, local_dcty, local_filename)
    print ('\n*** BACKUP COMPLETE\n')
except:
    print ('*** ERROR - Unable to complete backup request')



# --------------------------------
# LOGOUT OF THE UCS DOMAIN
# --------------------------------
handle.logout
print ("LOGGED OUT OF " + ucs_name.upper()+'\n\n\n')

