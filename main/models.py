from django.db import models

# Create your models here.

class BaszlAccount(models.Model):
    baszlUser = models.CharField(max_length=200)
    statusCodes = models.TextField(default="")

class InstagramAccount(models.Model):
    baszlAcct = models.ForeignKey(BaszlAccount, on_delete=models.CASCADE)
    accountID = models.CharField(max_length=300)
    timeStamp = models.IntegerField(default=0)
    handle = models.CharField(max_length=200,blank=True, null=True)
    numPosts = models.IntegerField(default=0)

    def __str__(self):
        string = "<p>ID: " + self.accountID + "</p>"
        string += "<p>Timestamp: " + str(self.timeStamp) + "</p"
        string += "<p>Handle: " + self.handle + "</p>"

        return string

class FacebookAccount(models.Model):
    baszlAcct = models.ForeignKey(BaszlAccount, on_delete=models.CASCADE)
    accessToken = models.CharField(max_length=400)
    pageToken = models.CharField(max_length=400)
    pageID = models.CharField(max_length=200)
    timeStamp = models.IntegerField(default=0)
    handle = models.CharField(max_length=200,blank=True, null=True)
    numPosts = models.IntegerField(default=0)

    def __str__(self):
        string = "<p>Access Token: " + self.accessToken.decode() + "</p>"
        string += "<p>Page Token: " + self.pageToken.decode() + "</p>"
        string += "<p>Page ID: " + self.pageID.decode() + "</p>"
        string += "<p>Timestamp: " + str(self.timeStamp) + "</p>"
        string += "<p>Handle: " + self.handle + "</p>"

        return string

class TwitterAccount(models.Model):
    baszlAcct = models.ForeignKey(BaszlAccount, on_delete=models.CASCADE)
    accessToken = models.CharField(max_length=300)
    accessSecret = models.CharField(max_length=300)
    timeStamp = models.IntegerField(default=0)
    handle = models.CharField(max_length=200, blank=True, null=True)
    numPosts = models.IntegerField(default=0)

    def __str__(self):
        string = "<p>Access Token: " + self.accessToken + "</p>"
        string += "<p>Access Secret: " + self.accessSecret + "</p>"
        string += "<p>Timestamp: " + str(self.timeStamp) + "</p>"
        string += "<p>Handle: " + self.handle + "</p>"

        return string

class ImageFile(models.Model):
    baszlAcct = models.ForeignKey(BaszlAccount, on_delete=models.CASCADE)