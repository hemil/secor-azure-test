from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    response = JsonResponse(
        {
            "hello": "world",
            "The answer is": 42
        }
    )
    return response
