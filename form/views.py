from django.shortcuts import render,redirect
from .models import Resume 
# from django.http import HttpResponse

# Create your views here.

def home(request):
    # print(request)
    return render(request,'home.html',{'name':'Hisham', 'age' : 17})

def redirect_view(request):

    # for key,value in dict(request.POST).items():
    #     print(key,value)

    name=request.POST['name']
    email=request.POST['email']
    phone=request.POST['phone']
    title=request.POST['title']

    website=request.POST['website']
    profile=request.POST['profile']
    location=request.POST['location']
    
    skills=request.POST['skills'].split()

    jobs={
        'employers':[],
        'titles':[],
        'end':[],
        'start':[]
    }

    edu={
        'degrees':[],
        'institutions':[],
        'end':[],
        'start':[]
    }

    for i in range(3):
        jobs['employers'].append(request.POST[f"employer-{i+1}"].strip())
        jobs['titles'].append(request.POST[f"job-title-{i+1}"].strip())
        jobs['end'].append(request.POST[f"end-work-{i+1}"].strip())
        jobs['start'].append(request.POST[f"start-work-{i+1}"].strip())

    for i in range(3):
        edu['degrees'].append(request.POST[f'degree-{i+1}'])
        edu['institutions'].append(request.POST[f'institution-{i+1}'])
        edu['end'].append(request.POST[f'end-education-{i+1}'])
        edu['start'].append(request.POST[f'start-education-{i+1}'])

    print(jobs,edu)
    # resume=Resume.objects.create(name=name, email=email,phone=phone,title=title);
    resume=Resume.objects.create(name=name, email=email,phone=phone,title=title, profile=profile,skills=skills,
    website=website,location=location, employers=jobs['employers'], titles=jobs['titles'],job_start=jobs['start'],job_end=jobs['end'],
     degrees=edu['degrees'], institutions=edu['institutions'], edu_start=edu['start'],edu_end=edu['end']);
    response = redirect('resumes')
    return response
    

def form(request):
    # print(request)
    return render(request,'form.html')

def resume(request, pk):
    res=Resume.objects.filter(id=pk).values()
    print(res)
    return render(request,'resume.html', {
        'res': res
    })
    

def resumes(request):
    # print()

    # Creating a row in the database (the conventional way)
    # print(request)
    # name=request.POST['name']
    # email=request.POST['email']
    # phone=request.POST['phone']
    # title=request.POST['title']
    # resume=Resume.objects.create(name=name, email=email,phone=phone,title=title);

    resumes= Resume.objects.all();
    # print(resume)
    # print(resumes[0].id)

    return render(request,'result.html',{
        'resumes': resumes
    })

