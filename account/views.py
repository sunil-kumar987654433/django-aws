from django.shortcuts import render
from django.views import View
from account.models import User
from django.contrib import messages
# Create your views here.


class RegisterUserViewSet(View):
    def get(self, request):
        context = {}
        return render(request, template_name="website/account/create-user.html", context=context)
    

    def post(self, request):
        data = (request.POST).copy()
        confirm_password = data.get("confirm_password")
        password = data.get("password")
        email = data.get("email")



        if confirm_password != password:
            messages.warning(request, "both password must be equal.")
            return render(request, template_name="website/account/create-user.html")



        context = {}
        print(data)
        try:
            User.objects.create_user(email=email, password=password)
            
            messages.warning(request, "Account successfully created.")
            return render(request, template_name="website/account/create-user.html", context=context)
        except Exception as e:
            messages.warning(request, f"{str(e)}")
            return render(request, template_name="website/account/create-user.html", context=context)
        

