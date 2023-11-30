from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View , CreateView,ListView
from .form import ProfilesForm
from .models import UserModel


class CreateProfileView(CreateView):
    template_name="create_profile.html"
    model=UserModel
    fields="__all__"
    success_url="/profiles"


class UserProfilesView(ListView):
    template_name="show_profile.html"
    model=UserModel
    context_object_name="profiles"

# class CreateProfileView(View):
#     def get(self,request):
#         form=ProfilesForm()
#         return render(request,"create_profile.html",{
#             "form":form
#         })
    
#     def post(self,request):
#         submitted_profile=ProfilesForm(request.POST,request.FILES)
#         if submitted_profile.is_valid():
#             profile=UserModel(image=request.FILES["user_image"])
#             profile.save()
#             return HttpResponseRedirect("/profiles")

#         return render(request,"create_profile.html",{
#             "form":submitted_profile
#         })
     