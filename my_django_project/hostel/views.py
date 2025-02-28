from django.shortcuts import render

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