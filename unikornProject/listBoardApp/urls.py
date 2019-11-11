from django.urls import path
from .import views


urlpatterns = [
    #/listBoard url에 리스트게시판 형식의 페이지가 보이도록 설정
    path('',views.listBoard,name='listBoard'),
    path('new',views.listBoardNew,name='new'),
    # path('create',views.communitycreate,name='create'),
    path('show/<int:post_id>',views.listBoardShow,name='show'),
    path('edit/<int:post_id>',views.listBoardEdit,name='edit'),
    path('update/<int:post_id>',views.listBoardUpdate,name='update'),
    path('delete/<int:post_id>',views.listBoardDelete,name='delete'),
    path('commentcreate/<int:post_id>',views.commentcreate,name='comentcreate'),
    path('commentdelete/<int:post_id>/<int:comment_id>',views.commentdelete,name='comentdelete'),
    
]