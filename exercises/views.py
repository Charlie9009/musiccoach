from django.shortcuts import render, redirect
from .models import Exercise
from .forms import ExerciseForm
from datetime import date, timedelta
from django.http import HttpResponse
from django.db.models import Sum
from django.utils import timezone


def index(request):
    today = timezone.now().date()
    latest_week = [
            today - timedelta(days=i) for i in range(6, -1, -1)
        ]  # last 7 days

    # Create a dict with total time per day
    data = []
    for day in latest_week:
        total = Exercise.objects.filter(
                date=day
            ).aggregate(Sum('time'))['time__sum'] or 0
        data.append({"date": day.strftime("%a"), "time": total})

    exercises = Exercise.objects.filter(
            date__gte=latest_week[0]
        ).order_by('-date')
    total_time = sum([o.time for o in exercises])

    return render(request, 'exercises/index.html', {
        'exercises': exercises,
        'total_time': total_time,
        'chart_labels': [d["date"] for d in data],
        'chart_data': [d["time"] for d in data],
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
