from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Posting,PostingComment,Notice
from django.contrib.auth.models import User
from .forms import listBoardCreate

# Create your views here.
#리스트게시판 페이지 보여주는 함수
def listBoard(request):
    posts = Posting.objects.all()
    paginator = Paginator(posts,10) 
    page = request.GET.get('page')
    page_posts = paginator.get_page(page)

    return render(request,'listBoard.html',{'page_posts':page_posts})

def listBoardNew(request):
        if request.method == 'POST': 
                form = listBoardCreate(request.POST)
                
                if form.is_valid():
                        posting = form.save(commit=False)
                        posting.author = request.user
                        posting.save()
                        return redirect('/listBoard')
                else:
                        return redirect('/')
        else:
                form = listBoardCreate()
                return render(request, 'listBoardNew.html', {'form': form})

def listBoardShow(request,post_id):
    one_post = get_object_or_404(Posting,id=post_id)
    comments = one_post.postingcomment_set.all()
    return render(request,'listBoardShow.html',{'posts':one_post,'comment':comments})

def listBoardEdit(request, post_id):
    if request.method == "POST":
        #수정 저장
        one_post = Posting.objects.get(pk = post_id)
        form = listBoardCreate(request.POST, instance=one_post)
        if form.is_valid():
             form.save()
             return redirect('/listBoard/show/'+str(one_post.id))
    else:
        #수정 입력
        one_post = Posting.objects.get(pk = post_id)
        if one_post.author == User.objects.get(username = request.user.get_username()):
                one_post = Posting.objects.get(pk = post_id)
                form = listBoardCreate(instance = one_post)
                return render(request, 'listBoardEdit.html', {'posts' : one_post, 'form' : form})
        else:
                return redirectForm(request, 'Not allow edit this post!') 


def listBoardUpdate(request,post_id):
    if(request.method == 'POST'):
        one_post = get_object_or_404(Posting,id=post_id)
        one_post.title = request.POST['title']
        one_post.content = request.POST['content']
        one_post.save()

        return redirect('/listBoard/show/'+str(one_post.id))

def listBoardDelete(request, post_id):
    one_post = Posting.objects.get(pk = post_id)
    if one_post.author == User.objects.get(username = request.user.get_username()):
        one_post.delete()
        return redirect('/listBoard')
    else:
        return redirectForm(request, 'Not allow delete this post!' )


def commentcreate(request,post_id):
    if(request.method == 'POST'):
        one_post = get_object_or_404(Posting,id=post_id)
        one_post.postingcomment_set.create(content=request.POST['comment_content'],author=request.POST['comm_nm'])
    return redirect('/listBoard/show/'+str(post_id))

def commentdelete(request,post_id,comment_id):
        one_comment = get_object_or_404(PostingComment,id=comment_id,posting=post_id)
        one_comment = get_object_or_404(PostingComment,id=comment_id,posting=post_id)
        one_comment.delete()
        return redirect('/listBoard/show/'+str(post_id))
        

def redirectForm(request,msg):
        return render(request, 'redirect.html', {'msg': msg})