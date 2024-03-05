from django.urls import path

from . import views

app_name = "vocapp"
urlpatterns = [
	path("", views.redir_home, name="redir_home"),
	path("home", views.home, name="home"),
	path("search", views.search, name="search"),
	path("expression/<int:expression_id>", views.inspect_expression, name="inspect_expression"),
	path("dashboard", views.dashboard, name="dashboard"),
	path("login", views.login_user, name="login_user"),
	path("signup", views.signup, name="signup"),
	path("logout", views.logout_user, name="logout_user"),
	path("adjust_confidence/<int:expression_id>", views.adjust_confidence, name="adjust_confidence"),
]