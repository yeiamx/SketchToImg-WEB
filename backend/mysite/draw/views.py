from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from . import models
import io
from PIL import Image
import numpy as np
import base64

@csrf_exempt
def index(request):
    context = {}
    #context['hello'] = 'Hello World! (draw version)'
    #context['imgUrl'] = 'imgs/Irene.jpg'
    if request.method == 'POST':
        #print(request.POST.get('data'))

        dataStr = str(request.POST.get('data'))
        #print(dataStr)
        print('processing...')
        ori_image_data = base64.b64decode(dataStr)
        image_bytes = io.BytesIO(ori_image_data)
        im = Image.open(image_bytes)
        arr = np.array(im)[:,:,0]
        print(arr.shape)

        print('saving...')
        fout = open('d:\\test_draw.png', 'wb')
        fout.write(ori_image_data)
        fout.close()
        print('finished!')

    return render(request, 'hello.html', context)