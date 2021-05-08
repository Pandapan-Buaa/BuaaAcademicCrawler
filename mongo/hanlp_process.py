# -*- coding:utf-8 -*-
import functools
from hanlp_restful import HanLPClient
import pandas as pd
import pprint

string1 = '''
梁若愚
副教授
博士
 lryasa@163.com 
研究方向：
开放式创新、设计管理、用户行为分析、数字化设计
简介
梁若愚，天津大学工学博士，江南大学设计学院专任教师，系统创新团队成员，江苏省工业设计协会会员，《Kybernetes Information》期刊审稿人。主要研究方向为开放式创新、设计管理、用户行为分析、数字化设计等，近年来发表学术论文多篇，其中被SCI/SSCI检索2篇，EI检索3篇。
作为主要成员先后参与了“汽车及模具产业链设计制造协同服务平台研发与应用”（863计划）、“远程网络化智能控制技术”（国家重点研发计划）“产品全生命周期信息闭环管理与应用示范”（国家科技支撑计划）、“个性化云印刷服务平台关键技术研发与应用”（天津市科技计划）等项目的研究工作。完成多个横向课题的设计研发工作，领域涵盖汽车、消费电子、健康照护、网络传媒等，为企业在策略规划、产品设计、交互设计等方面提供助力。
主讲课程：《计算机辅助工业设计》、《设计与工程基础》、《先进制造与实现》等。
学院版块SCHOOL 

'''


def getContent(string):
    HanLP = HanLPClient('https://hanlp.hankcs.com/api',
                        auth='MTk4N0BiYnMuaGFua2NzLmNvbTowSUdEZnhYZUhhN3JvOVBR')  # Fill in your auth

    raw_result = HanLP(string, tasks=["ner/pku", "ner/msra", "ner/ontonotes"])
    result = {}
    for name in ["ner/pku", "ner/msra", "ner/ontonotes"]:
        lenLs = len(raw_result[name])
        ls = []
        if (lenLs > 0):
            for i in range(lenLs):
                for j in raw_result[name][i]:
                    ls.append(j)
            result[name] = ls

    # print("raw_result:\n",raw_result)

    def classifyStd(result, std_list=["ner/pku", "ner/msra", "ner/ontonotes"]):
        '''

        Parameters
        ----------
        result :
            hanlp处理结果
        std_list :
            标准库列表. The default is ["ner/pku", "ner/msra", "ner/ontonotes"].

        Returns
        -------
        all_results :
            将每个标准下相同字段整合分类的结果

        '''
        all_results = {}

        for std in std_list:
            classified_result = {}
            for item in result[std]:
                item_type = item[1]
                item_content = item[0]
                if item_type not in classified_result.keys():
                    classified_result[item_type] = []
                classified_result[item_type].append(item_content)
            all_results[std] = classified_result
        return all_results

    def classifyTime(result):
        '''

        Parameters
        ----------
        result : list
            单个标准库下内容

        Returns
        -------
        dict
            将相邻地点和相邻时间看作一组，分别划分出来，可以在此基础上做个一一对应

        '''
        time_list = []
        pos_list = []
        temp_list = []
        pre_time = False
        pre_pos = False
        for item in result:
            if item[1] == 'DATE':
                if pre_time:
                    temp_list.append(item[0])
                else:
                    pre_time = True
                    pre_pos = False
                    if len(temp_list) > 0:
                        pos_list.append(temp_list)
                    temp_list = [item[0]]
            elif item[1] == 'ORGANIZATION':
                if pre_pos:
                    temp_list.append(item[0])
                else:
                    pre_time = False
                    pre_pos = True
                    if len(temp_list) > 0:
                        time_list.append(temp_list)
                    temp_list = [item[0]]
            elif item[1] == 'PHONE':
                time_list = []
                pos_list = []
                temp_list = []

        if pre_time:
            time_list.append(temp_list)
        else:
            pos_list.append(temp_list)

        return {'time': time_list, 'pos': pos_list}

    # print("classify_std:\n", classifyStd(result)['ner/pku'])
    # print("classify_std:\n", classifyStd(result)["ner/msra"])
    # print("classifyTime:\n", classifyTime(result["ner/msra"]))
    def sortTimeData(dic):
        ls1 = dic['time']
        ls2 = dic['pos']
        ls = []

        def getkey(a):
            i = 0
            while not a['time'][i][:4].isdigit():
                i += 1
            return int(a['time'][i][:4])

        def getkey1(b):
            j = 0
            while not b[j][:4].isdigit():
                j += 1
            return int(b[j][:4])

        for i in range(len(ls1)):
            if i >= len(ls2):
                break
            ls.append({'time': ls1[i], 'pos': ls2[i], 'timeKey': getkey1(ls1[i])})

        # print(ls1)
        # print(ls2)
        # print(ls, "\n\n\n")
        ls.sort(key=lambda x: x['timeKey'])
        existedPos = set()
        delItems = []
        for i in ls:
            if i['pos'][0].strip() in existedPos:
                delItems.append(i)
            else:
                existedPos.add(i['pos'][0].strip())
        for item in delItems:
            ls.remove(item)
        return ls

    timeData = classifyTime(result["ner/msra"])
    sortMsra = sortTimeData(timeData)

    # print(timeData)timeData

    def getPkuPosList():
        return set(classifyStd(result)['ner/pku']['nt'])

    def mergePosAndTime():
        posListByPkuStd = set(classifyStd(result)['ner/pku']['nt'])
        timeData = classifyTime(result["ner/msra"])
        msra_list = sortTimeData(timeData)
        merge_list = []
        for pos in posListByPkuStd:
            for msra_item in msra_list:
                pos_list = msra_item['pos']
                for msra_pos in pos_list:
                    if msra_pos == pos:
                        merge_list.append({'pos': pos, 'time': msra_item['timeKey']})
        return merge_list

    # print("mergeList:\n", mergePosAndTime())
    return [sortMsra, mergePosAndTime(), getPkuPosList()]

# print(getContent(string1))
