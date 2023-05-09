from django import urls
from django.urls import path
from . import views


urlpatterns = [
    path("departments", views.dept_get, name="get-data"),
    # path("departments/<int:id>", views.api_methods),
    path("departments-post", views.dept_post),
    path("departments-put/<int:id>", views.dept_put),
    path("departments-delete/<int:id>", views.dept_delete),

    path("employees", views.emp_get, name="get-data"),
    # path("departments/<int:id>", views.api_methods),
    path("employees-post", views.emp_post),
    path("employees-put/<int:id>", views.emp_put),
    path("employees-delete/<int:id>", views.emp_delete),
    path("employees-profile", views.save_profile),
]
