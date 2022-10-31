import json, os
from saleapp import app

def load_categories():
    with open('%s/data/categories.json' % app.root_path, encoding='utf-8') as f:
        return json.load(f)


def load_products(category_id=None, kw=None, fromPrice = None, toPrice = None):
    with open('%s/data/products.json' % app.root_path, encoding='utf-8') as f:
        products = json.load(f)
    if category_id:
        products = [p for p in products if p['category_id'] == int(category_id)]
    if kw:
        products = [p for p in products if p['name'].lower().find(kw.lower()) >= 0]
    if fromPrice:
        products = [p for p in products if p['price'] >= float(fromPrice)]
    if toPrice:
        products = [p for p in products if p['price'] <= float(toPrice)]
    return products

def getProductsId(productsId):
    with open('%s/data/products.json' % app.root_path, encoding='utf-8') as f:
        products = json.load(f)
    for p in products:
         if p['id'] == productsId:
             return p


