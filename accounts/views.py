from django.shortcuts import render
from django.contrib.admin.sites import AdminSite as BaseAdminSite
from django.template.response import  TemplateResponse
from .models import *
from django.utils import timezone
# Create your views here.


class AdminSite(BaseAdminSite) :
    def index(self, request, extra_context=None):
        app_list = self.get_app_list(request)

        context = {
            **self.each_context(request),
            'title': self.index_title,
            'app_list': app_list,
            'user_count_1' : User.objects.filter(created_at__gte=timezone.now()-timezone.timedelta(days=1))

            **(extra_context or {}),
        }

        request.current_app = self.name

        return TemplateResponse(request, self.index_template or 'admin/index.html', context)


admin = AdminSite(name='admin')