from django.shortcuts import render
import pyscreenshot
import time 
from datetime import datetime
from django.conf import settings
import schedule


def screenshot(request):
    # Screenshot information (filename)
    x = str(datetime.now())
    img_name = 'Screen - ' + x + '.jpg'

    ss = pyscreenshot.grab()
    filepath = str(settings.BASE_DIR) + '/all_ screenshots/' + img_name
    ss.save(filepath)

    return render(request, 'mainapp/index.html', {})


def index(request):
    schedule.every(10).seconds.do(screenshot, request)
    start = request.POST.get('start')
    end = request.POST.get('end')
    if request.method == 'POST':

        if start:
            while start:
                schedule.run_pending()
                time.sleep(10)
                print('START!!!!!!!')
                # if end:
                #     break
                # else:
                #     print('NOT END')

        elif request.POST.get('end'):
            print('END!!!!!!!')
            return render(request, 'mainapp/index.html', {})

    # while request.method == 'POST':
    #     time.sleep(1)

    return render(request, 'mainapp/index.html', {})


# statement = True
# while statement is True:
#     inp = input('input: ')
#     if inp == 'stop':
#         statement = False
#
# print('Wxecuted!!')




