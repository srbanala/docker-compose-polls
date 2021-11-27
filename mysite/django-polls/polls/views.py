from django.shortcuts import render, get_object_or_404
from .models import Question,Choice
# Create your views here.


from django.http import HttpResponse,HttpResponseRedirect,Http404
#from django.http import HttpResponseRedirect
#from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone


###Function base view#####
#def index(request):
	#latest_question_list=Question.objects.order_by('pub_date')[:5]
	#template=loader.get_template('polls/index.html')
	#context={
	#     'latest_question_list':latest_question_list,
	#	}
	
	#return HttpResponse(template.render(context,request))
	#context={'latest_question_list':latest_question_list}
	#return render(request,'polls/index.html',context)

class Indexview(generic.ListView):
	template_name='polls/index.html'
	context_object_name='latest_question_list'

	def get_queryset(self):
		return Question.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')[:5]
	
	
def detail(request, question_id):
	#try:
	#	question=Question.objects.get(pk=question_id)
	#except Question.DoesNotExist:
	#	raise Http404("Question does not exist.")
	question=get_object_or_404(Question,pk=question_id)
	return render(request,'polls/detail.html',{'question':question})

def results(request, question_id):
	question=get_object_or_404(Question,pk=question_id)
	return render(request,'polls/results.html',{'question':question})


def vote(request, question_id):
	question=get_object_or_404(Question,pk=question_id)
	try:
		selected_choice=question.choice_set.get(pk=request.POST['choice'])
	except(KeyError,Choice.DoesNotExist):
		return render(request,'polls/detail.html',{
			'question':question,
			'error_message':"You didn't select a choice.",
			})
	else:
		selected_choice.votes+=1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))


