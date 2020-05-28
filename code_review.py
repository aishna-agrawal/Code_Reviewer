#!/usr/bin/python3
import math
import re
from math import log2
import lizard

def ccn(code,lang):
    if(lang=="python"):
        i = lizard.analyze_file.analyze_source_code("zz.py",code)
        a = (len(i.function_list))
        z = i.function_list
        max =0
        for j in range(a):
            if(z[j].__dict__['cyclomatic_complexity']>max):
                max = z[j].__dict__['cyclomatic_complexity']
        return max
    elif(lang=="csharp"):
        i = lizard.analyze_file.analyze_source_code("zz.cs",code)
        a = (len(i.function_list))
        z = i.function_list
        max =0
        for j in range(a):
            if(z[j].__dict__['cyclomatic_complexity']>max):
                max = z[j].__dict__['cyclomatic_complexity']
        return max
    elif(lang=="cpp"):
        i = lizard.analyze_file.analyze_source_code("zz.cpp",code)
        a = (len(i.function_list))
        z = i.function_list
        max =0
        for j in range(a):
            if(z[j].__dict__['cyclomatic_complexity']>max):
                max = z[j].__dict__['cyclomatic_complexity']
        return max
    elif(lang=="c"):
        i = lizard.analyze_file.analyze_source_code("zz.c",code)
        a = (len(i.function_list))
        z = i.function_list
        max =0
        for j in range(a):
            if(z[j].__dict__['cyclomatic_complexity']>max):
                max = z[j].__dict__['cyclomatic_complexity']
        return max       

def removemulticomments(code, lang):
    z = code
    if(lang=='python'):
        a = [x.start() for x in re.finditer(r"\"\"\"", code)]
        for i in range(0,len(a),2):
            #print(code[a[i]:a[i+1]+3])
            z = z.replace(code[a[i]:a[i+1]+3],"")
        t=z
        b = [x.start() for x in re.finditer(r"\'\'\'", t)]
        for i in range(0,len(b),2):
            # print(code[a[i]:b[i]+2])
            t = t.replace(z[b[i]:b[i+1]+3],"")
        code=t
    else:
        a = [x.start() for x in re.finditer(r"/\*", code)]
        b = [x.start() for x in re.finditer(r"\*/", code)]
        
        for i in range(len(a)):
            # print(code[a[i]:b[i]+2])
            z = z.replace(code[a[i]:b[i]+2],"")
        code=z
    return code

def removeComments(line,lang):
    if(lang=="python"):
        pattern = re.compile("\#.*")
        if (re.search(pattern, line)):
            s = line.index("#")
            line = line[:s]
        return line
    else:
        pattern = r""" //.*?$ | /\*[^*]*\*+([^/*][^*]*\*+)*/|("(\\.|[^"\\])*"|'(\\.|[^'\\])*'|.[^/"'\\]*) """
        regex = re.compile(pattern, re.VERBOSE|re.MULTILINE|re.DOTALL)
        noncomments = [m.group(2) for m in regex.finditer(line) if m.group(2)]

        return "".join(noncomments)
    
def codeparams(code,lang):
    operatorsFileName = "operator_"+ lang
    # print("operator filename:"+operatorsFileName)
    q=code
    # Calculate CCN
    cyclomatic_n = ccn(q,lang) 
    # print("ccn:",cyclomatic_n)

    operators = {}
    operands = {}

    with open(operatorsFileName) as f:
        for op in f:
            operators[op.replace('\n','')] = 0

    code = removemulticomments(code,lang)

    t=code.split("\n")
    for line in t:
        line = removeComments(line,lang)
        line = line.strip("\n").strip(' ')

        if(line!=""):
            if(lang == "c" or lang == "cpp"):
                pattern = re.compile("\#include\s*<.*>")
                # mas = pattern.finditer(line)
                if(re.search(pattern,line)):
                    s = line.index("<")+1
                    e = line.index(">")
                    sub = line[s:e]
                    if sub in operands.keys():
                        operands[sub] = operands[sub] + 1
                    else:
                        operands[sub] = 1
                    line = line.replace(sub,"")

                pattern = re.compile("\#\s*define\s*")
                mas = pattern.finditer(line)
                l1 = []
                for i in mas:
                    l1.append(list(i.span()))
                for j in l1:
                    temps = line[j[1]:]
                    temps = temps.split()
                    searchpat = re.compile("[A-Za-z,_]")
                    m1 = searchpat.finditer(temps[1])
                    z1 =[]
                    for x in m1:
                        z1.append(list(x.span()))
                    if(len(z1)==0):
                        if(temps[0] in operands.keys()):
                            operands[temps[0]] +=1
                        else:
                            operands[temps[0]] =1
                    else:
                        if(temps[0] in operators.keys()):
                            operators[temps[0]+" "] +=1
                        else:
                            operators[temps[0]+" "] =1
                if(len(l1)!=0):
                    line = line[l1[0][0]:l1[0][1]].replace(" ","")
                    if(line in operators.keys()):
                        operators[line]+=1
                    else:
                        operators[line] =1
                    line = ""
            if(lang=="cpp" or lang=="csharp"):
                pat = re.compile(r"\s*[a-zA-z_]*\s*<[a-zA-z,_]*>")
                ma = pat.finditer(line)
                z1 =[]
                for i in ma:
                    z1.append(list(i.span()))
                    key = line[i.span()[0]:i.span()[1]].replace(" ","")+" "
                    if(key in operators):
                        operators[key] +=1 
                    else:
                        operators[key]=1
                line = re.sub(r"\s*[a-zA-z_]*\s*<[a-zA-z,_]*>"," ",line)
            # For Strings
            st = line
            s =""
            l =[]
            for i in range(len(st)):
                if(st[i]=='"' or st[i]=="'"):
                    l.append(i)
            if(len(l)!=0):
                s += st[0:l[0]]
                for i in range(2,len(l)):
                    if(i%2==0):
                        s+=st[l[i-1]+1:l[i]]
                for j in range(1,len(l)):
                    temp = st[l[j-1]+1:l[j]]
                    if(j%2==1):    
                        if temp in operands:
                            operands[temp] = operands[temp] + 1
                        else:
                            operands[temp] = 1
                s+=st[l[-1]+1:]
            if(len(l)!=0):
                line = s

            for key in operators.keys():
                operators[key] = operators[key] + line.count(key)
                line = line.replace(key,' ')
            for key in line.split():
                if key in operands:
                    operands[key] = operands[key] + 1
                else:
                    operands[key] = 1
    
    n1, N1, n2, N2 = 0, 0, 0, 0
    # print("OPERATORS:\n")
    for key in operators:
        if(operators[key] > 0):
            if(key not in ")}]"):
                n1, N1 = n1 + 1, N1 + operators[key]
                # print("{} = {}".format(key, operators[key]))
        
    # print("\nOPERANDS\n")
    for key in operands.keys():
        if(operands[key] > 0):
            n2, N2 = n2 + 1, N2 + operands[key]
            # print("{} = {}".format(key, operands[key]))
    if(n1==0):
        return (-1)
    else:
        val={}
        val['Cyclomatic Complexity']=cyclomatic_n
        val['Vocabulary']= n1 + n2
        val['Volume']= (N1 + N2) * log2(n1 + n2) 
        val['Program Length']= (N1 + N2)
        val['Difficulty']= (n1 * N2) / (2 * n2)
        val['Intelligence Count'] = val['Volume'] / val['Difficulty']
        val['Effort'] = val['Difficulty'] * val['Volume']
        val['Time'] = val['Effort'] / (18)
        val['Unique Operators']=n1
        val['Unique Operands']=n2
        val['Total Opeartors']=N1
        val['Total Operands']=N2

        return val

def main(code,lang):

    lst = codeparams(code,lang)
    return lst