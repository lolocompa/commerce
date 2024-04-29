from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User
from .models import listing
from .models import bid
from .models import category
from .models import comments

from decimal import Decimal



def index(request):
    """Render the index page with active listings."""
    return render(request, "auctions/index.html", {
        "listings": listing.objects.filter(is_active = True)
    })




def login_view(request):
    """Handle user login."""
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    """Handle user logout."""
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    """Handle user registration."""
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def create_listing(request):
    """Handle the creation of a new listing."""
    if request.method == "GET":
        return render(request, "auctions/create_listing.html")
    else:
        title = request.POST.get("title")
        description = request.POST.get("description")
        starting_bid = request.POST.get("starting_bid")
        image = request.POST.get("image")
        get_category = request.POST.get("category")
        new_category = category(category=get_category)
        new_category.save()
        user = request.user
        new_bid = bid(number=starting_bid, bidder=user)
        new_bid.save()

        try:
            # Validate starting_bid as a Decimal
            starting_bid = Decimal(starting_bid)
        except Decimal.InvalidOperation:
            return HttpResponse("Invalid starting bid value")


        if image and category: 
            new_listing = listing(title=title, description=description, image=image, category=new_category, user=user, starting=new_bid)
            new_listing.save()
        elif category and not image:
            new_listing = listing(title=title, description=description, category=new_category, user=user, starting=new_bid)
            new_listing.save()
        elif image and not category:
            new_listing = listing(title=title, description=description, image=image, user=user, starting=new_bid)
            new_listing.save()    
        else:
            new_listing = listing(title=title, description=description, user=user, starting=new_bid)
            new_listing.save()
        return HttpResponseRedirect(reverse("index"))
    



def see_list(request, pk):
    """Display details for a specific listing."""
    current_user = request.user
    all_comments = comments.objects.all()
    return render(request, "auctions/see_list.html", {
        "data": listing.objects.get(pk=pk),
        "current_user": current_user,
        "comments": all_comments
    })




def watchlist(request):
    """Handle adding/removing listings from the user's watchlist."""
    if request.method == "POST":
        watch1 = str(request.POST.get("watch"))
        id1 = request.POST.get("id")
        element = listing.objects.get(pk=id1)



        if watch1 == "add":
            element.watchlist = True
            element.save()
        else:
            element.watchlist = False
            element.save()
        return HttpResponseRedirect(reverse("index"))
    else:
            watchlist_lists = listing.objects.filter(watchlist = True)   
            return render(request, "auctions/index.html", {
            "listings": watchlist_lists
            })




def make_bid(request):
    """Handle placing bids on listings."""
    if request.method == "POST":
        list_id = request.POST.get("list_id")
        number_placed = request.POST.get("bid")
        number_placed = float(number_placed)

        current_list = listing.objects.get(pk=list_id)
        current_price = current_list.starting.number

        if number_placed > current_price:
            new_bid = bid(bidder=request.user, number=number_placed)
            new_bid.save()
            current_list.starting = new_bid
            current_list.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/error.html", {
                "message": "invalid bid"
            })
            



def close_bid(request):
        """Handle closing a bid/listing."""
        if request.method == "POST":
            list_id = request.POST.get("close_list")
            close_list = listing.objects.get(pk=list_id)
            close_list.is_active = False
            close_list.save()
            return HttpResponseRedirect(reverse("index"))
        


def categories(request):
    """Display all categories or filter listings by a selected category."""
    if request.method == "GET":
        all_categories = listing.objects.values_list('category__category', flat=True).distinct()
        return render(request, "auctions/categories.html", {
            "categories": all_categories
        })
    else:
        selected = request.POST.get("select")
        filtered_listings = listing.objects.filter(category__category=selected, is_active=True)
        return render(request, "auctions/index.html", {
            "listings": filtered_listings
        })



def comments_made(request):
    """Handle user-submitted comments on listings."""
    if request.method == "POST":
        id = request.POST.get("list_Index")
        submited = request.POST.get("comment")
        new_comment = comments(user=request.user, comment=submited)
        new_comment.save()
        return HttpResponseRedirect(reverse("index"))





