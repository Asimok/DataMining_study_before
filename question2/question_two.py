# coding:utf-8
import math
import jieba.analyse
from collections import Counter

# sentence1="A市A3区中海国际社区三期四期中间，即蓝天璞和洲幼儿园旁边那块空地一直处于三不管状态，物业不管城管不管市政不管，从去年开始周围建筑工地一有多余的、废的土渣都往这块空地上堆，同时等要用土的时候再过来挖，而且这个状态一直在延续，目前从上个月开始每天晚上四台挖土机从此处挖土，同时十几台小卡车每天从晚上十点工作到凌晨五点。噪音高达70分贝以上。多位自称城管干部的工作人员打电话给投诉业主，如电话*****************，这些城管人员接到投诉，一不去现场，二不亲自了解噪音情况，而是直接打电话给投诉业主，态度强硬恶劣充满无奈，同时表明分贝这样的词对他们城管来说太专业了。同时城管工作人员对夜间施工什么证，有效期吞吞吐吐，回答含糊不清，一会说不是夜间施工证，一会又说只有渣土车运行证。还说前面这块空地，属于水岸御园2期，以后这里施工还有得吵，估计要吵1年以上，他们爱莫能助。泱泱大国，影响上万人夜间休息的夜间施工，噪音扰民，竟然多年得不到解决，同时还称未来一两年不能改善。是执法部门失职还是存在不正当关系勾结。不管有没有证，噪音都要达到国家标准，希望市政府引起正视，还大家一个宁静的夜晚。"
# sentence2 = "高新区谷园路39号维也纳智好酒店里有团队在里从事卖淫行为，我在平台举报一直没有回复，是不是政府对这个举报没兴趣还是另有原因，我今天在把我调查的信息反应全面点，这伙人管理者加上妹子有五六十人，长期在酒店内，妹子休息的地方在酒店六楼的写字楼选客的房间也在六楼(酒店客房和写字楼是相通的)，你们的业务常在酒店一楼茶吧或二楼麻将房休息，他们的营业用房每天都会有更换在酒店的三楼到十五楼不等非常隐蔽，每天接待客人几十个，辖区派出所充当保护伞打电话举报了也只是走个过场而且还有人通风报信，现在正是扫黑除恶的时候，胁迫失足女卖淫也是一种黑恶势力，打电话举报没有用所以我在平台发贴举报希望警方能通过这点线索调查取证一举摧毁这个团伙。"
sentence1 = "A市经济学院强制学生实习各位领导干部大家好，我是A市经济学院的一名学生，临近毕业，学校开始组织学生参加实习，当然学生是必须实习，但是学生应该有自己的选择权，学校要求学生必须去学校安排的几个点实习，并且学生工资500元，他们必须要求我们去他们安排的地方。他们利用我们这种廉价劳动力。我知道我们必须实习，但是也有自己的选择。希望得到帮助"
sentence2 = "A市经济学院组织学生外出打工合理吗？一名中职院校的学生,学校组织我们学生在外边打工,在外省做流水线工作，还要倒白夜班。本来都在学校好好上课，十月底突然说组织外出外省打工，自愿去或者不去，对于未曾涉世的孩子们而言，岂不是都想着出去探索这个世界，弄得不去的孩子也是无心学习，去了的孩子家里人整日担心。虽说是有偿工作，工资为11元/小时，一天工作十个小时以上，（晚班时间是20：30-第二天08：:30），试问对于一个未成年的学生而言，学校的这种做法是出于什么目的？？胆敢说不是学校从中获得了私利吗？一个孩子去熬夜通宵做流水线！这并不是毕业前实习。再者，若是早早安排好的实习工作，是否在开学初就应该通知到位？临时性决定，事发突然，我们都猝不及防。希望教育部门严查，防止类似事件再重演！"


# sentence1 = "人工智能（Artificial Intelligence），英文缩写为AI。它是研究、开发用于模拟、延伸和扩展人的智能的理论、方法、技术及应用系统的一门新的技术科学。人工智能是计算机科学的一个分支，它企图了解智能的实质，并生产出一种新的能以人类智能相似的方式做出反应的智能机器，该领域的研究包括机器人、语言识别、图像识别、自然语言处理和专家系统等。[1]  2017年12月，人工智能入选“2017年度中国媒体十大流行语”。"
# sentence2 ="人工智能从诞生以来，理论和技术日益成熟，应用领域也不断扩大，可以设想，未来人工智能带来的科技产品，将会是人类智慧的“容器”。人工智能可以对人的意识、思维的信息过程的模拟。人工智能不是人的智能，但能像人那样思考、也可能超过人的智能。人工智能是一门极富挑战性的科学，从事这项工作的人必须懂得计算机知识，心理学和哲学。人工智能是包括十分广泛的科学，它由不同的领域组成，如机器学习，计算机视觉等等，总的说来，人工智能研究的一个主要目标是使机器能够胜任一些通常需要人类智能才能完成的复杂工作。但不同的时代、不同的人对这种“复杂工作”的理解是不同的。 "
# jieba.analyse.textrank(sentence, topK=20, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v'))
# result1 = " ".join(jieba.analyse.textrank(sentence, topK=20, withWeight=False, allowPOS=("ns", "n", "vn", "v")))
# print(result1)
#
# result2 = " ".join(jieba.analyse.textrank(sentence, topK=20, withWeight=False, allowPOS=("n", "v")))  # 只看动词和名词
# print(result2)
def anlyse_count(sentence):
    words = jieba.cut(sentence)
    words = [each.strip() for each in words]
    counter = Counter(words)
    for a in counter.most_common(20):
        print('%-10s\t%d' % (a[0], a[1]))
    print('\n')


# 关键词提取
# jieba.analyse.set_stop_words('./data/stopwords.txt')
# jieba.load_userdict('./data/stopwords.txt')
jieba.load_userdict('./data/new_places.txt')
jieba.load_userdict('./data/new_places_country.txt')


def print_topic(text):
    tags = jieba.analyse.extract_tags(text, withWeight=True)
    print("%10s\t%s" % ('关键词', '权重'))
    for v, n in tags:
        print("%-10s\t%d" % (v, n * 10000))
    print('')


# 相似度判断
def cut_word(sentence):
    # 使用TF-IDF算法
    res = jieba.analyse.extract_tags(sentence=sentence, topK=20, withWeight=True)
    return res


def tf_idf(res1=None, res2=None):
    # 向量，可以用list表示
    vector_1 = []
    vector_2 = []
    # 词频，可以使用dict表示
    tf_1 = {i[0]: i[1] for i in res1}
    tf_2 = {i[0]: i[1] for i in res2}
    res = set(list(tf_1.keys()) + list(tf_2.keys()))

    # 填充词频向量
    for word in res:
        if word in tf_1:
            vector_1.append(tf_1[word])
        else:
            vector_1.append(0)
            if word in tf_2:
                vector_2.append(tf_2[word])
            else:
                vector_2.append(0)

    return vector_1, vector_2


def numerator(vector1, vector2):
    # 分子
    return sum(a * b for a, b in zip(vector1, vector2))


def denominator(vector):
    # 分母
    return math.sqrt(sum(a * b for a, b in zip(vector, vector)))


def run(vector1, vector2):
    return numerator(vector1, vector2) / (denominator(vector1) * denominator(vector2))


def get_similarity(text1, text2):
    vectors = tf_idf(res1=cut_word(sentence=text1), res2=cut_word(sentence=text2))
    # 相似度
    similarity = run(vector1=vectors[0], vector2=vectors[1])
    # 使用arccos计算弧度
    # rad = math.acos(similarity)
    return similarity


# anlyse_count(sentence)
# print_topic(sentence)


print(get_similarity(sentence1, sentence2))
