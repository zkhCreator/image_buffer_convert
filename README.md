# buffer 图片转换器

由于 buffer 图片本身以二进制存储，所以需要进行转换后才能展示。

Buffer 的格式为 `[r1,g1,b1,a1,r2,g2,b2,a2,.....]`
所以图片的大小为 width * height * 4,每 4 为为 1 个像素

## install

`pip install -r requirements.txt`

# usage

`python convert.py ./test 260 260`

# 其他

可以通过 `python convert.py --help` 来查看变量含义