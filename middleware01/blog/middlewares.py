def my_middleware(get_response):
    print("One Time Initialization")

    def my_function(request):
        print("This is Before View")
        response = get_response(request)
        print("This is After view")
        return response
    return my_function
