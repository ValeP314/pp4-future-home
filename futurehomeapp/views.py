from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Listing
from .forms import QuestionForm


class ListingList(generic.ListView):
    model = Listing
    queryset = Listing.objects.filter(status=0).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class ListingDetail(View):

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
                "liked": liked,
                "question_form": QuestionForm()
            },
        )


class ListingDetail(View):

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
                "question_form": QuestionForm()
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
                "question_form": QuestionForm()
            },
        )
