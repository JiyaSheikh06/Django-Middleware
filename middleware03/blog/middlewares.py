from django.shortcuts import HttpResponse
class BrotherMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("One Time Brother Initialization")

    def __call__(self,request):
        print("This is Brother Before View")
        response = self.get_response(request)
        print("This is Brother After view")
        return response
    

class FatherMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("One Time Father Initialization")

    def __call__(self,request):
        print("This is Father Before View")
       #response = self.get_response(request)
        response = HttpResponse("Exit")
        print("This is Father After view")
        return response
    

class MotherMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("One Time Mother Initialization")

    def __call__(self,request):
        print("This is Mother Before View")
        response = self.get_response(request)
        print("This is Mother After view")
        return response
    