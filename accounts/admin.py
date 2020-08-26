from  adminCutomization.admin import admin
from .models import User
from .modeladmin import UserAdmin
# Register your models here.

admin.register(User,UserAdmin)
