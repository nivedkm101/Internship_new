from django.shortcuts import render

# Create your views here.
def infrastructure(request):
    Facilities = [
        {
            "pic": "images/T&P/Facilities/TNP Office.jpeg",
            "name": "TNP Office Room"
        },
        {
            "pic": "images/T&P/Facilities/TNP Officer Room.jpeg",
            "name": "TNP Officer Room"
        },
        {
            "pic": "images/T&P/Facilities/HR Panel.jpeg",
            "name": "HR Panel"
        },
        {
            "pic": "images/T&P/Facilities/GD Panel - 01.jpeg",
            "name": "GD Panel - 01"
        },
        {
            "pic": "images/T&P/Facilities/Tech Panel Corridor.jpeg",
            "name": "Tech Panel Corridor"
        },
        {
            "pic": "images/T&P/Facilities/Tech Panel.jpeg",
            "name": "Tech Panel - 1"
        },
        {
            "pic": "images/T&P/Facilities/Tech Panel - 2.jpeg",
            "name": "Tech Panel - 2"
        },
        {
            "pic": "images/T&P/Facilities/Tech Panel - 3.jpeg",
            "name": "Tech Panel - 3"
        },
        {
            "pic": "images/T&P/Facilities/GD Panel - 01.jpeg",
            "name": "GD Panel - 02"
        },
    ]

    return render(request, 'training_and_placement/infrastructure.html', {'Facilities': Facilities})

def procedure(request):
    file = [
    {
      'url': "/static/pdf/T&P/2024/Placement Brochure 25' - NIT Puducherry.pdf",
      'title': 'Training and Placement Brochure',
      'new':'true'
    },
    {
      'url': 'https://forms.gle/BhdNEYbSp6YC8jV6A',
      'title': 'Job Application Form(G-Form)'
    },
    {
      'url': 'https://docs.google.com/document/d/1IxEE0Dn1mmxiCw_YvOL7kvOHMb-hoUbA/edit?usp=sharing&ouid=102336531196086350020&rtpof=true&sd=true',
      'title': 'Job Application Form'
    },
  ]
    return render(request, 'training_and_placement/procedure.html', {'file': file})

def program(request):
    file = [
    {
      'url': '/static/pdf/T&P/General Recruitment Process.pdf',
      'title': 'General Recruitment Process'
    },

  ]
    return render(request, 'training_and_placement/program.html',{ 'file': file })

def recruitments(request):
    tableData = {
        "columns": [
            "S.No", "COMPANIES", "CSE", "CIVIL", "ECE", "EEE", "MECH", "CHEM", "PHY", "MATHS", "TOTAL"
        ],
        "data": [
        ["1", "ABB", "4", "-", "-", "1", "-", "-", "-", "-", "5"],
        ["2", "Mewurk", "1", "-", "-", "-", "-", "-", "-", "-", "1"],
        ["3", "Nexturn", "7", "1", "12", "9", "-", "-", "-", "-", "29"],
        ["4", "MBIT wireless", "1", "-", "-", "-", "-", "-", "-", "-", "1"],
        ["5", "Accenture", "7", "-", "1", "-", "-", "-", "-", "-", "8"],
        ["6", "Allen Career Institute Pvt. Ltd.", "-", "1", "2", "-", "-", "2", "1", "1", "7"],
        ["7", "Hitachi Energy", "-", "-", "-", "1", "-", "-", "-", "-", "1"],
        ["8", "Vedya Labs", "1", "-", "2", "1", "-", "-", "-", "-", "5"],
        ["9", "Samsung Noida", "3", "-", "2", "-", "-", "-", "-", "-", "5"],
        ["10", "L&T", "-", "-", "-", "7", "2", "-", "-", "-", "9"],
        ["11", "Factset Systems India Pvt. Ltd.", "1", "-", "-", "-", "-", "-", "-", "-", "1"],
        ["12", "Helix International Pvt Ltd", "1", "-", "-", "-", "-", "-", "-", "-", "1"],
        ["13", "Eaton", "-", "-", "-", "3", "1", "-", "-", "-", "5"],
        ["14", "TASL", "-", "-", "-", "-", "1", "-", "-", "-", "1"],
    ],
    }
    
    placementstat23 = [
        {
            "title": "Placement Statistics 2023 - 2024",
            "url": "/static/pdf/T&P/2024/Placement Statistics 2023 – 2024.pdf",
        },
        {
            "title": "Training and Placement Brochure 2023 - 2024",
            "url": "/static/pdf/T&P/2024/Placement Brochure 25' - NIT Puducherry.pdf",
        },
        {
            "title": "Annual report of T&P 2023 – 2024",
            "url": "/static/pdf/T&P/2024/T&P Annual and Audit Report 2023 – 2024.pdf",
        },
    ]

    placementstat22 = [
        {
            "title": "Placement Statistics 2022 - 2023",
            "url": "/static/pdf/T&P/testimonial/Placement Stat 2022 - 2023.pdf",
        },
        {
            "title": "Training and Placement Brochure 2022 - 2023",
            "url": "/static/pdf/T&P/PLACEMENT_BROCHURE_22.pdf",
        },
        {
            "title": "Annual report of T&P 2022 – 2023",
            "url": "/static/pdf/T&P/testimonial/Annual report of T&P 2022 – 2023.pdf",
        },
    ]

    placementstat21 = [
        {
            "title": "Placement Statistics B.Tech 2021 - 2022",
            "url": "/static/pdf/T&P/testimonial/Placement Statistics 2021 - 2022.pdf",
        },
        {
            "title": "Training and Placement Brochure 2021 - 2023",
            "url": "/static/pdf/T&P/Placement_Brochure_2021_2022.pdf",
        },
    ]


    context = {
        "tableData": tableData,
        "placementstat23": placementstat23,
        "placementstat22": placementstat22,
        "placementstat21": placementstat21,
    }

    return render(request, "training_and_placement/recruitments.html", context)


def testimonial(request):
    placement23 = [
        {"pic": "/static/pdf/T&P/testimonial/2023-2024/Vengatesh.png"},
        {"pic": "/static/pdf/T&P/testimonial/2023-2024/Akhil Lakshmanan.png"},
        {"pic": "/static/pdf/T&P/testimonial/2023-2024/Anandu S P.png"},
        {"pic": "/static/pdf/T&P/testimonial/2023-2024/tawfeeq.png"},
        {"pic": "/static/pdf/T&P/testimonial/2023-2024/Abhishek Priyan P.png"},
        {"pic": "/static/pdf/T&P/testimonial/2023-2024/G S PRIYANKA.png"},
        {"pic": "/static/pdf/T&P/testimonial/2023-2024/K P SRAYA JAYESH.png"},
        {"pic": "/static/pdf/T&P/testimonial/2023-2024/Kalidas Benny Asha.png"},
        {"pic": "/static/pdf/T&P/testimonial/2023-2024/Kirthiga.png"},
        {"pic": "/static/pdf/T&P/testimonial/2023-2024/Manideep.png"},
        {"pic": "/static/pdf/T&P/testimonial/2023-2024/Mufeed.png"},
        {"pic": "/static/pdf/T&P/testimonial/2023-2024/Rajesh.png"},
        {"pic": "/static/pdf/T&P/testimonial/19to23/ajay.jpg"},
        {"pic": "/static/pdf/T&P/testimonial/19to23/Catherine.jpg"},
        {"pic": "/static/pdf/T&P/testimonial/19to23/karthik.jpg"},
        {"pic": "/static/pdf/T&P/testimonial/19to23/Maddali Yaswanth.jpeg"},
        {"pic": "/static/pdf/T&P/testimonial/19to23/vidhya.jpg"},
        {"pic": "/static/pdf/T&P/testimonial/19to23/vishnu.jpeg"},
        {"pic": "/static/pdf/T&P/testimonial/19to23/balamohan.jpg"},
        {"pic": "/static/pdf/T&P/testimonial/19to23/bhavana.jpeg"},
        {"pic": "/static/pdf/T&P/testimonial/19to23/ritvik.jpg"},
        {"pic": "/static/pdf/T&P/testimonial/19to23/smilewin.jpg"},
        {"pic": "/static/pdf/T&P/testimonial/19to23/varun.jpg"},
    ]
    return render(request, "training_and_placement/testimonial.html", {"placement23": placement23})
