from flask import render_template, request
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


if __name__ == '__main__':
    app.run(debug=True)