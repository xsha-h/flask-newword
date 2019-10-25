from flask import Blueprint, render_template, request, redirect, url_for, abort, session

from helper import check_user
from models import Feedback, db, User

feedback_bp = Blueprint("feedback", __name__)


@feedback_bp.route("/")
def feedback_page():

    if not check_user():
        return redirect(url_for("reg_or_log.login_page"))

    else:
        return render_template("feedback.html")


@feedback_bp.route("/send_feedback", methods=["GET", "POST"])
def send_feedback():
    if request.method == "GET":
        return redirect(url_for("feedback.feedback_page"))
    else:
        try:
            feedback = Feedback()
            feedback.content = request.form.get("content")

            user = User.query.filter(User.user_name == session.get("user_name"),
                                     User.user_psd == session.get("user_psd")).first()

            # 这里暂时先设置第一个用户提交反馈意见
            feedback.user_id = user.id
            db.session.add(feedback)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
        return redirect(url_for("feedback.feedback_page"))


