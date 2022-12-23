from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePost.as_view(), name='home'),
    # path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    # path('category/<int:category_id>/', get_category, name='category'),
    path('category/<int:category_id>/', PostsByCategory.as_view(), name='category'),
    # path('post/add_post/', add_post, name='add_post'),
    path('post/add_post/', AddPost.as_view(), name='add_post'),
]