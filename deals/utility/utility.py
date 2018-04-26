#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    
class Utility:
    def __init__(self):
        pass
    @staticmethod
    def concatenateList(List):
        result = ''
        for l in List:
            l = l.strip('\n').strip()
            if(l != ''):
                result += ' '+ l
        return result
