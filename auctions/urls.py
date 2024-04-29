from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("see_list/<int:pk>", views.see_list, name="see_list"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("bid", views.make_bid, name="bid"),
    path("close_bid", views.close_bid, name="close_bid"),
    path("categories", views.categories, name="categories"),
    path("comments", views.comments_made , name="comments")
]
