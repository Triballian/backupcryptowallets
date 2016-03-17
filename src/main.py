'''
##
# Script to copy files and compress them and put them in a separate location
# Amit Sengupta, Sep 2015, HYD
# Written in Python 2.7
###
Modified on Mar 11, 2016

@author: Noe
create a folder named YearMonthDayMin
copy all dat files to it
encrypt encrypt and compress the folder into a file.
copy the file into a backup drive
remove the original folder
'''
import os
import datetime
import time
import shutil
import getpass
import subprocess

class Configinfo:
    sevenzip='C:\\Program Files\\7-Zip\\7z.exe'
    conffile = open('wcw.conf')
    for line in conffile:
        marker = '#'
        
        walletdat='wallet.dat'
        Line = line.partition(marker)[0]
        if not line:
            continue
        line = line.rstrip()
        line = line.replace(' ','')
        configdata = line.split('=')
        
        if configdata[0].lower() == 'wallets':        
            walletlist = configdata[1].split(',')
        
        if configdata[0].lower() == 'path':
            cfgpath = configdata[1].split(',')
            

class Fileinfo:
    appdata = os.getenv('APPDATA')
    sourcedir = appdata+"\\"
    __fldrname = ''
    
    
    def __init__(self, fldrname):
        self.__fldrname = fldrname
        
#     def set_fldrname(self, fldrname):
#         self.__fldrname = fldrname
        
    def get_fldrname(self):
        return self.__fldrname
        
    
    
    
    
class Copyfiles:
    
    
    def __init__(self, wallets, walletdat, srcfolder, dstfolder):
        
        if not os.path.exists(dstfolder):
            os.makedirs(dstfolder)
        for wallet in wallets:
            
            source=srcfolder+wallet+'\\'+walletdat
            dstfile=dstfolder+'\\'+wallet+'.dat'
            shutil.copy2(source, dstfile)
            

class Sevenzippassword:
    def getpasswd(self):
        confirmation = False
        while confirmation == False:
            p1 = getpass.getpass('Your Seven Zip file password:')
            p2 = getpass.getpass('Please confirm your password:')
            if p1 == p2:
                confirmation = True
            else:
                print "Passwords did not match. Please try again."
        return p1   
        
class Encryptnzip:
    def runzip(self, szpath, szpass, bkupfolder):
        wincommand = szpath+' a '+bkupfolder+' '+bkupfolder+' -p'+szpass
        print wincommand
        subprocess.call(wincommand)
                            


confirmpass = Sevenzippassword()
szpass=confirmpass.getpasswd()

 

if __name__ == '__main__':
    #print flinfo.sourcedir
    flinfo  = Fileinfo(datetime.datetime.strftime(datetime.datetime.now(), '%y%m%d%I%M%S'))

    foldername = flinfo.get_fldrname()
    cfginfo = Configinfo()
    encrypt = Encryptnzip()
    
    
    print foldername
    Copyfiles(cfginfo.walletlist, cfginfo.walletdat, flinfo.sourcedir, foldername)
    print foldername
    encrypt.runzip(Configinfo.sevenzip, szpass, foldername)
#     if not os.path.exists(fldrname.foldername):
#         os.makedirs(fldrname.foldername)
#     shutil.copy2('test.txt', fldrname.foldername)       
    
        
  
    pass