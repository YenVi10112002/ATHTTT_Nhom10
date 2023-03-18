import paypalrestsdk
from flask import render_template, request, session, redirect, url_for, jsonify
from tourapp import app
import utils


@app.route("/")
def home():
    cats = utils.load_categories()
    products = utils.load_product()
    return render_template('index.html', categories=cats,
                           products=products)


@app.route("/products")
def product_list():
    cate_id = request.args.get("category_id")
    kw = request.args.get("Keyword")
    from_price=request.args.get("from_price")
    to_price=request.args.get("to_price")
    cates = utils.load_categories()
    products = utils.load_product(cate_id=cate_id,
                                  kw=kw,from_price=from_price, to_price=to_price)
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


@app.route('/payment/<product_id>', methods=['GET', 'POST'])
def payment(product_id):
    msg = ''
    if request.method.__eq__('POST'):
        name = request.form['name']
        email = request.form['email']
        amount = request.form['amount']
        phone = request.form['phone']
        address = request.form['address']
        cccd = request.form['cccd']
        product_id = product_id
        price_big = request.form['price_big']
        session['price'] = float(price_big) * float(amount)

        # return render_template('Paypal.html', msg=msg)
        # Tạo một Payment với các thông tin cần thiết
        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal"
            },
            "transactions": [{
                "amount": {
                    "total": session['price'],
                    "currency": "USD"
                },
                "description": "Mua hàng trên Flask Shop"
            }],
            "redirect_urls": {
                "return_url": url_for('success', _external=True),
                "cancel_url": url_for('pay_product', product_id=product_id, _external=True)
            }
        })

        # Lưu thông tin Payment
        if payment.create():
            # Lưu Payment ID vào session
            session['payment_id'] = payment.id
            # Redirect user đến trang thanh toán của PayPal
            for link in payment.links:
                if link.method == 'REDIRECT':
                    redirect_url = str(link.href)
                    try:
                        utils.add_bill(name=name,
                                       email=email,
                                       amount=amount,
                                       phone=phone,
                                       address=address,
                                       cccd=cccd,
                                       product_id=product_id)
                        msg = 'Thanh cong'
                    except:
                        msg = 'Khong thanh cong'
                    return redirect(redirect_url)
        else:
            return "Lỗi trong quá trình tạo Payment"


@app.route('/success')
def success():
    # Lấy Payment ID từ session
    payment_id = session.get('payment_id')

    # Xác nhận thanh toán với PayPal
    payment = paypalrestsdk.Payment.find(payment_id)
    if payment.execute({"payer_id": payment.payer.payer_info.payer_id}):
        # Thanh toán thành công, hiển thị trang hoàn tất thanh toán
        return redirect(url_for('home'))
    else:
        return "Lỗi trong quá trình xác nhận thanh toán"


if __name__ == '__main__':
    app.run(debug=True)