import datetime

from flask import Blueprint
from flask_restful import Api, Resource

from models import Composition, Group, Word

index_bp = Blueprint("index", __name__)
api = Api(index_bp)


@index_bp.route("/words_rank", methods=["GET", "POST"])
def words_rank():
    """
    随机获取数据库中的一篇文章，并且以星级标准（这里是以单词的字符数）统计单词数量，
    并分析当前文章的难度系数
    :return: 返回的也是一个字典
    """
    today = datetime.datetime.now().weekday()
    composition = Composition.query.get(today+1)
    strip_arr = [",", ".", "\t", "\n"]
    for strip in strip_arr:
        content = composition.content.replace(strip, " ")
    words = content.split(" ")
    count_star = {"zero_star": [], "one_star": [], "two_star": [], "three_star": [], "four_star": [], "five_star": []}
    for word in words:
        if len(word) < 3:
            count_star["zero_star"].append(word)
        elif 2 < len(word) < 4:
            count_star["one_star"].append(word)
        elif 3 < len(word) < 5:
            count_star["two_star"].append(word)
        elif 4 < len(word) < 6:
            count_star["three_star"].append(word)
        elif 5 < len(word) < 7:
            count_star["four_star"].append(word)
        else:
            count_star["five_star"].append(word)
    return {
        "zero_star": len(count_star["zero_star"]),
        "one_star": len(count_star["one_star"]),
        "two_star": len(count_star["two_star"]),
        "three_star": len(count_star["three_star"]),
        "four_star": len(count_star["four_star"]),
        "five_star": len(count_star["five_star"]),
        "expect_zero": 60,
        "expect_one": 70,
        "expect_two": 60,
        "expect_three": 55,
        "expect_four": 45,
        "expect_five": 35,
    }


@index_bp.route("/group_rate", methods=["GET", "POST"])
def group_rate():
    """
    这里只获取前五个分组类型：
    :return: 返回的是一个以分组名为键，分组下的单词数量为值的字典
    """
    groups = Group.query.limit(5).all()
    # 统计数据库中所有的单词
    total = 0
    group_dict = {}
    for group in groups:
        total += len(group.words)
    for group in groups:
        group_dict[group.name] = len(group.words)/total*100
    return group_dict


# @index_bp.route("/word_count", methods=["GET", "POST"])
# def word_count():
#     """
#     获取最近7天的单词收藏量和标记量：
#     one_day: 今天、two_day: 昨天、three_day: 前天
#     four_day: 大前天、five_day: 前四天、six_day: 前五天
#     seven_day: 前六天
#
#     获取的值：0：表示星期一、1：表示星期二、2：表示星期三、依次类推
#     :return:返回的是一个字典里包含字典的数据字典类型
#     """
#     one_day = datetime.datetime.now()
#     two_day = one_day - datetime.timedelta(days=1)
#     three_day = one_day - datetime.timedelta(days=2)
#     four_day = one_day - datetime.timedelta(days=3)
#     five_day = one_day - datetime.timedelta(days=4)
#     six_day = one_day - datetime.timedelta(days=5)
#     seven_day = one_day - datetime.timedelta(days=6)
#     days = [one_day, two_day, three_day, four_day, five_day, six_day, seven_day]
#     uniform_days = {}
#     for day in days:
#         uniform_days[day.weekday()] = "-".join([str(day.year),
#                                                 "0"+str(day.month) if 0 < day.month < 10 else str(day.month),
#                                                 "0"+str(day.day) if 0 < day.day < 10 else str(day.day)])
#
#     # 定义一个收藏和标记的字典分别存储收藏和标记的单词
#     res_zero_dict = {}
#     res_one_dict = {}
#
#     for key, value in uniform_days.items():
#         res_zero_dict[key] = len(Word.query.filter(Word.tag == 0, Word.add_time.like("%"+value+"%")).all())
#         res_one_dict[key] = len(Word.query.filter(Word.tag == 1, Word.add_time.like("%"+value+"%")).all())
#     res_dict = {"收藏": res_zero_dict, "标记": res_one_dict}
#     return res_dict


class WordCount(Resource):
    def post(self):
        """
        采用restful方式，将获取的值放置api中
        获取最近7天的单词收藏量和标记量：
        one_day: 今天、two_day: 昨天、three_day: 前天
        four_day: 大前天、five_day: 前四天、six_day: 前五天
        seven_day: 前六天

        获取的值：0：表示星期一、1：表示星期二、2：表示星期三、依次类推
        前台访问：定义的api接口，前台只需要访问提供的接口
        :return:返回的是一个字典里包含字典的数据字典类型
        """
        one_day = datetime.datetime.now()
        two_day = one_day - datetime.timedelta(days=1)
        three_day = one_day - datetime.timedelta(days=2)
        four_day = one_day - datetime.timedelta(days=3)
        five_day = one_day - datetime.timedelta(days=4)
        six_day = one_day - datetime.timedelta(days=5)
        seven_day = one_day - datetime.timedelta(days=6)
        days = [one_day, two_day, three_day, four_day, five_day, six_day, seven_day]
        uniform_days = {}

        # 规定的时间格式实现：如2019-09-01
        for day in days:
            uniform_days[day.weekday()] = "-".join([str(day.year),
                                                    "0" + str(day.month) if 0 < day.month < 10 else str(day.month),
                                                    "0" + str(day.day) if 0 < day.day < 10 else str(day.day)])

        # 定义一个收藏和标记的字典分别存储收藏和标记的单词
        res_zero_dict = {}
        res_one_dict = {}

        for key, value in uniform_days.items():
            res_zero_dict[key] = len(Word.query.filter(Word.tag == 0, Word.add_time.like("%" + value + "%")).all())
            res_one_dict[key] = len(Word.query.filter(Word.tag == 1, Word.add_time.like("%" + value + "%")).all())
        res_dict = {"收藏": res_zero_dict, "标记": res_one_dict}
        return res_dict


api.add_resource(WordCount, "/word_count")
