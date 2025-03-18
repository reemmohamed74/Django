# from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy
# from django.contrib.auth.mixins import LoginRequiredMixin
# from .models import Trainee
# from .forms import TraineeForm
#
# class TraineeListView(LoginRequiredMixin, ListView):
#     model = Trainee
#     template_name = 'trainee/trainee_list.html'
#     context_object_name = 'trainees'
#
# class AddTraineeView(LoginRequiredMixin, CreateView):
#     model = Trainee
#     form_class = TraineeForm
#     template_name = 'trainee/add_trainee.html'
#     success_url = reverse_lazy('trainee-list')
#
# class UpdateTraineeView(LoginRequiredMixin, UpdateView):
#     model = Trainee
#     form_class = TraineeForm
#     template_name = 'trainee/add_trainee.html'
#     success_url = reverse_lazy('trainee-list')
#
# class DeleteTraineeView(LoginRequiredMixin, DeleteView):
#     model = Trainee
#     template_name = 'trainee/delete_trainee.html'
#     success_url = reverse_lazy('trainee-list')
