from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

#
# class AdminUserPermissionMixin:
#     def has_view_permission(self, request, obj=None):
#         return request.user.is_admin
#
#     def has_add_permission(self, request):
#         return request.user.is_admin
#
#     def has_change_permission(self, request, obj=None):
#         return request.user.is_admin
#
#     def has_delete_permission(self, request, obj=None):
#         return request.user.is_admin
#
#     def has_module_permission(self, request):
#         return request.user.is_admin
#
#
# class FirstAdmin(AdminUserPermissionMixin, admin.ModelAdmin):
#     list_display = (
#         'id',
#         'title',
#         'author'
#     )
#
#
# class SecondAdmin(AdminUserPermissionMixin, admin.ModelAdmin):
#     list_display = (
#         'id',
#         'category',
#     )


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email',)


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ('username', 'last_name', 'first_name', 'email', 'is_staff', 'is_active',)
    list_filter = ('username', 'email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'role', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
# admin.site.register(FirstAdmin)
