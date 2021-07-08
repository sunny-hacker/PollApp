from django.db import models


class Poll(models.Model):
    poll_question = models.TextField()
    poll_option1 = models.CharField(max_length=50)
    poll_option2 = models.CharField(max_length=50)
    poll_option3 = models.CharField(max_length=50)
    poll_option1_count = models.IntegerField(default=0)
    poll_option2_count = models.IntegerField(default=0)
    poll_option3_count = models.IntegerField(default=0)

    def total(self):
        return self.poll_option1_count + self.poll_option2_count + self.poll_option3_count

    def __str__(self):
        return "Poll id:- " + str(self.pk) + " created"


class EditPoll(models.Model):
    poll_question = models.TextField()
    poll_option1 = models.CharField(max_length=50)
    poll_option2 = models.CharField(max_length=50)
    poll_option3 = models.CharField(max_length=50)


class DeletePoll(models.Model):
    yes = models.BooleanField()
    no = models.BooleanField()


class DeleteAll(models.Model):
    yes = models.BooleanField()
    no = models.BooleanField()
