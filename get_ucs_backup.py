# CISCO UCS BACKUP
# v1.0
#                           CISCO SAMPLE CODE LICENSE
#                                  Version 1.0
#                Copyright (c) 2017 Cisco and/or its affiliates
#
#   These terms govern this Cisco example or demo source code and its
#   associated documentation (together, the "Sample Code"). By downloading,
#   copying, modifying, compiling, or redistributing the Sample Code, you
#   accept and agree to be bound by the following terms and conditions (the
#   "License"). If you are accepting the License on behalf of an entity, you
#   represent that you have the authority to do so (either you or the entity,
#   "you"). Sample Code is not supported by Cisco TAC and is not tested for
#   quality or performance. This is your only license to the Sample Code and
#   all rights not expressly granted are reserved.
#
#   1. LICENSE GRANT: Subject to the terms and conditions of this License,
#      Cisco hereby grants to you a perpetual, worldwide, non-exclusive, non-
#      transferable, non-sublicensable, royalty-free license to copy and
#      modify the Sample Code in source code form, and compile and
#      redistribute the Sample Code in binary/object code or other executable
#      forms, in whole or in part, solely for use with Cisco products and
#      services. For interpreted languages like Java and Python, the
#      executable form of the software may include source code and
#      compilation is not required.
#
#   2. CONDITIONS: You shall not use the Sample Code independent of, or to
#      replicate or compete with, a Cisco product or service. Cisco products
#      and services are licensed under their own separate terms and you shall
#      not use the Sample Code in any way that violates or is inconsistent
#      with those terms (for more information, please visit:
#      www.cisco.com/go/terms.
#
#   3. OWNERSHIP: Cisco retains sole and exclusive ownership of the Sample
#      Code, including all intellectual property rights therein, except with
#      respect to any third-party material that may be used in or by the
#      Sample Code. Any such third-party material is licensed under its own
#      separate terms (such as an open source license) and all use must be in
#      full accordance with the applicable license. This License does not
#      grant you permission to use any trade names, trademarks, service
#      marks, or product names of Cisco. If you provide any feedback to Cisco
#      regarding the Sample Code, you agree that Cisco, its partners, and its
#      customers shall be free to use and incorporate such feedback into the
#      Sample Code, and Cisco products and services, for any purpose, and
#      without restriction, payment, or additional consideration of any kind.
#      If you initiate or participate in any litigation against Cisco, its
#      partners, or its customers (including cross-claims and counter-claims)
#      alleging that the Sample Code and/or its use infringe any patent,
#      copyright, or other intellectual property right, then all rights
#      granted to you under this License shall terminate immediately without
#      notice.
#
#   4. LIMITATION OF LIABILITY: CISCO SHALL HAVE NO LIABILITY IN CONNECTION
#      WITH OR RELATING TO THIS LICENSE OR USE OF THE SAMPLE CODE, FOR
#      DAMAGES OF ANY KIND, INCLUDING BUT NOT LIMITED TO DIRECT, INCIDENTAL,
#      AND CONSEQUENTIAL DAMAGES, OR FOR ANY LOSS OF USE, DATA, INFORMATION,
#      PROFITS, BUSINESS, OR GOODWILL, HOWEVER CAUSED, EVEN IF ADVISED OF THE
#      POSSIBILITY OF SUCH DAMAGES.
#
#   5. DISCLAIMER OF WARRANTY: SAMPLE CODE IS INTENDED FOR EXAMPLE PURPOSES
#      ONLY AND IS PROVIDED BY CISCO "AS IS" WITH ALL FAULTS AND WITHOUT
#      WARRANTY OR SUPPORT OF ANY KIND. TO THE MAXIMUM EXTENT PERMITTED BY
#      LAW, ALL EXPRESS AND IMPLIED CONDITIONS, REPRESENTATIONS, AND
#      WARRANTIES INCLUDING, WITHOUT LIMITATION, ANY IMPLIED WARRANTY OR
#      CONDITION OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, NON-
#      INFRINGEMENT, SATISFACTORY QUALITY, NON-INTERFERENCE, AND ACCURACY,
#      ARE HEREBY EXCLUDED AND EXPRESSLY DISCLAIMED BY CISCO. CISCO DOES NOT
#      WARRANT THAT THE SAMPLE CODE IS SUITABLE FOR PRODUCTION OR COMMERCIAL
#      USE, WILL OPERATE PROPERLY, IS ACCURATE OR COMPLETE, OR IS WITHOUT
#      ERROR OR DEFECT.
#
#   6. GENERAL: This License shall be governed by and interpreted in
#     accordance with the laws of the State of California, excluding its
#      conflict of laws provisions. You agree to comply with all applicable
#      United States export laws, rules, and regulations. If any provision of
#      this License is judged illegal, invalid, or otherwise unenforceable,
#      that provision shall be severed and the rest of the License shall
#      remain in full force and effect. No failure by Cisco to enforce any of
#      its rights related to the Sample Code or to a breach of this License
#      in a particular situation will act as a waiver of such rights. In the
#      event of any inconsistencies with any other terms, this License shall
#      take precedence.
#
#

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

