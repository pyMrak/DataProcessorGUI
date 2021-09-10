# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 13:56:28 2017

@author: andmra2
"""
from time import strftime
from DataProcessor import Paths


def getIntDate(date=None):
    koef = [1, 30, 365]
    curr = 0
    if date:
        for k, d in zip(koef, date):
            curr += d*k
    else:
        sym = ["%d", "%m", "%y"]
        for k, s in zip(koef, sym):
            curr += int(strftime(s))*k
    return curr

def check(version):
    
    mainVersion = version.split('.')[0]
    subVersion = version.split('.')[1]
    checkPermission = False
    online = True
    try:
        permissionsFile = open(Paths.permissionFolder + "ver" + mainVersion + '.prm', 'r', encoding="utf-8")
        premissions = permissionsFile.readlines()
        
        for permission in premissions:
            permission = permission.strip('\n')
            if permission == subVersion:
                checkPermission = True
                online = True
                break
    except FileNotFoundError as e:
        print(e)
        if getIntDate() < 8426: #1.01.2023
            checkPermission = True
            online = False
    except Exception as e:
        online = False
        print(e)
        pass
    return checkPermission, online
