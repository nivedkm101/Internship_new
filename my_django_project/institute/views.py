from django.shortcuts import render

def institute(request):
   return render(request, "institute/institute.html")
def campus(request):
   content = [
    {
        "title": "Boys Hostel",
        "body": "NIT Puducherry is a residential institute and provides accommodation to students in the hostels. NITPY has presently two boy’s hostel that provides comfortable accommodation and are located close to the academic area. Presently over 800 students are residing in the hostels. The first year UG students are accommodated in a 4/2-occupancy style accommodation. In subsequent year, double/triple occupancy are allotted depending on the strength of the hostel inmates. Each room comes equipped with requisite amount of lighting and electrical ports, a fan, a chair and table and a steel cot. Wi-fi facility is provided in the hostel premises. PG and Ph.D inmates are given double occupancy accommodation. Barani Hostel (Boys Hostel -1):This hostel has 5 floors consisting of 215 rooms (43 rooms in each floor) and has ten washroom areas(2 in each floor). The hostels also have 04 nos of common rooms. Moyar Hostel (Boys Hostel -2):This hostel is designed for 04 occupancy type and it consists of 80 rooms in 10 blocks (08 rooms in each block) and each block has washroom areas.",
        "img": "/static/images/slideshow/img014.jpg",
        "url": "/hostel/hostel_facilities"
    },
    {
        "title": "Girls Hostel",
        "body": "NIT Puducherry is a residential institute and provides accommodation to students in the hostels. NITPY has presently one girl’s hostel that provides comfortable accommodation and are located close to the academic area. Staying in the campus is particularly attractive because the hostels are located in peaceful, clean, aesthetic environment in campus. The hostels are guarded round the clock by able private security staffs. Patrolling is also done by state security personnel during night. There are also separate wardens for each and every hostel in order to maintain discipline. Cleanliness and hygiene are taken care of and maintained in every aspect. Bhavani Hostel (Girls Hostel):This hostel has 3 floors consisting of 129 rooms (43 rooms in each floor) and has six washroom areas (2 in each floor).  The hostel also have a 02 nos of common room.",
        "img": "/static/images/slideshow/img015.jpg",
        "url": "/hostel/hostel_facilities"
    },
    {
        "title": "Library",
        "body": "The Central Library NIT Puducherry started functioning in 2010, and at present provides an enjoyable learning experience with optimum ambience for study and learning on all working days. The library is growing rapidly with exponential increase in number and type of collection to serve the information needs of the Users. It has very good reading room facility with proper ventilation and natural lighting. The Central Library provides information/knowledge resource through a carefully developed and balanced collection of Books, Journals, Magazines, and Newspapers etc. The Library is enabled with Wi-Fi and LAN facility for unlimited high speed internet access. Sufficient copies of textbooks and reference books are procured for the courses offered. Other books of general interest to students, faculty and staff have also been acquired. It also has a collection of audio-visual materials such as CD/DVD- ROM etc. The users of Central Library of NIT Puducherry are also registered with the National Digital Library sponsored by MHRD and coordinated by IIT Kharagpur.",
        "img": "/static/images/slideshow/img012.jpg",
        "url": "/institute/library"
    },
    {
        "title": "Medical Facilities",
        "body": "The Institute Health Centre is located within the campus. The NITPY health centre registered Clinical establishment under section 15 of The Clinical Establishments (Registration and Regulation) Act, 2010. The NITPY health centre has one  Medical Officer, Two Nurses and Two ambulance drivers. We provide primary health care to all students, staffs and faculty members and their families. We have two bed facility for observation and providing 24 x 7 ambulance services for any medical emergencies and also, we have a facility for Covid – 19 Rapid Antigen Testing. The NITPY health centre following the rules of Bio-Medical Waste Management as per Ministry of Environment and Forest.",
        "img": "/static/images/medical/img015.jpg",
        "url": "/students/medical"
    },
    {
        "title": "Sports Facilities",
        "body": "Sports activities help the students to cast their personality through physical,emotional and social well-being. A true sportsman will have an ability to observe, analyze and take a decision in a spurt of moment. Sports and Games will thus inculcate interpersonal relationship,team work,and cooperative workmanship required for an engineer and to lead a high standards of social and professional life. Sport specialties : At present NIT Puducherry has basketball and indoor Badminton court. Apart from these, students can access fitness center with multi gym and modern fitness facilities. NIT Puducherry has identified and area of 68,083 m2 and initiated work of establishing modern sports and games facilities like tennis courts, football and hockey fields, handball ground and Kho-Kho and Kabaddi courts. Also, an athletic field with 400 sq.m synthetic track is also been planned. Indoor sports complex and stadium has been proposed in 3958 sq. area with wooden flooring, and dormitory facilities for players and the officials during the events.",
        "img": "/static/images/slideshow/img13.jpg",
        "url": "/students/studentActivities"
    }
]
    
   return render(request, "institute/campus.html", {"content": content})
def rules(request):
    btech = [
        {"title": 2013, "url": "/static/docs/rules/B.tech/2013.pdf"},
        {"title": 2017, "url": "/static/docs/rules/B.tech/2017.pdf"},
        {"title": 2019, "url": "/static/docs/rules/B.tech/2019.pdf"},
        {"title": 2022, "url": "/static/docs/rules/B.tech/2022.pdf"},
    ]

    mtech = [
        {"title": 2017, "url": "/static/docs/rules/M.tech/2017.pdf"},
        {"title": 2019, "url": "/static/docs/rules/M.tech/2019.pdf"},
    ]

    msc = [
        {"title": 2022, "url": "/static/docs/rules/M.Sc/PG Rules_MSc_v7_web upload.pdf"},
    ]

    bsc = [
        {"title": 2023, "url": "/static/docs/rules/B.Sc/B.Sc. B.Ed. (Secondary Stage) Programme Regulations (Effective from AY 2023-24 onwards).pdf", "new": True},
    ]

    mtechrs = [
        {"title": 2021, "url": "/static/docs/rules/M.Techrs/NITPY_MTECH_BY_RESEARCH_REGULATION_2021.pdf"},
    ]

    phd = [
        {"title": 2014, "url": "/static/docs/rules/phd/2014.pdf"},
        {"title": 2017, "url": "/static/docs/rules/phd/2017.pdf"},
        {"title": 2019, "url": "/static/docs/rules/phd/2019.pdf"},
        {"title": "2024", "url": "/static/docs/rules/phd/2024.pdf", "new": True},
        {"title": "Amendment in PhD regulation", "url": "/static/docs/rules/phd/Amendment in Ph.D. Regulation 2023.pdf", "new": True},
    ]

    return render(request, "institute/rules.html", {"btech": btech,
        "mtech": mtech,
        "msc": msc,
        "bsc": bsc,
        "mtechrs": mtechrs,
        "phd": phd,})

def forms(request): 
    faculty = [
        {"title": "Casual Leave Form for Non Teaching Staff (Regular)", "url": "/static/docs/forms/Staff_Faculty/001-CL_Form-Non_Teaching_Staff_Regular.pdf"},
        {"title": "Casual Leave Form for Faculty (Regular)", "url": "/static/docs/forms/Staff_Faculty/002-CL_Form-Faculty_Regular.pdf"},
        {"title": "Earned Leave Form for Non Teaching Staff (Regular)", "url": "/static/docs/forms/Staff_Faculty/003-EL_Form-Non_Teaching_Staff_Regular.pdf"},
        {"title": "Earned Leave Form for Faculty Staff (Regular)", "url": "/static/docs/forms/Staff_Faculty/004-EL_Form_Faculty_Regular.pdf"},
        {"title": "Leave Form for Faculty (Contract)", "url": "/static/docs/forms/Staff_Faculty/005-Leave_Form_Faculty_Contract.pdf"},
        {"title": "Leave Form for Non Teaching Staff (Contract)", "url": "/static/docs/forms/Staff_Faculty/006-Leave_Form_Non_Teaching_Staff_Contract.pdf"},
        {"title": "Vacation Application Form for Faculty", "url": "/static/docs/forms/Staff_Faculty/Vacation_Form.pdf"},
        {"title": "Rejoining Report", "url": "/static/docs/forms/Staff_Faculty/Rejoining_Report.pdf"},
        {"title": "TA/DA/OTHERS Claim Form", "url": "/static/docs/forms/Staff_Faculty/007-TA_Form.pdf"},
        {"title": "Honorarium Claim Form", "url": "/static/docs/forms/Staff_Faculty/Honorarium.pdf"},
        {"title": "Receipt Form", "url": "/static/docs/forms/Staff_Faculty/009_Receipt.pdf"},
        {"title": "Advance Application Form", "url": "/static/docs/forms/Staff_Faculty/1. Advance Application Form.pdf"},
        {"title": "Advance Settlement Form", "url": "/static/docs/forms/Staff_Faculty/2. Advance Settlement Form.pdf"},
        {"title": "Imprest Application Form", "url": "/static/docs/forms/Staff_Faculty/3. Imprest Application Form.pdf"},
        {"title": "Imprest Settlement Form", "url": "/static/docs/forms/Staff_Faculty/4. Imprest Settlement Form.pdf"},
        {"title": "Claim-Children Education Allowance Application", "url": "/static/docs/forms/Staff_Faculty/006 - Claim-Children Education Allowance Application.pdf"},
        {"title": "Property Return Form", "url": "/static/docs/forms/Staff_Faculty/Property_return_New_Jan_2015.pdf"},
        {"title": "Attestation Form for Staff / Faculty (Regular)", "url": "/static/docs/forms/Staff_Faculty/ATTESTATION Form.pdf"},
        {"title": "Annual Performance Assessment report Form for Non Teaching Staff", "url": "/static/docs/forms/Staff_Faculty/APAR.pdf"},
        {"title": "Application Form for Quarters Allotment", "url": "/static/docs/forms/Staff_Faculty/Quaters_Allotment_Application_Form.pdf"},
        {"title": "Family Declaration Form", "url": "/static/docs/forms/Staff_Faculty/Family Declaration Form.pdf"},
        {"title": "LTC Application Form", "url": "/static/docs/forms/Staff_Faculty/LTC Application Form.pdf"},
        {"title": "Outstation Travelling Intimation - Form I", "url": "/static/docs/forms/Staff_Faculty/Outstation Travelling Intimation Form - I.pdf"},
        {"title": "Outstation Travelling Intimation - Form II", "url": "/static/docs/forms/Staff_Faculty/Outstation Travelling Intimation Form - II.pdf"},
    ]
    students = [                                                                
        {"title": "Application form for ID card correction/ Duplicate ID card","url": "/static/docs/forms/Students/Id_Card_Application.pdf"},
        {"title": "Hostel Requisition Form","url": "/static/docs/forms/Students/hostel_requisition_form.pdf"},
        {
            "title": "Hostel Mess Reduction Form",
            "url": "/static/docs/forms/Students/Hostel Mess Reduction Form.pdf"
        },
        {
            "title": "Requisition for Railway Concession Form for Students",
            "url": "/static/docs/forms/Students/Railway_form.pdf"
        },
        {
            "title": "Top Class Scholarship Application Form for SC&ST Students",
            "url": "/static/docs/forms/Students/Top_Class_Application_SC&ST.pdf"
        },
        {
            "title": "Govt of Puducherry –>Scholarship Application Form for Students",
            "url": "/static/docs/forms/Students/Govt of Puducherry Scholarship Schemes.pdf"
        },
        {
            "title": "Hostel Leave Form - Girl's or Women's Hostel",
            "url": "/static/docs/forms/Students/Hostel Leave Form - Girl's or Women's Hostel.pdf"
        },
        {
            "title": "Hostel Leave Form - Boy's or Men's Hostel",
            "url": "/static/docs/forms/Students/Hostel Leave Form - Boy's or Men's Hostel.pdf"
        },
    ]

    phd2024 = [
        {
            "title": "1. Choice of Guide",
            "url": "/static/docs/forms/phd/2024/3.1 Chice of Guide.pdf"
        },
        {
            "title": "2. Panel for the DC members",
            "url": "/static/docs/forms/phd/2024/3.2_Panel_for_the_DC_members.pdf"
        },
        {
            "title": "3. Minutes of First DC Meeting",
            "url": "/static/docs/forms/phd/2024/3.3_Minutes_of_First_DC_Meeting.pdf"
        },
        {
            "title": "4. Ph.D. Enrollment cum Course work Registration form",
            "url": "/static/docs/forms/phd/2024/3.4_PhD_Enrollment_Coursework_Registration.pdf"
        },
    ]
    phd = [
        {"title": "1. Choice of Guide", "url": "/static/docs/forms/phd/3.1_Choice_of_Guide.pdf"},
        {"title": "2. Panel for the DC members", "url": "/static/docs/forms/phd/3.2_Panel_for_the_DC_members.pdf"},
        {"title": "3. Minutes of First DC Meeting", "url": "/static/docs/forms/phd/3.3_Minutes_of_First_DC_Meeting.pdf"},
        {"title": "4. Enrollment cum Course Work Registration Form", "url": "/static/docs/forms/phd/PhD_Enrollment_Coursework_Registration.pdf"},
        {"title": "5. Monthly Report", "url": "/static/docs/forms/phd/3.5_Monthly_Report.pdf"},
        {"title": "6. Panel for External Expert nomination to Qualifying examination", "url": "/static/docs/forms/phd/3.6_Panel_External_Expert_Qualifying_Exam.pdf"},
        {"title": "7. Report of External Expert on proposed thesis for qualifying examination", "url": "/static/docs/forms/phd/3.7_Report_External_Expert_Thesis_Qualifying_Exam.pdf"},
        {"title": "8. Report of the Qualifying Examination Board with DC", "url": "/static/docs/forms/phd/3.8_Report_Qualifying_Exam_Board_DC.pdf"},
        {"title": "9. Forwarding note for submission of synopsis", "url": "/static/docs/forms/phd/3.9_Forwarding_Note_Synopsis_Submission.pdf"},
        {"title": "10. Panel submission form for External examiners", "url": "/static/docs/forms/phd/3.10_Panel_Submission_External_Examiners.pdf"},
        {"title": "11. PhD Thesis submission form", "url": "/static/docs/forms/phd/3.11_PhD_Thesis_Submission_Format.pdf"},
        {"title": "12. Minutes of DC meeting to recommend the subject expert for Oral Examination", "url": "/static/docs/forms/phd/3.12_Minutes_DC_Meeting_Oral_Exam.pdf"},
        {"title": "13. Report of PhD viva voce examination", "url": "/static/docs/forms/phd/3.13_Report_PhD_Viva_Voce.pdf"},
        {"title": "14. Guidelines for the preparation of Ph.D. Synopsis report", "url": "/static/docs/forms/phd/Synopsis_Guidelines_NITPY.pdf"},
        {"title": "15. Guidelines for the preparation of Ph.D. Thesis", "url": "/static/docs/forms/phd/Thesis_Guidelines_NITPY.pdf"},
        {"title": "16. Guidelines for preparation of Thesis proposal of Qualifying Examination", "url": "/static/docs/forms/phd/QE_Thesis_Proposal_Format_NITPY.pdf"},
        {"title": "17. Casual Leave Application Form for Research Scholar", "url": "/static/docs/forms/phd/Casual_Leave_Application_Research_Scholar.pdf", "new": True},
        {"title": "18. Shodhganga formatting instructions", "url": "/static/docs/forms/phd/Shodhganga_Formatting_Instructions.pdf", "new": True}
    ]

    general = [
        {"title": "Vehicle Requisition Form", "url": "/static/docs/forms/general/Updated_Vehicle_Requisition_Form_2024.pdf"},
        {"title": "Complaint Registration Form for Hostel Premises", "url": "/static/docs/forms/general/Complaint_Form_Hostel.pdf"},
        {"title": "Complaint Registration Form for Institute Premises", "url": "/static/docs/forms/general/Complaint_Form_Institute.pdf"},
        {"title": "SBI Bank -> Registration Form for Internet Banking", "url": "https://retail.onlinesbi.com/retail/login.htm#"},
        {"title": "Institute Registration Certificate", "url": "/static/docs/forms/general/Institute_Registration_Certificate.pdf"}
    ]

    stores = [
        {"title": "Stationery Indent Form", "url": "/static/pdf/stores/forms/New_Stationery_Indent_Form.pdf"},
        {"title": "Central Stores Manual 2019", "url": "/static/pdf/stores/forms/Central_Store_Rules.pdf"},
        {"title": "Proforma - Purchase of Consumable Asset", "url": "/static/pdf/stores/forms/Revised_Consumable_Proforma.pdf"},
        {"title": "Proforma - Purchase of Non-Consumable Asset", "url": "/static/pdf/stores/forms/Non_Consumable_Proforma.pdf"},
        {"title": "Asset Transfer Form", "url": "/static/pdf/stores/forms/Asset_Transfer_Form.pdf"},
        {"title": "Disposal/Write-Off Form", "url": "/static/pdf/stores/forms/Disposal_Form.pdf"},
        {"title": "Proforma - Upgradation of Non-Consumable Asset", "url": "/static/pdf/stores/forms/Upgrade_NCS_Performa.pdf"}
    ]
    cpda = [
        {"title": "Form 1 - CPDA for Activity A", "url": "/static/docs/forms/cpda/Form_1_CPDA_Activity_A.pdf"},
        {"title": "Form 1 - CPDA for Activity B", "url": "/static/docs/forms/cpda/Form_1_CPDA_Activity_B.pdf"},
        {"title": "Form 2 - CPDA Reimbursement", "url": "/static/docs/forms/cpda/Form_2_CPDA_Reimbursement.pdf"}
    ]
    medical = [
        {
            "title": "Medical Essential Certificate - A",
            "url": "/static/docs/forms/CPDA/medical_essential_certificate_A.pdf"
        },
        {
            "title": "Medical Essential Certificate - B",
            "url": "/static/docs/forms/CPDA/medical_certificate_B.pdf"
        },
        {
            "title": "Medical Essential Certificate - A & B",
            "url": "/static/docs/forms/CPDA/medical_essential_certificate_A_B.pdf"
        }
    ]

    academics = [
        {
            "title": "1. A) CGPA to Percentage Conversion Certificate For B.Tech., M.Tech. students admitted upto 2018 batch (admitted year 2010-2018)",
            "url": "/static/docs/forms/academics/CGPA_to_percentage_conversion_certificate.pdf"
        },
        {
            "title": "1. B ) For B.Tech., M.Tech. students admitted from 2019 batch (admitted year 2019 onwards)",
            "url": "/static/docs/forms/academics/CGPA_to_percentage_conversion_new.pdf"
        },
        {
            "title": "2. Bonafide Requisition Form",
            "url": "/static/docs/forms/Students/BONAFIDE_REQUISITION_FORM_01_05_2023.pdf"
        },
        {
            "title": "3. Certificate for Medium of Instruction",
            "url": "/static/docs/forms/academics/Medium_of_Instruction.pdf"
        },
        {
            "title": "4. Application Form for Transcripts",
            "url": "/static/docs/forms/academics/transcript_detail.pdf"
        },
        {
            "title": "5. Certificate Requisition Form",
            "url": "/static/docs/forms/academics/Certificate_Requisition_Form_2022.pdf"
        },
        {
            "title": "6. Application Form for B.Tech. Comprehensive Viva Voce",
            "url": "/static/docs/forms/academics/BTech_Comprehensive_Viva_Voce_Form.pdf"
        },
        {
            "title": "7. Application Form for B.Tech. Project Viva Voce",
            "url": "/static/docs/forms/academics/BTech_Project_Viva_Voce_Form.pdf"
        },
        {
            "title": "8. Application Form for M.Tech. Project Viva Voce",
            "url": "/static/docs/forms/academics/MTech_Project_Viva_Voce_Form.pdf"
        },
        {
            "title": "9. Redo Course Registration Form",
            "url": "/static/docs/forms/academics/Redo_Course_Registration_Form.pdf"
        }
    ]
    
    networks = [
        {
            "title": "Application Form for creation of email-individual",
            "url": "/static/docs/forms/Networks/Application_Form_Email_Individual.pdf"
        },
        {
            "title": "Application form for creation of mail-Bulk request",
            "url": "/static/docs/forms/Networks/Application_Form_Mail_Bulk_Request.pdf"
        }
    ]

    research = [
        {
            "title": "Format for submission of a patent",
            "url": "/static/docs/forms/R&C/Patent_Approval.pdf"
        },
        {
            "title": "Template for JRF SRF RA Advertisement Notification",
            "url": "/static/docs/forms/R&C/Template_JRF_SRF_RA_Advertisement_Notification.pdf"
        },
        {
            "title": "Application Form for JRF SRF RA Recruitment",
            "url": "/static/docs/forms/R&C/Application_Form_JRF_SRF_RA_Recruitment.pdf"
        },
        {
            "title": "Institute DSIR Certificate",
            "url": "/static/docs/forms/R&C/DSIR_Certificate_2022.pdf"
        }
    ]

    return render(request, "institute/forms.html", {"faculty": faculty, "students": students, "phd": phd, "phd2024": phd2024,
                                                     "general": general, "stores": stores, "cpda": cpda,
                                                       "medical": medical, "academics": academics, "networks": networks,"research": research})

def icc(request):
    ICC = [

    {
      "title": "Penal Consequences",
      'url': "/static/pdf/ICC/Penal_Consequences.pdf"
    },{
      'title': "Sexual Harssment at Workplace",
      'url': "/static/pdf/ICC/Sexual Harssment at Workplace.pdf"
    },
    {
      'title': "Steps for conducting inquiry in case of allegation of Sexual Harassment",
      'url': "/static/pdf/ICC/Steps for conducting inquiry in case of allegation of Sexual Harassment.pdf"
    },
    {
      'title': "SEXUAL HARASSMENT OF WOMEN AT WORKPLACE (Prevention, Prohibition and Redressal) Act, 2013",
      'url': "/static/pdf/ICC/SEXUAL HARASSMENT OF WOMEN AT WORKPLACE (Prevention, Prohibition and Redressal) Act, 2013.pdf"
    },
    {
      'title': "Handbook on Sexual Harassment of Women at Workplace",
      'url': "/static/pdf/ICC/Handbook on Sexual Harassment of Women at Workplace.pdf"
    },
    {
      'title': "Details of Members of the INTERNAL COMPLAINTS COMMITTEE (ICC)",
      'url': "/static/pdf/ICC/Details of Members of the INTERNAL COMPLAINTS COMMITTEE (ICC).pdf"
    },
  ]
    return render(request, "institute/icc.html", {"ICC": ICC})

def newsletter(request):    
    
  newsletter=[

    {
      'title':'Volume No.5, Issue No.2, January 2022',
      'url':'/static/docs/newsletter/January-2022.pdf'
    },
    {
      'title':'Volume No.5, Issue No.1, August 2021',
      'url':'/static/docs/newsletter/August-2021.pdf'
    },
    {
      'title':'Volume No.4, Issue No.2, January 2021',
      'url':'/static/docs/newsletter/January-2021.pdf'
    },
    {
      'title':'Volume No.4, Issue No.1, August 2020',
      'url':'/static/docs/newsletter/August-2020.pdf'
    },
    {
      'title':'Volume No.3, Issue No.2, January 2020',
      'url':'/static/docs/newsletter/January-2020.pdf'
    },
    {
      'title':'Volume No.3, Issue No.1, August 2019',
      'url':'/static/docs/newsletter/August-2019.pdf'
    },{
      'title':'Volume No.2, Issue No.2, January 2019',
      'url':'/static/docs/newsletter/January-2019.pdf'
    },
    {
      'title':'Volume No.2, Issue No.1, August 2018',
      'url':'/static/docs/newsletter/August-2018.pdf'
    },
    {
      'title':'Volume No.1, Issue No.1, July 2017',
      'url':'/static/docs/newsletter/July-2017.pdf'
    }
  ]
  return render(request, "institute/newsletter.html",{ "newsletter":newsletter})

def campusconnect(request):
   newsletter = [
        {
            "title": "Issue No.31, January 2025",
            "url": "/static/docs/campusconnect/Campus_connect_jan2025_issue31.pdf"
        },
        {
            "title": "Issue No.30, December 2024",
            "url": "/static/docs/campusconnect/NITPY CAMPUSCONNECT DEC2024.pdf"
        },
        {
            "title": "Issue No.29, November 2024",
            "url": "/static/docs/campusconnect/NITPY campus connect issue  November 2024.pdf"
        },
        {
            "title": "Issue No.28, October 2024",
            "url": "/static/docs/campusconnect/NITPY campus connect issue  October 2024.pdf"
        },
        {
            "title": "Issue No.27, September 2024",
            "url": "/static/docs/campusconnect/NITPY campus connect issue September 2024.pdf"
        },
        {
            "title": "Issue No.26, August 2024",
            "url": "/static/docs/campusconnect/NITPY campus connect issue August 2024.pdf"
        },
        {
            "title": "Issue No.25, July 2024",
            "url": "/static/docs/campusconnect/NITPY Campus Connect July 2024.pdf"
        },
        {
            "title": "Issue No.24, June 2024",
            "url": "/static/docs/campusconnect/NITPY Campus Connect June 2024.pdf"
        },
        {
            "title": "Issue No.23, May 2024",
            "url": "/static/docs/campusconnect/NITPY campus connect May 2024.pdf"
        },
        {
            "title": "Issue No.22, April 2024",
            "url": "/static/docs/campusconnect/NITPY Campus Connect April 2024.pdf"
        },
        {
            "title": "Issue No.21, March 2024",
            "url": "/static/docs/campusconnect/NITPY Campus Connect March 2024.pdf"
        },
        {
            "title": "Issue No.20, February 2024",
            "url": "/static/docs/campusconnect/NITPY Campus Connect Feb 2024.pdf"
        },
        {
            "title": "Issue No.19, January 2024",
            "url": "/static/docs/campusconnect/NITPY Campus Connect Jan 2024.pdf"
        },
        {
            "title": "Issue No.18, December 2023",
            "url": "/static/docs/campusconnect/NITPY CAMPUSCONNECT DEC2023.pdf"
        },
        {
            "title": "Issue No.17, November 2023",
            "url": "/static/docs/campusconnect/NITPY Campus Connect November 2023.pdf"
        },
        {
            "title": "Issue No.16, October 2023",
            "url": "/static/docs/campusconnect/October Issue_CC 2023.pdf"
        },
        {
            "title": "Issue No.15, September 2023",
            "url": "/static/docs/campusconnect/NITPY Campus Connect SEP_2023.pdf"
        },
        {
            "title": "Issue No.14, August 2023",
            "url": "/static/docs/campusconnect/NITPY Campus Connect August 2023.pdf"
        },
        {
            "title": "Issue No.13, July 2023",
            "url": "/static/docs/campusconnect/NITPY Campus connect JULY ISSUE 2023.pdf"
        },
        {
            "title": "Issue No.12, June 2023",
            "url": "/static/docs/campusconnect/Campus_Connect_june2023.pdf"
        },
        {
            "title": "Issue No.11, May 2023",
            "url": "/static/docs/campusconnect/NITPY Campus connect May 2023.pdf"
        },
        {
            "title": "Issue No.10, April 2023",
            "url": "/static/docs/campusconnect/NITPY Campus connect April 2023.pdf"
        },
        {
            "title": "Issue No.9, March 2023",
            "url": "/static/docs/campusconnect/NITPY Campus connect march 2023.pdf"
        },
        {
            "title": "Issue No.8, February 2023",
            "url": "/static/docs/campusconnect/NITPY campus connect feb 2023.pdf"
        },
        {
            "title": "Issue No.7, January 2023",
            "url": "/static/docs/campusconnect/NITPY Campus Connect jan 2023.pdf"
        },
        {
            "title": "Issue No.6, December 2022",
            "url": "/static/docs/campusconnect/nitpy newletter dec 2022.pdf"
        },
        {
            "title": "Issue No.5, November 2022",
            "url": "/static/docs/campusconnect/NITPY campus connect november.pdf"
        },
        {
            "title": "Issue No.4, October 2022",
            "url": "/static/docs/campusconnect/FINAL OCT ISSUE 4.pdf"
        },
        {
            "title": "Issue No.3, September 2022",
            "url": "/static/docs/campusconnect/updated_Campus_connect_issue_3_sep22.pdf"
        },
        {
            "title": "Issue No.2, August 2022",
            "url": "/static/docs/campusconnect/NITPY campus connect august.pdf"
        },
        {
            "title": "Issue No.1, July 2022",
            "url": "/static/docs/campusconnect/NITPY campus connect july-1.pdf"
        }
    ]
   return render(request, "institute/campusconnect.html", {"newsletter": newsletter})

def bulletin(request):
    newsletter = [
        {
            "title": "Issue No.22, January 2025",
            "url": "/static/docs/bulletin/NITPY Bullentin JANUARY 2025.pdf"
        },
        {
            "title": "Issue No.21, December 2024",
            "url": "/static/docs/bulletin/NITPY_BULLETIN_DEC2024.pdf"
        },
        {
            "title": "Issue No.20, September 2024",
            "url": "/static/docs/bulletin/NITPY BULLETIN SEPTEMBER 2024.pdf"
        },
        {
            "title": "Issue No.19, August 2024",
            "url": "/static/docs/bulletin/NITPY BULLETIN August 2024.pdf"
        },
        {
            "title": "Issue No.18, May 2024",
            "url": "/static/docs/bulletin/NITPY bulletin May-2024.pdf"
        },
        {
            "title": "Issue No.17, March 2024",
            "url": "/static/docs/bulletin/NITPY bulletin March 2024.pdf"
        },
        {
            "title": "Issue No.16, February 2024",
            "url": "/static/docs/bulletin/NITPY BULLETIN Feb 2024.pdf"
        },
        {
            "title": "Issue No.15, January 2024",
            "url": "/static/docs/bulletin/NITPY Bullentin Jan24.pdf"
        },
        {
            "title": "Issue No.14, December 2023",
            "url": "/static/docs/bulletin/NITPY BULLENTIN DECEMBER 2023.pdf"
        },
        {
            "title": "Issue No.13, October 2023",
            "url": "/static/docs/bulletin/NITPY BULLETIN OCTOBER 2023.pdf"
        },
        {
            "title": "Issue No.12, September 2023",
            "url": "/static/docs/bulletin/NITPY Sep 2023 Bulletin.pdf"
        },
        {
            "title": "Issue No.11, August 2023",
            "url": "/static/docs/bulletin/NITPY AUGUST BULLETIN 2023.pdf"
        },
        {
            "title": "Issue No.10, July 2023",
            "url": "/static/docs/bulletin/NITPY BULLETIN JULY 2023.pdf"
        },
        {
            "title": "Issue No.9, May 2023",
            "url": "/static/docs/bulletin/NITPY BULLETIN MAY 2023.pdf"
        },
        {
            "title": "Issue No.8, March 2023",
            "url": "/static/docs/bulletin/NITPY BULLETIN MARCH 2023.pdf"
        },
        {
            "title": "Issue No.7, February 2023",
            "url": "/static/docs/bulletin/NITPY_BULLETIN_FEB_2023.pdf"
        },
        {
            "title": "Issue No.6, January 2023",
            "url": "/static/docs/bulletin/NITPY BULLETIN JANUARY 2023.pdf"
        },
        {
            "title": "Issue No.5, December 2022",
            "url": "/static/docs/bulletin/NITPY BULLETIN DECEMBER  2022.pdf"
        },
        {
            "title": "Issue No.4, November 2022",
            "url": "/static/docs/bulletin/NITPY BULLETIN NOVERMBER 2022.pdf"
        },
        {
            "title": "Issue No.3, October 2022",
            "url": "/static/docs/bulletin/NITPY BULLETIN OCTOBER 2022.pdf"
        },
        {
            "title": "Issue No.2, September 2022",
            "url": "/static/docs/bulletin/NITPY BULLETIN SEPTEMBER 2022.pdf"
        },
        {
            "title": "Issue No.1, August 2022",
            "url": "/static/docs/bulletin/NITPY BULLETIN AUGUST 2022.pdf"
        }
    ]
    return render(request,"institute/bulletin.html", {"newsletter": newsletter})
def rti(request):
    file = [
    {
      'url': '/static/docs/RTI and Procedures/rtiact.pdf',
      'filename': 'RTI Act',
    },
    {
      'url': '/static/docs/RTI and Procedures/APPLICATION.pdf',
      'filename': 'Application Form',
    },
    {
      'url': '/static/docs/RTI and Procedures/procedure.pdf',
      'filename': 'Procedure',
    }
  ]
    return render(request, "institute/rti.html", {"file": file})

def nirf(request):  
    reports24 = [
    {
        "title": "Full Report (Engineering)",
        "url": "/static/docs/academics/nirf/2024/Engineering.pdf"
    },
    {
        "title": "Full Report (Innovation)",
        "url": "/static/docs/academics/nirf/2024/Innovation.pdf"
    },
    {
        "title": "Full Report (Overall)",
        "url": "/static/docs/academics/nirf/2024/Overall.pdf"
    },
]

    reports23 = [
    {
        "title": "Full Report (Overall)",
        "url": "/static/docs/academics/nirf/2023/Full Report (Overall)_PhD.pdf"
    },
    {
        "title": "Full Report (Engineering)",
        "url": "/static/docs/academics/nirf/2023/Full Report (Engineering)_PhD.pdf"
    },
]

    reports22 = [
    {
        "title": "Full Report (Overall)",
        "url": "/static/docs/academics/nirf/2022/Engineering 2022.pdf"
    },
]

    reports21 = [
    {
        "title": "Full Report (Overall)",
        "url": "/static/docs/academics/nirf/2021/Overall  2021.pdf"
    },
    {
        "title": "Full Report (Engineering)",
        "url": "/static/docs/academics/nirf/2021/Engineering 2021.pdf"
    },
]

    reports20 = [
    {
        "title": "Full Report (Overall)",
        "url": "/static/docs/academics/nirf/2020/Engineering  2020.pdf"
    },
]

    reports19 = [
    {
        "title": "Full Report (Overall)",
        "url": "/static/docs/academics/nirf/2019/All_Report.pdf"
    },
    {
        "title": "Financial Resources",
        "url": "/static/docs/academics/nirf/2019/Financial_Resources.pdf"
    },
    {
        "title": "PCS Facilities",
        "url": "/static/docs/academics/nirf/2019/PCS.pdf"
    },
    {
        "title": "Research Details",
        "url": "/static/docs/academics/nirf/2019/Research_Details.pdf"
    },
    {
        "title": "Faculty Details",
        "url": "/static/docs/academics/nirf/2019/Faculty_Details.pdf"
    },
    {
        "title": "Student Details",
        "url": "/static/docs/academics/nirf/2019/Student_Details.pdf"
    },
]

    reports18 = [
    {
        "title": "Full Report (Overall)",
        "url": "/static/docs/academics/nirf/2018/NIRF_2018.pdf"
    },
]

    reports17 = [
    {
        "title": "Consultany Projects",
        "url": "/static/docs/academics/nirf/2017/ConsultancyProjectDetail_Registrar.pdf"
    },
    {
        "title": "Entrepreneurship",
        "url": "/static/docs/academics/nirf/2017/Enterpreneurship_AC.pdf"
    },
    {
        "title": "Full time Executive Programs of One Year Duration",
        "url": "/static/docs/academics/nirf/2017/ExecutiveDevelopmentProgram.pdf"
    },
    {
        "title": "Students opting for higher studies",
        "url": "/static/docs/academics/nirf/2017/HigherStudiesAC.pdf"
    },
    {
        "title": "Sponsored Projects",
        "url": "/static/docs/academics/nirf/2017/SponsoredResearchDetail.pdf"
    },
    {
        "title": "Top University Details 3D",
        "url": "/static/docs/academics/nirf/2017/TopUniversityDetails_3D_AC.pdf"
    },
    {
        "title": "Top University DEtails 5D",
        "url": "/static/docs/academics/nirf/2017/TopUniversityDetails_5D_AC.pdf"
    },
]
    return render(request, "institute/nirf.html", {
        "reports24": reports24,
        "reports23": reports23,
        "reports22": reports22,
        "reports21": reports21,
        "reports20": reports20,
        "reports19": reports19,
        "reports18": reports18,
        "reports17": reports17,
    })