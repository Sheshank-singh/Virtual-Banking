from django.urls import path
from . import views

app_name = "profiles"

urlpatterns = [
    path("dashboard", views.display_menu, name="dashboard"),
    path("redirect_from_dashboard", views.get_function_chosen, name="get_function_chosen"),
    path("account_management", views.account_management, name="account_management"),
    path("process_account_action", views.get_account_action, name="get_account_action"),
    path("withdraw", views.withdraw, name="withdraw"),
    path("deposit", views.deposit, name="deposit"),
    path("stat_gen", views.stat_gen, name="stat_gen"),
    path("get_stat_gen", views.get_transaction_action, name="get_transaction_action"),
    path("show_ecs_options", views.show_ecs_options, name="show_ecs_options"),
    path("redirect_ecs", views.redirect_ecs, name="redirect_ecs"),
    path("start_ecs", views.start_ecs, name="start_ecs"),
    path("store_new_ecs_data", views.store_new_ecs_data, name="store_new_ecs_data"),
    path("show_due_bills", views.show_due_bills, name="show_due_bills"),
    path("pay_bill", views.pay_bill, name="pay_bill"),
]