from django.shortcuts import render

def institute(request):
   return render(request, "institute/institute.html")
def campus(request):
   return render(request, "institute/campus.html")
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