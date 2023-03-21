from sqlalchemy import Column, Integer, String, Float, Enum, Boolean, DateTime, ForeignKey, Date
from sqlalchemy.orm import relationship
from tourapp import db, app
from datetime import datetime
from flask_login import UserMixin
from  enum import Enum as UserEnum

class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)

class UserRole(UserEnum):
    ADMIN = 1
    USER = 2


class User(BaseModel, UserMixin):
    name = Column(String(50),nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable= False)
    email = Column(String(50))
    active = Column(Boolean, default=True)
    joined_date = Column(DateTime, default=datetime.now())
    user_role = Column(Enum(UserRole), default=UserRole.USER)
    Bill = relationship('Bill', backref='user', lazy=False)

    def __str__(self):
        return self.name

class Category(BaseModel):
    __tablename__ = 'category'

    name = Column(String(255), nullable=False)
    products = relationship('Product', backref='category', lazy=False)

    def __str__(self):
        return self.name


class Product(BaseModel):
    __tablename__ = 'product'

    name = Column(String(255), nullable=False)
    time = Column(String(255))
    price_big = Column(Float, default=0)
    price_small = Column(Float, default=0)
    datetime_start = Column(Date, nullable=True)
    datetime_end = Column(Date)
    go_start = Column(String(100), nullable=False)
    go_end = Column(String(100), nullable=False)
    vehicle = Column(String(100), nullable=False)
    image = Column(String(100))
    active = Column(Boolean, default=True)
    created_date = Column(DateTime, default=datetime.now())
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)
    Bill = relationship('Bill', backref='product', lazy=False)

    def __str__(self):
        return self.name


class Bill(BaseModel):
    _tablename_ = 'bill'

    name = Column(String(255))
    email = Column(String(255))
    amount_big = Column(Integer)
    amount_young = Column(Integer)
    phone = Column(Integer)
    address = Column(String(255))
    cccd = Column(Integer)
    pay_date = Column(Date)
    active = Column(Boolean, default=True)
    product_id = Column(Integer, ForeignKey(Product.id), nullable=False)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    total = Column(Integer)

    def __str__(self):
        return self.name


if __name__ == '__main__':
    with app.app_context():
        # db.create_all()
        # c1 = Category(name='MIỀN BẮC')
        # c2 = Category(name='MIỀN NAM')
        # c3 = Category(name='MIỀN TRUNG')
        #
        # db.session.add_all([c1,c2,c3])
        #
        # p1 = Product(name="DU LỊCH ĐẢO PHÚ QUỐC", time="4 ngày 3 đêm", price_big=7779, price_small=3889,
        #              datetime_start="2023-03-09", datetime_end="2023-03-13", go_start="TP. Hồ Chí Minh",
        #              go_end="Đà lạt", vehicle="Đi về bằng xe", image="images/anh1.jpg", category_id=1)
        #
        # p2 = Product(name="DU LỊCH ĐÀ NẴNG", time="2 ngày 2 đêm", price_big=4079, price_small=2040,
        #              datetime_start="2023-03-09", datetime_end="2023-03-13", go_start="TP. Hồ Chí Minh",
        #              go_end="Nha Trang", vehicle="Đi về bằng xe", image="images/anh2.jpg",
        #              category_id=2)
        #
        # p3 = Product(name="DU LỊCH ĐÀ LẠT", time="3 ngày 3 đêm", price_big=47790, price_small=2390,
        #              datetime_start="2023-03-09", datetime_end="2023-03-13", go_start="TP. Hồ Chí Minh",
        #              go_end="Miền Tây", vehicle="Đi về bằng xe", image="images/anh3.png", category_id=3)
        #
        # p4 = Product(name="DU LỊCH SAPA", time="2 ngày 1 đêm", price_big=5779, price_small=3260,
        #              datetime_start="2023-03-10", datetime_end="2023-03-13", go_start="TP. Hồ Chí Minh",
        #              go_end="Hội An - Đà Nẵng", vehicle="Hàng không Vietname Aỉlines",
        #              image="images/anh4.jpg", category_id=1)
        #
        # p5 = Product(name="DU LỊCH NHA TRANG", time="2 ngày 3 đêm", price_big=3779, price_small=1890,
        #              datetime_start="2023-03-11", datetime_end="2023-03-14", go_start="TP. Hồ Chí Minh",
        #              go_end="Đà Lạt", vehicle="Đi về bằng xe",
        #              image="images/anh5.jpg", category_id=2)
        #
        # p6 = Product(name="DU LỊCH HẠ LONG", time="3 ngày 2 đêm", price_big=4339, price_small=3120,
        #              datetime_start="2023-03-14", datetime_end="2023-03-17", go_start="TP. Hồ Chí Minh",
        #              go_end="Phú Quốc", vehicle="Hàng không Vietname Aỉlines",
        #              image="images/anh6.jpg", category_id=3)
        #
        # p7 = Product(name="DU LỊCH PHÚ YÊN", time="2 ngày 3 đêm", price_big=2779, price_small=1990,
        #              datetime_start="2023-03-15", datetime_end="2023-03-20", go_start="TP. Hồ Chí Minh",
        #              go_end="Đà Lạt", vehicle="Đi về bằng xe",
        #              image="images/anh7.jpg", category_id=1)
        #
        # p8 = Product(name="DU LỊCH HUẾ", time="3 ngày 4 đêm", price_big=4779, price_small=2990,
        #              datetime_start="2023-03-15", datetime_end="2023-03-20", go_start="TP. Hồ Chí Minh",
        #              go_end="Đà Lạt", vehicle="Đi về bằng xe",
        #              image="images/anh8.jpg", category_id=2)
        #
        # p9 = Product(name="DU LỊCH TÂY NGUYÊN", time="4 ngày 5 đêm", price_big=5779, price_small=3990,
        #              datetime_start="2023-03-15", datetime_end="2023-03-20", go_start="TP. Hồ Chí Minh",
        #              go_end="Đà Lạt", vehicle="Đi về bằng xe",
        #              image="images/anh9.jpg", category_id=3)
        #
        # p10 = Product(name="DU LỊCH MỸ THO", time="2 ngày 1 đêm", price_big=2779, price_small=1990,
        #              datetime_start="2023-03-15", datetime_end="2023-03-20", go_start="TP. Hồ Chí Minh",
        #              go_end="Đà Lạt", vehicle="Đi về bằng xe",
        #              image="images/anh10.jpg", category_id=1)
        #
        # p11 = Product(name="DU LỊCH HỘI AN", time="2 ngày 1 đêm", price_big=2290, price_small=1290,
        #               datetime_start="2023-03-15", datetime_end="2023-03-20", go_start="TP. Hồ Chí Minh",
        #               go_end="Đà Lạt", vehicle="Đi về bằng xe",
        #               image="images/anh11.jpg", category_id=1)
        #
        # p12 = Product(name="DU LỊCH HÀ GIANG", time="3 ngày 2 đêm", price_big=4290, price_small=2290,
        #               datetime_start="2023-03-15", datetime_end="2023-03-20", go_start="TP. Hồ Chí Minh",
        #               go_end="Đà Lạt", vehicle="Đi về bằng xe",
        #               image="images/anh12.jpg", category_id=1)
        # db.session.add_all([p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12])
        # db.session.commit()
        u1 = User(name='Lê Văn Lâm', username='Lâm', password='c4ca4238a0b923820dcc509a6f75849b', email='levanlam@ou.edu.vn')
        u2 = User(name='Huỳnh Minh Hoàng', username='Hoàng', password='c81e728d9d4c2f636f067f89cc14862c', email='hmh20172018@ou.edu.vn')
        db.session.add(u1)
        db.session.add(u2)
        b1 = Bill(name="Lê Văn Lâm", email="levanlam@ou.edu.vn",amount_young=7,phone="0966287704",address="8929 vườn Lài",cccd="28218",pay_date=datetime.now(),total=7500,product_id=1, user_id=1)
        b2 = Bill(name="Huỳnh Minh Hoàng", email="hmh20172018@ou.edu.vn", amount_young=6, phone="0364121547",address="635 Phan Văn Trị", cccd="21547",pay_date=datetime.now(), total=5000, product_id=2,  user_id=2)
        b3 = Bill(name="Lê Văn Lâm", email="levanlam@ou.edu.vn", amount_young=2, phone="0966287704",address="8929 vườn Lài", cccd="28218",pay_date=datetime.now(), total=9500, product_id=1,  user_id=1)
        db.session.add_all([b1,b2,b3])
        db.session.commit()
