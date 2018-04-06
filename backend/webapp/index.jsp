<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title></title>
        <style type="text/css"> 
			body
			{
				font-size:70%;
				font-family:verdana,helvetica,arial,sans-serif;
			}
			canvas
			{
				border:1px solid #c3c3c3;
			}
		</style>
    </head>
    
    <body>
        <canvas id="canvas" width="600" height="600"></canvas>
        <canvas id="canvas-show" width="600" height="600"></canvas>
        <script type="text/javascript">
            var c = document.getElementById('canvas');
            var ctx = c.getContext('2d');
			
            //按下标记
            var onoff = false;
            var oldx = -10;
            var oldy = -10;

            //设置颜色
            var linecolor = 'black';

            //设置线宽
            var linw = 4;

            //添加鼠标移动事件
            canvas.addEventListener('mousemove',draw,true);

            //添加鼠标按下事件
            canvas.addEventListener('mousedown',down,false);

            //添加鼠标弹起事件
            canvas.addEventListener('mouseup',up,false);

            function down(event) {
                onoff = true;
                oldx = event.pageX-10;
                oldy = event.pagey-10;
            }

            function up() {
                onoff = false;
            }

            function draw(event) {
                if(onoff == true) {
                    var newx = event.pageX-10;
                    var newy = event.pageY-10;
                    ctx.beginPath();
                    ctx.moveTo(oldx,oldy);
                    ctx.lineTo(newx,newy);
                    ctx.strokeStyle = linecolor;
                    ctx.lineCap = 'round';
                    ctx.stroke();

                    oldx = newx;
                    oldy = newy;
                }
            }
        </script>
    </body>
</html>