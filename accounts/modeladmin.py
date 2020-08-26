from django.contrib.auth.admin import UserAdmin as BaseUserAdmin




class UserAdmin(BaseUserAdmin):

    list_display = ('username', 'created_at')
    list_filter = ('created_at',)



    def change_status(self,request,queryset):
        for obj in queryset  :
            if obj.is_active :
                obj.is_active=False
            else :
                obj.is_active = True
            obj.save()



    actions = ['change_status']

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    # change_list_template = "admin/users_list_template.html"
    search_fields = ('username',)
    ordering = ('-created_at',)








