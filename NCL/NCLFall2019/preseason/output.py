# uncompyle6 version 3.4.1
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.16+ (default, Sep  4 2019, 08:19:57) 
# [GCC 9.2.1 20190827]
# Embedded file name: source.py
# Compiled at: 2018-04-13 00:07:59

a = 'SKY'
middle = 'CSRC'

def getFlag(uid, mid):
    print str(ord(uid[0]))
    return a + '-' + mid + '-' + str(ord(uid[0])).zfill(4)

middle = 'CSRC'
uid = 39d41bed6288044c8fae9052523e5911 
result = getFlag(uid, middle)
print result
