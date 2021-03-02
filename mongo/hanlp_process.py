# -*- coding:utf-8 -*-
import functools
from hanlp_restful import HanLPClient
import pandas as pd

string1 = '''
    张寒凝
    副教授
    博士硕士生导师
     hanning0104@126.com 
    研究方向：
    现代设计理论与方法、CMF趋势与战略设计、产品交互与体验设计、智能家居设计研发
    简介
    张寒凝副教授，南京林业大学工学博士，中国工业设计协会会员，中国流行色协会会员，江苏省工业设计学会会员、中国家具协会会员。
    长期从事产品设计专业教学与研究，现任江南大学设计学院“江南大学卡秀堡辉CMF联合创新实验室”负责人。以第一作者在专业学术期刊发表论文二十余篇，其中《On the Characteristics of Technological Aesthetics in Modern Furniture》、《On the Visual Image Similarities and Differences between Chinese and Foreign Vehicle Logo》、《Study on the 21st century SOHO Office System Design in China》、《On the Procedure and Methods in Modern Furniture Green Design》和《Application of Maslow’s Hierarchy of Needs to Modern Chinese Furniture》等十余篇专业论文分别被EI、CSSCI及CSCD检索收录，多篇论文获评江苏省工业设计学会年度学术奖，出版专业著作及教材四部——《魅力色彩——工业产品色彩设计教程》、《设计进行时——工业设计程序与方法教程》、《产品设计程序与方法》和《工业设计造型基础》。
    主持并参与十余项部、省级科研项目。连续主持并参与策划和主办2015年、2014年CMF国际趋势研讨会，曾多次参加国际会议并发表主题演讲。工作以来，与海尔、TCL、联想、长虹、正泰电器、南瑞电气、CMW卡秀堡辉等知名企业进行设计合作与项目策划，多款产品投放市场并获奖，申请并获批外观设计专利100余项。多次组织并指导学生参与国内外设计竞赛及workshop，指导作品多项获得红点奖、IF奖等各类设计奖项。
     Hanning Zhang, Associate Professor. Zhang holds a PhD in Furniture Design and Engineering from Nanjing Forestry University; with research interests in prototype innovation, furniture design and color planning and strategy. Zhang is a member of China Industrial Design Association, China Fashion Color Association and Jiangsu Province Industrial Design Society. Zhang engaged in teaching and research of industrial design.
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

    # print(result)

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
        if pre_time:
            time_list.append(temp_list)
        else:
            pos_list.append(temp_list)

        return {'time': time_list, 'pos': pos_list}

    # print(classifyStd(result))
    # print(classifyTime(result["ner/msra"]))
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
            ls.append({'time': ls1[i], 'pos': ls2[i], 'timeKey': getkey1(ls1[i])})

        # print(ls1)
        # print(ls2)
        # print(ls, "\n\n\n")
        ls.sort(key=lambda x: x['timeKey'])
        print(ls)
        return ls

    timeData = classifyTime(result["ner/msra"])
    return sortTimeData(timeData)
    # print(timeData)
    # return timeData
# getContent(string1)
