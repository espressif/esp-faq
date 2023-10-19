import os
import sys

def find_rst_files(folder_path):
    rst_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".rst"):
                rst_files.append(os.path.relpath(os.path.join(root, file), reference_path))
    return rst_files

# 获取命令行参数
if len(sys.argv) != 3:
    print("请提供文件夹路径和参考文件路径作为命令行参数。")
    sys.exit(1)

folder_path = sys.argv[1]
reference_path = sys.argv[2]

# 验证输入路径是否存在
if not os.path.exists(folder_path):
    print("指定的文件夹路径不存在。")
    sys.exit(1)
if not os.path.exists(reference_path):
    print("指定的参考文件路径不存在。")
    sys.exit(1)

# 查找所有 rst 文件的相对路径并按文件名首字母排序
rst_files = find_rst_files(folder_path)
rst_files = sorted(rst_files)

# 打印输出
if rst_files:
    print("以下是所有的 .rst 文件的相对路径（按文件名首字母排序）：")
    for rst_file in rst_files:
        print(rst_file)
else:
    print("未找到任何 .rst 文件。")