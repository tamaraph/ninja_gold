from django.shortcuts import render, HttpResponse, redirect
import random
from datetime import datetime

# Create your views here.
def index(request):
    if 'total_gold' not in request.session or 'activities' not in request.session:
        request.session['total_gold'] = 0
        request.session['activities'] = []
    return render(request, 'ninja_gold/index.html')

def process_money(request):
    if request.method == 'GET':
        return redirect('/')
    elif request.method == 'POST':
        print(request.POST['farming'])
        
        if request.POST['farming'] == 'farm':
            gold = random.randint(10, 20)
            request.session['activities'].append('Earned ' + str(gold) +  ' golds from the farm! ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ')')

        if request.POST['farming'] == 'cave':
            gold = random.randint(5, 10)
            request.session['activities'].append('Earned ' + str(gold) +  ' golds from the cave! ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ')')

        if request.POST['farming'] == 'house':
            gold = random.randint(2, 5)
            request.session['activities'].append('Earned ' + str(gold) +  ' golds from the house! ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ')')

        if request.POST['farming'] == 'casino':
            gold = random.randint(-50, 50)
            if gold >= 0:
                request.session['activities'].append('Entered a casino and Earned ' + str(gold) + ' golds... Oh hell yeah!!! ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ')')
            else:
                request.session['activities'].append('Entered a casino and Lost ' + str(gold) +  ' golds... Ouch! ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ')')

        request.session['total_gold'] += gold        

        if request.session['total_gold'] >= 100:
            return render(request,'ninja_gold/win.html')

        if request.session['total_gold'] <= -100:
            return render(request,'ninja_gold/lost.html')

    return render(request, 'ninja_gold/index.html')

def play_again(request):
    request.session.flush()
    return redirect('/')