# Create your views here.
from rest_framework.decorators import APIView, api_view
from rest_framework.response import Response

@api_view(["GET"])
def hello_world(request):
    name = request.query_params.get("name", "user not found")
    return Response({"message": f"Hello, {name}!"})

class HelloWorldView(APIView):
    def get(self, request):
        name = request.query_params.get("name", "user not found")
        return Response({"message": f"Hello, {name}!"})
    
    def post(self, request):
        name = request.data.get("name", "user not found")
        return Response({"message": f"Hello, {name}! (POST request)"})  