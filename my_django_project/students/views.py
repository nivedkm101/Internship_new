from django.shortcuts import render

def students(request):
    return render(request, 'students/students.html')
def studentrules(request):
    file = [
    {
      'url': '/static/pdf/announcement/2023/12/Students_General_Rules_updated 18_20.pdf',
      'filename': 'Institute Rules and Regulations'
    }
    ]
    return render(request, 'students/studentrules.html',{'file': file})
def anti_ragging(request):  
    file = [
    {
      'filename':"UGC Regulation on Curbing the Menace of Ragging in Higher Educational Institutions, 2009",
      'url':'/static/docs/studentwelfare/Anti-Ragging/UGC Regulation on Curbing the Menace of Ragging in Higher Educational Institutions, 2009.pdf',
    },
    {
      'filename':'UGC Regulation on Curbing the Menace of Ragging in Higher Educational Institutions (First Amendment), 2012',
      'url':'/static/docs/studentwelfare/Anti-Ragging/UGC Regulation on Curbing the Menace of Ragging in Higher Educational Institutions (First Amen.pdf'
    },
    {
      'filename':'UGC Regulation on Curbing the Menace of Ragging in Higher Educational Institutions (Second Amendment), 2013',
      'url':'/static/docs/studentwelfare/Anti-Ragging/UGC Regulation on Curbing the Menace of Ragging in Higher Educational Institutions (Second Ame.pdf'
    },
    {
      'filename':'UGC Regulation on Curbing the Menace of Ragging in Higher Educational Institutions (Third Amendment), 2016',
      'url':'/static/docs/studentwelfare/Anti-Ragging/UGC Regulation on Curbing the Menace of Ragging in Higher Educational Institutions (Third Amen.pdf'
    },
    {
      'filename':'Undertaking from the Parent as per the provisions of anti-ragging verdict by the Hon’ble Supreme Court (affidavit by parent_guardian)',
      'url':'/static/docs/studentwelfare/Anti-Ragging/Undertaking from the Parent as per the provisions of anti-ragging verdict by the Honble Supreme Court (affidavit by parent_guardian).pdf'
    },
    {
      'filename':'Undertaking from the Students as per the provisions of anti-ragging verdict by the Hon’ble Supreme Court (affidavit by the student)',
      'url':'/static/docs/studentwelfare/Anti-Ragging/Undertaking from the Students as per the provisions of anti-ragging verdict by the Honble Supreme Court (affidavit by the student).pdf'
    },
    {
      'filename':'Anti-ragging poster',
      'url':'/static/docs/studentwelfare/Anti-Ragging/Anti-ragging poster.pdf'
    },
    {
      'filename':'Anti Ragging Cell Circular_2023_UGC',
      'url':'/static/docs/studentwelfare/Anti-Ragging/Anti-Ragging_Cell_Circular.pdf'
    },
    {
      'filename':'Information education communication (IEC) guidelines for councils, universities & colleges_curbing the menace of ragging',
      'url':'/static/docs/studentwelfare/Anti-Ragging/ugc-iec-guidlines-for-councils-universities-and-colleges-for-curbing-the-menace-of-ragging.pdf'
    },
    ]
    files = [
    {
      'url': '/static/docs/studentwelfare/Anti-Ragging/AntiRagging report.pdf',
      'filename': 'Anti-Ragging Awareness Report.pdf'
    }
    ]
    return render(request, 'students/anti_ragging.html',{'file': file,'files': files})
def annualfest(request):    
    
    leciel=[
    {
        'title':"Leciel 2024-25",
        'url':'/static/docs/studentwelfare/leciel report/leciel report 2024-25.pdf',
    },
    ]
    return render(request, 'students/annualfest.html',{'leciel':leciel})
def orientation(request):
    orientation = [
    {
      'pic': "images/events/orientation program 01 2024.jpg",
      'name': ""
    },
    {
      'pic': "images/events/orientation program 02 2024.jpg",
      'name': ""
    },
    ]
    return render(request, 'students/orientation.html',{'orientation':orientation})
def clubs(request):
    clubCategories = [
        {
            'category': 'Technical Clubs',
            'clubs': [
                  { 'name': 'Design Club', 'facultyInCharge'  : ['Dr. Vani V AP CSE', 'Dr. Revathi S AP EEE'] },
                  { 'name': 'Esports Club', 'facultyInCharge': ['Dr. Narendran Rajagopalan Asso. Prof CSE'] },
                  { 'name': 'Coding Club', 'facultyInCharge': ['Dr. Kumaran P AP CSE', 'Dr. Karthik N AP CSE'] },
                  { 'name': 'FOSS Club', 'facultyInCharge': ['Dr. Narendran Rajagopalan Asso. Prof CSE'] },
                  { 'name': 'Robotics Club', 'facultyInCharge': ['Dr. M. V. A. Raju Bahubalendruni AP ME'] },
                  { 'name': 'ANTRiX Club', 'facultyInCharge': ['Dr. Amrtha Bhide Asso. Prof Physics'] },
                  { 'name': 'BIS Standards Club', 'facultyInCharge': ['Dr. J. Ronald Aseer AP ME'] }

            ]
        },
        {
            'category': 'Cultural Clubs',
            'clubs':[
                {"name": "Photography Club", "facultyInCharge": ["Dr. Ansuman Mahapatra AP CSE", "Dr. Sunanda Ambulkar AP CSE"]},
                {"name": "Videography Club", "facultyInCharge": ["Dr. Ansuman Mahapatra AP CSE"]},
                {"name": "Ragasvarupam Indian Performing Arts (RIPA) Club", "facultyInCharge": ["Dr. A. Venkadesan Asso. Prof EEE"]},
                {"name": "Dance Club", "facultyInCharge": ["Dr. Sanjay Bankapur AP CSE", "Dr. Nidhi M Civil Engg"]},
                {"name": "Music Club", "facultyInCharge": ["Dr. S. Babu SASO"]},
                {"name": "Arts and Crafts Club", "facultyInCharge": ["Dr. Gautham A AP Civil Engg", "Dr. Lalrinpuia Tlau AP Mathematics"]},
                {"name": "Culturehood - Fashion Club", "facultyInCharge": ["Dr. Nidhi M AP CE"]},
                {"name": "Literary Club", "facultyInCharge": ["Dr. Smrutisikta Mishra Asso. Prof Humanities and Social Sciences"]},
                {"name": "Year Book Club", "facultyInCharge": ["Dr. Thomas Joseph AP ECE"]},
                {"name": "Language Club", "facultyInCharge": ["Dr. Ajay Kumar Mishra AP Physics (Hindi)", "Dr Aniruddha Kanhe AP ECE(Hindi)", "Dr. Karpagaraj A AP ME (Tamil)", "Dr. Naveen Raj R AP ME (Tamil)", "Dr. Hemachander A AP EEE (Telugu)", "Dr. Nidhi M AP CE (Malayalam)"]},
            ],
        },
        {
            "category": "Social Clubs",
            "clubs": [
                {"name": "Finance Club", "facultyInCharge": ["Dr. Thomas Joseph AP ECE"]},
                {"name": "Propel & Progress Society", "facultyInCharge": ["Dr.Perumalla Venkata Mallikarjun Rao AP CE"]},
                {"name": "UPSC Civil Services Club", "facultyInCharge": ["Dr Aniruddha Kanhe AP ECE"]},
            ],
        },
    ]
    return render(request, 'students/clubs.html',{'clubCategories': clubCategories})
def student_association(request):
    associations = [
        {
            "department": "Civil Engineering",
            "association_name": "Civil Engineering Association (CEA)",
            "faculty_in_charge": ["Dr. Nidhi M", "Dr. Gautham A"],
        },
        {
            "department": "Computer Science and Engineering",
            "association_name": "Association of Computer Science Engineers (ACE)",
            "faculty_in_charge": ["Dr. Narendran Rajagopalan"],
        },
        {
            "department": "Electrical and Electronics Engineering",
            "association_name": "Society of Powerful and Realistic Electrical Engineers (SPREE)",
            "faculty_in_charge": ["Dr. Bijukumar B"],
        },
        {
            "department": "Electronics and Communication Engineering",
            "association_name": "ECE Student Association",
            "faculty_in_charge": ["Dr. Thomash Joseph"],
        },
        {
            "department": "Electronics and Communication Engineering",
            "association_name": "IEI Student Chapter",
            "faculty_in_charge": ["Dr. Sunada Ambulker"],
        },
        {
            "department": "Mathematics",
            "association_name": "Delta Mathematics Association",
            "faculty_in_charge": ["Dr. Lalrinpuia Tlau"],
        },
        {
            "department": "Mechanical Engineering",
            "association_name": "Mechanical Engineering Association (MEA)",
            "faculty_in_charge": ["Dr. Vadivukkarasan M", "Dr. Jack.J.Kenned"],
        },
        {
            "department": "Mechanical Engineering",
            "association_name": "Society of Automotive Engineers (SAE)",
            "faculty_in_charge": ["Dr. Karpagaraj. A", "Dr. SathishKumar . P"],
        },
    ]
    return render(request, 'students/student_association.html', {'associations': associations})
def counselling_service(request):
    return render(request, 'students/counselling_services.html')
def grievance_redressal(request):
    return render(request, 'students/grievance_redressal.html')

def sw_announcements(request):
     announcement24_25=[
    {
      'title':'The Election for the General Body of the Student Council for the AY 2024-2025 is scheduled on 25-07-2024',
      'url':''
    }
  ]
     return render(request, 'students/sw_announcements.html',{'announcement24_25':announcement24_25})
def medical_insurance(request):
    file = [
    
    {
      'filename':"Medi Assist - Reimbursement Claim Form",
      'url':'/static/docs/studentwelfare/mediclaim/2024-2025/Medi Assist - Reimbursement Claim Form.pdf',

    },
    {
      'filename':"Medi Assist - NOC format",
      'url':'/static/docs/studentwelfare/mediclaim/2024-2025/Medi Assist - NOC format.PDF',

    },
    {
      'filename':"Policy Schedule - Students Safety Package Insurance",
      'url':'/static/docs/studentwelfare/mediclaim/2024-2025/Policy Schedule - Students Safety Package Insurance.pdf',

    },
    {
      'filename':"Policy Schedule - Group Mediclaim Policy",
      'url':'/static/docs/studentwelfare/mediclaim/2024-2025/Policy Schedule - Group Mediclaim Policy.pdf',

    },
    {
      'filename':"Terms, Conditions and Procedures",
      'url':'/static/docs/studentwelfare/mediclaim/2024-2025/Terms, Conditions and Procedures.pdf',

    },

    ]
    return render(request, 'students/medical_insurance.html',{'file': file})

def studentActivities(request):
    return render(request, 'students/studentActivities.html')

def aluminiRelations(request):
    return render(request, "students/aluminiRelations.html")

def internship(request):
    
    details = [
    {
        "dept": "CIVIL",
        "internship": "A VBA-Based Application for Efficient Steel Structure Design",
        "duration": "Summer Vacation (2 months)",
    },
    {
        "dept": "CIVIL",
        "internship": "Assessment of Wind-Induced Damage to Critical Infrastructure",
        "duration": "Summer Vacation (2 months)",
    },
    {
        "dept": "CIVIL",
        "internship": "Machine Learning for Concrete Strength Prediction",
        "duration": "Summer Vacation (2 months)",
    },
    {
        "dept": "CIVIL",
        "internship": "Non-Linear Analysis of Prestressed Concrete Members",
        "duration": "Summer Vacation (2 months)",
    },
    {
        "dept": "CIVIL",
        "internship": "Movement of Microplastics in River Bed",
        "duration": "Summer Vacation (2 months)",
    },
    {
        "dept": "CIVIL",
        "internship": "Prediction of Coastline Erosion using AI",
        "duration": "Summer Vacation (2 months)",
    },
    {
        "dept": "CSE",
        "internship": "Computer Vision",
        "duration": "Summer Vacation (2 months)",
    },
    {
        "dept": "CSE",
        "internship": "Internet of Things",
        "duration": "Summer Vacation (2 months)",
    },
    {
        "dept": "CSE",
        "internship": "Cloud and Fog computing",
        "duration": "Summer Vacation (2 months)",
    },
    {
        "dept": "Mathematics",
        "internship": "Differential Equations and Their Applications",
        "duration": "Summer Vacation (2 months)",
    },
    {
        "dept": "Mathematics",
        "internship": "Mathematical Biology",
        "duration": "Summer Vacation (2 months)",
    },
    {
        "dept": "Mechanical",
        "internship": "Augmented Reality for Manufacturing applications",
        "duration": "Summer Vacation (2 months)",
    },
    {
        "dept": "Mechanical",
        "internship": "E-waste Management for Co2 release rate and Circular Economy",
        "duration": "Summer Vacation (2 months)",
    },
    {
        "dept": "Mechanical",
        "internship": "Human robot collaboration",
        "duration": "Summer Vacation (2 months)",
    },
    {
        "dept": "Mechanical",
        "internship": "Lattice Structures for specific energy absorption and blast resistance",
        "duration": "Summer Vacation (2 months)",
    },
    {
        "dept": "Mechanical",
        "internship": "Auxetic materials for biomedical applications",
        "duration": "Summer Vacation (2 months)",
    },
    {
        "dept": "Mechanical",
        "internship": "Damage Identification and localization based on vibration signals",
        "duration": "Summer Vacation (2 months)",
    },
    {
        "dept": "Mechanical",
        "internship": "Computer vision techniques to find vibration measurements from videos",
        "duration": "Summer Vacation (2 months)",
    },
    {
        "dept": "Mechanical",
        "internship": "Thermal Imaging",
        "duration": "Summer Vacation (2 months)",
    },
    {
        "dept": "Mechanical",
        "internship": "Computational Fluid Dynamics",
        "duration": "Summer Vacation (2 months)",
    },
]


    return render(request, "students/internship.html", {"details": details})