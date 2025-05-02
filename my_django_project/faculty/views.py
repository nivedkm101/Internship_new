from django.shortcuts import render
from django.views.generic import ListView
from .models import Staff, Role, HOD
from django.db.models import Q



def admin_directory(request):
    # Get administrative heads (Director, Registrar, etc.)
    admin_heads = Staff.objects.filter(
        role__role__in=['Director', 'Registrar', 'Dean', 'HOD']
    ).distinct().order_by('id')
    
    # Create a list of admin data with their roles and contact info
    admin_data = []
    for staff in admin_heads:
        roles = staff.role_set.all()
        for role in roles:
            if role.role in ['Director', 'Registrar', 'Dean', 'HOD']:
                admin_data.append({
                    'name': f"Dr. {staff.name}" if staff.designation.lower().startswith(('professor', 'dr')) else staff.name,
                    'designation': role.role,
                    'mail': role.mail if role.mail else '',
                    'phone': role.phone if role.phone else '',
                })
    
    return render(request, 'faculty/admin_directory.html', {
        'admin_data': admin_data,
        'page_title': 'Administration Head Directory'
    })

class FacultyListView(ListView):
    model = Staff
    template_name = 'faculty/faculty_list.html'
    context_object_name = 'faculty_members'

    def get_queryset(self):
        queryset = Staff.objects.all()
        role = self.request.GET.get('role', '')
        department = self.request.GET.get('department', '')
        position = self.request.GET.get('position','')
        
        if role:
            queryset = queryset.filter(role__role__icontains=role)
        if department:
            queryset = queryset.filter(department__icontains=department)
        if position:
            queryset = queryset.filter(position__icontains=position)
            
        return queryset.distinct()

def hod_directory(request):
    # Get all staff who have a role containing 'HOD'
    hods = Staff.objects.filter(role__role__icontains='HOD').distinct()
    departments = hods.values_list('department', flat=True).distinct()
    designations = hods.values_list('designation', flat=True).distinct()

    selected_dept = request.GET.get('department')
    selected_des = request.GET.get('designation')

    if selected_dept:
        hods = hods.filter(department=selected_dept)
    if selected_des:
        hods = hods.filter(designation=selected_des)

    context = {
        'departments': departments,
        'designations': designations,
        'hods': hods,
        'selected_dept': selected_dept,
        'selected_des': selected_des,
    }
    return render(request, 'faculty/hod_directory.html', context)

def dean_directory(request):
    # Get all roles that contain 'Dean'
    dean_roles = Role.objects.filter(role__icontains='Dean')
    # Get unique role names for the filter dropdown
    role_names = dean_roles.values_list('role', flat=True).distinct()
    # Get unique designations for the filter dropdown
    designations = Staff.objects.filter(role__role__icontains='Dean').values_list('designation', flat=True).distinct()

    selected_role = request.GET.get('role', '')
    selected_des = request.GET.get('designation', '')

    # Filter deans based on selected role and designation
    filtered_roles = dean_roles
    if selected_role:
        filtered_roles = filtered_roles.filter(role=selected_role)
    if selected_des:
        filtered_roles = filtered_roles.filter(id__designation=selected_des)

    # Get the related staff for each filtered role
    deans = filtered_roles.select_related('id')

    context = {
        'deans': deans,
        'role_names': role_names,
        'designations': designations,
        'selected_role': selected_role,
        'selected_des': selected_des,
        'page_title': 'Dean Directory'
    }
    return render(request, 'faculty/dean_directory.html', context)

def faculty_directory(request):
    departments = Staff.objects.values_list('department', flat=True).distinct()
    designations = Staff.objects.values_list('designation', flat=True).distinct()

    selected_dept = request.GET.get('department', '')
    selected_des = request.GET.get('designation', '')

    faculty = Staff.objects.all()
    if selected_dept:
        faculty = faculty.filter(department=selected_dept)
    if selected_des:
        faculty = faculty.filter(designation=selected_des)

    context = {
        'departments': departments,
        'designations': designations,
        'faculty': faculty,
        'selected_dept': selected_dept,
        'selected_des': selected_des,
        'page_title': 'Faculty Directory'
    }
    return render(request, 'faculty/faculty_directory.html', context)

def foc_directory(request):
    # Filter staff whose designation or role contains 'Contract'
    foc_staff = Staff.objects.filter(
        designation__icontains='contract'
    ).distinct()

    departments = foc_staff.values_list('department', flat=True).distinct()
    designations = foc_staff.values_list('designation', flat=True).distinct()

    selected_dept = request.GET.get('department', '')
    selected_des = request.GET.get('designation', '')

    if selected_dept:
        foc_staff = foc_staff.filter(department=selected_dept)
    if selected_des:
        foc_staff = foc_staff.filter(designation=selected_des)

    context = {
        'departments': departments,
        'designations': designations,
        'foc_staff': foc_staff,
        'selected_dept': selected_dept,
        'selected_des': selected_des,
        'page_title': 'Faculty on Contract Directory'
    }
    return render(request, 'faculty/foc_directory.html', context)

def officer_directory(request):
    # Get all officers (designation contains 'officer')
    officers = Staff.objects.filter(position__icontains='OFFICER').distinct()
    positions = officers.values_list('designation', flat=True).distinct()


    context = {
        'positions': positions,
        'officers': officers,
        'page_title': 'Officer Directory'
    }
    return render(request, 'faculty/officer_directory.html', context)

def pd_directory(request):
    pd_staff = Staff.objects.filter(position="P&D")
    return render(request, "faculty/pd_directory.html", {
        "page_title": "P&D Directory",
        "pd_staff": pd_staff,
    })

def staff_directory(request):
    # Get all unique departments and designations for filter options
    departments = Staff.objects.values_list('department', flat=True).distinct()
    designations = Staff.objects.values_list('designation', flat=True).distinct()
    
    # Get filter parameters from request
    department = request.GET.get('department')
    designation = request.GET.get('designation')
    
    # Start with all staff
    staff_list = Staff.objects.all()
    
    # Apply filters if provided
    if department:
        staff_list = staff_list.filter(department=department)
    if designation:
        staff_list = staff_list.filter(designation=designation)
    
    context = {
        'staff_list': staff_list,
        'departments': departments,
        'designations': designations,
        'department': department,
        'designation': designation,
    }
    
    return render(request, 'faculty/staff_directory.html', context)

def faculty_welfare(request):
    # Get all roles containing 'welfare' (case-insensitive)
    welfare_roles = Role.objects.filter(role__icontains='welfare').select_related('id')
    # Get unique staff members from those roles
    staff_ids = welfare_roles.values_list('id', flat=True).distinct()
    staff_list = Staff.objects.filter(id__in=staff_ids)

    # Optionally, get the relevant role for each staff (for display)
    staff_roles = {role.id_id: role for role in welfare_roles}

    context = {
        'staff_list': staff_list,
        'staff_roles': staff_roles,  # Map staff.id to their welfare role
    }
    return render(request, 'faculty/faculty_welfare.html', context)