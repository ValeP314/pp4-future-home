from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic import UpdateView, DeleteView
from django.http import HttpResponseRedirect
from .models import Listing, Question
from .forms import ListingForm, QuestionForm
from django.urls import reverse_lazy


class ListingList(generic.ListView):

    model = Listing
    queryset = Listing.objects.filter(status=0).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class ListingDetail(DetailView):

    def get(self, request, slug, *args, **kwargs):
        queryset = Listing.objects.filter(status=0)
        listing = get_object_or_404(queryset, slug=slug)
        questions = listing.questions.filter(
            approved=True).order_by("-created_on")
        liked = False
        if listing.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "listing_detail.html",
            {
                "listing": listing,
                "questions": questions,
                "asked": False,
                "liked": liked,
                "question_form": QuestionForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Listing.objects.filter(status=0)
        listing = get_object_or_404(queryset, slug=slug)
        questions = listing.questions.filter(
            approved=True).order_by("-created_on")
        liked = False
        if listing.likes.filter(id=self.request.user.id).exists():
            liked = True

        question_form = QuestionForm(data=request.POST)

        if question_form.is_valid():
            question_form.instance.email = request.user.email
            question_form.instance.name = request.user.username
            question = question_form.save(commit=False)
            question.listing = listing
            question.save()
        else:
            question_form = QuestionForm()

        return render(
            request,
            "listing_detail.html",
            {
                "listing": listing,
                "questions": questions,
                "asked": True,
                "liked": liked,
                "question_form": QuestionForm(),
            },
        )


class ListingLike(View):

    def post(self, request, slug):
        listing = get_object_or_404(Listing, slug=slug)

        if listing.likes.filter(id=self.request.user.id).exists():
            listing.likes.remove(request.user)
        else:
            listing.likes.add(request.user)

        return HttpResponseRedirect(reverse('listing_detail', args=[slug]))


class AddListingView(CreateView):
    model = Listing
    form_class = ListingForm
    template_name = 'add_listing.html'


class UpdateListingView(UpdateView):
    model = Listing
    template_name = 'update_listing.html'
    fields = ['content', 'status', 'price']


class DeleteListingView(DeleteView):
    model = Listing
    template_name = 'delete_listing.html'
    success_url = reverse_lazy('home')
