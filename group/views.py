from flask import Blueprint, render_template, request, redirect, url_for, abort

from helper import check_user
from models import Group, db

group_bp = Blueprint("group", __name__)


def trans_dict(groups):
    """
    转换标准格式
    :param groups:
    :return: dict
    """
    groups_dict = {"groups": [], "total": len(groups)}
    for group in groups:
        temp = {}
        temp["id"] = group.id
        temp["name"] = group.name
        temp["count"] = len(group.words)
        temp["add_time"] = "-".join([str(group.add_time.year), str(group.add_time.month), str(group.add_time.day)])
        groups_dict["groups"].append(temp)
    return groups_dict


@group_bp.route("/", methods=["GET", "POST"])
@group_bp.route("/<int:page>", methods=["GET", "POST"])
def group_page(page=1):

    """
    视图函数需要实现关键字查询和页面渲染
    :param page: 根据请求获取两个查询参数
    :return: render word.html
    """

    if not check_user():
        # abort(404)
        return redirect(url_for("reg_or_log.login_page"))
    else:
        group_name = request.args.get("group_name")
        if group_name==None or group_name == "所有分组":
            groups = Group.query.order_by(Group.id.asc()).paginate(page=page, per_page=10)
        else:
            groups = Group.query.filter(Group.name == group_name).paginate(page=page, per_page=10)
        return render_template("group.html", groups=groups.items, pagination=groups)


@group_bp.route("/show_info", methods=["GET", "POST"])
@group_bp.route("/edit_info", methods=["GET", "POST"])
def show_info():

    """
    视图函数实现编辑页面和展现页面的渲染
    :param: 获取单词的唯一标识
    :return: dict
    """

    group_id = request.form.get("group_id")
    group = Group.query.get(group_id)
    return {
        "name": group.name,
        "word_count": len(group.words),
        "add_time": "-".join([str(group.add_time.year), str(group.add_time.month), str(group.add_time.day)])
    }


@group_bp.route("/save", methods=["GET", "POST"])
def save():

    """
    视图函数需要实现保存单词的功能，如果单词存在则返回单词已存在，否则就保存
    :param: 获取输入的单词
    :return: 返回提示信息
    """

    group_name = request.form.get("group_name")
    group = Group.query.filter(Group.name==group_name).first()
    if group:
        return group_name+"已存在！"
    else:
        try:
            group = Group(name=group_name)
            db.session.add(group)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(e)
        return group_name+"添加成功！"


@group_bp.route("/update", methods=["GET", "POST"])
def update():

    """
    视图函数需要修改单词的部分信息
    :param: 获取修改页面的输入框的相关信息
    :return: 返回提示信息
    """

    try:
        group_name = request.form.get("group_name")
        group_id = request.form.get("group_id")
        group = Group.query.filter(Group.id == group_id).first()
        group.name = group_name
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
    return "分组信息修改成功"


@group_bp.route("/delete", methods=["GET", "POST"])
def delete():

    """
    视图函数需要删除不可用的单词词组，如果这个词组下由单词，系统是不允许删除，
    如果非要删除，则需要在创建表格的时候，在建立外键的时候增加一个关键字参数：
    ondelete='CASCADE'
    :param: 获取单词的唯一标识
    :return: 返回空字符串
    """

    try:
        group = Group.query.get(request.form.get("group_id"))
        db.session.delete(group)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return "该分组删除失败"
    return ""
