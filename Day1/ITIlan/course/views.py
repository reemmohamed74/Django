from django.shortcuts import render, redirect

# قائمة من الأسماء فقط (دون استخدام معرفات)
courses = ['Ahmed', 'Mohamed', 'Ali']

def course_list(request):
    return render(request, 'course_list.html', {'courses': courses})

def add_course(request):
    if request.method == 'POST':
        course_name = request.POST.get('name')
        courses.append(course_name)  # إضافة الكورس إلى القائمة
        return redirect('course_list')  # إعادة التوجيه إلى قائمة الكورسات

    return render(request, 'add_course.html')

def delete_course(request, course_name):
    if course_name in courses:
        courses.remove(course_name)  # إزالة الكورس من القائمة
        return redirect('course_list')  # إعادة التوجيه إلى قائمة الكورسات
    else:
        return render(request, 'delete_course.html', {'error': 'Course not found'})  # إذا لم يتم العثور على الكورس
