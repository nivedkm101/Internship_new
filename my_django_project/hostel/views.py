from django.shortcuts import render
from .models import Staff, Role

def hostel(request):
    
    return render(request, "hostel/hostel.html")

def hostelRules(request):
    
    return render(request, "hostel/hostelRules.html")

def circular_hostel(request):
    announcement24_25 = [{
            "title": "Hostel Fee Circular for students of B.Tech (1st,2nd,3rd & 4th Year), M.Tech (1st & 2nd Year), M.Sc. (1st & 2nd Year), Integrated (B.Sc. B.Ed) & Ph.D students of even semester (Academic Year 2024 - 25)",
            "url": "/static/pdf/Hostel Fee Circular for students of B.Tech (1st,2nd,3rd & 4th Year), M.Tech (1st & 2nd Year), M.Sc. (1st & 2nd Year), Integrated (B.Sc. B.Ed) 2nd Year & Ph.D students of even semes"
            
            },
        {
            "title": "Hostel Fee Circular for First Year Students (B.Sc.B.Ed) (Academic Year 2024 - 25)",
            "url": "/static/pdf/announcement/2024/09/Hostel Fee Circular for First Year Students (B.Sc.B.Ed) (Academic Year 2024 - 25).pdf",
        },
        {
            "title": "Hostel Fee circular - Date Extension - ODD sem of the AY 2024-25",
            "url": "/static/pdf/announcement/2024/08/Fee extension circular - odd sem 2024-25.pdf",
        },
        {
            "title": "Hostel Fee circular - First Year - odd sem 2024-25",
            "url": "/static/pdf/announcement/2024/07/Hostel Fee circular - First Year - odd sem 2024-25.pdf",
        },
        {
            "title": "Hostel Fee Circular - ODD Semester of the Academic Year 2024-25",
            "url": "/static/pdf/announcement/2024/06/Hostel Fee Circular - ODD Semester of the Academic Year 2024-25.pdf",
        },
    ]
    return render(request, "hostel/hostelCircular.html",{ "announcement24_25": announcement24_25, })


def hostel_facilities(request):
    Boys_Hostel1 = [
        {"pic": "/static/images/hostel/img001.jpg"},
        {"pic": "/static/images/hostel/img002.jpg"},
        {"pic": "/static/images/hostel/img003.jpg"},
        {"pic": "/static/images/hostel/img004.jpg"},
        {"pic": "/static/images/hostel/img005.jpg"},
        {"pic": "/static/images/hostel/img006.jpg"},
    ]

    Boys_Hostel2 = [
        {"pic": "/static/images/hostel/img007.jpg"},
        {"pic": "/static/images/hostel/img008.jpg"},
        {"pic": "/static/images/hostel/img009.jpg"},
    ]

    Girls_Hostel = [
        {"pic": "/static/images/hostel/img010.jpg"},
        {"pic": "/static/images/hostel/img001.jpg"},
        {"pic": "/static/images/hostel/img011.jpg"},
        {"pic": "/static/images/hostel/img012.jpg"},
        {"pic": "/static/images/hostel/img006.jpg"},
    ]

    return render(request, "hostel/hostel_facilities.html", {
        "Boys_Hostel1": Boys_Hostel1,
        "Boys_Hostel2": Boys_Hostel2,
        "Girls_Hostel": Girls_Hostel,
    })


def hostelAdministration(request):
  
    office_staff = Staff.objects.filter(department__icontains="Hostel").select_related('id')
    
    warden_roles = Role.objects.filter(role__icontains="warden")

    chief_roles = warden_roles.filter(role__icontains="chief").select_related('id')

    boys_roles = warden_roles.filter(role__icontains="boys").select_related('id')
    
    girls_roles = warden_roles.filter(role__icontains="girls").select_related('id')

    
    Senior_Assistant_roles = warden_roles.filter(role__icontains="Senior Assistant','Hostel'").select_related('id')
    
    # Get unique staff members from those roles
    office_staff_ids = office_staff.values_list('id', flat=True).distinct()
    office_staff_list = Staff.objects.filter(id__in=office_staff_ids)
    
    chief_ids = chief_roles.values_list('id', flat=True).distinct()
    chief_list = Staff.objects.filter(id__in=chief_ids)
    
    boys_ids = boys_roles.values_list('id', flat=True).distinct()
    boys_list = Staff.objects.filter(id__in=boys_ids)
    
    girls_ids = girls_roles.values_list('id', flat=True).distinct()
    girls_list = Staff.objects.filter(id__in=girls_ids)

    Senior_Assistant_ids = Senior_Assistant_roles.values_list('id', flat=True).distinct()
    Senior_Assistant_list = Staff.objects.filter(id__in=Senior_Assistant_ids)
    # Get the relevant role for each staff (for display)
    chief_roles = {role.id_id: role for role in chief_roles}
    boys_roles = {role.id_id: role for role in boys_roles}
    girls_roles = {role.id_id: role for role in girls_roles}
    
    Senior_Assistant_roles = {role.id_id: role for role in Senior_Assistant_roles}
    context = {
        'chief_list': chief_list,
        'chief_roles': chief_roles,
        'boys_list': boys_list,
        'boys_roles': boys_roles,
        'girls_list': girls_list,
        'girls_roles': girls_roles,
        'office_list': office_staff_list,
        'office_roles': office_staff,
    }
    return render(request, 'hostel/hostelAdministration.html',context)