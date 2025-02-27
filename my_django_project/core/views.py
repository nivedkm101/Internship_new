from django.shortcuts import render
from django.templatetags.static import static  # Import static
def home(request):
    nav_items =  [
        {
            "title": "The Institute",
            "link": "/institute",
            "content": [
                {"title": "About the Institute", "link": "/institute/about"},
                {"title": "Campus and Facilities", "link": "/institute/campus"},
                {"title": "Rules and Regulation", "link": "/institute/rules"},
                {"title": "RTI", "link": "/institute/rti"},
                {"title": "CVC", "link": "/institute/administration/vigilanceOfficer"},
                {"title": "Public Grievances", "link": "/PublicGrievances"},
                {"title": "Photo Gallery", "link": "/institute/gallery"},
                {"title": "Forms to Download", "link": "/forms/institute"},
                {"title": "Contact Administration", "link": "/institute/contact"},
                {"title": "NIRF", "link": "/institute/nirf"},
                {"title": "Women Cell", "link": "/womencell"},
                {"title": "ICC", "link": "/institute/ICC"},
                {"title": "Spicmacay", "link": "/institute/Spicmacay"},
                {"title": "IQAC", "link": "/institute/iqac"},
                {"title": "Newsletter (Pariprashna)", "link": "/newsletter"},
                {"title": "Campus Connect Newsletter", "link": "/campusconnect"},
                {"title": "Bulletin Ph.D Newsletter", "link": "/bulletin"},
                {"title": "Networks & Systems", "link": "/institute/netandsys"},
            ],
        },
        {
            "title": "Academics",
            "link": "/academics",
            "content": [
                {"title": "Departments", "link": "/academics/departments"},
                {"title": "Academic Office", "link": "/academics/office"},
                {"title": "Admission", "link": "/students/admission"},
                {"title": "Exam Results", "link": "/academics/results"},
                {"title": "Academic Calendar", "link": "/academics/calendar"},
                {"title": "Curriculum and Syllabi", "link": "/academics/curriculum"},
                {"title": "Institute Fee Structure", "link": "/academics/fee-structure"},
                {"title": "NEP-2020 Cell", "link": "/academics/nep"},
                {"title": "Forms to Download", "link": "/forms/academics"},
                {"title": "Rules and Regulation", "link": "/academics/rules"},
                {"title": "Convocation", "link": "/academics/convocation"},
                {"title": "NAD", "link": "/academics/nad"},
                {"title": "Scholarship", "link": "/academics/scholarship"},
                {"title": "Exam Schedule", "link": "/academics/exam"},
                {"title": "Physical Education", "link": "/academics/physicalEducation"},
                {"title": "Emails for Contacts", "link": "/academics/emailContacts"},
                {"title": "Educational Verification Procedure", "link": "/static/pdf/Educational Verification Procedure/Procedure_for_verification2022.pdf"},
            ],
        },
        {
            "title": "Administration",
            "link": "/institute/administration"
        },
        {
            "title": "Students Welfare",
            "link": "/students",
            "content": [
                {"title": "Rules and Regulations", "link": "/students/rulesandregulation"},
                {"title": "Anti-ragging", "link": "/students/antiragging"},
                {"title": "Student Council", "link": "/students/council"},
                {"title": "Annual Fest", "link": "/students/annualFest"},
                {"title": "Orientation", "link": "/students/orientation"},
                {"title": "Student Clubs", "link": "/students/clubs"},
                {"title": "Student Associations", "link": "/students/student-associations"},
                {"title": "Counselling Services", "link": "/students/councelling"},
                {"title": "Medical Insurance", "link": "/students/medical-insurance"},
                {"title": "NCC", "link": "/students/studentActivities/NCC"},
                {"title": "NSS", "link": "/students/studentActivities/NSS"},
                {"title": "Physical Education & Sports", "link": "/academics/physicalEducation"},
                {"title": "Forms to Download", "link": "/forms/students"},
                {"title": "Alumni Relations", "link": "/alumni/alumniRelations"},
                {"title": "Grievance Redressal", "link": "/students/Grievance Redressal"},
                {"title": "Announcements", "link": "/students/sw-announcements"},
            ],
        },
        {
            "title": "Hostel",
            "link": "/hostel",
            "content": [
                {"title": "Hostel Administration", "link": "/hostelAdministration"},
                {"title": "Hostel Facilities", "link": "/hostel_facilities"},
                {"title": "Rules and Regulations", "link": "/static/docs/hostel/Hostel Rules.pdf"},
                {"title": "Code of Conduct", "link": "/static/docs/hostel/Updated code of conduct - Hostel.pdf"},
                {"title": "Circular", "link": "hostel/circular_hostel"},
                {"title": "Contact Us", "link": "/students/hostels"},
                {"title": "Forms to Download", "link": "/forms/students"},
            ],
        },
        {
            "title": "Faculty & Staff",
            "link": "/people_nit",
            "content": [
                {"title": "Administration Head Directory", "link": "/faculty/adminDirectory"},
                {"title": "Dean Directory", "link": "/faculty/deanDirectory"},
                {"title": "HOD Directory", "link": "/faculty/hodDirectory"},
                {"title": "Faculty Directory", "link": "/faculty/facultyDirectory"},
                {"title": "Faculty On Contract Directory", "link": "/faculty/focDirectory"},
                {"title": "Officer Directory", "link": "/faculty/OfficerDirectory"},
                {"title": "P&D Directory", "link": "/faculty/P&dDirectory"},
                {"title": "Staff Directory", "link": "/faculty/staffDirectory"},
                {"title": "Career", "link": "/Opportunities"},
                {"title": "Forms to Download", "link": "/forms/faculty"},
            ]
        },
        {
            "title": "Research & Consultancy",
            "link": "/research",
            "content": [
                {"title": "Research & Consultancy Office", "link": "/research/office"},
                {"title": "IEEE", "link": "/research/IEEE"},
                {"title": "List of R&C Committees", "link": "/research/committees"},
                {"title": "Patents", "link": "/research/publications"},
                {"title": "Funded Projects", "link": "/research/fundedProjects"},
                {"title": "Journals", "link": "/research/journal"},
                {"title": "Book Chapter", "link": "/research/bookChapter"},
                {"title": "Conference", "link": "/research/conference"},
                {"title": "Consultancy Projects", "link": "/research/consultancyProjects"},
                {"title": "IPR Cell", "link": "/research/ipr"},
                {"title": "Forms to Download", "link": "/forms/research"},
                {"title": "IIC", "link": "/research/innovation"},
                {"title": "NISP", "link": "/research/nisp"},
                {"title": "Industry Consultancy", "link": "/alumni/industryConsultancy"},
                {"title": "MoU", "link": "/alumni/mou"},
                {"title": "Central Instrumentation Facility (CIF)", "link": "/CIF"},
            ]
        },
        {
            "title": "Training and Placement",
            "link": "/trainingAndPlacement",
            "content": [
                {"title": "About", "link": "/trainingAndPlacement"},
                {"title": "Placement Procedure", "link": "/training_and_placement/procedure"},
                {"title": "Training Programs & Activities", "link": "/training_and_placement/program"}, 
                {"title": "Infrastructure and Facilities", "link": "/training_and_placement/infrastructure"},
                {"title": "Placement Statistics", "link":  "/training_and_placement/recruitments"},
                {"title": "Testimonial", "link": "/training_and_placement/testimonial"},
                {"title": "Internship", "link": "/students/internship"},
                {"title": "Contact", "link": "/tnpcontact"},
            ],
        },
    ]

    quickLinks = [
        {"title": "Gallery", "link": "/institute/gallery"},
        {"title": "Forms for Download", "link": "/forms"},
        {"title": "People at NITPY", "link": "/people_nit"},
        {"title": "NAD", "link": "/academics/nad"},
        {"title": "Women Cell", "link": "/womencell"},
        {"title": "Stores and Purchase", "link": "/institute/administration/stores"},
        {"title": "ID Cards", "link": "/idcard"},
        {"title": "Alumni", "url": "https://www.nitpyalumni.com/home/index"},
        {"title": "NISP", "link": "/research/nisp"},
        {"title": "SC/ST/OBC cell", "link": "/scstobc_cell"},
        {"title": "Networks & Systems", "link": "/institute/netandsys"},
        {"title": "List of Holidays", "url": static("docs/holidays/List_of_holidays_NIT_Puducherry_2025.pdf")},
        {"title": "Public Grievances", "link": "/PublicGrievances"},
        {"title": "Medical Facilities", "link": "/students/medical"},
        {"title": "Physical Education", "link": "/academics/physicalEducation"},
        {"title": "List of committees", "link": "/institute/administration/committeeList"},
        {"title": "PARIPRASHNA", "link": "/institute/administration/newsletter"},
        {"title": "Campus Connect Newsletter", "link": "/campusconnect"},
        {"title": "NITPY BULLETIN", "link": "/institute/administration/bulletin"},
        {"title": "Central Library", "link": "/library"},
        {"title": "DASA", "url": "https://dasanit.org/dasa2021/"},
        {"title": "SMDP", "url": "https://www.nitpy.ac.in/old_website/SMDPWebsite/"},
        {"title": "Guest House", "link": "/GuestHouse"},
        {"title": "Hostel Facilities", "link": "/hostel_facilities"},
        {"title": "NCC", "link": "/students/studentActivities/NCC"},
        {"title": "Support Center", "url": "http://172.18.5.212/"},
    ]
    instituteCarouselSlides = [
        {"link": "images/instituteCarousel/NIRF.jpg", "alt": "Slide 1"},
        {"link": "images/instituteCarousel/Banner 1.jpg", "alt": "Slide 2"},
        {"link": "images/instituteCarousel/img104.jpg", "alt": "Slide 3"},
        {"link": "images/instituteCarousel/img102.jpg", "alt": "Slide 4"},
        {"link": "images/instituteCarousel/img014.jpg", "alt": "Slide 5"},
        {"link": "images/instituteCarousel/img016.jpg", "alt": "Slide 6"},
        {"link": "images/instituteCarousel/Banner 2.jpg", "alt": "Slide 7"},
        {"link": "images/instituteCarousel/img003.jpg", "alt": "Slide 8"},
        {"link": "images/instituteCarousel/img011.jpg", "alt": "Slide 9"},
        {"link": "images/instituteCarousel/img012.jpg", "alt": "Slide 10"},
    ]

    overlayCards = [
        {"title": "Admission", "link": "/students/admission", "content": "", "new": True},
        {"title": "Directory", "link": "/people_nit", "content": ""},
        {"title": "Opportunities", "link": "/Opportunities", "content": "", "new": True},
        {"title": "Departments", "link": "/academics/departments", "content": ""}
    ]
    importantNewsSlides = [
        {"link": "https://gyanith.org/",
         "title": "Gyanith- Technical Fest of NITPY on Feb 27-28, 2025",
         "new": True
        },
    ]
    stats = [
        {"title": "10", "subtitle": "Departments"},
        {"title": "1421", "subtitle": "Students"},
        {"title": "63", "subtitle": "Faculties"},
        {"title": "1730", "subtitle": "Publications"},
    ]

    # we need to change the url to link for the some  announcements
    announcements = [
         {
        "title": "Students_General_Rules",
        "url": "pdf/announcement/2023/12/Students_General_Rules_updated 18_20.pdf",
    },
    {
        "title": "Fine Circular for Late Registration of Courses during the Even Semester of AY 2024-25",
        "url": "pdf/announcement/2025/01/Fine Circular for the Late enrollment students.pdf",
        "new": True,
    },
    {
        "title": "Circular - ADB-ROK Scholarship Program for Master's and Doctoral Studies in Korea",
        "url": "pdf/announcement/2025/01/Circular - ADB-ROK Scholarship Program for Master's and Doctoral Studies in Korea.pdf",
        "new": True,
    },
    {
        "title": "Advertisement for Recruitment of JRF under SMDP C2S Project is extended till 10-02-2025",
        "url": "/Opportunities",
        "new": True,
    },
    {
        "title": "Advertisement for Residential Students Counselor (RSC) post in Girls Hostel at NITPY",
        "url": "/Opportunities",
        "new": True,
    },
    {
        "title": "Fee circular for the Even semester of the AY 2024-25 for the B.Tech. (I Year) 2024 admitted batch",
        "url": "pdf/announcement/2025/01/Fee circular for the Even semester of the AY 2024-25 for the B.Tech. (I Year) 2024 admitted batch.pdf",
        "new": True,
    },
    {
        "title": "The Ph.D. Public Viva-Voce examination of Ms V. Jeyasakthi (Roll No. EN19D2002), Dept of HSS is scheduled on 19.02.2025, at 10.30 AM",
        "url": "pdf/announcement/2025/01/Viva Circular_Jeyasakthi.pdf",
        "new": True,
    },
    {
        "title": "Final Assessment Timetable for the ODD semester of the AY 2024-25 for the B.Sc. B.Ed. (I Year)",
        "url": "/academics/exam",
        "new": True,
    },
    {
        "title": "Advertisement for Recruitment of Project Assistant Under ANRF-SERB Research Project",
        "url": "/Opportunities",
        "new": True,
    },
    {
        "title": "Advertisement for Recruitment of Project Associate (PA) Under SERB Project",
        "url": "/Opportunities",
        "new": True,
    },
    {
        "title": "Semester fee details for the B.Tech 2024 (I year) batch for the academic year 2024-25",
        "url": "pdf/announcement/2025/01/Semester fee details for the B.Tech 2024 (I year) batch for the academic year 2024-25.pdf",
        "new": True,
    },
    {
        "title": "Circular, Schedule, and Registration form for Make - Up Examinations First Year to be held in January - 2025",
        "url": "/academics/exam",
        "new": True,
    },
    {
        "title": "End Semester Results for the B.Tech. (III & IV year) examination held on November 2024",
        "url": "/academics/results",
    },
    {
        "title": "Advertisement for Recruitment of Project Associate (PA) Under SERB Project Date Extended till 10.01.2025",
        "url": "/Opportunities",
    },
    {
        "title": "Advertisement for Faculty on contract – for Integrated B.Sc.-B.Ed. program",
        "url": "/Opportunities",
    },
    {
        "title": "The PhD Public Viva-Voce Examination of Mr. Nettimi Satya Sai Srinivas (Roll No. EC16D2001), Department of Electronics and Communication Engineering is scheduled on 10/01/2025,11.00 AM",
        "url": "pdf/announcement/2024/12/Ph.D Public Viva-Voce Examination of Mr. N. S. S. Srinivas (EC16D2001)- Invitation.pdf",
    },
    {
        "title": "The PhD Public Viva-Voce Examination of Mr. Vishnu Sankar S (CH20D1003), Department of Chemistry is scheduled on 24.01.2025, 11:00 AM",
        "url": "pdf/announcement/2024/12/Vishnu_ PhD Viva Notification.pdf",
    },
    ]
   
    tendersCarouselSlides = [
    {
        "title": "Notice Inviting Quotation - Purchase of Soil mechanics lab accessories and equipment",
        "link": "pdf/tenders/2025/NIQ Purchase of Soil mechanics lab accessories and equipment .pdf",
        "new": True
    },
    {
        "title": "Notice Inviting Quotation - Purchase of Extensometer for structural engineering laboratory",
        "link": "pdf/tenders/2025/NIQ- Purchase of Extensometer for structural engineering laboratory.pdf",
        "new": True
    },
    {
        "title": "Notice Inviting Quotation - Workstation Computer with Advanced GPU Architecture - Last Date to receive sealed quotations is On or Before 11.02.2025 (Tuesday), 05:00 p.m.",
        "link": "pdf/tenders/2025/NITPY_NIQ_Workstation_Sc.pdf",
        "new": True
    },
    {
        "title": "Notice Inviting Quotation - Hot Stirrer Setup - Last Date to receive sealed quotations is On or Before 03.02.2025 (Monday), 05:00 p.m.",
        "link": "pdf/tenders/2025/NITPY_NIQ_Hot-Stirrer_Sc-1.pdf",
        "new": True
    },
    {
        "title": "Notice Inviting Quotation - Homogenizer Setup - Last Date to receive sealed quotations is On or Before 03.02.2025 (Monday), 05:00 p.m.",
        "link": "pdf/tenders/2025/NITPY_NIQ_Homogenizer_Sc-1.pdf",
        "new": True
    },
    {
        "title": "Notice Inviting Quotation - Probe Ultrasonicator Setup - Last Date to receive sealed quotations is On or Before 03.02.2025 (Monday), 05:00 p.m.",
        "link": "pdf/tenders/2025/NITPY_NIQ_Probe-Ultrasonicator_Sc-1.pdf",
        "new": True
    },
    {
        "title": "NIQ - Architectural design, preparation of 2D & 3D drawings and BOQ with specifications for faculty rooms type I, II and III, HoD room, Department Meeting room and Research scholar hall in the Composite Block of NITPY Campus Karaikal",
        "link": "pdf/tenders/2025/Architectural design, preparation of 2D & 3D drawings.pdf",
        "new": True
    },
    {
        "title": "Notice Inviting Quotation - Kitchen Exhaust System",
        "link": "pdf/tenders/2025/Notice Inviting Quotation - Kitchen Exhaust System.pdf"
    },
    {
        "title": "Notice Inviting Quotation - For the purchase of equipment for a project sanctioned by DST under the scheme NCSCT",
        "link": "pdf/tenders/2024/NIQ-DST NCSTC_extension.pdf"
    },
    {
        "title": "Notice Inviting Quotation - Equipment for a project sanctioned by DST under the scheme NCSCT",
        "link": "pdf/tenders/2024/NIQ-DST NCSTC.pdf"
    }
]



    eventsCarouselSlides = [
    {
        "title": "Gyanith- Technical Fest of NITPY",
        "category": "",
        "dept": "",
        "date": "27 FEB ",
        "link": "https://gyanith.org/",
        "img": "images/events/Gyanith- Technical Fest.jpg",
        "alt": ""
    },
    {
        "title": "ICWEES 2025 - International Conference on Water, Environment, Energy & Society",
        "category": "Conference",
        "dept": "Department of Civil",
        "date": "26 APR ",
        "link": "https://icwees2025.com/",
        "img": "images/events/ICWEES 2025.jpeg",
        "alt": ""
    },
    {
        "title": "Harnessing AI for Medical Signal and Imaging Diagnostics organized by department of ECE ...",
        "category": "Workshop",
        "dept": "Department of ECE",
        "date": "09 DEC ",
        "link": "pdf/Upcomming Events/2024/12/ATAL_FDP_Brochure_2024.pdf",
        "img": "images/events/Harnessing AIfor Medical.jpg",
        "alt": ""
    },
    {
        "title": "4th International Conference on Future Technologies in Manufacturing, ...",
        "category": "Conference",
        "dept": "Department of Mechanical Engineering",
        "date": "11 DEC ",
        "link": "https://2024.icoftnitpy.com/",
        "img": "images/events/ICOFT - 2024.png",
        "alt": ""
    },
    {
        "title": 'Five days short-term course on "Trends in Shaping Energy Transition” through hybrid mode ...',
        "category": "Workshop",
        "dept": "Department of EEE",
        "date": "25 NOV ",
        "link": "pdf/Upcomming Events/2024/11/STC_TSET_NITPY_Brochure.pdf",
        "img": "images/events/Trends in Shaping Energy Transition.png",
        "alt": ""
    },
    {
        "title": "Decoding Chemistry Horizons: A Workshop for Aspiring Chemists (DCHWAC-2024)",
        "category": "Workshop",
        "dept": "Department of Chemistry",
        "date": "",
        "link": "pdf/Upcomming Events/2024/09/Decoding Chemistry Horizons A National Workshop for Aspiring Chemists (DCHWAC-2024).pdf",
        "img": "images/events/DCHWAC-2024.JPG",
        "alt": ""
    },
    {
        "title": "IConSCEPT 2024 on 4 - 5 July, 2024 at National Institute of Technology Puducherry, Karaikal",
        "category": "Workshop",
        "dept": "Department of EEE",
        "date": "04 JULY",
        "link": "pdf/Upcomming Events/2024/04/IConscept -2024 brochure.pdf",
        "img": "images/events/IConSCEPT 2023 .jpg",
        "alt": ""
    },
    {
        "title": "Artificial Intelligence Models for Remote Sensing and its Applications (AIRS-2024)",
        "category": "Workshop",
        "dept": "Department of CSE",
        "date": "06 JUNE",
        "link": "https://prabakarankannan.github.io/airs2024/",
        "img": "images/events/AIRS 2024.jpg",
        "alt": ""
    }
]
    researchCarouselSlides = [
    {
        "title": "Impact of online teaching on virtual laboratory course analysis using machine learning..",
        "dept": "Mechanical",
        "link": "https://pubs.aip.org/aip/acp/article-abstract/3217/1/020001/3327691/Impact-of-online-teaching-on-virtual-laboratory?redirectedFrom=fulltext",
        "img": "images/instituteCarousel/research/Impact of online teaching on virtual laboratory course analysis using machine learning technique.jpg",
        "alt": "",
        "authors": ["Dr. Karpagaraj"]
    },
    {
        "title": "Hot corrosion and high-temperature oxidation studies of hard-faced nickel alloy..",
        "dept": "Mechanical",
        "link": "https://shop.elsevier.com/books/advances-in-sustainable-materials/kumar/978-0-443-13849-2",
        "img": "images/instituteCarousel/research/Advances in Sustainable Materials.jpg",
        "alt": "",
        "authors": ["Dr. Karpagaraj"]
    },
    {
        "title": "Optimized static configuration for output power maximization of..",
        "dept": "Electrical and Electronics",
        "link": "https://www.sciencedirect.com/science/article/abs/pii/S0306261924019810",
        "img": "images/instituteCarousel/research/Applied Energy.jpeg",
        "alt": "",
        "authors": ["Dr. BIJUKUMAR B"]
    },
    {
        "title": "Cost-effective one-time configuration for bridge-linked thermoelectric ..",
        "dept": "Electrical and Electronics",
        "link": "https://www.sciencedirect.com/science/article/abs/pii/S0959652624022650",
        "img": "images/instituteCarousel/research/Journal of Cleaner Production.png",
        "alt": "",
        "authors": ["Dr. BIJUKUMAR B"]
    },
    {
        "title": "A novel one-time unified configuration strategy with L-SHADE ..",
        "dept": "Electrical and Electronics",
        "link": "https://www.sciencedirect.com/science/article/abs/pii/S1359431124020441",
        "img": "images/instituteCarousel/research/Applied Thermal Engineering.jpeg",
        "alt": "",
        "authors": ["Dr. BIJUKUMAR B"]
    },
    {
        "title": "Effect of cold metal transfer process on hardfacing of Inconel 718 over ..",
        "dept": "Mechanical",
        "link": "https://www.sciencedirect.com/science/article/abs/pii/S0167577X24011698",
        "img": "images/instituteCarousel/research/Effect of cold metal transfer process.jpg",
        "alt": "",
        "authors": ["Dr. Karpagaraj"]
    },
    {
        "title": "Book of Abstracts - International conference on i-Computer 2023 ...",
        "dept": "CSE",
        "link": "https://drive.google.com/file/d/1fVE_q0avKFvfmt4nUOIvAHmPKEf7eKds/view",
        "img": "images/events/AIRS 2024.jpg",
        "alt": "",
        "authors": [""]
    },
    {
        "title": "Phosphazene-Based Covalent Organic Framework as an Efficient Catalyst...",
        "dept": "Chemistry",
        "link": "https://pubs.acs.org/doi/10.1021/acsomega.3c08763",
        "img": "images/instituteCarousel/research/COF.jpg",
        "alt": "",
        "authors": ["Dr. Seenuvasan Vedachalam"]
    },
    {
        "title": "Experimental study on mechanical, damping and corrosion properties of Inconel..",
        "dept": "Mechanical",
        "link": "https://www.sciencedirect.com/science/article/abs/pii/S1350630723008257?via%3Dihub",
        "img": "images/instituteCarousel/research/hard-faced stainless steel 304.jpg",
        "alt": "",
        "authors": ["Dr. Karpagaraj"]
    },
    {
        "title": "Optimizing electric vehicle charging in distribution networks ...",
        "dept": "Electrical and Electronics",
        "link": "https://www.sciencedirect.com/science/article/abs/pii/S0360544224005875",
        "img": "images/instituteCarousel/research/Optimizing electric vehicle charging.jpg",
        "alt": "",
        "authors": ["Dr.T.Vinopraba"]
    },
    {
        "title": "Dynamic pricing for load shifting: Reducing electric vehicle charging impacts ",
        "dept": "EEE",
        "link": "https://www.sciencedirect.com/science/article/pii/S2210670724000854",
        "img": "images/instituteCarousel/research/Dr.T.Vinopraba.jpg",
        "alt": "",
        "authors": ["Dr.T.Vinopraba"]
    },
    {
        "title": "Profuse Channel Estimation and Signal Detection Techniques for Orthogonal Time Frequency",
        "dept": "ECE",
        "link": "https://ieeexplore.ieee.org/document/10319451",
        "img": "images/instituteCarousel/research/downlink.jpg",
        "alt": "",
        "authors": ["Dr. Surendar M"]
    }

]
    gallery_images = [
    {
        "url": "images/instituteCarousel/homegallery/2025/Republic Day 2025.jpeg",
        "description": "Republic Day 2025"
    },
    {
        "url": "images/instituteCarousel/homegallery/2024/12/ATAL.jpeg",
        "description": "Faculty Development Program titled 'Smart Manufacturing Systems from Industry 5.0 Perspective' from 11 to 17 December 2024 funded by AICTE Training and Learning (ATAL) Academy"
    },
    {
        "url": "images/instituteCarousel/homegallery/2024/12/ICOFT 2025.JPG",
        "description": "4th International Conference on Future Technologies in Manufacturing, Automation, Design & Energy (Hybrid Mode) 11-13 DECEMBER 2024 Organized by department of mechanical engineering"
    },
    {
        "url": "images/instituteCarousel/homegallery/2024/12/Vigilance Awareness Week.jpg",
        "description": "'Observance of Vigilance Awareness Week 2024'"
    },
    {
        "url": "images/instituteCarousel/homegallery/2024/10/One day hands-on training about MY Bharat Portal.jpeg",
        "description": "One day hands-on training about MY Bharat Portal"
    },
    {
        "url": "images/instituteCarousel/homegallery/2024/09/XI - CONVOCATION.png",
        "description": "XI - CONVOCATION 2024"
    },
    {
        "url": "images/instituteCarousel/homegallery/2024/07/IEEE Conference ICONSCEPT 2024.jpeg",
        "description": "IEEE Conference ICONSCEPT 2024"
    },
    {
        "url": "images/instituteCarousel/homegallery/2024/06/Student visit from School students from PM SHRI Kamban.jpg",
        "description": "Student visit from School students from PM SHRI Kamban Govt. Higher Secondary School, Nettapakkam, Puducherry and Govt. High School, Thirukkanur, Puducherry"
    },
    {
        "url": "images/instituteCarousel/homegallery/2024/06/International Day against Drug Abuse & Illicit Trafficking.jpg",
        "description": "International Day against Drug Abuse & Illicit Trafficking"
    },
    {
        "url": "images/instituteCarousel/homegallery/2024/06/Seminar on New Criminal Laws  by Mr. R. Thambiraj B.A.B.L., Advocate & Notary, Karaikal.jpg",
        "description": "Seminar on New Criminal Laws  by Mr. R. Thambiraj B.A.B.L., Advocate & Notary, Karaikal"
    },
    {
        "url": "images/instituteCarousel/homegallery/2024/06/International Day of Yoga.jpg",
        "description": "International Day of Yoga - 2024"
    },
    {
        "url": "images/instituteCarousel/homegallery/2024/05/Dr Makarand Madhao Ghangrekar has taken charge as Director of the NIT Puducherry.jpeg",
        "description": "Dr. Makarand Madhao Ghangrekar has taken charge on 06/05/2024 as Director of the NIT Puducherry"
    },
    {
        "url": "images/instituteCarousel/homegallery/2024/04/Five-Day Training Programme on Fish processing and Value Addition.jpg",
        "description": "Five-Day Training Programme on Fish processing and Value Addition"
    },
    {
        "url": "images/instituteCarousel/homegallery/2024/02/EMERGING TRENDS IN ENGINEERING AND TECHNOLOGY - ETET 2024.jpg",
        "description": "EMERGING TRENDS IN ENGINEERING AND TECHNOLOGY - ETET 2024"
    },
    {
        "url": "images/instituteCarousel/homegallery/2024/02/STI Hub Inauguration.jpg",
        "description": "STI Hub Inauguration"
    },
    {
        "url": "images/instituteCarousel/homegallery/2024/01/25 January.jpg",
        "description": "National Voter's Day"
    },
    {
        "url": "images/instituteCarousel/homegallery/2024/01/Faculty Development Programme (FDP).jpg",
        "description": "Faculty Development Programme (FDP) on AMSE"
    },
    {
        "url": "images/instituteCarousel/homegallery/2024/01/Ram Navami Celebration.jpg",
        "description": "Ram Navami Celebration"
    },
    {
        "url": "images/instituteCarousel/homegallery/2023/12/Talk by CVO.JPG",
        "description": "VIGILANCE AWARENESS WEEK 2024 - Talk by CVO"
    },
    {
        "url": "images/instituteCarousel/homegallery/2023/12/VIGILANCE AWARENESS WEEK 2024 - Pledge by Faculties .JPG",
        "description": "VIGILANCE AWARENESS WEEK 2024 - Pledge by Faculties"
    },
    {
        "url": "images/instituteCarousel/homegallery/2023/12/VIGILANCE AWARENESS WEEK 2024 - Prize distribution.jpg",
        "description": "VIGILANCE AWARENESS WEEK 2024 - Prize distribution"
    },
    {
        "url": "images/instituteCarousel/homegallery/2023/12/Indeas for Viksit Bharat @2047.PNG",
        "description": "Indeas for Viksit Bharat @2047"
    },
    {
        "url": "images/instituteCarousel/homegallery/2023/12/Memorandum of Understanding Between National Institute of Technology Puducherr.jpg",
        "description": "Memorandum of Understanding Between National Institute of Technology Puducherry, Karaikal & Dr. B R Ambedkar Institute of Technology (Department Of Higher Education, Andaman & Nicobar Administration, Port Blair)"
    }
]


    return render(request, 'core/home.html', {
        "nav_items": nav_items,
        "quickLinks": quickLinks,
        "stats": stats,
        "instituteCarouselSlides": instituteCarouselSlides,
        "overlayCards": overlayCards,
        "importantNewsSlides": importantNewsSlides,
        "announcements": announcements,
        "tendersCarouselSlides": tendersCarouselSlides,
        "eventsCarouselSlides":eventsCarouselSlides,
        "researchCarouselSlides": researchCarouselSlides,
        "gallery_images":gallery_images,
        
        })  # Passing nav_items to the template
def about(request):
    return render(request, 'core/about.html') 
def reach_us(request):
    return render(request, 'core/reach_us.html') 
def contact(request):
    return render(request, 'core/contact.html') 
def announcement_banner(request):
    return render(request, 'core/announcement_banner.html') 
def announcement_banner(request):
    return render(request, 'core/announcement_banner.html') 

def announcement(request):
    return render(request, 'core/announcement.html') 

def newsletter(request):
    return render(request, 'newsletter.html')

def upcommingEvents(request):
    return render(request, 'upcommingEvents.html')

def tendernews(request):
    return render(request, 'tenders.html')
def research_component(request):
    researchCarouselSlides = [
    {
        "title": "Impact of online teaching on virtual laboratory course analysis using machine learning..",
        "dept": "Mechanical",
        "link": "https://pubs.aip.org/aip/acp/article-abstract/3217/1/020001/3327691/Impact-of-online-teaching-on-virtual-laboratory?redirectedFrom=fulltext",
        "img": "images/instituteCarousel/research/Impact of online teaching on virtual laboratory course analysis using machine learning technique.jpg",
        "alt": "",
        "authors": ["Dr. Karpagaraj"]
    },
    {
        "title": "Hot corrosion and high-temperature oxidation studies of hard-faced nickel alloy..",
        "dept": "Mechanical",
        "link": "https://shop.elsevier.com/books/advances-in-sustainable-materials/kumar/978-0-443-13849-2",
        "img": "images/instituteCarousel/research/Advances in Sustainable Materials.jpg",
        "alt": "",
        "authors": ["Dr. Karpagaraj"]
    },
    {
        "title": "Optimized static configuration for output power maximization of..",
        "dept": "Electrical and Electronics",
        "link": "https://www.sciencedirect.com/science/article/abs/pii/S0306261924019810",
        "img": "images/instituteCarousel/research/Applied Energy.jpeg",
        "alt": "",
        "authors": ["Dr. BIJUKUMAR B"]
    },
    {
        "title": "Cost-effective one-time configuration for bridge-linked thermoelectric ..",
        "dept": "Electrical and Electronics",
        "link": "https://www.sciencedirect.com/science/article/abs/pii/S0959652624022650",
        "img": "images/instituteCarousel/research/Journal of Cleaner Production.png",
        "alt": "",
        "authors": ["Dr. BIJUKUMAR B"]
    },
    {
        "title": "A novel one-time unified configuration strategy with L-SHADE ..",
        "dept": "Electrical and Electronics",
        "link": "https://www.sciencedirect.com/science/article/abs/pii/S1359431124020441",
        "img": "images/instituteCarousel/research/Applied Thermal Engineering.jpeg",
        "alt": "",
        "authors": ["Dr. BIJUKUMAR B"]
    },
    {
        "title": "Effect of cold metal transfer process on hardfacing of Inconel 718 over ..",
        "dept": "Mechanical",
        "link": "https://www.sciencedirect.com/science/article/abs/pii/S0167577X24011698",
        "img": "images/instituteCarousel/research/Effect of cold metal transfer process.jpg",
        "alt": "",
        "authors": ["Dr. Karpagaraj"]
    },
    {
        "title": "Book of Abstracts - International conference on i-Computer 2023 ...",
        "dept": "CSE",
        "link": "https://drive.google.com/file/d/1fVE_q0avKFvfmt4nUOIvAHmPKEf7eKds/view",
        "img": "images/events/AIRS 2024.jpg",
        "alt": "",
        "authors": [""]
    },
    {
        "title": "Phosphazene-Based Covalent Organic Framework as an Efficient Catalyst...",
        "dept": "Chemistry",
        "link": "https://pubs.acs.org/doi/10.1021/acsomega.3c08763",
        "img": "images/instituteCarousel/research/COF.jpg",
        "alt": "",
        "authors": ["Dr. Seenuvasan Vedachalam"]
    },
    {
        "title": "Experimental study on mechanical, damping and corrosion properties of Inconel..",
        "dept": "Mechanical",
        "link": "https://www.sciencedirect.com/science/article/abs/pii/S1350630723008257?via%3Dihub",
        "img": "images/instituteCarousel/research/hard-faced stainless steel 304.jpg",
        "alt": "",
        "authors": ["Dr. Karpagaraj"]
    },
    {
        "title": "Optimizing electric vehicle charging in distribution networks ...",
        "dept": "Electrical and Electronics",
        "link": "https://www.sciencedirect.com/science/article/abs/pii/S0360544224005875",
        "img": "images/instituteCarousel/research/Optimizing electric vehicle charging.jpg",
        "alt": "",
        "authors": ["Dr.T.Vinopraba"]
    },
    {
        "title": "Dynamic pricing for load shifting: Reducing electric vehicle charging impacts ",
        "dept": "EEE",
        "link": "https://www.sciencedirect.com/science/article/pii/S2210670724000854",
        "img": "images/instituteCarousel/research/Dr.T.Vinopraba.jpg",
        "alt": "",
        "authors": ["Dr.T.Vinopraba"]
    },
    {
        "title": "Profuse Channel Estimation and Signal Detection Techniques for Orthogonal Time Frequency",
        "dept": "ECE",
        "link": "https://ieeexplore.ieee.org/document/10319451",
        "img": "images/instituteCarousel/research/downlink.jpg",
        "alt": "",
        "authors": ["Dr. Surendar M"]
    }

]
    return render(request, 'research_component.html',{
        "researchCarouselSlides": researchCarouselSlides,})



def gallery_view(request):
    
    return render(request, "gallery.html")
