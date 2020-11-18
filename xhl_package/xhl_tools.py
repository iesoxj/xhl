# coding=utf-8

def sTo2dList(s):
    '''
    把文本拆分成2dList 以; 做为第一级拆分， 以 , 做为第二级拆分
        输入 aaa,123;bbb,456;ccc,789 
        输出  [['aaa', '123'], ['bbb', '456'], ['ccc', '789']]
    
    '''
    l = ([i.split(',') for i in s.split(';')])
    return l
