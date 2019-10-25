from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from sqlalchemy import or_

from models import Feedback, User, db

cms_feedback_bp = Blueprint("cms_feedback", __name__)


@cms_feedback_bp.route("/feedback", methods=["GET", "POST"])
@login_required
def cms_feedback():
    """
    装饰器@login_required会自动检测这次请求的页面有没有session值
    :return:
    """
    if request.method == "GET":
        feedbacks = Feedback.query.all()
        infos = []
        temp = {}
        for feedback in feedbacks:
            temp["id"] = feedback.id
            temp["user_name"] = feedback.users.user_name
            temp["user_phone"] = feedback.users.user_phone
            temp["is_checked"] = "已审核" if feedback.is_checked else "待审核"
            infos.append(temp)
    else:
        keyword = request.form.get("keyword")
        if keyword != "1" and keyword == "已审核":
            feedbacks = Feedback.query.filter(Feedback.is_checked == 1).all()
        elif keyword != "0" and keyword == "待审核":
            feedbacks = Feedback.query.filter(Feedback.is_checked == 0).all()
        else:
            feedbacks = []
            users = User.query.filter(or_(User.user_name.like("%"+keyword+"%"),
                                          User.user_phone.like("%"+keyword+"%"))).all()
            # 从用户获取发表的反馈意见
            for user in users:
                for feedback in user.feedbacks:
                    feedbacks.append(feedback)

        infos = []
        temp = {}
        for feedback in feedbacks:
            temp["id"] = feedback.id
            temp["user_name"] = feedback.users.user_name
            temp["user_phone"] = feedback.users.user_phone
            temp["is_checked"] = "已审核" if feedback.is_checked else "待审核"
            infos.append(temp)
    return render_template("cms/feedback.html", infos=infos)


@cms_feedback_bp.route("/feedback/info", methods=["GET", "POST"])
def feedback_info():
    feedback_id = request.form.get("feedback_id")
    feedback = Feedback.query.get(feedback_id)
    return {
        "user_email": feedback.users.user_email,
        "content": feedback.content
    }


@cms_feedback_bp.route("/feedback/check", methods=["GET", "POST"])
def feedback_check():
    feedback_id = request.form.get("feedback_id")
    feedback = Feedback.query.get(feedback_id)
    feedback.is_checked = 1
    db.session.commit()
    return ""
