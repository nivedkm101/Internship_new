from django.shortcuts import render

def calendar_view(request):
    calendar = [
    {
        "title": "Academic Calendar for the EVEN semester of the AY 2024-25",
        "url": "docs/academics/Academics calender/Academic_Calendar_EVEN_Semester_2024-25_All programme.pdf",
        "new": True
    },
    {
        "title": "Academic Calendar for the ODD semester of the AY 2024-25 for the B.Sc. B.Ed. programme",
        "url": "docs/academics/Academics calender/Academic Calendar for the ODD_B.Sc. B.Ed._2024-25.pdf",
        "new": True
    },
    {
        "title": "Academic Calendar for the B. Tech (I Year/2024 admitted batch)",
        "url": "docs/academics/Academics calender/Academic Calendar for the B. Tech (I Year- 2024 admitted batch).pdf",
    },
    {
        "title": "Academic Calendar for the ODD semester of the AY 2024-25",
        "url": "docs/academics/Academics calender/Academic_Calendar_Odd_Semester_2024-25.pdf",
    },
    {
        "title": "Academic Calendar for the EVEN semester of the AY 2023-24",
        "url": "docs/academics/Academics calender/Academic_Calendar_EVEN_Semester_2023-24_All programme.pdf",
    },
    {
        "title": "Academic Calendar of the B.Sc. B. Ed. Programme for the AY 2023-24 Odd Semester",
        "url": "docs/academics/Academics calender/Academic_Calendar_Odd Semester_2023-24_I Year B.Sc. B.Ed.pdf",
    },
    {
        "title": "Academic Calendar for the B.Tech._M.Tech._M.Sc. (I Year/2023 admitted batch)",
        "url": "docs/academics/Academics calender/Academic_Calendar_Odd Semester_2023-24_I Year_b.Tech._M.Tech._M.Sc_II.pdf",
    },
    {
        "title": "Academic_Calendar_Odd_semester_2023-24_B.Tech.(II_III_IV) Year, M.Tech. (II Year), M.Sc. (II Year), M.Tech. (by Research) & Ph.D.",
        "url": "docs/academics/Academics calender/Academic_Calendar_Odd_Semester_2023-24_II.pdf",
    },
    {
        "title": "Academic_Calendar_Even semester_2022-23_B.Tech._II_III_IV Year & PG_Ph.D.",
        "url": "docs/academics/Academics calender/Academic_Calendar_Even semester_2022-23_B.Tech._II_III_IV Year & PG_Ph.D.pdf",
    },
    {
        "title": "Academic_Calendar_2022-23 for B.Tech._first year_admitted in 2022",
        "url": "docs/academics/Academics calender/Academic_Calendar_2022-23 for B.Tech._first year_admitted in 2022.pdf",
    },
    {
        "title": "Academic Calendar_July 2022 to December 2022 ( M.Sc., M.Tech. & Ph.D. - Course work)",
        "url": "docs/academics/Academics calender/Academic_Calendar_July_2022_MTech._M.Sc_PhD.pdf",
    },
    {
        "title": "Academic Calendar - JULY 2022 To December 2022 - B.Tech",
        "url": "docs/academics/Academics calender/Academic_Calendar_July_2022.pdf",
    },
    {
        "title": "Academic Calendar - November 2019 To July 2020",
        "url": "docs/academics/Academics calender/2019-2020.pdf"
    },
    {
        "title": "Academic Calendar - July 2019 to December 2019",
        "url": "docs/academics/Academics calender/Academic Calendar July-Dec 2019.pdf"
    },
    {
        "title": "Academic Calendar - January 2019 to July 2019",
        "url": "docs/academics/Academics calender/Academic_Calendar_Jan_July_2019.pdf"
    },
    {
        "title": "Revised Academic Calendar - July 2018 to December 2018",
        "url": "docs/academics/Academics calender/Academic_Calendar_July_2018(Revised).pdf"
    },
    {
        "title": "Academic Calendar - July 2018 to December 2018",
        "url": "docs/academics/Academics calender/Academic_Calendar_July_2018.pdf"
    },
    {
        "title": "Academic Calendar - January 2018 to July 2018",
        "url": "docs/academics/Academics calender/Academic_Calendar_Jan_2018.pdf"
    },
]

    
    return render(request, 'academics/calendar.html', {"calendar": calendar})


def email_queries(request):
    table_data = {
        "data": [
            ["Educational Verification of students", "academicoffice@nitpy.ac.in"],
            ["Queries related to Academic activities of UG Programmes", "ad-ugacad@nitpy.ac.in"],
            ["Queries related to Academic activities of PG Programmes & Research", "ad-pgacad@nitpy.ac.in"],
            ["Queries related to Scholarship and Fee Details", "asstreg@nitpy.ac.in"],
            ["Queries related to Examination Cell", "academicoffice@nitpy.ac.in"]
        ]
    }
    return render(request, 'academics/emailContacts.html', {"tableData": table_data})

def convocation(request):
    table1 = [
        {
            'Sl': '01',
            'Name': 'Balcony, KiRaa Auditorium, V. O. Chidambaram Pillai Block, Administrative Building, NIT Puducherry',
            'Quantity': 'Parents/Family Members of Ph.D. Degree recipients, M.Tech. Degree recipients and Medal Winners',
        },
        {
            'Sl': '02',
            'Name': 'SF5, SF6 & SF7, Vikram Sarabhai Block, NIT Puducherry',
            'Quantity': 'Parents/Family Members of B.Tech. Degree recipients',
        },
    ]

    table2 = [
        {
            'Name': '5:00 AM',
            'Quantity': 'Railway station - Bus stand - Nehru Nagar - Keelakazhakudy - Kottucherry - Varichikudy - NITPY',
        },
        {
            'Name': '6:00 AM',
            'Quantity': 'Bus stand - Nehru Nagar - Keelakazhakudy - Kottucherry - Varichikudy - NITPY',
        },
        {
            'Name': '7:00 AM',
            'Quantity': 'Bus stand - Nehru Nagar - Keelakazhakudy - Kottucherry - Varichikudy - NITPY',
        },
        {
            'Name': '8:00 AM',
            'Quantity': 'Varichikudy - NITPY',
        },
    ]

    table3 = [
        {
            'Name': '3:00 PM',
            'Quantity': 'NITPY - Varichikudy',
        },
        {
            'Name': '3:30 AM',
            'Quantity': 'NITPY - Varichikudy',
        },
        {
            'Name': '4:00 PM',
            'Quantity': 'NITPY - Varichikudy - Kottucherry - Keelakazhakudy - Nehru Nagar - Bus stand',
        },
    ]

    table11 = [
        { 'Sl': 1, 'Name': 'Balcony, KiRaa Auditorium', 'Quantity': 'Parents / Family Members of Ph.D., M.Tech., M.Sc., M.Tech. (By Research) Degree recipients and Medal Winners' },
        { 'Sl': 2, 'Name': 'SF-7, Vikram Sarabhai Block', 'Quantity': '1. Department of CE, 2. Department of EEE, 3. Department of ME, B.Tech.' },
        { 'Sl': 3, 'Name': 'SF-5, Vikram Sarabhai Block', 'Quantity': 'Department of CSE' },
        { 'Sl': 4, 'Name': 'SF-6, Vikram Sarabhai Block', 'Quantity': 'Department of ECE' },
    ]

    ELEVENTH = [
        {
            'title': 'List of Graduands & Medal Winners - Updated',
            'url': '/static/pdf/CONVOCATION/ELEVENTH CONVOCATION/List of Graduands & Medal Winners.pdf',
        },
        {
            'title': '11th Convocation - Accommodation',
            'url': '/static/pdf/CONVOCATION/ELEVENTH CONVOCATION/XI Convocation - Accommodation.pdf',
        },
        {
            'title': 'Revised Circular - 11th Convocation of National Institute of Technology Puducherry',
            'url': '/static/pdf/CONVOCATION/ELEVENTH CONVOCATION/11th Convocation Circular.pdf',
        },
        {
            'title': 'Letter to Graduands (REVISED SCHEDULE)',
            'url': '/static/pdf/CONVOCATION/ELEVENTH CONVOCATION/Letter to Graduands (Revised Schedule) - 11th Convocation.pdf',
        },
        {
            'title': 'Note to the Graduands (REVISED SCHEDULE)',
            'url': '/static/pdf/CONVOCATION/ELEVENTH CONVOCATION/Note to Graduands (Revised Schedule) - 11th Convocation - 23.09.2024 @ 04.00 PM.pdf',
        },
    ]
    TENTH = [
        {
            'title': '10th convocation - Photos link',
            'url': 'https://drive.google.com/drive/u/0/folders/1IgvJbJy9DcanQemOxL6z4Lty_C4BihGj',
        },
        {
            'title': 'Note to Graduands',
            'url': '/static/pdf/CONVOCATION/TENTH CONVOCATION/Note to Graduands - 10th Convocation.pdf',
        },
        {
            'title': 'Letter to Graduands',
            'url': '/static/pdf/CONVOCATION/TENTH CONVOCATION/Letter to Graduands - 10th Convocation.pdf',
        },
        {
            'title': 'List of Graduands & Medal Winners',
            'url': '/static/pdf/CONVOCATION/TENTH CONVOCATION/List of Graduands & Medal Winners.pdf',
        },
        {
            'title': 'Circular - 10th Convocation of National Institute of Technology Puducherry',
            'url': '/static/pdf/CONVOCATION/TENTH CONVOCATION/10th Convocation Circular.pdf',
        },
    ]

    NINENTH = [
        {
            'title': '9th convocation - Photos link',
            'url': 'https://drive.google.com/drive/folders/1VdOgi0969M9Gy_Gj8AcLrUinyk43XxVL',
        },
        {
            'title': 'Transport Arrangements for Graduands and Parents Ninth (9th) convocation - 21.02.2023',
            'url': '/static/pdf/CONVOCATION/NINENTH CONVOCATION/Transportation Arrangements for Graduands - 9th Convocation (21.02.2023).pdf',
        },
        {
            'title': 'Note to Graduands',
            'url': '/static/pdf/CONVOCATION/NINENTH CONVOCATION/Note to Graduands - 9th Convocation - 21.02.2023.pdf',
        },
        {
            'title': 'Letter to Graduands',
            'url': '/static/pdf/CONVOCATION/NINENTH CONVOCATION/Letter to Graduands - 9th Convocation - 21.02.2023.pdf',
        },
        {
            'title': 'Circular - 9th Convocation of National Institute of Technology Puducherry',
            'url': '/static/pdf/CONVOCATION/NINENTH CONVOCATION/Initial Circular.pdf',
        },
        {
            'title': 'List of Graduands',
            'url': '/static/pdf/CONVOCATION/NINENTH CONVOCATION/Graduands list _9th convocation_web upload.pdf',
        },
    ]
    EIGHTH = [
        {'title': 'Invitation', 'url': '/static/pdf/CONVOCATION/EIGHTH CONVOCATION/Invitation_8th Convocation.pdf'},
        {'title': 'Circular - 8th Convocation of National Institute of Technology Puducherry', 'url': '/static/pdf/CONVOCATION/EIGHTH CONVOCATION/Initial Circular.pdf'},
        {'title': 'Letter to Graduands - 8th Convocation - 19th May, 2022', 'url': '/static/pdf/CONVOCATION/EIGHTH CONVOCATION/Letter to Graduands - 8th Convocation - 19.05.2022.pdf'},
        {'title': '1.List of Medal Winners', 'url': '/static/pdf/CONVOCATION/EIGHTH CONVOCATION/Medal Winners_2021.pdf'},
        {'title': '2. List of Graduands', 'url': '/static/pdf/CONVOCATION/EIGHTH CONVOCATION/Graduands list_8th convocation.pdf'},
        {'title': '3. Instructions for the degree recipients of 8th Convocation', 'url': '/static/pdf/CONVOCATION/EIGHTH CONVOCATION/Note to the Graduands - 8th Convocation - 14.05.2022.pdf'},
    ]

    SEVENTH = [
        {'title': ' Invitation', 'url': '/static/pdf/CONVOCATION/SEVENTH CONVOCATION - 19th FEBRUARY 2021/NITPy 7th Convocation_Invitation.jpg'},
        {'title': ' Graduands List', 'url': '/static/pdf/CONVOCATION/SEVENTH CONVOCATION - 19th FEBRUARY 2021/Graduands list for the 7th Convocation-new.pdf'},
        {'title': ' List of Medal Winners', 'url': '/static/pdf/CONVOCATION/SEVENTH CONVOCATION - 19th FEBRUARY 2021/Medal Winners.pdf'},
        {'title': ' Guidelines for attending Convocation', 'url': '/static/pdf/CONVOCATION/SEVENTH CONVOCATION - 19th FEBRUARY 2021/Guidelines for attending 7th convocation in NITPY.pdf'},
        {'title': ' 7th Convocation - Form to Upload photo with Shawl', 'url': 'https://accounts.google.com/ServiceLogin/signinchooser?service=wise&passive=1209600&continue=https%3A%2F%2Fdocs.google.com%2Fforms%2Fd%2Fe%2F1FAIpQLSdx4fHxkq0dpGtCYdO7_wfQPiZWmBVziLG6tcfMl5FbM6fEPA%2Fviewform%3Fusp%3Dsend_form&followup=https%3A%2F%2Fdocs.google.com%2Fforms%2Fd%2Fe%2F1FAIpQLSdx4fHxkq0dpGtCYdO7_wfQPiZWmBVziLG6tcfMl5FbM6fEPA%2Fviewform%3Fusp%3Dsend_form&ltmpl=forms&flowName=GlifWebSignIn&flowEntry=ServiceLogin'},
    ]

    SIXTH = [
        {'title': ' Invitation', 'url': '/static/pdf/CONVOCATION/SIXTH CONVOCATION - 28th FEBRUARY 2020/Invitation_6th_Convocation.pdf'},
        {'title': ' Graduands List', 'url': '/static/pdf/CONVOCATION/SIXTH CONVOCATION - 28th FEBRUARY 2020/Name_List.pdf'},
        {'title': ' Important Dates', 'url': '/static/pdf/CONVOCATION/SIXTH CONVOCATION - 28th FEBRUARY 2020/Important_Dates_6th Convocation.pdf'},
        {'title': ' Convocation Circular', 'url': '/static/pdf/CONVOCATION/SIXTH CONVOCATION - 28th FEBRUARY 2020/Circular.pdf'},
        {'title': ' List of Medal Winners', 'url': '/static/pdf/CONVOCATION/SIXTH CONVOCATION - 28th FEBRUARY 2020/MEDAL_WINNERS.pdf'},
        {'title': ' Letter to the Graduands', 'url': '/static/pdf/CONVOCATION/SIXTH CONVOCATION - 28th FEBRUARY 2020/Letter_to_Graduands_6th Convocation.pdf'},
        {'title': ' Instructions to the Graduands', 'url': '/static/pdf/CONVOCATION/SIXTH CONVOCATION - 28th FEBRUARY 2020/Instructions to the Graduands.pdf'},
    ]

    context = {
        'table1': table1,
        'table2': table2,
        'table3': table3,
        'table11': table11,
        'ELEVENTH': ELEVENTH,
        'TENTH': TENTH,
        'NINENTH': NINENTH,
        'EIGHTH': EIGHTH,
        'SEVENTH': SEVENTH,
        'SIXTH': SIXTH,
    }

    return render(request, 'academics/convocation.html', context)


def exam(request):
    exams = [
        {
            "title": "Final Assessment Timetable for the ODD semester of the AY 2024-25 for the B.Sc. B.Ed. (I Year)",
            "url": "/static/pdf/Examination Schedule/2025/Final Assessment Timetable for the ODD semester of the AY 2024-25 for the B.Sc. B.Ed. (I Year).pdf",
        },
        {
            "title": "Circular, Schedule, and Registration form for Make - Up Examinations First Year to be held in January - 2025",
            "url": "/static/pdf/Examination Schedule/2025/Circular, Schedule, and Registration form for Make - Up Examinations First Year to be held in January - 2025.pdf",
        },
        {
            "title": "Circular, Schedule, and Registration form for Make-Up Examinations to be held in January-2025",
            "url": "/static/pdf/Examination Schedule/2025/Circular, Schedule, and Registration form for Make-Up Examinations to be held in January-2025.pdf",
        },
        {
            "title": "Final Assessment Timetable for the ODD semester of the AY 2024-25 for the B.Tech. (I year), M.Tech. (I Year), M.Sc. (I Year)",
            "url": "/static/pdf/Examination Schedule/Final Assessment Timetable for the ODD semester of the AY 2024-25 for the B.Tech. (I year), M.Tech. (I Year), M.Sc. (I Year).pdf",
        },
        {
            "title": "Final Assessment Timetable for the ODD semester of the AY 2024-25 for the B.Tech. (II/III/IV year), M.Sc. (II Year) & B.Sc. B.Ed. (II Year)",
            "url": "/static/pdf/Examination Schedule/November Exam Time Table_2024.pdf",
        },
        {
            "title": "Circular, Schedule, and Registration form for Make-Up Examinations to be held in July-2024",
            "url": "/static/pdf/Examination Schedule/Circular, Schedule, and Registration form for Make-Up Examinations to be held in July-2024.pdf",
        },
        {
            "title": "Final Assessment Timetable for the Even semester of the AY 2023-24 for the B.Sc. B.Ed.",
            "url": "/static/pdf/Examination Schedule/Final Assessment Timetable for the Even semester of the AY 2023-24 for the B.Sc. B.Ed.pdf",
        },
        {
            "title": "Final Assessment Timetable for the Even semester of the AY 2023-24 for the B.Tech., M.Tech., M.Sc. (I year)",
            "url": "/static/pdf/Examination Schedule/Final Assessment Timetable for the Even semester of the AY 2023-24 for the (I year).pdf",
        },
        {
            "title": "Final Assessment Timetable for the Even semester of the AY 2023-24 for the B.Tech. (II/III/IV year)",
            "url": "/static/pdf/Examination Schedule/EVEN Sem time table_Apr_2024 - Final.pdf",
        },
        {
            "title": "Final Assessment Time Table for the ODD Semester of the Academic Year 2023-24 (B.Sc. B.Ed. (I year))",
            "url": "/static/pdf/Examination Schedule/Final Assessment Time Table for the ODD Semester of the Academic Year 2023-24 (B.Sc. B.Ed. (I year)).pdf",
        },
        {
            "title": "Circular, Schedule, and Registration form for Make-Up Examinations to be held in February-2024",
            "url": "/static/pdf/Examination Schedule/Circular, Schedule, and Registration form for Make-Up Examinations to be held in February-2024.pdf",
        },
        {
            "title": "Final Assessment Time Table for the ODD Semester of the Academic Year 2023-24 (B.Tech./M.Tech./M.Sc. I year)",
            "url": "/static/pdf/Examination Schedule/Odd Sem time table_B.Tech._M.Tech._M.Sc. web upload.pdf",
        },
        {
            "title": "Final Assessment Time Table for the ODD Semester of the Academic Year 2023-24 (B.Tech. II/III/IV year and M.Sc. II year)",
            "url": "/static/pdf/Examination Schedule/ODD Sem time table_NOV_2023 - Final.pdf",
        },
        {
            "title": "Circular, Schedule, and Registration form for Make-Up Examinations to be held in July-2023 for the B.Tech. students (I year / II Semester)",
            "url": "/static/pdf/announcement/2023/07/Circular, Schedule, and Registration form for Make-Up Examinations to be held in July-2023 for the B.Tech. students I year.pdf",
        },
        {
            "title": "Circular, Schedule, and Registration form for Make-Up Examinations to be held in July-2023 for the B.Tech. students (II, III & IV year)",
            "url": "/static/pdf/announcement/2023/06/Circular, Schedule, and Registration form for Make-Up Examinations to be held in July-2023 for the B.Tech. students (II, III & IV year).pdf",
        },
        {
            "title": "Final Assessment Time Table for the EVEN Semester of the Academic Year 2022-23 (B.Tech.I Year)",
            "url": "/static/pdf/announcement/2023/05/Final Assessment Time Table for the EVEN Semester of the Academic Year 2022-23 (B.Tech.I Year).pdf",
        },
        {
            "title": "Final Assessment Time Table for the Even Semester of the Academic Year 2021-22 (for B.Tech. II Year and M.Tech. I Year)",
            "url": "/static/pdf/announcement/2022/04/Even Sem time table with instructions 29.04.2022 web upload.pdf",
        },
        {
            "title": "Final Assessment Time Table for the Even Semester of the Academic Year 2021-22 (for B.Tech. III & IV Year)",
            "url": "/static/pdf/announcement/2022/03/Even Sem time table with instructions for noticeboard web upload.pdf",
        },
        {
            "title": "Time Table for the Final Assessment of Theory Courses except I Year B.Tech -Academic Year 2021-22",
            "url": "/static/pdf/Examination Schedule/Final exam Time table for the odd semester_December 2021_to notice board.pdf",
        },
        {
            "title": "Even Semester Theory Examination Schedule May 2019",
            "url": "/static/pdf/Examination Schedule/Time_Table_for_UG_PG_May_2019.pdf",
        },
        {
            "title": "Updated End Semester Lab Examination Schedule (Even Semester 2018-19) April 2019",
            "url": "/static/pdf/Examination Schedule/Lab_Schedule_2019April.pdf",
        },
        {
            "title": "Supplementary Examination (December 2018 - January 2019) Time Table",
            "url": "/static/pdf/Examination Schedule/Supplementary_TimeTable.pdf",
        },
        {
            "title": "Supplementary Examinations (December 2018 - January 2019) Circular",
            "url": "/static/pdf/Examination Schedule/Supplementary_Circular.pdf",
        },
        {
            "title": "Semester Examination Time Table Ph.D",
            "url": "/static/pdf/Examination Schedule/Sem_theory_Time_table_for_PhD.pdf",
        },
    ]
    return render(request, "academics/exam.html", {"exams": exams})


def fee(request):
    Btech = [
    {
        "title": "Institute Fee Structure for the AY 2024-25 - Under Graduate Programme",
        "url": "/static/docs/academics/fees structure/Institute Fee Structure for the AY 2024-25 - Under Graduate Programme.pdf",
        "new": True
    },
    {
        "title": "Institute Fee Structure for the AY 2023-24 - Under Graduate Programme",
        "url": "/static/docs/academics/fees structure/consolidated fee structure for academic year 2023-24 UG.pdf",
    },
    {
        "title": "Institute Fee Structure for the AY 2022-23 - Under Graduate Programme",
        "url": "/static/docs/academics/fees structure/consolidated fee structure_UG.pdf",
    },
]

    Bsc = [
    {
        "title": "Institute Fee Structure for the AY 2024-25 - B.Sc. B.Ed. programme",
        "url": "/static/docs/academics/fees structure/Institute Fee Structure for the AY 2024-25 - B.Sc. B.Ed. programme.pdf",
        "new": True
    },
    {
        "title": "Institute Fee Structure for the AY 2023-24 - B.Sc. B.Ed. programme",
        "url": "/static/docs/academics/fees structure/Institute Fee Structure for the AY 2023-24 B Sc BeD programme.pdf",
    },
]

    PG = [
    {
        "title": "Institute Fee Structure for the AY 2024-25 - Post Graduate & Ph.D. programme",
        "url": "/static/docs/academics/fees structure/Institute Fee Structure for the AY 2024-25 - Post Graduate & Ph.D. programme.pdf",
        "new": True
    },
    {
        "title": "Institute Fee Structure for the AY 2023-24 - Post Graduate & Ph.D. programme",
        "url": "/static/docs/academics/fees structure/consolidated fee structure for academic year 2023-24 PG & PhD.pdf",
    },
    {
        "title": "Institute Fee Structure for the AY 2022-23 - Post Graduate & Ph.D. programme",
        "url": "/static/docs/academics/fees structure/consolidated fee structure_PG.pdf",
    },
]

    fee = [
    {
        "title": "Institute Fee Structure for the AY 2023-24 - Under Graduate Programme",
        "url": "/static/docs/academics/fees structure/consolidated fee structure for academic year 2023-24 UG.pdf",
        "new": True
    },
    {
        "title": "2. Institute Fee Structure for the AY 2023-24 - Post Graduate & Ph.D. programme",
        "url": "/static/docs/academics/fees structure/consolidated fee structure for academic year 2023-24 PG & PhD.pdf",
        "new": True
    },
    {
        "title": "3. Institute Fee Structure for the AY 2022-23 - Under Graduate Programme",
        "url": "/static/docs/academics/fees structure/consolidated fee structure_UG.pdf",
    },
    {
        "title": "4. Institute Fee Structure for the AY 2022-23 - Post Graduate & Ph.D. programme",
        "url": "/static/docs/academics/fees structure/consolidated fee structure_PG.pdf",
    },
]

    return render(request, "academics/fee-structure.html", {"fee": fee, "Btech": Btech, "Bsc": Bsc, "PG": PG})
def nad(request):
    return render(request, "academics/nad.html")
def scholarship(request):
    return render(request, "academics/scholarship.html")