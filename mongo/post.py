

# print(requests.request("post", "https://zhitulist.com/academic/api/v1/scholars/trend",
#                        data={"fieldNames": "Artificial intelligence"}))
def simplifyContent(content):
    conBeginStrs = ['个人经历', '简历']
    paperBeginStrs = ['论文', '论著']
    newContent = ''
    for str in conBeginStrs:
        if str in content:
            print(content.split(str))
            newContent = content.split(str)[1]
            break
    for str in paperBeginStrs:
        if str in newContent:
            newContent = newContent.split(str)[0]
    print(newContent)
    return newContent


print(simplifyContent('''万见峰 职称： 副教授 博导/硕导： 硕导 所属二级机构： 
    相变与结构研究所 通讯地址： 上海市闵行区东川路800号 邮编： 
    200240 E-mail： jfwan@sjtu.edu.cn 联系电话： 
    13916496412 从事专业： 材料科学与工程 学习与工作简历： 
    2008.12-至今，上海交通大学,副教授;2003.10-2008.12，
    上海交通大学,讲师;2007.9-2008.9，
    美国MIT，访问学者(公派);2001.10-2003.10,上海交通大学,博士后;1998.1-2001.9,
    上海交通大学,博士;1995.9-1998.1,兰州交通大学,硕士;1991.9-1995.7,北京科技大学,
    本科; 研究方向一 增材制造与材料基因工程 研究方向二 先进功能材料；相变、组织调控及性能设计 
    研究情况 自1996年以来一直从事智能材料、固态相变、材料设计、材料的表面与界面等基础研究工作，
    先后主持国家自然科学基金5项、教育部归国留学人员启动基金1项、上海宝钢合作1项，
    参与国家自然科学基金项目以及博士点专项基金、美国爱默生电气公司国际合作等项目多项。
    以第一作者或通讯作者在APL,PRB, MD, PCCP, JAP, SM, COSSMS, MMTA, IJSS, JMMM, PLA, 
    SSC,MT,中国科学,科学通报等杂志上发表研究论文60余篇，SCI检索50余篇。
    并申请中国发明专利七项（均已授权），国际发明专利1项。 讲授主要课程 [1]《金属材料强韧化与组织调控》，
    主讲之一[2]《绿色材料与绿色能源》，主讲[3]《材料强度与断裂》，主讲之一 教学研究 代表性论文、论著 
    [1]Shushan Cui, Jianfeng Wan*, Xunwei Zuo, Nailu Chen, Jihua Zhang and Yonghua Rong. 
    International Journal of Solids and Structures,2017,109:1-11.[2]Shushan Cui, Jianfeng Wan*, Yonghua Rong and Jihua Zhang. 
    Metallurgical and Materials Transactions A,2017,48(6):2706-2712.[3]Shushan Cui, Jianfeng Wan*, Yonghua Rong and Jihua Zhang.
     Computational Materials Science.2017,139:285-294.[4]Jianfeng Wan*, Shushan Cui, Jihua Zhang and Yonghua Rong. Metallurgical 
     and Materials Transactions A,2017,48(10):4447-4452.[5]Yanguang Cui, Yunlong Guo, Yangxin Li, Jianfeng Wan*, Jihua Zhang, 
     Yonghua Rong, Nailu Chen, Dong Wang and Yunzhi Wang. Computational Materials Science.2017,140:89-94.[6]Shi Shi, Chuan Liu, 
     Jianfeng Wan*, Jihua Zhang and Yonghua Rong. Materials and Design.2016,92:960-970.[7]Chuan Liu, Feng Yuan, Zhen Gen, Lin Wang, 
     Yanguang Cui, Jianfeng Wan*, Jihua Zhang and Yonghua Rong. Journal of Magnetism and Magnetic Materials.2016,407:1-7.
     [8]Shushan Cui,Yanguang Cui, Jianfeng Wan*, Yonghua Rong and Jihua Zhang. Computational Materials Science.2016,121:131-142.
     [9]Shushan Cui, Jianfeng Wan*, Xunwei Zuo, Nailu Chen and Yonghua Rong. Materials and Design.2016,109:88-97.[10]Shushan Cui, Shi Shi,
      Zhimin Zhao, Yanguang Cui,Chuan Liu, Feng Yuan, Jianwen Hou, Jianfeng Wan*, Jihua Zhang and Yonghua Rong. Mater.Research Express,2016,
      3(7):075701.[11]Shi Shi, Jianfeng Wan*, Xunwei Zuo, Nailu Chen, Jihua Zhang and Yonghua Rong. Physical Chemistry Chemical Physics,2016,
      18(43):29923-29934.[12]Lin Wang, Yanguang Cui, Jianfeng Wan*, Yonghua Rong, Jihua Zhang, Xin Jin and Minmin Cai. Appl. Phys. Lett.2013,
      102(18),181901.[13]Yanguang Cui, Jianfeng Wan*, Jihua Zhang and Yonghua Rong. Appl. Phys. Lett.2013,102(20),201907.[14] Yanguang Cui, 
      Jianfeng Wan*, Jihua Zhang and Yonghua Rong. Journal of Applied Physics,2012,112(9),094908.[15]Jianfeng Wan*. Chin. Phys. Lett.,2012,29(10):
      106301.[16]Jianfeng Wan*, Xiaolin Lei, Shipu Chen and T.Y. Hsu (Xu Zuyao), Phys. Rev. B,2004,70,014303.[17]Jianfeng Wan*, 
      Xiaolin Lei, Shipu Chen and T.Y. Hsu (Xu Zuyao), Script Mater.,2005,52(2):123-127.[18]Jianfeng Wan, Shipu Chen*, 
      Current Opinion in Solid State Materials Science,2005,9(6):303-312.*通讯作者 毕业博士生数 毕业硕士生
    数 参加学术团体、任何职务 申请专利 国家发明专利6项(均已授权)。 荣誉和奖励 其他 '''
                      ))
