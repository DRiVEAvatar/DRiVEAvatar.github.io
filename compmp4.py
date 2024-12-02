import os
import subprocess

def compress_video(input_file, output_file):
    # 获取视频文件的宽度和高度
    command = [
        'ffmpeg',  # 确保 FFmpeg 路径正确（如果你已添加到系统 PATH 中，则可以直接用 'ffmpeg'）
        '-i', input_file,  # 输入文件
        '-vcodec', 'libx264',  # 设置视频编解码器
        '-crf', '30',  # 增加压缩比，质量可能会更低，文件更小
        '-preset', 'slower',  # 更高效的压缩
        '-acodec', 'aac',  # 设置音频编解码器
        '-b:a', '128k',  # 设置音频比特率为 128k
        '-y',  # 覆盖输出文件
        output_file  # 输出文件
    ]
    
    # 输出调试信息，查看最终的命令
    print("Running command: ", " ".join(command))
    
    # 执行命令，并捕获错误信息
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # 输出执行结果的错误信息
    print("Command output:", result.stdout.decode())  # 输出标准输出
    if result.stderr:
        print("Error:", result.stderr.decode())  # 输出错误信息
    else:
        print(f"Video processed and saved as: {output_file}")

def compress_directory(directory):
    # 遍历目标目录及其子目录
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.mp4'):  # 只处理 MP4 格式的视频文件
                input_file = os.path.join(root, file)
                # 为输出文件添加 'comp_' 前缀
                output_file = os.path.join(root, f"comp_{file}")
                print(f"Compressing: {input_file}")
                compress_video(input_file, output_file)
                
                # 文件压缩完成后，删除原始文件并重命名压缩后的文件
                if os.path.exists(output_file):
                    # 删除原始文件
                    os.remove(input_file)
                    print(f"Original file removed: {input_file}")
                    # 将压缩后的文件重命名为原始文件名
                    os.rename(output_file, input_file)
                    print(f"Renamed compressed file: {output_file} to {input_file}")

if __name__ == "__main__":
    target_directory = "/Users/yisuanwang/Developer/DRiVEAvatar.github.io/static/images/Tpose_anime_inputs"  # 替换为目标目录路径
    compress_directory(target_directory)
