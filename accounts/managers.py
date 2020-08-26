
from django.contrib.auth.base_user import BaseUserManager




class UserManager(BaseUserManager) :

    def create_user(self,username,password):
        user = self.model(username= username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,password):
        user = self.create_user(username,password)

        user.is_superuser=True
        user.is_admin =True
        user.is_staff=True
        user.save(using=self._db)
        return user
