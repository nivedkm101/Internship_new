from django.shortcuts import render

# Create your views here.
def physicalEducation(request):
    from django.shortcuts import render
def physicalEducation(request):
    mainLink = {
        'title': 'Physical Education & Sports',
        'link': '/physicalEducation'
    }
    links = [
    {
        "title": "Events",
        "link": "Physicaleducation-events"
    },
    {
        "title": "Sports Day",
        "link": "sportsday"
    },
    {
        "title": "Conference",
        "link": "physicaledu-conference"
    },
    {
        "title": "International Yoga Day",
        "link": "physicaledu-yoga"
    },
    {
        "title": "Independence Day",
        "link": "physicaledu-independenceday"
    },
    {
        "title": "Republic Day",
        "link": "physicaledu-republicday"
    },
]

    return render(request, 'physicalEducation/physicalEducation.html', {'links': links
                                                        , 'mainLink': mainLink})
