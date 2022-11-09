from django.shortcuts import render,redirect
from .models import Resume 
from django.contrib.auth.models import User
# from django.http import HttpResponse

# Create your views here.

def home(request):
    # print(request)
    return render(request,'home.html')

def redirect_view(request):

    # for key,value in dict(request.POST).items():
    #     print(key,value)
    if not User.is_authenticated :
        return redirect('accounts/login')

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
       if len(request.POST[f"employer-{i+1}"].strip())!=0: 
            jobs['employers'].append(request.POST[f"employer-{i+1}"].strip())
       if len(request.POST[f"job-title-{i+1}"].strip())!=0: 
            jobs['titles'].append(request.POST[f"job-title-{i+1}"].strip())
       if len(request.POST[f"end-work-{i+1}"].strip())!=0:
            jobs['end'].append(request.POST[f"end-work-{i+1}"].strip())
       if len(request.POST[f"start-work-{i+1}"].strip())!=0: 
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
     degrees=edu['degrees'], institutions=edu['institutions'], edu_start=edu['start'],edu_end=edu['end'], uid=request.user);
    response = redirect('resumes')
    return response
    

def form(request):
    # print(request)
    if User.is_authenticated :
        return render(request,'form.html')
    else: 
        return redirect('accounts/login')

def resume(request, pk):
    res=Resume.objects.filter(id=pk).values()
    print(res)
    return render(request,'resume.html', {
        'resume': res
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

    resumes= Resume.objects.filter(uid=request.user);
    # print(resume)
    # print(resumes[0].id)

    return render(request,'result.html',{
        'resumes': resumes
    })


def delete(request, id,):
    resume = Resume.objects.get(id=id)
    print(resume)
    resume.delete();
    return redirect('resumes')
