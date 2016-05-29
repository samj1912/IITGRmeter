from django.shortcuts import get_object_or_404, render
from .models import Board
# Create your views here.
def home(request):
	boards = Board.objects.all().order_by("title")
	context = {
	'boards' : boards,
	'color' : 'cyan',
	}
	return render(request,'base.html',context)

def board(request,boardreq):
	boards = Board.objects.all().order_by("title")
	board = get_object_or_404(Board,title=boardreq)
	reps = board.representative_set.all()
	a=(
		('C','Completed'),
		('WIP','In Progress'),
		('NS','Not Started'),
		('B','Broken'),
		)
	textcol = {
	'C' : 'teal',
	'WIP' : 'text-accent-4 yellow' , 
	'NS' : 'grey',
	'B' :'red',
	}
	icons = {
	'C' : 'done_all',
	'WIP' : 'trending_up' , 
	'NS' : 'av_timer',
	'B' :'warning',
	}
	context = {
	'boards' : boards,
	'curr_board' : board,
	'reps' : reps,

	'color' : 'cyan',
	'status' : a,
	'textcol' : textcol,
	'icons' : icons,
	}
	return render(request, 'board.html',context)