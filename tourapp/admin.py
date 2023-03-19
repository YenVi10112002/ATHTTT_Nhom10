from flask import redirect
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import logout_user, current_user

from tourapp import app, db
from tourapp.models import Product, Category,UserRole

admin = Admin(app=app, name="Admin hello", template_mode='bootstrap4')


class AuthenticatedModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated \
               and current_user.user_role.__eq__(UserRole.ADMIN)


class ProductView(AuthenticatedModelView):
    can_view_details = True
    can_export = True
    column_searchable_list = ['name', 'time']
    column_filters = ['name', 'price_big', 'price_small']



class LogoutView(BaseView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')

    def is_accessible(self):
        return current_user.is_authenticated


admin.add_view(AuthenticatedModelView(Category, db.session))
admin.add_view(ProductView(Product, db.session))
admin.add_view(LogoutView(name='Logout'))
