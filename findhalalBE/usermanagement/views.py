# usermanagement/views.py
import json
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login
from .models import CustomUser  # Import your custom user model

@method_decorator(csrf_exempt, name='dispatch')
class RegisterView(View):
    def post(self, request):
        try:
            # Parse the JSON request body
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')

            # Create a new user
            user = CustomUser.objects.create_user(username=username, password=password)
            user.save()

            return JsonResponse({'message': 'User registered successfully!'}, status=201)
        except IntegrityError:
            return JsonResponse({'error': 'Username already exists.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):
    def post(self, request):
        try:
            # Parse the JSON request body
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')

            # Authenticate the user
            user = authenticate(request, username=username, password=password)
            print("user",user)
            if user is not None:
                # Log the user in
                login(request, user)
                return JsonResponse({'message': 'User logged in successfully!'}, status=200)
            else:
                return JsonResponse({'error': 'Invalid credentials.'}, status=401)
        except Exception as e:
            print("error",e)
            return JsonResponse({'error': str(e)}, status=500)
