# from django.views.generic import ListView, CreateView
# from django.urls import reverse_lazy
# from django.contrib.auth.mixins import LoginRequiredMixin
# from .models import Course
# from .forms import CourseForm
# # Create your views here.
#
# class CourseListView(LoginRequiredMixin, ListView):
#     model = Course
#     template_name = 'course/course_list.html'
#     context_object_name = 'courses'
#
# class AddCourseView(LoginRequiredMixin, CreateView):
#     model = Course
#     form_class = CourseForm
#     template_name = 'course/add_course.html'
#     success_url = reverse_lazy('course-list')