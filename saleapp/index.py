from saleapp import app
from flask import render_template, request
import utils


@app.route("/")
def home():
    cates = utils.load_categories()
    return render_template('index.html', categories=cates)


@app.route("/products")
def products_list():
    cates = utils.load_categories()
    cate_id = request.args.get("category_id")
    kw = request.args.get("keyword")
    fromPrice = request.args.get("fromPrice")
    toPrice = request.args.get("toPrice")
    product = utils.load_products(cate_id, kw=kw, fromPrice=fromPrice, toPrice=toPrice)
    return render_template('products.html', products=product,categories=cates)


@app.route("/products/<int:productsId>")
def productsDetail(productsId):
    cates = utils.load_categories()
    products= utils.getProductsId(productsId)
    return render_template('detail.html', products=products,categories=cates)



if __name__ == '__main__':
    app.run(debug=True)