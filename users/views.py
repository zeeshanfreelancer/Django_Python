from django.http import JsonResponse


def hello(request):
    return JsonResponse({
        "message": "Hello World"
    })

def profile(request):
    return JsonResponse({
        "name": "Zeeshan",
        "age": 24,
        "role": "Full Stack Developer",
        "experience": "2+ years"
    })