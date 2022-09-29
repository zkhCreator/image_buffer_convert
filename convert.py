from datetime import datetime
import os
from PIL import Image
import numpy as np
import argparse

parser =  argparse.ArgumentParser(description="将 imageBuffer 图片转成本地图片")
parser.add_argument('filePath', help="文件路径")
parser.add_argument('imageWidth', help="图片宽度", default=100)
parser.add_argument('imageHeight', help="图片高度", default=100)

def decode_image(filepath, height=100, width=100):
    # filename
    file_name = os.path.split(filepath)[1]
    
    # get buffer
    _buffer = open(filepath, 'rb').read()
    # decode image
    format = np.frombuffer(_buffer, dtype=np.uint8)
    res = format.reshape(height, width, 4)
    _image = Image.fromarray(res).convert('RGB')
    export_filename = file_name + str(datetime.now()) + ".png"
    _image.save(export_filename)

if __name__ == '__main__':
    args = parser.parse_args()
    filepath = args.filePath
    imageW = int(args.imageWidth)
    imageH = int(args.imageHeight)
    
    decode_image(filepath=filepath, width=imageW, height=imageH)
    