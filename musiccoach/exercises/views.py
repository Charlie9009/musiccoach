from django.shortcuts import render, redirect
from .models import Exercise
from .forms import ExerciseForm
from datetime import date, timedelta
from django.http import HttpResponse


def index(request):
    today = date.today()
    latest_week = today - timedelta(days=7)
    exercises = Exercise.objects.filter(date__gte=latest_week).order_by('-date')
    total_time = sum([o.time for o in exercises])
    return render(request, 'exercises/index.html', {
        'exercises': exercises,
        'total_time': total_time
    })


def create_exercise(request):
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ExerciseForm()

    return render(request, 'exercises/create_exercise.html', {'form': form})

