from django.shortcuts import render, HttpResponse, redirect
from polls.models import Registration, Customer, Win, Admins
import random
import datetime
from django.contrib.auth.models import User, Permission, Group
from django.contrib.auth.decorators import permission_required

def Customer_Registration(request) :
    if request.method == 'POST':
        name = request.POST.get('name')
        mail = request.POST.get('mail')
        pswd = request.POST.get('pswd')
    
        customer = Registration(name=name, mail=mail, pswd=pswd)

        if customer.isExists() :
            return HttpResponse('Mail Id All Ready Exists')
        
        customer.register()
    return render(request, 'registration.html')

def login(request) :
    if request.method == 'GET' :
        return render(request, 'registration.html')
    
    else :
        mail = request.POST.get('mail')
     
        customer = Registration.objects.filter(mail=request.POST['mail'])
        
        if customer :
            request.session['mail'] = mail
            return redirect(f'/Amount-Deposite')
        
        else :
            return HttpResponse('Mail Id is Invalid')   

@permission_required('polls.withdraw')
def opetion_provide(request) :
   
    # user = User.objects.get(username="abhishek")
    # permission = Permission.objects.get(codename="withdraw") 
    # user.user_permissions.add(permission)
    
    # print(f"Permission {permission} added successfully to user {user.username}.")
    # print('user permission Adding', user.user_permissions)   
    # print(user.has_perm("<polls).view_poll"))
    
    # Assigning permissions to a group
    # group = Group.objects.get(name="abhishek")
    # group.permissions.add(permission)         
    # return render(request, 'index.html',{'user':request.user.username})

    mail = request.session['mail'] 
    Admin_mail = Admins.get_all_Admins_Data()
    for i in Admin_mail :
        Admin_mail = i.mail
    
    if mail == Admin_mail :
        return render(request, 'index.html',{'mail':mail})
    else :
        return render(request, 'index.html')

def get(request) :
    return render(request, 'Enter-Amount.html')

def Amount_view(request) :

    mail = request.session['mail']
    customer = Registration.objects.filter(mail=mail).first()

    name = customer.name
    amount = request.POST.get('amount')

    print('customer Details', customer)        
    print('Actual Amount Is', amount)
    print('name is',name)

    amount = Customer(name=name, amount=amount).save()
    return redirect(f'/Amount-Deposite')

def Draw(request) :
    mail = request.session['mail']
    
    if request.session.has_key('mail') :
        total = Customer.get_all_user_data()
        print('data', total)

        grand_total = 0
      
        # Calculate total for each item and the grand total
        for item in total :
            item.total = item.amount
            grand_total += int(item.total)

        print('total', grand_total)

        # get all user id's
        user_ids = Customer.get_all_user_ids()
        print(user_ids)  # This will print a list of all user IDs

        if grand_total:
            for i in total:
                # withdraw name a variable store a random selected Data store 
                withdraw = random.choice(user_ids)
            print(f"Withdrawing ID: {withdraw}") 

        # ======================== Get Current Date ==========================
        
        current_date = datetime.date.today()
        print('Current_Date : ', current_date)

        # =================== Get Dates from Database ======================
        
        create_at_Date = Customer.get_all_user_data()
        for i in create_at_Date :
            Date = i.create_at_Date
        print('to days Date is', Date)    
                    
        if current_date and withdraw :
            user_data = Customer.objects.get(id=withdraw) 
            
            name = user_data.name 
            amount = user_data.amount
            print(name, amount)  
        
            # Check if there is already a record with the current date
            # Check if an entry with today's date exists
            win_entry = Win.objects.filter(Date=current_date).first()
    
            if win_entry:
                return HttpResponse('Lucky Candidates All Ready Chosse')
        
            else:
                # Create a new entry with today's date
                Win.objects.create(Date=current_date, name=name, amount=grand_total).save()
                return redirect(f'/Amount-Deposite')
       
        else :
            return HttpResponse('page does not found')  

    else :
        return redirect(f'/login')
            
def Cash_Back(request) :
    mail = request.session['mail'] 
    
    if request.session.has_key('mail') :       
        store = Win.get_all_win_user_data()
        
        for s in store :        
            name = s.name
            amount = s.amount
      
        # x name a variable store a amount value      
        x = amount
            
        grand_total = int(amount) - 90 
        
        data = {
            'name' : name,
            'amount' : amount,
            'grand_total' : grand_total
        }
                 
        return render(request, 'Amount_withdraw.html',data)    
    
    else :
        return redirect(f'/login')