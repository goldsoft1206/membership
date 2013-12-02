from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from .models import Boat, MembershipType, Membership, EmailList, CustomUser


# part of boat
class BoatList(ListView):
    model = Boat

class BoatDetail(DetailView):
    model = Boat

class BoatCreate(CreateView):
    model = Boat
    fields = ['name', 'type', 'length', 'beam', 'draft']
    template_name = "profile/general_create.html"

class BoatUpdate(UpdateView):
    model = Boat
    fields = ['name', 'type', 'length', 'beam', 'draft']
    template_name = "profile/general_update.html"

class BoatDelete(DeleteView):
    model = Boat
    success_url = reverse_lazy('boat_list')
    template_name = "profile/general_confirm_delete.html"


# part of membership type
class MembershipTypeList(ListView):
    model = MembershipType

class MembershipTypeDetail(DetailView):
    model = MembershipType

class MembershipTypeCreate(CreateView):
    model = MembershipType
    template_name = "profile/general_create.html"

class MembershipTypeUpdate(UpdateView):
    model = MembershipType
    template_name = "profile/general_update.html"

class MembershipTypeDelete(DeleteView):
    model = MembershipType
    success_url = reverse_lazy('mtype_list')
    template_name = "profile/general_confirm_delete.html"


# part of membership
class MembershipList(ListView):
    model = Membership

class MembershipDetail(DetailView):
    model = Membership

class MembershipCreate(CreateView):
    model = Membership
    template_name = "profile/general_create.html"

class MembershipUpdate(UpdateView):
    model = Membership
    template_name = "profile/general_update.html"

class MembershipDelete(DeleteView):
    model = Membership
    success_url = reverse_lazy('membership_list')
    template_name = "profile/general_confirm_delete.html"


# part of EmailList
class EmailListView(ListView):
    model = EmailList

class EmailDetail(DetailView):
    model = EmailList

class EmailCreate(CreateView):
    model = EmailList
    template_name = "profile/general_create.html"

class EmailUpdate(UpdateView):
    model = EmailList
    template_name = "profile/general_update.html"

class EmailDelete(DeleteView):
    model = EmailList
    success_url = reverse_lazy('email_list')
    template_name = "profile/general_confirm_delete.html"


# part of User
class UserList(ListView):
    model = CustomUser

class UserDetail(DetailView):
    model = CustomUser

class UserCreate(CreateView):
    model = CustomUser
    fields = ['first_name', 'last_name', 'email', 'birth_date', 'phone', 'membership', 'email_lists']
    template_name = "profile/general_create.html"

class UserUpdate(UpdateView):
    model = CustomUser
    fields = ['first_name', 'last_name', 'email', 'birth_date', 'phone', 'membership', 'email_lists']
    template_name = "profile/general_update.html"

class UserDelete(DeleteView):
    model = CustomUser
    success_url = reverse_lazy('user_list')
    template_name = "profile/general_confirm_delete.html"


