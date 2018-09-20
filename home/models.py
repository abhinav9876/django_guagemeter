from django.db import models

# Create your models here.
class user(models.Model):
    fname    = models.CharField(max_length=30)
    lname    = models.CharField(max_length=30)
    email    = models.CharField(max_length=50)
    pnumber  = models.IntegerField()
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.email
    def isLoggedIn( email, password):
        check = user.objects.filter(email=email,password=password)
        print(str(check),"<-log msg2............")
        user1=""
        if str(check) !=  "<QuerySet []>":
            user1 = check.first().__dict__
        return user1, check.count()


#datatable models
class Datatable(models.Model):
    server = models.CharField(max_length=30)
    last_tested = models.CharField(max_length=30)
    avg_speed = models.CharField(max_length=30)
    ping_RTT = models.CharField(max_length=30)
    upload_speed = models.CharField(max_length=30)
    download_speed = models.CharField(max_length=30)
    download = models.CharField(max_length=30)

    def add_entry(test_data_list):
        a = Datatable.objects.create()
        a.server = test_data_list[0]
        a.last_tested = test_data_list[1]
        a.avg_speed = test_data_list[2]
        a.ping_RTT = test_data_list[3]
        a.upload_speed = test_data_list[4]
        a.download_speed = test_data_list[5]
        a.download = test_data_list[6]
        a.save()
    def check_entry(server_ip):
        check = Datatable.objects.filter(server=server_ip)
        test_num=""
        if str(check) !=  "<QuerySet []>":
            test_num = check.first().__dict__
        return test_num
class Test_history(models.Model):
    server = models.CharField(max_length=30)
    last_tested = models.CharField(max_length=30)
    avg_speed = models.CharField(max_length=30)
    ping_RTT = models.CharField(max_length=30)
    upload_speed = models.CharField(max_length=30)
    download_speed = models.CharField(max_length=30)
    download = models.CharField(max_length=30)
    def add_entry(test_data_list):
        a = Test_history.objects.create()
        a.server = test_data_list[0]
        a.last_tested = test_data_list[1]
        a.avg_speed = test_data_list[2]
        a.ping_RTT = test_data_list[3]
        a.upload_speed = test_data_list[4]
        a.download_speed = test_data_list[5]
        a.download = test_data_list[6]
        a.save()
    def check_entry(server_ip):
        check = Test_history.objects.filter(server=server_ip)
        test_num=""
        if str(check) !=  "<QuerySet []>":
            test_num = check.first().__dict__
        return test_num
