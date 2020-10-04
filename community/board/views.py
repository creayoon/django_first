from django.shortcuts import render, redirect
from django.http import Http404
from django.core.paginator import Paginator
from .models import Board
from user.models import User
from .forms import BoardForm


def board_detail(request, pk):
    print('pk::: ', pk, type(pk))
    
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다')

    print('contents:::', board.contents)
    return render(request, 'board_detail.html', {'board':board})

def board_write(request):
    if not request.session.get('user'):
         return redirect('/user/login')

    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            user = User.objects.get(pk=user_id)

            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = user
            board.save()

            return redirect('/board/list/')
    else:
        form = BoardForm()
    return render(request, 'board_write.html', {'form':form})
 
def board_list(request):
    all_boards = Board.objects.all().order_by('-id') # id 역순으로 정렬, 시간역순, 최신글이 최상단
    page = int(request.GET.get('p', 1))
    paginator = Paginator(all_boards, 3) # 1page당 게시글 갯수

    boards = paginator.get_page(page)
    return render(request, 'board_list.html', {'boards':boards})
