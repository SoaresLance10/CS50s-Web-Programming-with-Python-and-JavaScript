from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("CreateListing/<username>", views.new_listing, name="new"),
    path("listings/<int:id>",views.listingpage,name="listingpage"),
    path("bidsubmit/<int:listing_id>",views.bidsubmit,name="bidsubmit"),
    path("cmntsubmit/<int:listing_id>",views.cmntsubmit,name="cmntsubmit"),
	path("categories", views.categories, name="categories"),
    path("category/<str:category>", views.category, name="category"),
    path("create", views.create, name="create"),
    path("addwatchlist/<int:listing_id>",views.addwatchlist,name="addwatchlist"),
    path("removewatchlist/<int:listing_id>",views.removewatchlist,name="removewatchlist"),
    path("watchlist/<str:username>",views.watchlistpage,name="watchlistpage"),
    path("closebid/<int:listing_id>",views.closebid,name="closebid"),
    path("mywinnings",views.mywinnings,name="mywinnings")
]
