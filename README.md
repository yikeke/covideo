# covideo - 基于 ffmpeg 开发的批量处理命令行工具

> [ffmpeg](https://zh.wikipedia.org/wiki/FFmpeg) 是视频处理最常用的开源软件。它功能强大，用途广泛，大量用于视频网站和商业软件（比如 Youtube 和 iTunes），也是许多音频和视频格式的标准编码/解码实现。——来自[阮一峰](https://www.ruanyifeng.com/blog/2020/01/ffmpeg.html)

covideo 是一个视频处理相关的命令行工具。只需一行命令，便可批量处理视频。

covideo 的实现原理也很简单，就是用 Python 脚本调用 ffmpeg 强大的视频处理功能，并**补足 ffmpeg 命令行本身不提供的批处理能力**。

### covideo 功能概览

目前，covideo 的功能还很初级：

|目前支持的功能|待支持和优化的功能|
|---|---|
|剪切视频|合并视频、加字幕、加背景音乐或旁白，甚至转码视频、转化格式、连续截图等|
|剪切常见格式的视频文件，如 .mp4、.m4v、mov、.avi、.mpeg、.wmv、flv、f4v 等|剪切更多格式的音视频文件|
|支持剪切单个文件，也支持批量剪切给定目录下的所有文件|支持过滤掉某些文件等|
|用户必须给出剪切的起始时间点和结束时间点，来剪切该时间段的视频|支持起始时间点或者结束时间点为空|
|仅支持用户利用终端交互方式配置剪切时间点|支持在配置文件中定义各个文件的剪切时间点，适合大批量的视频文件处理|

### 下载 covideo

> **准备工作：**
>
> - 需要提前安装 **ffmpeg** 和 **pip**。安装 ffmpeg 的小白教程可以参考[韩林涛]。
> - 注意记下 **ffmpeg 可执行文件解压后所在的目录**，后面会用到。

准备工作做好后，打开终端，执行如下命令，下载 covideo 命令行工具：

```
pip install covideo
```

预期输出如下，包含“Successfully installed covideo-xxx”关键词即下载成功：

```
Collecting covideo
  Downloading https://files.pythonhosted.org/packages/62/f2/61045e4654fd5b9ff6ba5cf499e08a78d5f1a509d89334be4dea41455fb3/covideo-0.0.3-py3-none-any.whl
Installing collected packages: covideo
Successfully installed covideo-0.0.3
```

### covideo 选项介绍

下载完成后，就可以使用 covideo 命令行啦！

先在终端执行 `covideo -h`，看看 covideo 目前支持哪些选项 (Options)：

```
yikekedembp:~ coco$ covideo -h
Usage: covideo [options]

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -c CLIP, --clip=CLIP  Use this option to clip videos of many formats;
                        receive one argument that can be a file path or a
                        directory
```

选项说明：

- `--version` 和 `-h`/`--help` 是默认选项，方便用户查看命令行工具的版本和帮助信息。
- `-c`/`--clip` 选项对应的就是剪切视频的功能（目前唯一的功能😅）。用户需要在选项后提供单个视频或文件夹的地址，便可自动批量剪切给定地址下的视频。

### 使用 `covideo -c` 命令剪切视频

接下来看看使用 `covideo -c` 命令来剪切视频，有多么简单、丝滑（尖叫般的体验，为 ffmpeg 打 call！）：

首先，进入前面提到的 **ffmpeg 可执行文件解压后所在的目录**，在终端执行如下命令：

```
cd <替换成你的 ffmpeg 可执行文件解压后的目录地址>
```

这样便可以愉快地调用 ffmpeg 的强大能力来处理视频了！

比如执行 `covideo -c "/Users/coco/Documents/test-videos"` 命令，做的事情是：

- 遍历 `test-videos` 目录下的所有视频
- 用户针对不同视频给出指令，确定剪切的起始时间和结束时间
- 目录下非支持格式的视频，会在最后报出来

大概 1~5 秒内，两个剪出的视频就出现在新生成的 `/Users/coco/Documents/test-videos/clips` 目录了：

401 MB 的第一个视频剪了 10 分钟出来，生成视频为 67.7 MB；130.6 MB 的第二个视频剪了 111 秒出来，生成视频为 10.6 MB。可以看出，剪辑的速度和压缩率还是不错的。
