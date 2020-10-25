#!/usr/bin/env python3
# encoding=utf-8

import re
import sys
import os
from optparse import OptionParser

def clip_path(path):
    supported_video_formats = (".mp4", ".avi", ".mpeg", ".wmv", ".m4v", "mov", "flv", "f4v") # 常见的视频文件格式还有：asf、rmvb、rm、3gp、vob等等。(https://ffmpeg.org/ffmpeg-all.html#toc-mov_002fmp4_002f3gp)
    if not (path.endswith(supported_video_formats)): # or .avi, .mpeg, whatever.
        err = "ERROR: " + path + " 格式不支持处理。"
        return err
    else:
        print("正在剪辑 " + path + "...")
        start_time = input('请输入剪切起始时间（按回车确认）：')
        stop_time = input('请输入剪切结束时间（按回车确认）：')
        file_dir, filename = os.path.split(path)     # 分割文件名与目录
        name, suffix = os.path.splitext(filename)    # 分离文件名与扩展名
        clips_path = os.path.join(file_dir,'clips')
        if not os.path.exists(clips_path):
            os.makedirs(clips_path)
        output_file = os.path.join(clips_path,name) + '-' + start_time + '-' + stop_time + suffix
        if os.system("ffmpeg -ss {2} -to {3} -accurate_seek -i {0} -c copy -avoid_negative_ts 1 {1}".format(path,output_file,start_time,stop_time)) == 0:
            print(path + " 视频剪切成功！请稍等片刻，剪切好的视频会存放在 " + clips_path + "。")
            return 0
        else:
            exit("ERROR: 视频剪切失败！请确保 ffmpeg 已下载，且你是在包含 ffmpeg 可执行程序的目录下执行 covideo 命令。")

def clip_dir(directory):
    err = []
    for root, dirs, files in os.walk(directory, topdown=True):
        # 忽略 clips 文件夹
        dirs[:] = [d for d in dirs if d not in ['clips']]
        for name in files:
            print(files)
            errors = clip_path(os.path.join(root, name))
            if errors:
                err.append(errors)
    print('\n'.join(err))

def check_requirements():
    if os.system("ffmpeg -formats >/dev/null 2>&1") == 0: # silence the outputs
        print("You are all set! Initiating covideo...")
    else:
        exit("注意：使用 covideo 需要先安装 ffmpeg 可执行文件，请前往 https://www.ffmpeg.org/ 下载安装包。\n安装完毕后，执行以下命令 `cd <你的 ffmpeg 可执行文件解压后的目录地址>`，便可使用 covideo 了。")

def process(opt):
    # clip, merge = opt.clip, opt.merge
    clip = opt.clip
    check_requirements()
    if clip:
        # clip = clip.strip() # 去掉首尾空格
        if os.path.isfile(clip):
            print("下面输入的时间支持两种格式：")
            print("1. 纯数字格式，以秒为单位。如输入 60 表示视频的第 60 秒；")
            print("2. 时:分:秒格式。如输入 00:03:40 表示视频的 3 分 40 秒。\n")
            clip_path(clip)

        elif os.path.isdir(clip):
            print("下面输入的时间格式支持两种格式：")
            print("1. 纯数字格式，以秒为单位。如输入 60 表示视频的第 60 秒；")
            print("2. 时:分:秒格式。如输入 00:03:40 表示视频的 3 分 40 秒。\n")
            clip_dir(clip)
        else:
            print('ERROR: 输入视频读取源地址有误，请重新输入。读取源地址需要是一个文件路径或者目录。')
            exit(1)
    # elif merge:
    #     if os.path.isfile(merge):
    #     elif os.path.isdir(merge):
    #     else:
    #         print('Please specify a file path or a directory path as the argument.')
    else:
        print('请选定一个选项，执行 `covideo -h` 列出所有选项。')

def exe_main():
    parser = OptionParser(version="%prog 0.0.3")
    parser.set_defaults(verbose=True)
    parser.add_option("-c", "--clip", dest="clip", type="string",
                      help="Use this option to clip videos of many formats; receive one argument that can be a file path or a directory", metavar="CLIP")
    # parser.add_option("-m", "--merge", dest="merge", type="string",
    #                   help="Merge mp4 videos", metavar="MERGE")
    options, args = parser.parse_args()
    process(options)