from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.


def polls_page(request):
    poll = Poll.objects.all()
    context = {'polls': poll}
    return render(request, 'polls.html', context)


def questions_page(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    question = poll.question_set.all()
    context = {'questions': question}
    return render(request, 'questions.html', context)



def choiceanswer_page(request, question_id):
    question = Question.objects.get(id=question_id)
    choiceanswer = question.choiceanswer_set.all()
    form = AnswerForm(initial={'question': question})
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            form.save()
            if form.cleaned_data['answer'] == question.true_answer:
                question.poll.points += 1
                question.poll.save()

    context = {'choiceanswers': choiceanswer, 'questions': question, 'form': form}
    return render(request, 'answer.html', context)


