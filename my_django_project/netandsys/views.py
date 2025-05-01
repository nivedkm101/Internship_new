from django.shortcuts import render
def netandsys(request):
    mainLink = {
        'title': 'Networks & Systems',
        'link': '/netandsys'
    }
    links = [
    {
        "title": "AI Server",
        "link": "aiserver"
    },
    {
        "title": "Hardware",
        "link": "hardware"
    },
    {
        "title": "Software",
        "link": "software"
    },
    {
        "title": "Email Services",
        "link": "emailkb"
    },
    {
        "title": "Forms to Download",
        "link": "/institute/forms"
    },
    {
        "title": "Standard Operating Procedure",
        "link": "/static/pdf/networks/Standard-Operating-Procedure/Standard-Operating-Procedure-Networks-and-Systems.pdf"
    },
    {
        "title": "Faculty & Staff",
        "link": "faculty"
    },
    {
        "title": "Support Center",
        "url": "http://172.18.5.212/"
    }
]

    return render(request, 'netandsys/netandsys.html', {'links': links
                                                        , 'mainLink': mainLink})

def aiserver(request):  
    return render(request, 'netandsys/aiserver.html')
def hardware(request):
    return render(request, 'netandsys/hardware.html')
def software(request):
    file = [

    {
      'url': '/matlab',
      'filename': 'Click Here : Mathworks MATLAB Softwre',
      'new': 'true'
    },

  ]
    return render(request, 'netandsys/software.html', {'file': file})
def emailkb(request):
    file = [

    {
      'url': '/static/pdf/networks/email/email backup guide.pdf',
      'filename': 'Email Account Backup Guide',
    },

    {
      'url': '/static/pdf/networks/email/SOP for email contact Updation.pdf',
      'filename': 'SOP for email contact Updation',
    },

  ]
    return render(request, 'netandsys/emailkb.html', {'file': file})