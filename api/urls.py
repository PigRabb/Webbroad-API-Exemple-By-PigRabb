
from django.urls import path,include
from .views import CreatePost,CreateComment,ListALLPost,ListPostWithPostId,ListALLPostWithUserId,ListComment,EditComment,EditPost

urlpatterns = [
    path('post/create', CreatePost),
    path('post/comment/create', CreateComment),
    path('post/show/post_id',ListPostWithPostId),
    path('post/show/user_id',ListALLPostWithUserId),
    path('post/show/all',ListALLPost),
    path('post/comment/show',ListComment),
    path('post/edit',EditPost),
    path('post/comment/edit', EditComment),

]
