from django.http import JsonResponse, Http404
import json
from django.views.decorators.csrf import csrf_exempt

menu = {
    "pasta": {"price": 8.99, "available": True},
    "Pizza": {"price": 11, "available": True},
}


# Create your views here.
def getmenu():
    return menu


def display_menu(request):
    if request.method == "GET":
        menu = getmenu()
        return JsonResponse(menu)


@csrf_exempt
def update_menu(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        name = data.get("name")
        avil = data.get("available")

        if name in menu:
            menu[name]["available"] = avil
            return JsonResponse(menu)
        else:
            raise Http404("Dish not found in menu")
    else:
        raise Http404("Invalid request method")


@csrf_exempt
def addnew(request):
    global menu

    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        name = data.get("name")
        price = data.get("price")
        avail = data.get("available")

        if name in menu:
            raise Http404.JsonResponse("Dish is already present")

        menu[name] = {"price": price, "available": avail}
        return JsonResponse({"data": menu})
    else:
        raise Http404.JsonResponse("Invalid request method")

@csrf_exempt
def deletone(request):
    global menu

    if request.method == "DELETE":
        data = json.loads(request.body.decode("utf-8"))
        name = data.get("name")

        if name in menu:
            del menu[name]
            return JsonResponse({"data": menu})
        else:
            raise Http404("Dish is not  present")

    else:
        raise Http404("Invalid request method")
