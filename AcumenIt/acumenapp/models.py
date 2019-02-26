from django.db import models

"""
Must:
Write full names for each variable dont use shortcuts.
dont use capitals for attribute names or variables, 
only use capitals for Classes and Choices
Optional:
Use underscore conventions for all attributes
"""


"""
Must haves:
Points for each participant: each participant gets some points for participation depending on the event,
and gets some more points if he gets merit in those events.
Add team field
"""
class Profile(models.Model):
    YEAR_CHOICES = (('I', 'I'), ('II', 'II'), ('III', 'III'), ('IV', 'IV'))

    IT = 'IT'
    EEE = 'EEE'
    ECE = 'ECE'
    CIVIL = 'CIVIL'
    CSE = 'CSE'
    MECH = 'MECH'
    CHEMICAL = 'CHEMICAL'
    EIE = 'EIE'
    TEXTILE = 'TEXTILE'

    BRANCH_CHOICES = ((IT, 'Information Technology'), (EEE, 'Electronics and Electrical Engineering'),
                      (ECE, 'Electronics and Communication Engineering'), (CIVIL, 'Civil'), (CSE, 'Computer Sciece'),
                      (MECH, 'Mechanical'), (CHEMICAL, 'Chemical'),
                      (EIE, 'Electronics and Instrumentation Engineering'), (TEXTILE, 'Textile'))

    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50, primary_key=True)
    roll = models.CharField(max_length=20, default="1602-70-700-777")
    Year = models.CharField(max_length=2, choices=YEAR_CHOICES, default="I")
    Branch = models.CharField(max_length=50, choices=BRANCH_CHOICES, default="IT")
    College = models.CharField(max_length=50)
    Phone_number = models.CharField(max_length=10, default="NoNumber")
    qid = models.CharField(max_length=10)


"""
As mentioned above
every events should have 2 fields one for points that the participant would get for participation
and other for merit
"""
class Event(models.Model):
    eId = models.CharField(max_length=5, default="NULL", primary_key=True)
    eName = models.CharField(max_length=50)
    eCount = models.IntegerField(default=0)
    eorganiser = models.CharField(max_length=20)
    cost = models.IntegerField(default=0)


"""
Use good names for attributes
move paid field from team to this, as payment is for different events not for teams
also move payment mode field to here
"""
class EventDetails(models.Model):
    eid = models.ForeignKey('Event', on_delete='CASCADE', max_length=5)
    tid = models.CharField(max_length=20)
    uid = models.ForeignKey('Profile', on_delete='CASCADE', max_length=50)


    
"""
Better add a team size attribute, becasue each event may require team of different sizes
Think of any other attributes that would be needed
"""
class Team(models.Model):
    Waiting = 'W'
    Running = 'R'
    Played = 'P'

    STATUS_CHOICES = ((Running, 'Running'), (Played, 'Played'), (Waiting, 'Waiting'))
    online = 'ON'
    offline = 'OFF'
    none = 'N'
    STATUS_CHOICES1 = ((online, 'Online'), (offline, 'Offline'), (none, 'None'))

    status_choice = models.CharField(max_length=8, choices=STATUS_CHOICES)
    tid = models.CharField(max_length=20)
    eid = models.ForeignKey('Event', on_delete='CASCADE', max_length=5)
    qid = models.CharField(max_length=10)
    total = models.IntegerField(default=0)
    paymentMode = models.CharField(max_length=10, choices=STATUS_CHOICES1)
    paid = models.BooleanField(default=False)







