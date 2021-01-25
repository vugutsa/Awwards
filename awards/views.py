from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from .models import Projects,Profile
from .forms import NewProjectsForm,ProfileForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  AwardsMerch
from .serializer import MerchSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly
# Create your views here.

def welcome(request):
    return render(request, 'welcome.html')

def awards_day(request):
    date = dt.date.today()
    projects = Projects.objects.all()
    # FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY
    day = convert_dates(date)

    html = f'''
        <html>
            <body>
                <h1> {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>   
            '''
    return render(request, 'all-awards/today-awards.html', {"date": date,"projects":projects})
def convert_dates(dates):
    
    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

def past_days_awards(request,past_date):
    try:
    # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    if date == dt.date.today():
        return redirect(awards_day) 
  
    return render(request, 'all-awards/past-awards.html', {"date": date})

def search_results(request):
    
    if 'projects' in request.GET and request.GET["projects"]:
        search_term = request.GET.get("projects")
        searched_projects = Projects.search_by_project_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-awards/search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-awards/search.html',{"message":message})
    
def projects(request,projects_id):
    try: 
        projects = Projects.objects.get(id = projects_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-awards/projects.html", {"projects":projects})  
  
@login_required(login_url='/accounts/login/')
def new_projects(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectsForm(request.POST, request.FILES)
        if form.is_valid():
            projects = form.save(commit=False)
            projects.title = current_user
            projects.save()
        return redirect('awardsToday')

    else:
        form = NewProjectsForm()
    return render(request, 'new_projects.html', {"form": form})

@login_required(login_url='/accounts/login/')  
def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('awardsToday')

    else:
        form = ProfileForm()
    return render(request, 'profile.html', {"form": form})

class MerchList(APIView):
    def get(self, request, format=None):
        all_merch = MoringaMerch.objects.all()
        serializers = MerchSerializer(all_merch, many=True)
        return Response(serializers.data)
    def post(self, request, format=None):
        serializers = MerchSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    permission_classes = (IsAdminOrReadOnly,)
    
class MerchDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_merch(self, pk):
        try:
            return MoringaMerch.objects.get(pk=pk)
        except MoringaMerch.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        merch = self.get_merch(pk)
        serializers = MerchSerializer(merch)
        return Response(serializers.data)   
    
    def put(self, request, pk, format=None):
        merch = self.get_merch(pk)
        serializers = MerchSerializer(merch, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None):
        merch = self.get_merch(pk)
        merch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   