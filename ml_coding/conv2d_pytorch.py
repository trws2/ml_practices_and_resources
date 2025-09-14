# from https://www.tryexponent.com/courses/ml-engineer/ml-coding/implement-2d-convolutional-filter

import torch
import torch.nn as nn
import numpy as np
def conv2d(input, weight, bias=None, stride=1, padding=0):
    _, in_channels, in_height, in_width = input.shape
    out_channels, _, kernel_height, kernel_width = weight.shape

    print(f"in_channels={in_channels}, in_height={in_height}, in_width={in_width}")
    print(f"out_channels={out_channels}, kernel_height={kernel_height}, kernel_width={kernel_width}")

    conv_layer = nn.Conv2d(in_channels, out_channels, kernel_size=(kernel_height, kernel_width), bias=bias, stride=stride, padding=0)
    conv_layer.weight = nn.Parameter(weight)
    if bias is not None:
        conv_layer.bias = nn.Parameter(bias)

    return conv_layer(input)


# prompt: write a test function and 2 tests to test the above conv2d function 
import unittest 
import numpy as np 
class Conv2dTest(unittest.TestCase): 
    def test_simple(self): 
        input = torch.tensor([[1,-1,0],[-3,0,2],[8,9,1]]).float() 
        # 1 batch, 1 channel 
        input = input.unsqueeze(0).unsqueeze(0) 
        print('input shape: ', input.shape)
        print(input)
        # kernel 
        weight = torch.tensor([[1,-1],[-1,1]]).float() 
        # 1 out_channel, 1 in_channel 
        weight = weight.unsqueeze(0).unsqueeze(0) 
        print('weight shape: ', weight.shape) 
        print(weight)
        output = conv2d(input, weight) 
        print(output.shape) 
        print(output) 
        self.assertEqual(output.shape, (1,1,2,2)) 
        self.assertTrue(torch.equal(output, torch.tensor([[[[ 5., 1.], [ -2., -10.]]]])))


if __name__ == '__main__': 
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

