from django.urls import path
from blog import views
# url 규칙
urlpatterns = [
    path("", views.index, name="index"),
    path("post/<int:pk>", views.PostDetailView.as_view(), name="post"),
    path("post/create", views.PostCreate.as_view(), name="post_create"),
    path("post/delete/<int:pk>", views.PostDelete.as_view(), name="post_delete"),
    path("post/update/<int:pk>", views.PostUpdate.as_view(), name="post_update"),
]
