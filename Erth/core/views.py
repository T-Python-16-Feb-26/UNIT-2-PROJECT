from django.shortcuts import render


def home(request):
    timeline = [
        {
            'year': '1902م',
            'title': 'مدرعات التوحيد',
            'text': 'انطلق الملك عبدالعزيز -طيب الله ثراه- لاستعادة الرياض بـ 63 رجلاً، وكانت "الهجن" وسيلتهم اللوجستية الوحيدة. طوت الفيافي بصمت مهيب، فكانت المدرعة التي لا ينضب وقودها، والشريك الذي حمل أركان الدولة قبل أن تُعبّد الطرق.'
        },
        {
            'year': '1950م - 1959م',
            'title': 'ميزان الاقتصاد وقوت الأجساد',
            'text': 'بينما كانت الدولة تبني مؤسساتها، ظلت الإبل هي الركيزة الاقتصادية والغذائية للمجتمع. من وبرها نُسجت بيوت الشعر التي احتضنت مجالس القبائل، ومن حليبها استمد الإنسان السعودي صموده في أقسى الظروف المناخية.'
        },
        {
            'year': '1974م',
            'title': 'انطلاقة ميادين الفخر',
            'text': 'في عهد الملك خالد -رحمه الله-، بدأت الإبل تأخذ مكانتها كرياضة تراثية منظمة. انطلق أول سباق هجن رسمي في مهرجان الجنادرية، ليتحول الجمل من وسيلة ترحال إلى أيقونة احتفال ومنافسة شريفة تجمع أبناء الوطن.'
        },
        {
            'year': '2017م',
            'title': 'نادي الإبل',
            'text': 'بصدور الأمر الملكي الكريم من خادم الحرمين الشريفين الملك سلمان بن عبدالعزيز بتأسيس "نادي الإبل"، دخل القطاع مرحلة التنظيم العالمي. أصبحت الصياهد عاصمةً عالميةً للإبل، وتحولت المهرجانات إلى محركات اقتصادية وثقافية كبرى.'
        },
        {
            'year': '2024م',
            'title': 'السيادة الثقافية الدولية',
            'text': 'احتفت المملكة بعام 2024 كـ "عام للإبل" لترسيخ مكانتها كركيزة للهوية الوطنية. وفي هذا العام برزت المكانة التنظيمية والثقافية للإبل بشكل أوضح، وتوسع حضورها بوصفها رمزاً سعودياً أصيلاً.'
        },
        {
            'year': '2026م',
            'title': 'رقمنة الأصالة',
            'text': 'اليوم، تحت ظل رؤية 2030، نعيش مرحلة جديدة تتجه فيها المملكة نحو "الإبل الذكية" عبر التوثيق الرقمي، وتحليل البيانات، واستخدام أدوات تقنية تحفظ السلالات وتخدم القطاع وتربط أصالته بالمستقبل.'
        },
    ]
    return render(request, 'home.html', {'timeline': timeline})


def breeds(request):
    return render(request, 'breeds.html')


def impact(request):
    return render(request, 'impact.html')


def festivals(request):
    return render(request, 'festivals.html')


def stories(request):
    return render(request, 'stories.html')


def science(request):
    return render(request, 'science.html')


def map_page(request):
    return render(request, 'map.html')


def future(request):
    return render(request, 'future.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def login_page(request):
    return render(request, 'login.html')