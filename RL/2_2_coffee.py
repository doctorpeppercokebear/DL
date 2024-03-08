from flask import Flask, render_template, request

'''
퀴즈
메뉴 주문을 받는 서버를 구축하세요
주문 방법: 이름 , 메뉴
'''
# 메뉴 목록
menus = {
    "라떼"
    "아메리카노"
    "카푸치노"
    "바닐라 라떼"
    "돌체 라뗴"

}

# 주문 목록
orders = []

app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("index.html", menus=menus)
#
# @app.route("/order", methods=["POST"])
# def order():
#     name = request.form["name"]
#     menu = request.form["menu"]
#     option = request.form.get("option")
#     price = menus[menu]
#
#     # 주문 정보 저장
#     orders.append({"name": name, "menu": menu, "option": option, "price": price})
#
#     return render_template("order_complete.html", name=name, menu=menu, option=option, price=price)
#
# @app.route("/orders")
# def orders_list():
#     return render_template("orders.html", orders=orders)
#
# if __name__ == "__main__":
#     app.run(debug=True)

@app.route('/oder')
def order():
    name = request.args.get('name')
    menu = request.args.get('menu')

    orders[name] = menu
    return render_template('coffe_order.html', orders)