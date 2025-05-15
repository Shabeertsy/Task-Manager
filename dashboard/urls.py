from django.urls import path
from . import views


urlpatterns = [
    path('admin_login/',views.login_view,name='admin_login'),
    path('admin_dashboard/',views.admin,name='admin_dashboard'),
    path('super_admin/',views.super_admin,name='super_admin'),
    path('admin_logout/',views.admin_logout,name='admin_logout'),

    path('assign_users/<int:admin_id>/',views.assign_users,name='assign_users'),
    path('assign_task/<str:task_id>',views.assign_task,name='assign_task'),


    ## manage users 
    path('list_users/',views.list_users,name='list_users'),
    path('add_user/',views.add_user,name='add_user'),
    path('view_user/<int:user_id>',views.view_user,name='view_user'),
    path('update_user/<int:user_id>',views.update_user,name='update_user'),
    path('delete_user/<int:user_id>',views.delete_user,name='delete_user'),
    path('assign_task/<int:user_id>',views.assign_task,name='assign_task'),

    ## manage admin
    path('promote_user/<int:user_id>',views.promote_user,name='promote_user'),
    path('demote_user/<int:user_id>',views.demote_user,name='demote_user'),
    path('create_admin/',views.create_admin,name='create_admin'),
    path('update_admin/<int:user_id>',views.update_admin,name='update_admin'),
    path('delete_admin/<int:user_id>',views.delete_admin,name='delete_admin'),


    ## manage tasks
    path('create_task/',views.create_task,name='create_task'),
    path('delete_task/<str:task_id>/',views.delete_task,name='delete_task'),
    path('view_task/<str:task_id>/',views.view_task,name='view_task'),
    path('update_task/<str:task_id>/',views.update_task,name='update_task'),

    ## task report
    path('task_report/<str:task_id>/',views.view_report,name='task_report'),


    
]
