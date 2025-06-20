class CaseInsensitiveMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.path_info = request.path_info.lower()
        response = self.get_response(request)
        return response