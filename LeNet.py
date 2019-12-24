"""
LeNet 使用 paddlepaddle 1.5.2 进行实现
"""

import paddle.fluid as fluid



def LeNet5():
    # conv_1 = fluid.layers.conv2d()
    fluid.nets.img_conv_group()
    fluid.nets.simple_img_conv_pool()