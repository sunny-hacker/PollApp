from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from .forms import CreateForm, EditForm, DeleteForm, DeleteAllForm
from .models import Poll


# Creating a Sample Poll
def create_sample_poll(poll):
    poll.poll_question = 'This is a Sample Poll'
    poll.poll_option1 = 'Choice 1'
    poll.poll_option2 = 'Choice 2'
    poll.poll_option3 = 'Choice 3'
    poll.poll_option1_count = 0
    poll.poll_option2_count = 0
    poll.poll_option3_count = 0

    poll.save()


# Home Page
def home(request):
    polls = Poll.objects.all()

    if polls.count() == 0:
        poll = Poll()
        create_sample_poll(poll)

    context = {
        'polls': polls
    }
    return render(request, 'poll/home.html', context)


# Create a New Poll
def create(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()

            # Remove Sample Poll When there is a Poll
            if Poll.objects.filter(poll_question='This is a Sample Poll').exists():
                Poll.objects.get(poll_question='This is a Sample Poll').delete()
            return redirect('home')
        else:
            print('Invalid Form')
            return redirect('create')
    else:
        form = CreateForm()
        context = {
            'form': form
        }
        return render(request, 'poll/create.html', context)


# Edit an Existing Poll
def edit(request, poll_id):
    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        return HttpResponseNotFound('<h1> Page Not Found</h1>')

    if request.method == 'POST':
        form = EditForm(request.POST)
        if form.is_valid():
            poll.poll_question = form.cleaned_data['poll_question']
            poll.poll_option1 = form.cleaned_data['poll_option1']
            poll.poll_option2 = form.cleaned_data['poll_option2']
            poll.poll_option3 = form.cleaned_data['poll_option3']
            poll.poll_option1_count = poll.poll_option2_count = poll.poll_option3_count = 0
            poll.save()
            return redirect('home')
    else:
        form = EditForm()
        context = {
            'form': form
        }
        return render(request, 'poll/edit.html', context)


# Delete an Existing Poll
def delete(request, poll_id):
    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        return HttpResponseNotFound('<h1> Page Not Found</h1>')

    if request.method == 'POST':
        option = request.POST['delete']
        if option == "YES":
            poll.delete()

        return redirect('home')
    else:
        form = DeleteForm()
        context = {
            'form': form
        }
        return render(request, 'poll/delete.html', context)


# Delete All Polls
def delete_all(request):
    if request.method == 'POST':
        option = request.POST['delete']
        if option == "YES":
            Poll.objects.all().delete()

        return redirect('home')
    else:
        form = DeleteAllForm()
        context = {
            'form': form
        }
        return render(request, 'poll/deleteAll.html', context)


# Vote for a Particular Poll
def vote(request, poll_id):
    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        return HttpResponseNotFound('<h1> Page Not Found</h1>')

    if request.method == 'POST':
        option = request.POST['poll']
        if option == "option1":
            poll.poll_option1_count += 1
        elif option == "option2":
            poll.poll_option2_count += 1
        elif option == "option3":
            poll.poll_option3_count += 1
        else:
            return HttpResponse('Invalid Form')
        poll.save()
        return redirect(results, poll_id)
    else:
        context = {
            'poll': poll
        }
        return render(request, 'poll/vote.html', context)


# Result of a Poll
def results(request, poll_id):
    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        return HttpResponseNotFound('<h1> Page Not Found</h1>')

    context = {
        'poll': poll
    }
    return render(request, 'poll/results.html', context)
