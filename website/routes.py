from flask import render_template, flash, url_for, flash, make_response, request
from website import app
from website.forms import *
from website import database
from scraper import webpage_retriever as wr


@app.route('/', methods = ["GET", "POST"])
@app.route('/index', methods = ["GET", "POST"])
def index():
    return render_template("index.html")


@app.route('/reg_checker', methods = ["GET", "POST"])
def reg_checker():
    check_form = CheckForm()
    email_form = EmailForm()

    course_code = None
    course_data = None

    if check_form.validate_on_submit():
        course_code = check_form.code.data
        if course_code:
            course_data = wr.getResultByCode(str(course_code))
            resp = make_response(render_template("reg_checker.html", check_form = check_form, course_data = course_data, email_form = email_form))
            resp.set_cookie("COURSE_CODE_COOKIE", course_code)
            return resp


    if email_form.validate_on_submit():
        course_code = request.cookies.get("COURSE_CODE_COOKIE")
        msg = database.save(str(email_form.email.data), str(course_code))
        category = "success" if msg == "Success." else "danger"
        flash(msg, category)

    return render_template("reg_checker.html", check_form = check_form)



@app.route('/user', methods = ["GET", "POST"])
def user():
    user_form = UserForm()
    drop_form = DropForm()
    if user_form.validate_on_submit():
        email_addr = user_form.email.data
        course_code_list = database.load(str(email_addr))
        if course_code_list:
            course_data_list = [wr.getResultByCode(code) for code in course_code_list]
            resp = make_response(render_template("user.html", user_form = user_form, course_data_list = course_data_list, drop_form = drop_form))
            resp.set_cookie("EMAIL_COOKIE", email_addr) 
            return resp
        else:
            flash("There is no course registered under this email addr.", "danger")

    if drop_form.validate_on_submit():
        email_addr = request.cookies.get("EMAIL_COOKIE")
        msg = database.drop(str(email_addr), str(drop_form.code.data))
        category = "success" if msg == "Success." else "danger"
        flash(msg, category)

    return render_template("user.html", user_form = user_form)
