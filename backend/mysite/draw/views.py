from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from . import models
import base64

@csrf_exempt
def index(request):
    context = {}
    #context['hello'] = 'Hello World! (draw version)'
    #context['imgUrl'] = 'imgs/Irene.jpg'
    if request.method == 'POST':
        #print(request.POST.get('data'))

        dataStr = str(request.POST.get('data'))
        print(dataStr)
        print('processing...')
        ori_image_data = base64.b64decode(dataStr)
        print('saving...')
        fout = open('d:\\test_draw.png', 'wb')
        fout.write(ori_image_data)
        fout.close()
        print('finished!')

    return render(request, 'hello.html', context)