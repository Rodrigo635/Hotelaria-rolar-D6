from django.shortcuts import render
from django.http import JsonResponse
import random

def roll_dice(request):
    result = random.randint(1, 6)
    dice_icons = {
        1: "&#9856;",
        2: "&#9857;",
        3: "&#9858;",
        4: "&#9859;",
        5: "&#9860;",
        6: "&#9861;"
    }
    print(f"rolou: {result}")
    return JsonResponse({'result': result, 'icon': dice_icons[result]})

def home(request):
    return render(request, 'home.html')