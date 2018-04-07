from django.shortcuts import render
from django.http.response import *
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
from .pix2pix import *
import io
import numpy as np
import base64


def process():
    if a.seed is None:
        a.seed = random.randint(0, 2**31 - 1)

    tf.set_random_seed(a.seed)
    np.random.seed(a.seed)
    random.seed(a.seed)

    a.output_dir = 'D://test_draw_output'
    if not os.path.exists(a.output_dir):
        os.makedirs(a.output_dir)

    a.checkpoint = 'E://ML//TensorFlow//pix2pix-tensorflow//edges2shoes_AtoB'

    # load some options from the checkpoint
    options = {"which_direction", "ngf", "ndf", "lab_colorization"}
    with open(os.path.join(a.checkpoint, "options.json")) as f:
        for key, val in json.loads(f.read()).items():
            if key in options:
                print("loaded", key, "=", val)
                setattr(a, key, val)
    # disable these features in test mode
    a.scale_size = CROP_SIZE
    a.flip = False

    examples = load_examples('D://test_draw_input')
    print("examples count = %d" % examples.count)

    # inputs and targets are [batch_size, height, width, channels]
    model = create_model(examples.inputs, examples.targets)

    outputs = deprocess(model.outputs)

    def convert(image):
        if a.aspect_ratio != 1.0:
            # upscale to correct aspect ratio
            size = [CROP_SIZE, int(round(CROP_SIZE * a.aspect_ratio))]
            image = tf.image.resize_images(image, size=size, method=tf.image.ResizeMethod.BICUBIC)

        return tf.image.convert_image_dtype(image, dtype=tf.uint8, saturate=True)

        # reverse any processing on images so they can be written to disk or displayed to user
    with tf.name_scope("convert_outputs"):
        converted_outputs = convert(outputs)

    with tf.name_scope("encode_images"):
        display_fetches = {
            "paths": examples.paths,
            "outputs": tf.map_fn(tf.image.encode_png, converted_outputs, dtype=tf.string, name="output_pngs"),
        }

    saver = tf.train.Saver(max_to_keep=1)
    logdir = None
    sv = tf.train.Supervisor(logdir=logdir, save_summaries_secs=0, saver=None)
    with sv.managed_session() as sess:
        if a.checkpoint is not None:
            print("loading model from checkpoint")
            checkpoint = tf.train.latest_checkpoint(a.checkpoint)
            saver.restore(sess, checkpoint)

        max_steps = 2**32
        if a.max_epochs is not None:
            max_steps = examples.steps_per_epoch * a.max_epochs
        if a.max_steps is not None:
            max_steps = a.max_steps
        # testing
        # at most, process the test data once
        max_steps = min(examples.steps_per_epoch, max_steps)
        for step in range(max_steps):
            results = sess.run(display_fetches)
            filesets = save_images(results)
            for i, f in enumerate(filesets):
                print("evaluated image", f["name"])

@csrf_exempt
def index(request):
    context = {}
    #context['hello'] = 'Hello World! (draw version)'
    #context['imgUrl'] = ''

    return render(request, 'hello.html', context)

@csrf_exempt
def edges2bag(request):
    if request.method == 'POST':
        #print(request.POST.get('data'))

        dataStr = str(request.POST.get('data'))
        #print(dataStr)
        print('saving...')
        ori_image_data = base64.b64decode(dataStr)

        fout = open('d:\\test_draw_input\\test_draw.jpg', 'wb')
        fout.write(ori_image_data)
        fout.close()

        print('processing input downto 24 bit(RGB)')
        #A bad solution to process input to 24 bit
        input_img = Image.open("d:\\test_draw_input\\test_draw.jpg")
        input_img.load() # required for png.split()

        background = Image.new("RGB", input_img.size, (255, 255, 255))
        background.paste(input_img, mask=input_img.split()[3]) # 3 is the alpha channel
        background.save('d:\\test_draw_input\\test_draw.jpg', 'JPEG', quality=80)

        print('processing local edge pic...')
        process()

        print('passing pic data...')
        with open("d:\\test_draw_output\\images\\test_draw-outputs.png","rb") as f:
            # b64encode是编码，b64decode是解码
            base64_data = base64.b64encode(f.read())
            # base64.b64decode(base64data)
        print('Done!')
        base64_data_str = str(base64_data).split('\'')[1]

        return HttpResponse(json.dumps({
                "status": 'success',
                "result": 'data:image/png;base64,'+base64_data_str
            }))
