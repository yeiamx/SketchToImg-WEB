#SketchToImg-WEB

##Introduction

这是一个基于去年之前读过的一篇论文[pix2pix](https://phillipi.github.io/pix2pix/)的交互式网页版实现(demo)。</br>


pix2pix是深度学习领域大热的GAN(对抗神经网络)下的一个分支，它学习输入图像到输出图像的映射，下图是论文里几个实验的截图。</br>
![Alt text](https://github.com/yeiamx/SketchToImg-WEB/raw/master/Screenshots/examples.png)</br>
当时读完论文就觉得很有意思，正好这次系统设计有这么一个制作个人项目的机会，结合最近项目的经历，决定做成一个能够在线将画出的草稿变成现实物品的这么一个网站。

##Usage
[我的demo网站](http://www.dwwd.fun:8000/draw/)</br>
点击上方链接即可进入网站，在左处画下一只鞋（由于时间以及机器限制只针对了鞋，更准确地是皮鞋进行了训练），点击send，耐心等待半分钟到一分钟后右边将会出现一只真实（看人品以及你画画的水平）的鞋子。</br>
![Alt text](https://github.com/yeiamx/SketchToImg-WEB/raw/master/Screenshots/good.png)</br>

##Prospect
这个网站之所以称之为demo版是因为它还有许多进行增量开发的空间。首先速度方面在要求即时性的WEB世界是没法接受的。而且因为各种原因（主要是垃圾的服务器），时常出现无法返回数据的情况。如果对这个项目有任何想法，welcome to 联系我。</br>
我的邮箱:925166340@qq.com



