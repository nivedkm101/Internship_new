from django.shortcuts import render

def announcements(request):
    announcement25 = [
        {
            "title": "Fine Circular for Late Registration of Courses during the Even Semester of AY 2024-25",
            "url": "/static/pdf/announcement/2025/01/Fine Circular for the Late enrollment students.pdf",
            "new": True
        },
        {
            "title": "Circular - ADB-ROK Scholarship Program for Master's and Doctoral Studies in Korea",
            "url": "/static/pdf/announcement/2025/01/Circular - ADB-ROK Scholarship Program for Master's and Doctoral Studies in Korea.pdf",
            "new": True
        },
        {
            "title": "Advertisement for Recruitment of JRF under SMDP C2S Project is extended till 10-02-2025",
            "url": "/Opportunities",
            "new": True
        },
        {
            "title": "Advertisement for Residential Students Counselor (RSC) post in Girls Hostel at NITPY",
            "url": "/Opportunities",
            "new": True
        },
        {
            "title": "The Ph.D. Public Viva-Voce examination of Ms V. Jeyasakthi (Roll No. EN19D2002), Dept of HSS is scheduled on 19.02.2025, at 10.30 AM",
            "url": "/static/pdf/announcement/2025/01/Viva Circular_Jeyasakthi.pdf",
            "new": True
        },
        {
            "title": "Final Assessment Timetable for the ODD semester of the AY 2024-25 for the B.Sc. B.Ed. (I Year)",
            "url": "/academics/exam",
            "new": True
        },
        {
            "title": "Fee circular for the Even semester of the AY 2024-25 for the B.Tech. (I Year) 2024 admitted batch",
            "url": "/static/pdf/announcement/2025/01/Fee circular for the Even semester of the AY 2024-25 for the B.Tech. (I Year) 2024 admitted batch.pdf",
            "new": True
        },
        {
            "title": "Fee circular for the Even semester of the AY 2024-25 (except B.Tech. (I Year) 2024 admitted batch",
            "url": "/static/pdf/announcement/2024/12/Fee circular for the Even semester of the AY 2024-25 (except B.Tech. (I Year) 2024 admitted batch.pdf",
            "new": True
        },
        {
            "title": "Advertisement for Recruitment of Project Assistant Under ANRF-SERB Research Project",
            "url": "/Opportunities",
            "new": True
        },
        {
            "title": "Advertisement for Recruitment of Project Associate (PA) Under SERB Project",
            "url": "/Opportunities",
            "new": True
        },
        {
            "title": "Semester fee details for the B.Tech 2024 (I year) batch for the academic year 2024-25",
            "url": "/static/pdf/announcement/2025/01/Semester fee details for the B.Tech 2024 (I year) batch for the academic year 2024-25.pdf",
            "new": True
        },
        {
            "title": "Circular, Schedule, and Registration form for Make - Up Examinations First Year to be held in January - 2025",
            "url": "/academics/exam",
        },
        {
            "title": "Circular, Schedule, and Registration form for Make-Up Examinations to be held in January-2025",
            "url": "/academics/exam",
        },
        {
            "title": "Advertisement for Recruitment of JRF under SMDP C2S Project",
            "url": "/Opportunities",
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
    ]
    announcement24 = [
    {
        "title": "The PhD Public Viva-Voce Examination of Mr. Nettimi Satya Sai Srinivas (Roll No. EC16D2001), Department of Electronics and Communication Engineering is scheduled on 10/01/2025, 11.00 AM",
        "url": "/static/pdf/announcement/2024/12/Ph.D Public Viva-Voce Examination of Mr. N. S. S. Srinivas (EC16D2001)- Invitation.pdf",
    },
    {
        "title": "The PhD Public Viva-Voce Examination of Mr. Vishnu Sankar S (CH20D1003), Department of Chemistry is scheduled on 24.01.2025, 11:00 AM",
        "url": "/static/pdf/announcement/2024/12/Vishnu_ PhD Viva Notification.pdf",
    },
    {
        "title": "Hostel Fee Circular for students of B.Tech (1st, 2nd, 3rd & 4th Year), M.Tech (1st & 2nd Year), M.Sc. (1st & 2nd Year), Integrated (B.Sc. B.Ed) & Ph.D students of even semester (Academic Year 2024 - 25)",
        "url": "/static/pdf/announcement/2024/12/Hostel Fee Circular for students of B.Tech (1st, 2nd, 3rd & 4th Year), M.Tech (1st & 2nd Year), M.Sc. (1st & 2nd Year), Integrated (B.Sc. B.Ed) 2nd Year & Ph.D students of even semes.pdf",
    },
    {
        "title": "Details of Provisionally Selected Candidates of the Teaching Group A Posts",
        "url": "/Opportunities",
    },
    {
        "title": "Details of Provisionally Selected Candidates of the Non Teaching Group B & Group C Posts",
        "url": "/Opportunities",
    },
    {
        "title": "Advertisement for Recruitment of Project Associate (PA) Under SERB Project",
        "url": "/Opportunities",
    },
    {
        "title": "Provisionally selected candidates for the session of January 2025 Ph.D. admission",
        "url": "/students/admission/phd",
    },
    {
        "title": "Ph.D Viva-Voice Examination of Mr. Baranidharan B (MA20D1002), 17-12-2024 (Tuesday) at 10.00 AM",
        "url": "/static/pdf/announcement/2024/12/Viva voce circular_Baranidharan.pdf",
    },
    {
        "title": "List of provisionally shortlisted candidates for the Written Test for the post of Office Attendant scheduled to be held on 07.12.2024",
        "url": "/Opportunities",
    },
    {
        "title": "Final Assessment Timetable for the ODD semester of the AY 2024-25 for the B.Tech. (I year), M.Tech. (I Year), M.Sc. (I Year)",
        "url": "/academics/exam",
    },
    {
        "title": "List of provisionally shortlisted candidates for the Written Test for the post of Lab Attendant scheduled to be held on 05.12.2024",
        "url": "/Opportunities",
    },
    {
        "title": "List of provisionally shortlisted candidates for the Written Test for the post of Technical Assistant scheduled to be held on 03.12.2024",
        "url": "/Opportunities",
    },
    {
        "title": "Provisionally shortlisted candidates for written test for admission to PhD programme January 2025",
        "url": "/students/admission/phd",
    },
    {
        "title": "List of provisionally shortlisted candidates for the Written Test for the post of Senior Technician scheduled to be held on 28.11.2024",
        "url": "/Opportunities",
    },
    {
        "title": "List of provisionally shortlisted candidates for the Written Test for the post of Technician scheduled to be held on 26.11.2024",
        "url": "/Opportunities",
    },
    {
        "title": "Applications are invited for allotment of 22 Nos. of Type-III Staff Quarters (C1 - C22) and 48 Nos. of Type-IV Faculty/Officers Quarters (B1 - B48) at NITPY, Karaikal. The last date of receipt of applications is 10-12-2024",
        "url": "/static/docs/forms/Staff_Faculty/Quaters_Allotment_Application_Form.pdf",
    },
    {
        "title": "Provisionally Shortlisted Candidates Assistant Professor (AGP 6000 -On Contract)- Dept. of Civil for Interview on 21.11.2024",
        "url": "/Opportunities",
    },
    {
        "title": "Provisionally Shortlisted Candidates Assistant Professor (AGP 6000 -On Contract)- Dept. of Physics for Interview on 19.11.2024",
        "url": "/Opportunities",
    },
    {
        "title": "Provisionally Shortlisted Candidates Assistant Professor (AGP 6000 -On Contract)- Dept. of Chemistry for Interview on 19.11.2024",
        "url": "/Opportunities",
    },
    {
        "title": "Corrigendum for Annexure A - List of provisionally shortlisted candidates (Final List) for the post of Technical Assistant",
        "url": "/Opportunities",
    },
    {
        "title": "Provisionally Shortlisted Candidates Assistant Professor (AGP 6000 -On Contract)- Dept. of Mathematics for Interview on 18.11.2024",
        "url": "/Opportunities",
    },
    {
        "title": "Schedule for Conduct of Examinations / Selection process for the post of Technical Assistant",
        "url": "/Opportunities",
    },
    {
        "title": "List of provisionally shortlisted candidates (Final List) for the post of Technical Assistant",
        "url": "/Opportunities",
    },
    {
        "title": "Detailed Instructions to Candidates - Technical Assistant (Group B) - Pattern, Modalities of Examinations & Syllabus",
        "url": "/Opportunities",
    },
    {
        "title": "Provisionally Shortlisted Candidates Assistant Professor (AGP 6000 -On Contract)- Dept. of CSE for Interview on 14.11.2024",
        "url": "/Opportunities",
    },
    {
        "title": "Final Assessment Timetable for the ODD semester of the AY 2024-25 for the B.Tech. (II/III/IV year), M.Sc. (II Year) & B.Sc. B.Ed. (II Year)",
        "url": "/academics/exam",
    },
    {
        "title": "Provisionally Shortlisted Candidates Assistant Professor (AGP 6000 -On Contract)- Dept. of EEE for Interview on 13.11.2024",
        "url": "/Opportunities",
    },
    {
        "title": "Admission to the PH.D. Programme Academic Year 2024-2025 (JANUARY Session)",
        "url": "/students/admission/phd",
    },
    {
        "title": "Provisionally Shortlisted Candidates Assistant Professor (AGP 6000 -On Contract)- Dept. of ECE for Interview on 12.11.2024",
        "url": "/Opportunities",
    },
    {
        "title": "Schedule for Conduct of Examinations/Selection Process for the Non Teaching Recruitment - Group C posts",
        "url": "/Opportunities",
    },
    {
        "title": "List of Provisionally Eligible Candidates - Technical Assistant (Initial List)",
        "url": "/Opportunities",
    },
    {
        "title": "Details of Provisionally Selected Candidates of the Non Teaching Recruitment - Group A & Group C posts against the Advt. No. NITPY/01/2024/T-NT/01032024 Dated: 01.03.2024",
        "url": "/Opportunities",
    },
    {
        "title": "List of candidates shortlisted for the selection process for the post of Assistant Professor (AGP 6000 -On Contract)- Dept. of Chemistry",
        "url": "/Opportunities",
    },
    {
        "title": "Schedule for the selection process for the post of Assistant Professor (AGP 6000 -On Contract)- Dept. of Chemistry, Civil Engineering, Mathematics and Physics",
        "url": "/Opportunities",
    },
    {
        "title": "Details of Provisionally Selected Candidates of the Non Teaching Recruitment - Group B & Group C posts against the Advt. No. NITPY/01/2024/T-NT/01032024 Dated: 01.03.2024",
        "url": "/Opportunities",
    },
    {
        "title": "Circular - Vigilance Awareness week-2024: e-pledge",
        "url": "/static/pdf/announcement/2024/10/Circular - Vigilance Awareness week-2024 e-pledge.pdf",
    },
    {
        "title": "Advertisement for the Recruitment of JRF under DRDO-ARDB Research Project",
        "url": "/Opportunities",
    },
    {
        "title": 'List of candidates shortlisted for Written Test for the post of Junior Assistant scheduled to be held on 26.10.2024',
        "url": "/Opportunities",
    },
    {
        "title": 'List of candidates shortlisted for appearing Skill Test (Stage II) scheduled to be held on 25.10.2024 for the post of Junior Assistant',
        "url": "/Opportunities",
    },
    {
        "title": 'List of candidates shortlisted for the selection process for the post of Assistant Professor (AGP 6000 -On Contract)- Dept. of Civil Engineering, Mathematics and Physics.',
        "url": "/Opportunities",
    },
    {
        "title": 'List of candidates shortlisted for the Skill Test for the post of Junior Assistant scheduled to be held on 25.10.2024',
        "url": "/Opportunities",
    },
    {
        "title": 'Schedule for the Selection process for the post of Associate Professor and Professor for the department of ECE, CSE, EEE and Mathematics',
        "url": "/Opportunities",
    },
    {
        "title": 'List of candidates shortlisted for the Written Test for the post of Senior Assistant scheduled to be held on 23.10.2024',
        "url": "/Opportunities",
    },
    {
        "title": 'List of candidates shortlisted for the Skill Test for the post of Senior Assistant scheduled to be held on 22.10.2024.',
        "url": "/Opportunities",
    },
    {
        "title": 'Advertisement for Recruitment of Project Assistant Under ANRF-SERB Research Project',
        "url": "/Opportunities",
    },
    {
        "title": 'List of candidates shortlisted for the Written Test for the post of Personal Assistant scheduled to be held on 16.10.2024 (AN) @ 02:15 PM.',
        "url": '/Opportunities',
    },
    {
        "title": 'List of candidates shortlisted for the Written Test for the post of Pharmacist scheduled to be held on 16.10.2024 (AN) @ 01:30 PM.',
        "url": '/Opportunities',
    },
    {
        "title": 'List of Candidates shortlisted for appearing Certificate Verification & Written Test scheduled to be held on 16.10.2024 for the post of Superintendent',
        "url": '/Opportunities',
    },
    {
        "title": 'List of Candidates shortlisted for appearing Certificate Verification & Written Test scheduled to be held on 15.10.2024 (AN) for the post of Library & Information Assistant',
        "url": '/Opportunities',
    },
    {
        "title": 'List of Candidates shortlisted for appearing Skill Test scheduled to be held on 15.10.2024 for the post of Superintendent',
        "url": '/Opportunities',
    },
    {
        "title": "Observance of Vigilance Awareness Week 2024 - Poster Presentation Competition",
        "url": '/static/pdf/announcement/2024/10/Observance of Vigilance Awareness Week 2024 - Poster Presentation Competition.pdf',
    },
    {
        "title": 'ADVERTISEMENT FOR RECRUITMENT OF JRF ANRF - SERB - CRG RESEARCH PROJECT',
        "url": '/Opportunities',
    },
    {
        "title": 'Circular for downloading of Admit Card - Non Teaching Recruitment scheduled during October, 2024 for Group A, Group B & Group C Positions',
        "url": "/Opportunities",
    },
    {
        "title": 'Schedule for conduct of Examinations for the Non-Teaching Recruitment - Group A, Group B & Group C Positions',
        "url": "/Opportunities",
    },
    {
        "title": 'ADVERTISEMENT FOR RECRUITMENT OF JRF UNDER SMDP C2S PROJECT',
        "url": "/Opportunities",
    },
    {
        "title": 'List of provisionally selected candidates for admission to Visvesvaraya Ph.D Scheme for July 2024 session',
        "url": "/students/admission/phd",
    },
    {
        "title": 'List of candidates shortlisted for the Interview for the post of Assistant Registrar scheduled to be held on 26.09.2024',
        "url": "/Opportunities",
    },
    {
        "title": 'List of candidates shortlisted for the Written Test for the post of Assistant Registrar scheduled to be held on 25.09.2024',
        "url": "/Opportunities",
    },
    {
        "title": 'List of Graduands & Medal Winners - Updated',
        "url": '/academics/convocation',
    },
    {
        "title": 'Circular for downloading of Admit Card - Non Teaching Recruitment - Group A posts of Medical Officer/Deputy Registrar/Assistant Registrar',
        "url": "/Opportunities",
    },
    {
        "title": '11th Convocation - Accommodation',
        "url": '/academics/convocation',
    },
    {
        "title": "Ph.D Viva-Voice Examination of Mr. Eswaran M (ME21D1001), 20-09-2024 (Friday) at 3.00 PM",
        "url": '/static/pdf/announcement/2024/09/ME21D1001_PhD Viva.pdf',
    },
    {
        "title": 'Visvesvaraya PHD scheme Shortlisted Candidates PhD Written Test September 2024',
        "url": "/students/admission/phd",
    },
    {
        "title": 'Revised Circular - 11th Convocation of National Institute of Technology Puducherry',
        "url": '/academics/convocation',
    },
    {
        "title": 'Letter to Graduands (REVISED SCHEDULE)',
        "url": '/academics/convocation',
    },
    {
        "title": 'Note to the Graduands (REVISED SCHEDULE)',
        "url": '/academics/convocation',
    },
    {
        "title": "Ph.D Viva-Voice Examination of Mr. Gejendhiran S (ME21D1008), 19.09.2024 (Thursday) at 9.30 AM",
        "url": '/static/pdf/announcement/2024/09/viva circular - Gejendhiran S (ME21D1008).pdf',
    },
    {
        "title": "Ph.D Viva-Voice Examination of Mr.Mirothali Chand C. (Roll No. CS20D1004), 18-09-2024 (Wednesday) at 11:00 a.m",
        "url": '/static/pdf/announcement/2024/09/Ph.D Viva-Voice Examination of Mr.Mirothali Chand.pdf',
    },
    {
        "title": "List of provisionally selected students and Waiting List for Spot Round for admission to B.Sc. B.Ed. programme for the AY 2024-25",
        "url": '/students/admission/BSc_BEd',
    },
    {
        "title": 'List of Provisionally Eligible Candidates for various Group B and C Non-Teaching positions along with Pattern, Modalities & Syllabus against the Advt. No. NITPY/01/2024/T-NT/01032024 Dated: 01.03.2024',
        "url": "/Opportunities",
    },
    {
        "title": "Hostel Fee Circular for First Year Students (B.Sc.B.Ed) (Academic Year 2024 - 25)",
        "url": '/static/pdf/announcement/2024/09/Hostel Fee Circular for First Year Students (B.Sc.B.Ed) (Academic Year 2024 - 25).pdf',
    },
    {
        "title": "Vacant Seats for Spot Round for admission to B.Sc. B.Ed. programme for the AY 2024-25",
        "url": '/students/admission/BSc_BEd',
    },
    {
        "title": "Ph.D. Viva-Voce Examination of Mr. Sundaresan S (EC20D1003), 17.09.2024 (Tuesday), 11.00 AM ",
        "url": '/static/pdf/announcement/2024/09/PhD Viva Circular_Sundaresan S.pdf',
    },
    {
        "title": 'List of Provisionally Eligible Candidates (Initial list) for the post of Superintendent ',
        "url": "/Opportunities",
    },
    {
        "title": "Provisionally selected candidates list for the M.Tech Self-Support Program- July 2024 session",
        "url": '/students/admission/mtech',
    },
    {
        "title": 'Revised Schedule for Conduct of Examination for the Non Teaching Recruitment - Group A posts of Medical Officer/Deputy Registrar/ Assistant Registrar ',
        "url": "/Opportunities",
    },
    {
        "title": "Ph.D. Viva-Voce Examination of Mr. Inkulu Anil Kumar (ME20D1002), 19-09-2024 (Thursday) at 11.00 AM ",
        "url": '/static/pdf/announcement/2024/09/Mr. Inkulu Anil Kumar (ME20D1002) phd viva notice.pdf',
    },
    {
        "title": "Notice for the Physical Reporting of the B.Sc. B.Ed. students admitted in the Academic year of 2024-25",
        "url": '/students/admission/BSc_BEd',
    },
    {
        "title": 'Walk-in for FOC Physics Faculty - Education Department on 11.09.2024',
        "url": "/Opportunities",
    },
    {
        "title": 'Submission Deadline for Visvesvaraya Ph.D. Scheme Applications - Extended to 12.09.2024',
        "url": "/students/admission/phd",
    },
    {
        "title": "Ph.D. Viva-Voce Examination of Mr. Paquianadin V (EE19D1001), 13.09.2024 (Friday), 10.00 AM ",
        "url": '/static/pdf/announcement/2024/09/Viva_voce_Mr. V. Paquianadin.pdf',
    },
    {
        "title": "Ph.D. Viva-Voce Examination of Mr. R. Nagaraj (Roll No. EC20D1006), 03.09.2024 (Tuesday) at 11:00AM",
        "url": '/static/pdf/announcement/2024/09/Ph.D. public Viva-Voce Examination of Mr. R. Nagaraj (Roll No. EC20D1006) - Invitation.pdf',
    },
    {
        "title": 'List of provisionally selected students for Round I for admission to B.Sc. B.Ed. programme for the AY 2024-25',
        "url": '/students/admission/BSc_BEd',
    },
    {
        "title": 'Corrigendum on Round 2 - Ph.D. Admission 2024-2025 (July Session) under Visvesvaraya PHD Scheme',
        "url": "/students/admission/phd",
    },
    {
        "title": "Redo Examinations Results",
        "url": '/static/pdf/announcement/2024/08/Redo Examinations Results.pdf',
    },
    {
        "title": "Makeup Examinations Results – July 2024",
        "url": '/static/pdf/announcement/2024/08/Makeup Examinations Results – July 2024.pdf',
    },
    {
        "title": "Provisional list of candidates shortlisted for the written test for M.Tech Self-support program",
        "url": '/students/admission/mtech',
    },
    {
        "title": "Notice for B. Tech. 2024-28 Batch Students",
        "url": '/static/pdf/announcement/2024/08/Notice for B. Tech. 2024-28 Batch Students.pdf',
    },
    {
        "title": "Admission Brochure for the 4 Year Integrated Teacher’s Education Program (ITEP) - B.SC. B.ED. for the Academic Year 2024-2025",
        "url": '/students/admission/BSc_BEd',
    },
    {
        "title": 'Round 2 - Ph.D. Admission 2024-2025 (July Session) under Visvesvaraya PHD Scheme',
        "url": "/students/admission/phd",
    },
    {
        "title": 'Admission To M. Tech. (Self-Support) Programme 2024-2025 (July Session)',
        "url": "/students/admission/mtech",
    },
    {
        "title": "First Year UG/ PG orientation programme 2024",
        "url": '/static/pdf/announcement/2024/08/orientation program 2024.pdf',
    },
    {
        "title": "Transport Arrangement on 12.08.2024 during the Physical Reporting of I-B.Tech. students",
        "url": '/static/pdf/announcement/2024/08/Transport Arrangement on 12.08.2024 during the Physical Reporting of I-B.Tech. students.pdf',
    },
    {
        "title": 'ADVERTISEMENT FOR RECRUITMENT OF JRF UNDER SMDP C2S PROJECT ',
        "url": "/Opportunities",
    },
    {
        "title": 'Academic Calendar for the B. Tech (I Year/2024 admitted batch)',
        "url": '/academics/calendarf',
    },
    {
        "title": 'Academic Calendar for the ODD semester of the AY 2024-25',
        "url": '/academics/calendar',
    },
    {
        "title": "Instruction notice for online registration and profile update in samarth portal for M.Tech/M.Sc admitted through CCMT/CCMN-2024",
        "url": '/static/pdf/announcement/2024/08/Instruction notice for online registration and profile update in samarth portal for M.Tech-M.Sc admitted through CCMT-CCMN-2024.pdf',
    },
    {
        "title": 'Provisionally Shortlisted Candidates - Teaching posts against the Advt. No. NITPY/01/2024/T-NT/01032024 Dated: 01.03.2024',
        "url": "/Opportunities",
    },
    {
        "title": "Hostel Fee circular - Date Extension - ODD sem of the AY 2024-25",
        "url": '/static/pdf/announcement/2024/08/Fee extension circular - odd sem 2024-25.pdf',
    },
    {
        "title": 'ADVERTISEMENT FOR THE RECRUITMENT OF JRF UNDER ARMREB – DRDO RESEARCH PROJECT',
        "url": "/Opportunities",
    },
    {
        "title": 'ADVERTISEMENT FOR RECRUITMENT OF PROJECT ASSISTANT UNDER ANRF-SERB RESEARCH PROJECT',
        "url": "/Opportunities",
    },
    {
        "title": 'Walk-in for FOC Physics Faculty - Education Department',
        "url": "/Opportunities",
    },
    {
        "title": 'Advertisement for Recruitment of Project Associate Under ANRF Research Project',
        "url": "/Opportunities",
    },
    {
        "title": 'Notice for the Physical Reporting of the B.Tech. students admitted in the Academic year of 2024 through the SII-2024',
        "url": "/students/admission/btech",
    },
    {
        "title": 'Postponement of Schedule for Conduct of Examination for the Non Teaching Recruitment - Group A posts of Medical Officer/ Assistant Registrar/Student Activity & Sports (SAS) Officer/ Deputy Registrar against the Advt. No. NITPY/01/2024/T-NT/01032024 Dated: 01.03.2024',
        "url": "/Opportunities",
    },
    {
        "title": 'Notice for the Online Reporting and Physical Reporting of the B.Tech. students admitted in the Academic year of 2024 through the DASA-2024',
        "url": "/students/admission/btech",
    },
    {
        "title": 'List of Provisionally Eligible Candidates (Initial list) for the post of SAS Assistant/ Library and Information Assistant/Personal Assistant/Technician/Junior Assistant',
        "url": "/Opportunities",
    },
    {
        "title": 'Schedule for Conduct of Examination for the Non Teaching Recruitment - Group A posts of Medical Officer/ Assistant Registrar/Student Activity & Sports (SAS) Officer/ Deputy Registrar',
        "url": "/Opportunities",
    },
    {
        "title": "Hostel Fee circular - First Year - odd sem 2024-25",
        "url": '/static/pdf/announcement/2024/07/Hostel Fee circular - First Year - odd sem 2024-25.pdf',
    },
    {
        "title": 'List of Provisionally Eligible Candidates (Final List) against the Advt. No. NITPY/01/2024/T-NT/01032024 Dated: 01.03.2024 - GROUP ‘A’ (NON-TEACHING)',
        "url": "/Opportunities",
    },
    {
        "title": 'Notice for the Physical Reporting of the B.Tech. students admitted in the Academic year of 2024 through the CSAB/JoSAA',
        "url": "/students/admission/btech",
    },
    {
        "title": 'Fee Remission Notice for the Academic Year 2024-25 for the batch of B.Tech. 2024-28.pdf',
        "url": "/students/admission/btech",
    },
    {
        "title": 'Notice - M.Tech. & M.Sc. (admission through CCMT & CCMN 2024) provisionally selected candidates Physical Reporting',
        "url": '/static/pdf/mtech admission/CCMT_2024.pdf',
    },
    {
        "title": 'Provisionally selected candidates for the session of July 2024 Ph.D. admission',
        "url": "/students/admission/phd",
    },
    {
        "title": "Semester Fee circular for the ODD semester of the Academic year 2024-25",
        "url": '/static/pdf/announcement/2024/07/Semester Fee circular for the ODD semester of the Academic year 2024-25.pdf',
    },
    {
        "title": 'List of Provisionally Eligible Candidates against the Advt. No. NITPY/01/2024/T-NT/01032024 Dated: 01.03.2024 - GROUP ‘C’ (NON-TEACHING)',
        "url": "/Opportunities",
    },
    {
        "title": 'End Semester Results for the B.Tech. (II Sem), M.Tech. (II Sem), and M.Sc. (II Sem) examinations held on May 2024',
        "url": 'https://nitpy.samarth.edu.in/index.php/site/login',
    },
    {
        "title": 'Visiting Faculty Walk-in Interview - CSE Department',
        "url": "/Opportunities",
    },
    {
        "title": "Circular, Schedule, and Registration form for Make-Up Examinations to be held in July-2024.pdf",
        "url": '/academics/exam',
    },
    {
        "title": 'Walk-in-Interview for the Faculty on Contract and Visiting Faculty Purely Temporary Basis (CHEMISTY)',
        "url": "/Opportunities",
    },
    {
        "title": 'Walk-in Advertisement for Visiting Faculty in Economics',
        "url": "/Opportunities",
    },
    {
        "title": "Hostel Fee Circular - ODD Semester of the Academic Year 2024-25",
        "url": '/static/pdf/announcement/2024/06/Hostel Fee Circular - ODD Semester of the Academic Year 2024-25.pdf',
    },
    {
        "title": 'Walk-In Advertisement for Faculty on contract – for Integrated B.Sc.-B.Ed. program',
        "url": "/Opportunities",
    },
    {
        "title": 'End Semester Examination Results for the M.Tech. & M.Sc. (II year) held on May2024',
        "url": 'https://www.nitpy.ac.in/Apr2024/',
    },
    {
        "title": 'List of shortlisted candidates for written test for admission to PhD programme July 2024',
        "url": "/students/admission/phd",
    },
    {
        "title": "Ph.D. Viva-Voce Examination of Mr. Syed Shahul Hameed (Roll No. CS20D1003), 11.07.2024 (Thursday) at 04:00PM",
        "url": '/static/pdf/announcement/2024/06/Ph.D Viva Voce Examination of Mr. Syed Shahul Hameed.pdf',
    },
    {
        "title": "Redo Examination Results-April/May 2024",
        "url": '/static/pdf/announcement/2024/06/Redo Results_april_2024.pdf',
    },
    {
        "title": 'End Semester Examination Results for the B.Tech (II, III, & IV Year) held on April 2024',
        "url": 'https://www.nitpy.ac.in/Apr2024/',
    },
    {
        "title": "Final Assessment Timetable for the Even semester of the AY 2023-24 for the B.Sc. B.Ed.",
        "url": '/academics/exam',
    },
    {
        "title": 'List of Provisionally Eligible Candidates against the Advt. No. NITPY/01/2024/T-NT/01032024 Dated: 01.03.2024 - GROUP ‘A’ (NON-TEACHING)',
        "url": "/Opportunities",
    },
    {
        "title": 'ADVERTISEMENT FOR RECRUITMENT OF JRF UNDER SMDP C2S PROJECT - ADVERTISEMENT NO. NITPY/ADVT/R&C/20',
        "url": "/Opportunities",
    },
    {
        "title": 'ADMISSION TO Ph.D. PROGRAMMES 2024-2025 (JULY Session)',
        "url": "/students/admission/phd",
    },
    {
        "title": "Ph.D. Viva-Voce Examination of Mr. Raja. S (Roll No. EE16D1001), 11.06.2024 (Tuesday) at 03.30 PM",
        "url": '/static/pdf/announcement/2024/05/VIVA_NOTIFICATION Raja.pdf',
    },
    {
        "title": "Final Assessment Timetable for the Even semester of the AY 2023-24 for the B.Tech., M.Tech., M.Sc. (I year)",
        "url": '/academics/exam',
    },
    {
        "title": "Ph.D. Viva-Voce Examination of Ms. Asha Raveendran (Roll No. CH21D1001), 31.05.2024 (Friday) at 03.00 PM",
        "url": '/static/pdf/announcement/2024/05/VIVA_NOTIFICATION Asha.pdf',
    },
    {
        "title": "Ph.D. Viva-Voce Examination of Mr. Senthamizh Selvan S (Roll No. EE18D1004), 31.05.2024 (Friday) at 10.15 AM",
        "url": '/static/pdf/announcement/2024/05/VIVA_NOTIFICATION Senthamizh Selvan.pdf',
    },
    {
        "title": "Ph.D. Viva-Voce Examination of Mr. Prem Kumar R. (Roll No. MA18D2001), 16-05-2024 (Thursday) at 3.30 PM",
        "url": '/static/pdf/announcement/2024/05/Viva voce circular_Premkumar.pdf',
    },
    {
        "title": "Ph.D. Viva-Voce Examination of Mr. Saravanakumar. R (Roll No. EE18D1003), 20.05.2024 (Monday), 11.00 AM",
        "url": '/static/pdf/announcement/2024/05/viva-voce circular_saravanakumar.pdf',
    }, {
        "title": "Ph.D. Viva-Voce Examination of Ms. Dhakshayani J (Roll No. CS20D1001), on 20.05.2024 (Monday), 09.30 AM",
        "url": '/static/pdf/announcement/2024/05/Circular PhD Final Viva Voce CS20D1001 signed.pdf',
    },
    {
        "title": "Advertisement for National Overseas Scholarship Scheme for the 2024-25",
        "url": '/static/pdf/announcement/2024/04/Advertisement for National Overseas Scholarship Scheme for the 2024-25.pdf',
    },
    {
        "title": "Admission to B.Sc. B.Ed. 2024 - Last Date for application is extended Up to 15 May 2024 (11:30 P.M.)",
        "url": '/students/admission/BSc_BEd',
    },
    {
        "title": "Final Assessment Timetable for the Even semester of the AY 2023-24 for the B.Tech. (II/III/IV year)",
        "url": '/static/pdf/Examination Schedule/EVEN Sem time table_Apr_2024 - Final.pdf',
    },
    {
        "title": "Redo Examination Results-November/December 2023",
        "url": '/static/pdf/announcement/2024/04/REDO_Results_Nov_Dec_2023 web upload.pdf',
    },
    {
        "title": "Fee Remission Notice for the Academic Year 2024-25",
        "url": '/static/pdf/announcement/2024/03/Fee Remission Notice for the Academic Year 2024-25.pdf',
    },
    {
        "title": "Semester Fee Circular for the Even Semester of the AY 2023-24 for the B.Sc. B.Ed. programme",
        "url": '/static/pdf/announcement/2024/03/Semester Fee Circular for the Even Semester of the AY 2023-24 for the B.Sc. B.Ed. programme.pdf',
    },
    {
        "title": "Ph.D. Viva-Voce Examination of Mr. Rasheed Abdul Haq K. P. (EC18D1003), on 18.03.2024 (Monday) at 02.30 PM",
        "url": '/static/pdf/announcement/2024/03/Mr. Rasheed Abdul Haq Viva.pdf',
    },
    {
        "title": "ADVERTISEMENT TEACHING & NON-TEACHING RECRUITMENT Advt. No. NITPY/01/2024/T-NT/01032024 Dated: 01.03.2024",
        "url": '/Opportunities',
    },
    {
        "title": "Make-up, Withdrawn & Winter Redo examinations results of January/February - 2024",
        "url": '/static/pdf/announcement/2024/02/Makeup_Results_FEB_2024_webupload.pdf',
    },
    {
        "title": "Ph.D. Viva-Voce Examination of Mr. Maneckshaw B. (MA19D2001), on 25-03-2024 (Monday) at 10.00 AM",
        "url": '/static/pdf/announcement/2024/02/Viva voce circular_Maneckshaw.pdf',
    },
    {
        "title": "Ph.D. Viva-Voce Examination of Mr. Vipin V. (EC20D1007) on 26.03.2024 (Tuesday) at 03.00 PM",
        "url": '/static/pdf/announcement/2024/02/Viva-Voce_Mr.Vipin-EC20D1007-26.03.2024.pdf',
    },
    {
        "title": "Ph.D. Viva-Voce Examination of Mr.P.Sudhan (PE19D2001) on 07.03.2024 (Thursday) at 10.30 A.M",
        "url": '/static/pdf/announcement/2024/02/Sudan Viva Invitation.pdf',
    },
    {
        "title": "Ph.D. Viva-Voce Examination of Mr. Logeswaran J (Roll No. EC20D1005) - on 06.03.2024 (Wednesday), at 11.00 A.M",
        "url": '/static/pdf/announcement/2024/02/Logeswaran_Viva.pdf',
    },
    {
        "title": "Fee Remission List with Amount Remitted details for B.Tech. 2023",
        "url": '/static/pdf/announcement/2024/01/Fees Remission list B.TECH. 2023.pdf',
    },
    {
        "title": 'Semester Fee Circular for the Even Semester of the AY 2023-24 for the 1st Year of 2023 admitted batch (B.Tech., M.Tech., M.Sc.)',
        "url": '/static/pdf/announcement/2024/02/Semester Fee Circular for the Even Semester of the AY 2023-24 for the 1st Year of 2023 admitted batch (B.Tech., M.Tech., M.Sc.).pdf',
    },
    {
        "title": 'Final Assessment Time Table for the ODD Semester of the Academic Year 2023-24 (B.Sc. B.Ed. (I year))',
        "url": '/academics/exam',
    },
    {
        "title": "Institute Fee Structure for the AY 2023-24 - B.Sc. B.Ed. programme",
        "url": '/academics/fee-structure',
    },
    {
        "title": "Advertisement for Walk-in-Interview for the Visiting Faculty -PHYSICS– purely temporary basis",
        "url": '/Opportunities',
    },
    {
        "title": 'Circular, Schedule, and Registration form for Make-Up Examinations to be held in February-2024',
        "url": '/academics/exam',
    },
    {
        "title": 'End Semester Examination Results for the Ph.D. held on November and December 2023',
        "url": 'https://www.nitpy.ac.in/PhD/',
    },
    {
        "title": "Academic Calendar for the EVEN semester of the AY 2023-24",
        "url": '/academics/calendar',
    },
    {
        "title": 'End Semester Examination Results for the B.Tech/M.Tech/M.Sc held on November and December 2023',
        "url": 'https://nitpy.ac.in/December2023/',
    },
    {
        "title": "Advertisement for The Walk-in-Interview for the Faculty (on Contract) – purely temporary basis (Humanities & Social Sciences)",
        "url": '/Opportunities',
    },
    {
        "title": "Hostel Fee Circular for the Even Semester of the AY 2023-24",
        "url": '/static/pdf/announcement/2024/01/Circular - Hostel Fee- Even semester of the AY 23-24.pdf',
    },
    {
        "title": "Ph.D. JAN 2023-24 admission provisionally selected list",
        "url": '/students/admission/phd',
    },]
    return render(request, "announcements/announcements.html",
                  {"announcement24": announcement24, "announcement25": announcement25})

def tenders(request):
    tender25 = [{
            "title": "Notice Inviting Quotation - Purchase of Soil mechanics lab accessories and equipment",
            "url": "/static/pdf/tenders/2025/NIQ Purchase of Soil mechanics lab accessories and equipment.pdf",
            "new": True
        },
        {
            "title": "Notice Inviting Quotation - Purchase of Extensometer for structural engineering laboratory",
            "url": "/static/pdf/tenders/2025/NIQ- Purchase of Extensometer for structural engineering laboratory.pdf",
            "new": True
        },
        {
            "title": "Notice Inviting Quotation - Workstation Computer with Advanced GPU Architecture - Last Date to receive sealed quotations is On or Before 11.02.2025 (Tuesday), 05:00 p.m.",
            "url": "/static/pdf/tenders/2025/NITPY_NIQ_Workstation_Sc.pdf",
            "new": True
        },
        {
            "title": "Notice Inviting Quotation - Hot Stirrer Setup - Last Date to receive sealed quotations is On or Before 03.02.2025 (Monday), 05:00 p.m.",
            "url": "/static/pdf/tenders/2025/NITPY_NIQ_Hot-Stirrer_Sc-1.pdf",
            "new": True
        },
        {
            "title": "Notice Inviting Quotation - Homogenizer Setup - Last Date to receive sealed quotations is On or Before 03.02.2025 (Monday), 05:00 p.m.",
            "url": "/static/pdf/tenders/2025/NITPY_NIQ_Homogenizer_Sc-1.pdf",
            "new": True
        },
        {
            "title": "Notice Inviting Quotation - Probe Ultrasonicator Setup - Last Date to receive sealed quotations is On or Before 03.02.2025 (Monday), 05:00 p.m.",
            "url": "/static/pdf/tenders/2025/NITPY_NIQ_Probe-Ultrasonicator_Sc-1.pdf",
            "new": True
        },
        {
            "title": "NIQ - Architectural design, preparation of 2D & 3D drawings and BOQ with specifications for faculty rooms type I, II and III, HoD room, Department Meeting room and Research scholar hall in the Composite Block of NITPY Campus Karaikal",
            "url": "/static/pdf/tenders/2025/Architectural design, preparation of 2D & 3D drawings.pdf",
            "new": True
        },
        {
            "title": "Notice Inviting Quotation - Kitchen Exhaust System",
            "url": "/static/pdf/tenders/2025/Notice Inviting Quotation - Kitchen Exhaust System.pdf",
            "new": False
        }
    ]
    tender24 = [
        {
            "title": "Notice Inviting Quotation - For NCC uniform and ornaments.",
            "url": "/static/pdf/tenders/2024/NIQ-NCC Uniform and Ornaments.pdf",
            "new": False
        },
        {
            "title": "Notice Inviting Quotation - For the purchase of equipment for a project sanctioned by DST under the scheme NCSCT",
            "url": "/static/pdf/tenders/2024/NIQ-DST NCSTC_extension.pdf",
            "new": False
        },
        {
            "title": "Notice Inviting Quotation - sports equipment - Physical Education and Sports section",
            "url": "/static/pdf/tenders/2024/9 NIQ for sports equipment.pdf",
            "new": False
        },
        {
            "title": "Notice Inviting Quotation - Equipment for a project sanctioned by DST under the scheme NCSCT",
            "url": "/static/pdf/tenders/2024/NIQ-DST NCSTC.pdf",
            "new": False
        },
        {
            "title": "TENDER - weight lifting equipment - Physical Education and Sports section",
            "url": "/static/pdf/tenders/2024/NIQ Tender.pdf",
            "new": False
        },
        {
            "title": "TENDER - CANTEEN, PANTRY AND LAUNDRY SERVICES FOR NITPY GUEST HOUSE",
            "url": "/static/pdf/tenders/2024/CANTEEN, PANTRY AND LAUNDRY SERVICES FOR NITPY GUEST HOUSE.pdf",
            "new": False
        },
        {
            "title": "Tender - Construction of Permanent Open Stage Platform for Le-Ciel and other institute related functions",
            "url": "https://eprocure.gov.in/eprocure/app",
            "new": False
        },
        {
            "title": "NIQ for sanitary items for the institute",
            "url": "/static/pdf/tenders/2024/NIQ-Institute.pdf",
            "new": False
        },
        {
            "title": "NIQ for sanitary items for the hostels",
            "url": "/static/pdf/tenders/2024/NIQ-Hostels.pdf",
            "new": False
        }
    ]
    tender23 = [
    {
        "title": "Tender for Mixer Machine , Concrete Cube Mould , Concrete Cylinder Mould , Weighing Machine , Hot Air Oven",
        "url": "/static/pdf/tenders/2023/GeM-Bidding-5637631.pdf",
    },
    {
        "title": "Tender for Workstation (Q2)",
        "url": "/static/pdf/tenders/2023/GeM-Bidding-5645800.pdf",
    },
    {
        "title": "Tender for GNSS system with accessories",
        "url": "/static/pdf/tenders/2023/GNSS system with accessories.pdf",
    },
    {
        "title": "Tender for Accelerated Weathering Test Chamber",
        "url": "/static/pdf/tenders/2023/Accelerated Weathering Test Chamber.pdf",
    },
    {
        "title": "Tender for 3D experience simulia software",
        "url": "/static/pdf/tenders/2023/3D experience simulia software.pdf",
    },
    {
        "title": "NITPY/MECH/NR/SERB-EEQ/PURCHASE/023 dated 18.08.2023",
        "url": "/static/pdf/tenders/2023/Tender-1.pdf",
    },
    {
        "title": "NITPY/MECH/NR/SERB-EEQ/PURCHASE/024 dated 18.08.2023",
        "url": "/static/pdf/tenders/2023/Tender-2.pdf",
    },
    {
        "title": "Tender for Multifunction Machines MFM (Q2) ( PAC Only )",
        "url": "/static/pdf/tenders/2023/Multifunction Machines MFM (Q2) ( PAC Only ).pdf",
    },
    {
        "title": "Tender for Workstation (Q2) ( PAC Only )",
        "url": "/static/pdf/tenders/2023/Workstation (Q2) ( PAC Only ).pdf",
    },
    {
        "title": "Tender for Operation of students mess for preparation and serving of breakfast, lunch, evening snacks and dinner at mess building situated in NIT Puducherry campus (e-Tender Event Number : NITPY/Mess Catering/2023-24/22, Dt.:21.07.2023)",
        "url": "/static/pdf/tenders/2023/MESS-CATERING-SERVICE.pdf",
    },
    {
        "title": "The tender for Rental Car Service ( NITPY/Transport Committee/2023/21 dated 18.07.2023 )",
        "url": "/static/pdf/tenders/2023/Rental Car Tender.pdf",
    },
    {
        "title": "Expression of Interest (EoI) for running of Juice Tea Coffee Corner Shop at NITPY",
        "url": "/static/pdf/tenders/2023/Expression of Interest (EoI) for running of Juice Tea Coffee Corner Shop at NITPY.pdf",
    },
    {
        "title": "Supply of All Geared Lathe Machine Laboratory Equipment for Department of Mechanical Engineering (Last date for submission of Bid: 22.06.2023)",
        "url": "/static/pdf/tenders/2023/Supply of All Geared Lathe Machine Laboratory Equipment for Department of Mechanical Engineering.pdf",
    },
]
    tender22 = [
    {
        "title": "Outsourcing of Manpower tender(eProcurement Portal Tender ID:2022_NITPY_727800_1)",
        "url": "/static/pdf/tenders/2022/12/Manpower Tender Document - updated on 07.12.2022.pdf",
    },
    {
        "title": "Global Tender for the Procurement of 250kN Dynamic Universal Testing Machine(eProcurement Portal Tender ID:2022_NITPY_721167_1)",
        "url": "/static/pdf/tenders/2022/11/Tendernotice_1.pdf",
    },
    {
        "title": "Tender notification for DST SEED STI HUB Project, Deptartment of ECE.",
        "url": "/static/pdf/tenders/2022/10/Tender-DST-SEED-STI-HUB-Project.pdf",
    },
    {
        "title": "Empanelment of Vendors for Supply of Books (Print and others documents ) - Central Library",
        "url": "/static/docs/library/EOI 2022-23 Book Purchase.pdf",
    },
]

    tender21 = [
    {
        "title": "E-Tender for Registration of contractors for NIT Puducherry - Last date for submission 07.12.2021 on 3.00 PM",
        "url": "https://eprocure.gov.in/eprocure/app",
    },
    {
        "title": "E-Tender for Procurement of Linear double inverted pendulum, Magnetic levitation system, Ball and beam system, and Active suspension system for Control and Instrumentation Laboratory --> Last date of Submission is 18-May-2021 03:00 PM",
        "url": "https://eprocure.gov.in/eprocure/app",
    },
    {
        "title": "E-Tender for Procurement of Oil breakdown voltage test kit and Oil resistivity and tan delta set for Control and Instrumentation Laboratory --> Last date of Submission is 18-May-2021 03:00 PM",
        "url": "https://eprocure.gov.in/eprocure/app",
    },
    {
        "title": "E-Tender for Procurement of Electrical Materials for Institute Electrical Maintenance --> Last date of Submission is 20-04-2021",
        "url": "https://eprocure.gov.in/eprocure/app",
    },
    {
        "title": "E-Tender for Procurement of High temperature conductivity measurement setup for Material Synthesis and Characterization Laboratory --> Last date of Submission is 15-04-2021",
        "url": "https://eprocure.gov.in/eprocure/app",
    },
    {
        "title": "E-Tender for Procurement of Mini Sputter Coater for Material Synthesis and Characterization Laboratory to Department of Physics --> Last date of Submission is 15-04-2021",
        "url": "https://eprocure.gov.in/eprocure/app",
    },
    {
        "title": "E-Tender for Purchase of wiring materials for UPS connections to various computer labs --> Last date of Submission is 30-03-2021",
        "url": "",
    },
    {
        "title": "E-Tender for Supply of Micro-Hardness Tester Laboratory Equipment for Mechanical Engineering Department--Last date of Submission is 18-01-2021",
        "url": "https://eprocure.gov.in/eprocure/app",
    },
    {
        "title": "E-Tender for Supply of Laboratory Equipments for Mechanical Engineering Department --Last date of Submission is 19-01-2021",
        "url": "https://eprocure.gov.in/eprocure/app",
    },
    {
        "title": "E-Tender for Supply of Optical Microscope Laboratory Equipment for Mechanical Engineering Department--Last date of Submission is 12-01-2021",
        "url": "https://eprocure.gov.in/eprocure/app",
    },
    {
        "title": "E-Tender for Supply of Pin-on-Disc Tribometer Laboratory Equipment for Mechanical Engineering Department-- Last date of Submission is 12-01-2021",
        "url": "https://eprocure.gov.in/eprocure/app",
    },
    ]
    tender20 = [
    {
        "title": "E - Tender for Supply and Installation of 26 Nos of cassette type Air Conditioners (AC) work in Administrative block at NIT Puducherry (corrigendum added) - Last date of Submission is 15-Dec-2020 @ 3 PM",
        "url": "/static/eprocure.gov.in/eprocure/app"
    },
    {
        "title": "E - Tender for Spin Coating Unit with UV Curing and Auto-dispensing System for Materials Synthesis and Characterization Laboratory (Physics) at NIT Puducherry - Last date of Submission is 07-Dec-2020 @ 3 PM",
        "url": "/static/eprocure.gov.in/eprocure/app"
    },
    {
        "title": "E - Tender for Procurement of Tube Furnace for Physics Laboratory at NIT Puducherry - Last date of Submission is 02-Dec-2020 @ 3 PM",
        "url": "/static/eprocure.gov.in/eprocure/app"
    },
    {
        "title": "E - Tender for Procurement of Hydraulic Press and Die for Materials Synthesis and Characterization Laboratory (Physics) at NIT Puducherry - Last date of Submission is 02-Dec-2020 @ 3 PM",
        "url": "/static/eprocure.gov.in/eprocure/app"
    },
    {
        "title": "E - Tender for Supply & Installation of English Language Laboratory on Turn Key Basis at NIT Puducherry - Last date of Submission is 01-Dec-2020 @ 3 PM",
        "url": "/static/eprocure.gov.in/eprocure/app"
    },
    {
        "title": "E - Tender for Procurement of TG DTA for Chemistry Laboratory at NIT Puducherry - Last date of Submission is 17-Nov-2020 @ 3 PM",
        "url": "/static/eprocure.gov.in/eprocure/app"
    },
    {
        "title": "E - Tender for Procurement of FT Raman Spectrometer for Chemistry Laboratory at NIT Puducherry - Last date of Submission is 17-Nov-2020 @ 3 PM",
        "url": "/static/eprocure.gov.in/eprocure/app"
    },
    {
        "title": "E- tender for Supply and Installation of high available server with storage and accessories for Web and Mail Server @ NIT Puducherry - Last date of Submission is 12-Nov-2020 @ 3 PM",
        "url": "/static/eprocure.gov.in/eprocure/app"
    },
    {
        "title": "E- tender for Supply and Installation of Power Cables and Lighting at Poovam side gate @ NIT Puducherry - Last date of Submission is 05-Nov-2020 @ 3 PM",
        "url": "/static/eprocure.gov.in/eprocure/app"
    },
    {
        "title": "E- tender for Supply and Installation of high available server & storage and accessories for CSE Department Labs @ NIT Puducherry - Last date of Submission is 02-Nov-2020 @ 3 PM",
        "url": "/static/eprocure.gov.in/eprocure/app"
    },
    {
        "title": "E - Tender for On-site Making and Supplying of 3-seater portable work station (84 Nos.) and 2-seater portable work station (17 Nos.) for use at NIT Puducherry - Last date of Submission is 02-Nov-2020 @ 3 PM",
        "url": "/static/eprocure.gov.in/eprocure/app"
    },
    {
        "title": "E - Tender for EMPANELMENT OF CONTRACTORS at NIT Puducherry - Last date of Submission is 28-Oct-2020 @ 3 PM",
        "url": "/static/eprocure.gov.in/eprocure/app"
    },
    {
        "title": "E-Tender for Outsourcing of Security Services at NIT Puducherry - Last date of Submission is 14-Sep-2020 @ 3 PM",
        "url": "/static/eprocure.gov.in/eprocure/app"
    },
    {
        "title": "E-Tender for Provision Of Intercom Cable Laying and Shifting Of Epabx System - Last date of Submission is 14-02-2020",
        "url": "/static/eprocure.gov.in/eprocure/app"
    },
    {
        "title": "E-Tender for Making and Supplying of 160 Nos single cot in Moyar Hostel (2nd Cluster) at NITPY Karaikal - Last date of Submission is 05-03-2020",
        "url": "/static/eprocure.gov.in/eprocure/app"
    },
    {
        "title": "E - Tender for Supplying and fixing of anodized aluminium frame section along with aluminium grill for Balcony opening area to be covered in the Guest House Building at NITPY Karaikal - Last date of Submission is 02-03-2020",
        "url": "/static/eprocure.gov.in/eprocure/app"
    },
    {
        "title": "E-Tender for Provision of electrical power Supply and Lighting to Badminton Court - Last date of Submission is 28-02-2020",
        "url": "/static/eprocure.gov.in/eprocure/app"
    },
    {
        "title": "E-Tender for Provision of OFC Cable Laying Work From Science Block to Admin Block - Last date of Submission is 14-02-2020",
        "url": "/static/eprocure.gov.in/eprocure/app"
    },
    {
        "title": "E-Tender for Provision of electrical power points in different laboratory in Admin Block - Last date of Submission is 28-01-2020",
        "url": "/static/eprocure.gov.in/eprocure/app"
    },
    {
        "title": "E-Tender for the supply of Dustbin - Last date of Submission is 10-01-2020",
        "url": "/static/eprocure.gov.in/eprocure/app"
    }
]
    tender19 = [
    {
        "title": "Tender fee/EMD/Security Deposit for any tender (if applicable) should be paid through SB Collect under the option'Tender",
        "url": "/static/pdf/tenders/2019/CPPP.pdf"
    },
    {
        "title": "E-Tender for Supply of Wall Calendar and Table top Calendar Last date of Submission is 27-11-2019",
        "url": "https://eprocure.gov.in/eprocure/app"
    },
    {
        "title": "E-Tender for Supply and Installation of Multimedia Projector at NITPuducherry--> Last date of Submission is 18-11-2019",
        "url": "https://eprocure.gov.in/cppp/"
    },
    {
        "title": "E-Tender for Proposed to construction of steel shed structure for Covering of Main sub-station at NITPY Campus--> Last date of Submission is 01-11-2019",
        "url": "https://eprocure.gov.in/cppp/"
    },
    {
        "title": "E-Tender for proposed to construction of paver block area by two wheeler parking at Main Enterance of NITPY Campus-> Last date of Submission is 24-10-2019",
        "url": "https://eprocure.gov.in/cppp/"
    },
    {
        "title": "Notice Inviting Tender for providing Catering Services at NIT Puducherry -> Last date of Submission is 21-10-2019",
        "url": "/static/pdf/tenders/2019/Catering tender final copy 25.09.2019.pdf"
    },
    {
        "title": "Notice Inviting Tender for providing Technical and Non-Technical Manpower at NIT Puducherry -> Last date of Submission is 26-09-2019",
        "url": "/static/pdf/tenders/2019/Tender for Manpower - Opening Date 0n 26 -09-19 modified.pdf"
    },
    {
        "title": "Procurement of Microsoft Office 2019 Professional plus academic license-> Last date of submission is 16-09-2019",
        "url": "https://eprocure.gov.in/eprocure/app"
    },
    {
        "title": "Notice Inviting Tender For Outsourcing of House-Keeping Services--> Last date of submission is 10-09-2019",
        "url": "https://eprocure.gov.in/eprocure/app"
    },
    {
        "title": "The Outsourcing of Manpower (Technical and Non-Technical) Tender notification (NITPY/ADMIN/MANPOWER/2019-20, dated 06-06-19), stands cancelled due to administrative reason",
        "url": "https://eprocure.gov.in/eprocure/app"
    },
    {
        "title": "e-Tender for Supply of Aquaculture Water Quality Monitoring System -> Last date of submission is 12-08-2019",
        "url": "https://eprocure.gov.in/eprocure/app"
    },
    {
        "title": "Notice Inviting Tender for Outsourcing of security services -> Last date of Submission is 29-07-2019",
        "url": "/static/pdf/tenders/2019/Security_Tender_2019.pdf"
    },
    {
        "title": "Notice Inviting Tender for Cab Transport services -> Last date of Submission is 24-07-2019",
        "url": "/static/pdf/tenders/2019/finalized_Transport_tender_for_cab_02_07_2019.pdf"
    },
    {
        "title": "Notice Inviting Tender for Van Transport services -> Last date of Submission is 24-07-2019",
        "url": "/static/pdf/tenders/2019/Finalized_Van_transport_tender_02_07_2019.pdf"
    },
    {
        "title": "e-Tender for Making On-site assembly and supplying of reading table for Hostels at NITPY -> Last date of submission is 22-07-2019",
        "url": "https://eprocure.gov.in/eprocure/app"
    },
    {
        "title": "e-Tender for Making onsite assembly and Supplying of Single Steel cot in Boys and Girls Hostel at NITPY -> Last date of submission is 18-07-2019",
        "url": "https://eprocure.gov.in/eprocure/app"
    },
    {
        "title": "Corrigendum To Tender for the construction of Multipurpose Semi-Permanent Shed in front of Boys Hostel Building at NITPY Karaikal -> Last date of Submission is 05-07-2019",
        "url": "/static/pdf/tenders/2019/Corrigendum_Multipurpose_Shed.pdf"
    },
    {
        "title": "Corrigendum for Providing Technical and Non-Technical Manpower Services at NIT Puducherry -> Last date of Submission is 05-07-2019",
        "url": "/static/pdf/tenders/2019/Corrigendum_Manpower.pdf"
    },
    {
        "title": "Notice Inviting Tender for Providing Canteen services at NIT Puducherry -> Last date of Submission is 05-07-2019",
        "url": "/static/pdf/tenders/2019/Canteen_Tender_2019.pdf"
    },
    {
        "title": "e-Tender for Supply & Installation of 500Lph and 250 Lph Reverse Osmosis Plant fully Automatic in NIT Puducherry -> Last date of Submission is 19-06-2019",
        "url": "https://eprocure.gov.in/eprocure/app"
    },
    {
        "title": "Notice Inviting Tender for providing Catering Services at NIT Puducherry -> Last date of Submission is 14-06-2019",
        "url": "/static/pdf/tenders/2019/Catering_Tender.pdf"
    },
    {
        "title": "Tender for Construction of Multipurpose Semi-Permanent Shed in front of Boys Hostel Building at NITPY Karaikal -> Last date of Submission is 17-05-2019",
        "url": "/static/pdf/tenders/2019/Multipurpose_Shed.pdf"
    },
    {
        "title": "Tender for the Supply of Electrospinning Apparatus -> Last date of Submission is 15-04-2019",
        "url": "/static/pdf/tenders/2019/Tender_Chemistry_Electrospinning.pdf"
    },
    {
        "title": "Revised Tender for Cycle Parking Shed in the rear side of Science block-> Last date of Submission is 04-01-2019",
        "url": "/static/pdf/tenders/2019/Revised_Tender_for_cycle_parking_shed.pdf"
    }
]


    return render(request, "announcements/tenders.html",
                  {"tender25": tender25,"tender24": tender24, 
                   "tender23": tender23,"tender22": tender22,
                    "tender21": tender21 , "tender20": tender20,
                      "tender19": tender19})