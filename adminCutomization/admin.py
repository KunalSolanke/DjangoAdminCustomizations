from django.contrib.admin.sites import AdminSite as BaseAdminSite
from django.template.response import  TemplateResponse
from accounts.models import User,mailing_list
from django.urls import path
from django.shortcuts import redirect,reverse
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings

from django.utils import timezone
# Create your views here.


class AdminSite(BaseAdminSite) :
    def index(self, request, extra_context=None):
        app_list = self.get_app_list(request)

        context = {
            **self.each_context(request),
            'title': self.index_title,
            'app_list': app_list,
            'user_count_1' : User.objects.filter(created_at__gte=timezone.now()-timezone.timedelta(days=1)).count(),
            'user_count_7': User.objects.filter(created_at__gte=timezone.now() - timezone.timedelta(days=7)).count(),
            'user_count_30': User.objects.filter(created_at__gte=timezone.now() - timezone.timedelta(days=30)).count(),

            **(extra_context or {}),
        }

        request.current_app = self.name

        return TemplateResponse(request, self.index_template or 'admin/index.html', context)

    def functions(self,request, extra_context=None):
        context = {
            **self.each_context(request),

            **(extra_context or {}),
        }
        return TemplateResponse(request,'admin/functions.html',context)




    def send_mail(self,request, extra_context=None):
        context = {
            **self.each_context(request),

            **(extra_context or {}),
        }

        send_mail(request.POST['subject'],request.POST['message'],settings.DEFAULT_FROM_EMAIL,mailing_list,fail_silently=True)


        return redirect(reverse('admin:functions'))



    def get_urls(self):
        urls = super(AdminSite,self).get_urls()
        urls+=[
            path('functions/',view= self.functions,name="functions"),
            path('send-mail',view=self.send_mail ,name ="send_mail")
        ]

        return urls


admin = AdminSite(name='admin')