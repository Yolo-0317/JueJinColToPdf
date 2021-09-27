### 项目来源：[【玩转掘金】掘金专栏文章正生成pdf文档 ｜Python 主题月](https://juejin.cn/post/6990140519342932004)，在原文代码基础上，修改出适用于unix环境的脚本，并结合Node服务，提供API接口，https://github.com/Yolo-0317/YoloNodeService，最终会提供可视化的交互界面

## 功能介绍
把掘金**某篇文章**内容下载到本地，并生成pdf文件。

生成的pdf功能支持：
1. 大纲目录
2. 代码高亮
3. 文章图片
4. 链接点击

其他：
1. 支持自定义pdf显示的样式

## 预览
[我的掘金前端周栏.pdf](./pdfs/我的掘金前端周栏.pdf)     
[前端基础进阶.pdf](./pdfs/前端基础进阶.pdf)     

## 思路

1. 通过专栏ID获取专栏信息，文章列表和文章详情
2. 下载JSON格式的数据到本地
3. 把markdown语法的文章内容转为html格式，并生成html文件
4. 借助`wkhtmltopdf.exe`生成pdf文件



## 开发环境
原文开发文件是windows 10，将main.py进行修改，改为unix开发
1.  linux/macos
2.  Python 3.9.1

## 使用

请注意运行环境 windows以及Python版本

1. 下载 [wkhtmltopdf](https://wkhtmltopdf.org/), 并配置环境变量
2. 下载本地项目，进入项目文件
3. 执行命令 
acid: 文章ID
type: 默认为专栏`c`，如果是文章请输入`a`
```python   
# python main.py 6989422484722286600 a  例子
python main.py [acid] [type]

```

## 已知问题
1. 中文路径问题
    那就使用英文路径吧，文件名是中文没问题


## 预览
项目`pdfs\前端基础进阶.pdf`是已经生成好的pdf文件。


### 参考引用

[python+markdown+Pygments高亮代码](https://blog.csdn.net/JONE_WUQINGJIANG/article/details/100511760)
