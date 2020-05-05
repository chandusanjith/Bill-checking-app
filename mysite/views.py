from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.http import HttpResponseRedirect
from datetime import datetime
import calendar
from django.contrib import messages
from mysite.models import MainData, MonthWise


def LoginLoad(request):
  return render(request, 'index.html')

def login(request):
  id = request.POST['usernamelolgin']
  password = request.POST['passsed']

  user = auth.authenticate(username = id, password = password)
  
  if user is not None:
    auth.login(request, user)
    return HttpResponseRedirect('/main/')
  else:
    messages.info(request, 'Invalid login details')
    return render(request, 'index.html')




def MainLoad(request):
  user = request.user
  currentDay = datetime.now().day
  currentMonth = datetime.now().month
  currentYear = datetime.now().year
  dates = calendar.monthcalendar(currentYear, currentMonth)
  week1 = dates[0]
  week2 = dates[1]
  week3 = dates[2]
  week4 = dates[3]
  week5 = dates[4]
  displist1 =[]
  displist2 =[]
  displist3 =[]
  displist4 =[]
  displist5 =[]
  dispamt1 = []
  dispamt2 = []
  dispamt3 = []
  dispamt4 = []
  dispamt5 = []
  for week1date in week1:
    if week1date == 0:
       displist1.append(" ")
       dispamt1.append(" ")
    elif MainData.objects.filter(UserID =user, day = str(week1date), month = (str(currentMonth)+str(currentYear))).exists():
           a = MainData.objects.filter(UserID =user,day = str(week1date), month = (str(currentMonth)+str(currentYear)))
           displist1.append(a[0].Discription)
           dispamt1.append(a[0].Amount)
    else:
          displist1.append(" ")
          dispamt1.append(" ")
  weeklist1 = list(zip(week1,displist1,dispamt1))
  print(weeklist1)
  for week1date in week2:
    if week1date == 0:
       displist2.append(" ")
       dispamt2.append(" ")
    elif MainData.objects.filter(UserID =user, day = str(week1date), month = (str(currentMonth)+str(currentYear))).exists():
           a = MainData.objects.filter(UserID =user,day = str(week1date), month = (str(currentMonth)+str(currentYear)))
           displist2.append(a[0].Discription)
           dispamt2.append(a[0].Amount)
    else:
          displist2.append(" ")
          dispamt2.append(" ")
  weeklist2 = list(zip(week2,displist2,dispamt2))

  for week1date in week3:
    if week1date == 0:
       displist3.append(" ")
       dispamt3.append(" ")
    elif MainData.objects.filter(UserID =user, day = str(week1date), month = (str(currentMonth)+str(currentYear))).exists():
           a = MainData.objects.filter(UserID =user,day = str(week1date), month = (str(currentMonth)+str(currentYear)))
           displist3.append(a[0].Discription)
           dispamt3.append(a[0].Amount)
    else:
          displist3.append(" ")
          dispamt3.append(" ")
  weeklist3 = list(zip(week3,displist3,dispamt3))

  for week1date in week4:
    if week1date == 0:
       displist4.append(" ")
       dispamt4.append(" ")
    elif MainData.objects.filter(UserID =user, day = str(week1date), month = (str(currentMonth)+str(currentYear))).exists():
           a = MainData.objects.filter(UserID =user,day = str(week1date), month = (str(currentMonth)+str(currentYear)))
           displist4.append(a[0].Discription)
           dispamt4.append(a[0].Amount)
    else:
          displist4.append(" ")
          dispamt4.append(" ")
  weeklist4 = list(zip(week4,displist4,dispamt4))

  for week1date in week5:
    if week1date == 0:
       displist5.append(" ")
       dispamt5.append(" ")
    elif MainData.objects.filter(UserID =user, day = str(week1date), month = (str(currentMonth)+str(currentYear))).exists():
           a = MainData.objects.filter(UserID =user,day = str(week1date), month = (str(currentMonth)+str(currentYear)))
           displist5.append(a[0].Discription)
           dispamt5.append(a[0].Amount)
    else:
          displist5.append(" ")
          dispamt5.append(" ")
  weeklist5 = list(zip(week5,displist5,dispamt5))


  datatodisp = MainData.objects.filter(UserID =user,month = (str(currentMonth)+str(currentYear)))
  print(datatodisp)
  monthwords = calendar.month_name[currentMonth]
  date = monthwords + " " + str(currentYear)
  monthdata = MonthWise.objects.filter(userid = user, month =str(currentMonth)+str(currentYear))
  context = {'week1': weeklist1,
             'week2': weeklist2,
             'week3': weeklist3,
             'week4': weeklist4,
             'week5': weeklist5,
             'datecal':date,
             'month':monthdata}
            
  return render(request, 'main.html', context)

def LoadDate(request):
    user = request.user
    month = request.POST['month']
    year = request.POST['year']
    currentMonth = int(month)
    currentYear = int(year)
    dates = calendar.monthcalendar(currentYear, currentMonth)
    print(dates)
    week1 = dates[0]
    week2 = dates[1]
    week3 = dates[2]
    week4 = dates[3]
    week5 = dates[4]
    displist1 =[]
    displist2 =[]
    displist3 =[]
    displist4 =[]
    displist5 =[]
    dispamt1 = []
    dispamt2 = []
    dispamt3 = []
    dispamt4 = []
    dispamt5 = []
    for week1date in week1:
      if week1date == 0:
        displist1.append(" ")
        dispamt1.append(" ")
      elif MainData.objects.filter(UserID =user, day = str(week1date), month = (str(currentMonth)+str(currentYear))).exists():
            a = MainData.objects.filter(UserID =user,day = str(week1date), month = (str(currentMonth)+str(currentYear)))
            displist1.append(a[0].Discription)
            dispamt1.append(a[0].Amount)
      else:
            displist1.append(" ")
            dispamt1.append(" ")
    weeklist1 = list(zip(week1,displist1,dispamt1))
    print(weeklist1)
    for week1date in week2:
      if week1date == 0:
         displist2.append(" ")
         dispamt2.append(" ")
      elif MainData.objects.filter(UserID =user, day = str(week1date), month = (str(currentMonth)+str(currentYear))).exists():
             a = MainData.objects.filter(UserID =user,day = str(week1date), month = (str(currentMonth)+str(currentYear)))
             displist2.append(a[0].Discription)
             dispamt2.append(a[0].Amount)
      else:
            displist2.append(" ")
            dispamt2.append(" ")
    weeklist2 = list(zip(week2,displist2,dispamt2))

    for week1date in week3:
      if week1date == 0:
         displist3.append(" ")
         dispamt3.append(" ")
      elif MainData.objects.filter(UserID =user, day = str(week1date), month = (str(currentMonth)+str(currentYear))).exists():
             a = MainData.objects.filter(UserID =user,day = str(week1date), month = (str(currentMonth)+str(currentYear)))
             displist3.append(a[0].Discription)
             dispamt3.append(a[0].Amount)
      else:
            displist3.append(" ")
            dispamt3.append(" ")
    weeklist3 = list(zip(week3,displist3,dispamt3))

    for week1date in week4:
      if week1date == 0:
         displist4.append(" ")
         dispamt4.append(" ")
      elif MainData.objects.filter(UserID =user, day = str(week1date), month = (str(currentMonth)+str(currentYear))).exists():
            a = MainData.objects.filter(UserID =user,day = str(week1date), month = (str(currentMonth)+str(currentYear)))
            displist4.append(a[0].Discription)
            dispamt4.append(a[0].Amount)
      else:
            displist4.append(" ")
            dispamt4.append(" ")
    weeklist4 = list(zip(week4,displist4,dispamt4))

    for week1date in week5:
      if week1date == 0:
         displist5.append(" ")
         dispamt5.append(" ")
      elif MainData.objects.filter(UserID =user, day = str(week1date), month = (str(currentMonth)+str(currentYear))).exists():
             a = MainData.objects.filter(UserID =user,day = str(week1date), month = (str(currentMonth)+str(currentYear)))
             displist5.append(a[0].Discription)
             dispamt5.append(a[0].Amount)
      else:
            displist5.append(" ")
            dispamt5.append(" ")
    weeklist5 = list(zip(week5,displist5,dispamt5))


    datatodisp = MainData.objects.filter(UserID =user,month = (str(currentMonth)+str(currentYear)))
    print(datatodisp)
    monthwords = calendar.month_name[currentMonth]
    date = monthwords + " " + str(currentYear)
    monthdata = MonthWise.objects.filter(userid = user, month =str(currentMonth)+str(currentYear))
    context = {'week1': weeklist1,
             'week2': weeklist2,
             'week3': weeklist3,
             'week4': weeklist4,
             'week5': weeklist5,
             'datecal':date,
             'month':monthdata}
    return render(request, 'main.html', context)

def AdminsLoad(request):
  users = User.objects.all()
  context = {'users': users}
  return render(request, 'AdminPass.html', context)

def LoadData(request):
   uid = request.POST['usersed']
   mnth = request.POST['mnth']
   currentYear = datetime.now().year
   print("chandu at check month")
   print(mnth)
   month = mnth+str(currentYear)
   users = User.objects.all()
   data = MainData.objects.filter(UserID = uid, month = month)
   monthdata = MonthWise.objects.filter(userid = uid, month = month)
   context = {'data': data,
             'users': users,
             'monthdata':monthdata,
             'workinguser': uid,
             'wmonth': month}
   return render(request, 'AdminPass.html', context)

def AddDataLoad(request):
   users = User.objects.all()
   context = {'users': users}
   return render(request, 'AddData.html', context)


def AddData(request):
  user = request.POST['user']
  dateuser = request.POST['dateuser']
  disp = request.POST['disp']
  amount = request.POST['amount']
  users = User.objects.all()
  split = dateuser.split("-")
  month = split[1]
  day = split[2]
  month = month.lstrip('0')
  day = day.lstrip('0')
  currentYear = datetime.now().year
  month = month+str(currentYear)
  a = MainData(UserID = user, Discription = disp, Dateed = dateuser, month = month, day = day,Amount = int(amount), Status = "Not paid" )
  a.save() 
  if MonthWise.objects.filter(userid = user, month = month).exists():

      b = MonthWise.objects.filter(userid = user, month = month)
      total = b[0].total + int(amount)
      c = MonthWise.objects.filter(userid = user, month = month).update(total = total)
  else:
     d = MonthWise(userid = user,month = month, total =  amount, status = "Not paid")
     d.save()

  context = {'users': users}
  return render(request, 'AddData.html', context)


def ChangeStatus(request, uid, month):
    wuser = request.user
    b= MonthWise.objects.filter(userid = uid, month = month).update(status = "Paid")
    c = MainData.objects.filter(UserID = uid, month = month)
    for data in c:
      d = MainData.objects.filter(UserID = uid, month = month, day = data.day).update(Status = "Paid")
    users = User.objects.all()
    data = MainData.objects.filter(UserID = uid, month = month)
    monthdata = MonthWise.objects.filter(userid = uid, month = month)
    context = {'data': data,
             'users': users,
             'monthdata':monthdata,
             'workinguser': wuser,
             'wmonth': month}
    return render(request, 'AdminPass.html', context)

