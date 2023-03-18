from tourapp import app, db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from tourapp.models import Product,Category


admin= Admin(app=app,name="Admin hello",template_mode='bootstrap4')

admin.add_view(ModelView(Category, db.session))
admin.add_view(ModelView(Product, db.session))