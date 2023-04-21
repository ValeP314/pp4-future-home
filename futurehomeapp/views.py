from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from .models import Listing, Question, Booking
from .forms import QuestionForm, BookingForm


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
                "asked": False,
                "liked": liked,
                "question_form": QuestionForm(),
                "booking_form": BookingForm()
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
            booking_form = BookingForm()

        return render(
            request,
            "listing_detail.html",
            {
                "listing": listing,
                "questions": questions,
                "asked": True,
                "liked": liked,
                "question_form": QuestionForm(),
                "booking_form": BookingForm()
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


class RequestViewing(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Booking.objects.filter(status=0)
        bookings = get_object_or_404(queryset, slug=slug)
        requested = bookings.filter(
            approved=True).order_by("-created_on")

        return render(
            request,
            "listing_detail.html",
            {
                "requested": requested,
                "booking_form": BookingForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Booking.objects.filter(status=0)
        bookings = get_object_or_404(queryset, slug=slug)
        requested = bookings.filter(
            approved=True).order_by("-created_on")

        booking_form = BookingForm(data.request.POST)

        if booking_form.is_valid():
            booking_form.instance.email = request.user.email
            booking_form.instance.name = request.user.username
            booking_form = booking_form.save(commit=False)
            booking_form.save()

        else:
            booking_form = BookingForm()

        return render(
            request,
            "listing_detail.html",
            {
                "requested": requested,
                "booking_form": BookingForm()
            },
        )
