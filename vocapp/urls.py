from django.urls import path

from . import views

app_name = "vocapp"
urlpatterns = [
	path("", views.redir_home, name="redir_home"),
	path("home", views.home, name="home"),
	path("search", views.search, name="search"),
	path("expression/<int:expression_id>", views.inspect_expression, name="inspect_expression"),
	path("find_expression", views.find_expression, name="find_expression"),
	path("dashboard", views.dashboard, name="dashboard"),
	path("login", views.login, name="login"),
	path("signin", views.signin, name="signin"),
	path("validation", views.validation, name="validation")	
]