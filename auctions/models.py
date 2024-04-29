from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass



class category(models.Model):
    category = models.CharField( max_length=50)



class bid(models.Model):
    number = models.DecimalField(null=False, max_digits=5, decimal_places=2)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"bid: {self.number} from {self.bidder}"



class listing(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    title = models.CharField(max_length=50, null=False)
    description = models.TextField(null=False)
    starting = models.ForeignKey(bid , on_delete=models.CASCADE, related_name="bidprice")
    image = models.URLField(max_length=200, blank=True)
    category = models.ForeignKey(category, on_delete=models.CASCADE, related_name="filter_categoy")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    watchlist = models.BooleanField(default=False)  
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"title: {self.title}, description:{self.description}, starting:{self.starting}, image:{self.image}, category:{self.category}, user:{self.user}, watchlist:{self.watchlist}"



class comments(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.user} commented: {self.comment}"
