

from flask import render_template, request, redirect, url_for

import utils
from tourapp import app,login
from flask_login import login_user,logout_user

@app.route("/")
def home():
    cats = utils.load_categories()
    products = utils.load_product()
    return render_template("index.html", categories=cats,
                           products=products)


@app.route("/products")
def product_list():
    cate_id = request.args.get("category_id")
    kw = request.args.get("Keyword")
    from_price = request.args.get("from_price")
    to_price = request.args.get("to_price")
    cates = utils.load_categories()
    products = utils.load_product(cate_id=cate_id,
                                  kw=kw, from_price=from_price, to_price=to_price)
    return render_template("products.html", products=products, categories=cates)


@app.route("/products/<int:product_id>")
def product_detail(product_id):
    cates = utils.load_categories()
    products = utils.get_product_by_id(product_id)

    return render_template("product_detail.html", products=products, categories=cates)


@app.route("/pay/<int:product_id>")
def pay_product(product_id):
    cates = utils.load_categories()
    products = utils.get_product_by_id(product_id)

    return render_template("pay.html", products=products, categories=cates)


@app.route('/register', methods=['get', 'post'])
def user_register():
    err_mgs = ""
    if request.method.__eq__('POST'):
        name = request.form.get('name')
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        confirm = request.form.get('confirm')

        try:
            if password.strip().__eq__(confirm.strip()):
                utils.add_user(name=name, username=username, password=password, email=email)
                return redirect(url_for('user_signin'))
            else:
                err_mgs = 'Mật khẩu không khớp'
        except Exception as ex:
            err_msg = 'Hệ thống đang lỗi!!!' + str(ex)

    return render_template('register.html', err_msg=err_mgs)


@app.route('/user-login',methods=['get','post'])
def user_signin():
    err_msg=''
    if request.method.__eq__('POST'):
        username=request.form.get('username')
        password = request.form.get('password')

        user = utils.check_login(username=username,password=password)
        if user:
            login_user(user=user)
            return redirect(url_for('home'))
        else:
            err_msg='Tên đăng nhập hoặc mật khẩu không chính xác'

    return render_template('login.html',err_msg=err_msg)


@login.user_loader
def user_load(user_id):
    return  utils.get_user_by_id(user_id=user_id)

@app.route('/user-logout')
def user_signout():
    logout_user()
    return redirect(url_for('user_signin'))

if __name__ == '__main__':
    from tourapp.admin import *
    app.run(debug=True)
