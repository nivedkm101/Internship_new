from django.shortcuts import render


def career(request):
    JRFECE2020 = [
    {
      'title': 'Advertisement - JRF Postion in the Dept. of Electronics and Communication Engineering ',
      'url': '/static/docs/opportunities/JRFECE2022/Advertisement for JRF in the Department of ECE (DST SEED Project).pdf',
      'new': 'true'
    },

    {
      'title': ' Application for the Post of Junior Research Fellow (JRF)',
      'url': '/static/docs/opportunities/JRFECE2022/Application Form for Recruitment of JRF Department of ECE (DST SEED Project).docx',
      'new': 'true'
    },
]
    return render(request, 'faculty/career.html',)