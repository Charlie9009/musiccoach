from django.shortcuts import render, redirect
from .models import Exercise
from .forms import ExerciseForm
from datetime import date, timedelta
from django.http import HttpResponse
from django.db.models import Sum
from django.utils import timezone


def index(request):
    today = date.today()
    latest_week = today - timedelta(days=7)
    exercises = Exercise.objects.filter(date__gte=latest_week).order_by('date')

    # group minutes by date
    chart_labels = [ex.date.strftime("%a") for ex in exercises]
    chart_data = [ex.time for ex in exercises]

    total_time = sum(chart_data)

    return render(request, "exercises/index.html", {
        "exercises": exercises,
        "total_time": total_time,
        "chart_labels": chart_labels,
        "chart_data": chart_data,
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
