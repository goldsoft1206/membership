from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from .models import Boat, MembershipType, Membership, EmailList, UserProfile


# part of boat
class BoatList(ListView):
    model = Boat

class BoatDetail(DetailView):
    model = Boat

class BoatCreate(CreateView):
    model = Boat
    fields = ['name', 'type', 'length', 'beam', 'draft']

class BoatUpdate(UpdateView):
    model = Boat
    fields = ['name', 'type', 'length', 'beam', 'draft']
    template_name_suffix = '_update'

class BoatDelete(DeleteView):
    model = Boat
    success_url = reverse_lazy('boat_list')

# part of membership type
class MembershipTypeList(ListView):
    model = MembershipType

class MembershipTypeDetail(DetailView):
    model = MembershipType

class MembershipTypeCreate(CreateView):
    model = MembershipType

class MembershipTypeUpdate(UpdateView):
    model = MembershipType
    template_name_suffix = '_update'

class MembershipTypeDelete(DeleteView):
    model = MembershipType
    success_url = reverse_lazy('mtype_list')
