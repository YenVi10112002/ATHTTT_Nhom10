from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey, Date
from sqlalchemy.orm import relationship
from tourapp import db, app
from datetime import datetime


class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)


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

    def __str__(self):
        return self.name


if __name__ == '__main__':
    with app.app_context():
        # db.create_all()
        # c1 = Category(name='TOUR DU LỊCH')
        # c2 = Category(name='DỊCH VỤ')
        # c3 = Category(name='LIÊN HỆ')
        #
        # db.session.add_all([c1,c2,c3])

        #
        p1 = Product(name="Du lịch Đà Lạt", time="4 ngày 3 đêm", price_big=3779000, price_small=1889000,
                     datetime_start="2023-03-09", datetime_end="2023-03-13", go_start="TP. Hồ Chí Minh",
                     go_end="Đà lạt", vehicle="Đi về bằng xe", image="images/MaiLinhCafe_1220690695.jpg", category_id=1)
        p2 = Product(name="Du lịch Nha Trang", time="4 ngày 3 đêm", price_big=4079000, price_small=2040000,
                     datetime_start="2023-03-09", datetime_end="2023-03-13", go_start="TP. Hồ Chí Minh",
                     go_end="Nha Trang", vehicle="Đi về bằng xe", image="images/Nha-Trang-resorts_487229248.jpg",
                     category_id=2)
        p3 = Product(name="Du lịch Mỹ Tho", time="4 ngày 3 đêm", price_big=4779000, price_small=2390000,
                     datetime_start="2023-03-09", datetime_end="2023-03-13", go_start="TP. Hồ Chí Minh",
                     go_end="Miền Tây", vehicle="Đi về bằng xe", image="images/CA-mau-Dat-mui.jpg", category_id=1)
        p4 = Product(name="Du lịch tại Đà Nẵng", time="3 ngày 2 đêm", price_big=5779000, price_small=3260000,
                     datetime_start="2023-03-10", datetime_end="2023-03-13", go_start="TP. Hồ Chí Minh",
                     go_end="Hội An - Đà Nẵng", vehicle="Hàng không Vietname Aỉlines",
                     image="images/Dragon-River-Bridge_676759177.jpg", category_id=3)
        p5 = Product(name="Du lịch Đà Lạt", time="4 ngày 3 đêm", price_big=3779000, price_small=1890000,
                     datetime_start="2023-03-11", datetime_end="2023-03-14", go_start="TP. Hồ Chí Minh",
                     go_end="Đà Lạt", vehicle="Đi về bằng xe",
                     image="images/DaLat-CauDatFarm_1106355956.jpg", category_id=1)
        p6 = Product(name="Du lịch Phú Quốc", time="3 ngày 2 đêm", price_big=4339000, price_small=3120000,
                     datetime_start="2023-03-14", datetime_end="2023-03-17", go_start="TP. Hồ Chí Minh",
                     go_end="Phú Quốc", vehicle="Hàng không Vietname Aỉlines",
                     image="images/DaLat-CauDatFarm_1106355956.jpg", category_id=4)
        p7 = Product(name="Du lịch Buôn Ma Thuột", time="5 ngày 4 đêm", price_big=5779000, price_small=2990000,
                     datetime_start="2023-03-15", datetime_end="2023-03-20", go_start="TP. Hồ Chí Minh",
                     go_end="Đà Lạt", vehicle="Đi về bằng xe",
                     image="images/DaLat-CauDatFarm_1106355956.jpg", category_id=4)

        db.session.add_all([p1, p2, p3, p4, p5])
        db.session.commit()
