# -*- coding:utf-8 -*-
import functools
from hanlp_restful import HanLPClient
import pandas as pd
import pprint

string1 = '''
丁文江
职称：
教授、中国工程院院士
博导/硕导：
博导
所属二级机构：
轻合金研究所
通讯地址：
上海市闵行区东川路800号材料学院B楼
邮编：
200240
E-mail：
wjding@sjtu.edu.cn 
联系电话：
86-21-54742912
从事专业：
金属材料（镁合金）
学习与工作简历：
中国工程院院士，中共党员，教授，博士生导师。1981年毕业于上海交通大学铸造专业。现任轻合金精密成型国家工程研究中心主任，中国镁业协会副会长，中国材料研究学会常务理事，中共上海交通大学材料科学与工程学院委员会委员。曾任上海交通大学副校长、上海市科委副主任、上海市科协副主席。2013年当选为中国工程院院士。
研究方向一
长期从事轻金属，特别是镁材料及其精密成型方面的研究。
研究方向二
研究情况
丁文江长期从事先进镁合金及工程化研究，获国家科技进步二等奖、国家技术发明二等奖、国防科技进步二等奖、上海市科技功臣奖和上海市技术发明奖一等奖，发表论文321篇，SCI收录184篇，EI收录211篇，累计他引次数839次，申请发明专利105项（美国专利1项，已授权75项）。创建了轻合金精密成型国家工程研究中心，担任国家重大基础研究项目“面向未来××××的高能性能镁合金基础研究”技术首席。针对镁的易腐蚀、强度低和难变形三大难题进行了长期系统研究，取得了以下突破：1.探明了镁的氧化腐蚀本质，创制了阻燃耐蚀镁合金2.找到了镁合金中的高效强化相，创制了高强耐高温镁合金3.掌握了镁的细晶塑性变形规律，创制了高延性镁合金4.研制了轻金属熔体纯净化等新工艺5.推动了镁的研发与应用进程
讲授主要课程
教学研究
代表性论文、论著
1、《镁科学与技术》，2007年，第1作者，主要合作者袁广银、王渠东，科学出版社。2、Formation of 14H-type long period stacking ordered structure in the as-cast and solid-solution-treated Mg-Gd-Zn-Zr alloys.2009年,《Journal of Materials Research》，第1作者,主要合作者吴玉娟.3、Study on the microstructure and mechanical property of high strength Mg-Nd-Zn-Zr alloy,2007年,《Materials Science Forum》，第1作者,主要合作者付彭怀.4、Effect of CeCl3-containing flux on microstructure and mechanical properties of Mg alloy containing Rare Earth,2007,《Materials Science Forum》，第一作者，主要合作者吴国华5、Effects of Second Phase on the Mechanical Properties of Mg-Al-Zn Alloy by Equal Channel Angular Extrusion，2007年，《Materials Science Forum》,第1作者,主要合作者靳丽.6、Cyclic oxidation behaviour of cerium implanted AZ31 magnesium alloys,2006年,《Materials Letters》,第1作者,主要合作者王雪敏.7、Microstructure and mechanical properties of hot-rolled Mg-Zn-Nd-Zr alloys,2008年,《Materials Science and Engineering A》,第1作者,主要合作者李大全.8、Influence of ultrasonic power on the structure and composition of anodizing coatings on Mg alloys，2004年，《Surface and Coating Technology》,第2作者，主要合作者郭兴伍.9、Study on ignition proof magnesium alloy by beryllium and rare earth addition，2000年，《Scripta Materilia》,第4作者，主要合作者曾小勤.10、Fracture behavior of AZ91 magnesium alloy，2000年，《Materials Letters》,第3作者，主要合作者吕宜振.
毕业博士生数
毕业硕士生数
参加学术团体、任何职务
2004-至今中国材料研究学会常务理事2006.11-至今上海市科协副主席2002-至今中国有色金属工业协会镁分会副会长2001-至今上海市新材料学会副理事长2003-至今国务院学位委员会学科评议组成员2006-至今总装备部××专业组成员
申请专利
1、铸造阻燃镁合金及其熔炼和铸造工艺，1999年，专利号ZL99113861.9，丁文江，排名第1，主要合作者王渠东。2、含稀土高强度铸造镁合金及其制备方法，2005年，专利号ZL200510030457.8，排名第1，主要合作者付彭怀、彭立明。3、高强度耐热镁合金及其制备方法，2005年，专利号ZL200510025251.6，排名第4，主要合作者何上明、曾小勤、彭立明。4、镁合金专用水平连铸机，2001年，专利号ZL01105715.7，排名第3，主要合作者彭立明，曾小勤。5、发泡镁合金覆盖剂及其制备方法，2001年，专利号ZL00125301.8，排名第1，主要合作者翟春泉。6、汽车用多元耐热镁合金及其熔铸工艺，2001年，专利号ZL01126463.2，排名第2，主要合作者袁广银。
荣誉和奖励
1、新型高性能耐热镁合金研制及其在汽车上的应用，第1完成人，上海市技术发明一等奖2007年，20073033-1-001，主要合作者，袁广银。2、铝液纯净化及铝合金耐压容器制造工艺技术，国家技术发明二等奖，第1完成人，2006年，2006-F-215-2-03-R01，主要合作者孙宝德。3、高强度镁合金及其在国防工业中的应用研究，国防科技进步二等奖，第1完成人，2006年，2006GFJ2202-1,主要合作者曾小勤。4、阻燃镁合金及其应用关键技术研究,国家科技进步二等奖，第1完成人，2003年，2003-J-215-2-04-R01，主要合作者卢晨。5、镁合金便携式电子产品外壳制造技术开发，上海市科技进步二等奖，第1完成人，2001年，012014，主要合作者卢晨、曾小勤。6、 ZLJD-1S合金在××鱼雷铸造壳体上应用研究，国防专用国家级科技进步三等奖，第3完成人，1988年，85Y-KG6-080-03，主要合作者黄良余。
其他


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

            # elif item[1] == 'PHONE':
            #     time_list = []
            #     pos_list = []
            #     temp_list = []

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
    # print(result["ner/msra"])
    # print(timeData)
    sortMsra = sortTimeData(timeData)

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
                        break
        return merge_list

    # print("mergeList:\n", mergePosAndTime())
    return [sortMsra, mergePosAndTime(), getPkuPosList()]

# print(getContent(string1))