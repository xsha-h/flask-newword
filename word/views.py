from flask import Blueprint, render_template, request, redirect, url_for, abort
from sqlalchemy import or_, and_

from helper import check_user
from models import Word, Group, db

word_bp = Blueprint("word", __name__)


def trans_dict(words):
    """
    转换标准格式
    :param words:
    :return: dict
    """
    words_dict = {"words": [], "total": len(words)}
    temp = {}
    for word in words:
        temp["id"] = word.id
        temp["word"] = word.word
        temp["translation"] = word.translation
        temp["introduction"] = word.introduction
        temp["group_name"] = word.groups.name
        temp["add_time"] = "-".join([str(word.add_time.year), str(word.add_time.month), str(word.add_time.day)])
        temp["star"] = word.star
        words_dict["words"].append(temp)
    print(words_dict)
    return words_dict


@word_bp.route("/", methods=["GET", "POST"])
@word_bp.route("/<int:page>", methods=["GET", "POST"])
def word_page(page=1):

    """
    视图函数需要实现关键字查询和页面渲染
    :param page: 根据请求获取两个查询参数
    :return: render word.html
    """

    if not check_user():
        # abort(404)
        return redirect(url_for("reg_or_log.login_page"))
    else:
        # 前台get请求方式获取的参数
        group_name = request.args.get("group_name")
        keyword = request.args.get("keyword")

        # 关键字查询
        if keyword:
            if group_name == "所有分组":
                words = Word.query.filter((Word.tag == 0,
                                           or_(Word.word.like("%" + keyword + "%"),
                                               Word.translation.like("%" + keyword + "%")))).paginate(page=page,
                                                                                                      per_page=10)
            else:
                group_id = Group.query.filter(Group.name == group_name).first()
                words = Word.query.filter(group_id == group_id.id, Word.tag == 0,
                                          or_(Word.word.like("%" + keyword + "%"),
                                              Word.translation.like("%" + keyword + "%"))).paginate(page=page,
                                                                                                    per_page=10)

        # 分组查询
        else:
            if group_name == "所有分组":
                words = Word.query.filter(Word.tag == 0,
                                          or_(Word.word.like("%" + keyword + "%"),
                                              Word.translation.like("%" + keyword + "%"))).paginate(page=page,
                                                                                                    per_page=10)

            # 没有查询条件的时候执行
            elif group_name == None:
                words = Word.query.filter(Word.tag == 0).order_by(Word.id.desc()).paginate(page=page, per_page=10)
            else:
                group_id = Group.query.filter(Group.name == group_name).first()
                words = Word.query.filter(Word.tag == 0, Word.group_id == group_id.id).paginate(page=page, per_page=10)
        return render_template("word.html", words=words.items, pagination=words)


@word_bp.route("/show_info", methods=["GET", "POST"])
@word_bp.route("/edit_info", methods=["GET", "POST"])
def edit_info():
    """
    视图函数实现编辑页面和展现页面的渲染
    :param: 获取单词的唯一标识
    :return: dict
    """
    # 获取前台post请求方式的参数
    word_id = request.form.get("word_id")
    word = Word.query.get(word_id)
    return {
        "word": word.word,
        "translation": word.translation,
        "introduction": word.introduction,
        "group_name": word.groups.name,
        "star": word.star,
        "example": word.example
    }


@word_bp.route("/save", methods=["GET", "POST"])
def save():
    """
    视图函数需要实现保存单词的功能，如果单词存在则返回单词已存在，否则就保存
    :param: 获取输入的单词
    :return: 返回提示信息
    """
    word_name = request.form.get("word")
    word = Word.query.filter(Word.word == word_name).first()
    if word:
        return word+"已存在"

    else:
        try:
            translation = request.form.get("translation")
            introduction = request.form.get("introduction")
            star = request.form.get("star")
            example = request.form.get("words")
            group_id = Group.query.filter(Group.name == request.form.get("group_name")).first()
            word_O = Word(word=word_name, translation=translation, introduction=introduction,
                          star=star, group_id=group_id.id, example=example)

            db.session.add(word_O)
            db.session.commit()
            return word_name + "已添加"
        except Exception as e:
            db.session.rollback()
            print(e)
            return word_name + "失败"


@word_bp.route("/update", methods=["GET", "POST"])
def update():
    """
    视图函数需要修改单词的部分信息
    :param: 获取修改页面的输入框的相关信息
    :return: 返回提示信息
    """
    try:
        word_id = request.form.get("word_id")
        word = Word.query.get(word_id)
        word.word = request.form.get("word")
        word.translation = request.form.get("translation")
        word.introduction = request.form.get("introduction")
        word.star = request.form.get("star")
        word.example = request.form.get("words")
        group_id = Group.query.filter(Group.name == request.form.get("group_name")).first()
        word.group_id = group_id.id
        db.session.commit()
        return "单词修改成功"
    except Exception as e:
        db.session.rollback()
        print(e)
        return "单词修改失败"


@word_bp.route("/delete", methods=["GET", "POST"])
def delete():
    """
    视图函数需要删除不可用的单词
    :param: 获取单词的唯一标识
    :return: 返回空字符串
    """
    word_id = request.form.get("word_id")
    try:
        word = Word.query.get(word_id)
        # 将单词设置为标记，将其作为删除的标记
        word.tag = 1
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
    return ""
