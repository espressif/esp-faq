#  the script to detect inconsistent line number between EN and CN documents
#  the command is : python3 detect_inconsistent_line_num.py <directory>

import os
import argparse

ERROR_FILES = {}


def reformat_target_file_by_src_file(target_file_path, src_file_path):
    """
    To check the formatting of a translated file based on the format of a source file
    """
    global ERROR_FILES
    with open(target_file_path, "r", errors='ignore') as tf, open(src_file_path, "r", errors='ignore') as sf:
        tf_line_number = 0
        tf_read_lines = tf.readlines()
        tf_max_len = len(tf_read_lines)

        for src_line in sf:
            if tf_line_number >= tf_max_len:
                ERROR_FILES[target_file_path] = tf_line_number + 1  # if src_file longer than target_file
                return
            tf_line = tf_read_lines[tf_line_number]
            src_line_strip = src_line.strip()
            tf_line_strip = tf_line.strip()

            if (tf_line.startswith('---') ^ src_line.startswith('---')) or (src_line_strip and not tf_line_strip) or (
                    not src_line_strip and tf_line_strip):
                ERROR_FILES[target_file_path] = tf_line_number + 1  # the file has error
                return

            tf_line_number += 1

    with open(src_file_path, "r", errors='ignore') as sf:  # if src_file shorter than target_file
        sf_read_lines = sf.readlines()
        sf_max_len = len(sf_read_lines)
        if tf_max_len != sf_max_len:
            ERROR_FILES[target_file_path] = sf_max_len + 1  # the file has error
            return


def get_out_file_path(file_name):
    _, pure_filename = os.path.split(file_name)
    out_file_path = None

    if '/en/' in file_name:
        out_file_path = file_name.replace('/en/', '/zh_CN/')
    elif '/zh_CN/' in file_name:
        out_file_path = file_name.replace('/zh_CN/', '/en/')
    else:
        print('\033[31m Not found the other file!\033[0m')

    return out_file_path


def get_file_list(directory):
    """
    Get all files in the directory or single file.
    """
    file_list = []
    if os.path.isfile(directory):
        return [directory]
    for path, _, files in os.walk(directory, topdown=True):
        subdir_file_list = [os.path.join(path, file) for file in files]
        file_list.extend(subdir_file_list)
    return file_list


if __name__ == "__main__":
    """
    This script will read all the files in the input directory
    and translate text stored in each file.11
    """
    CMD_EPILOG = 'Example of use: sk-... (OPENAI_API_KEY)'
    parser = argparse.ArgumentParser(epilog=CMD_EPILOG, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('filename', action='store', type=str,
                        help='specify file or tcf(all files in translate_config.yml)')
    args = parser.parse_args()

    file_list = get_file_list(args.filename)

    for file in file_list:
        out_file_path = get_out_file_path(file)
        if out_file_path:
            reformat_target_file_by_src_file(out_file_path, file)

    if ERROR_FILES:
        print(
            '\033[31m These files have inconsistent line numbers between Chinese and English (begin line num):\033[0m')
    for error_file in ERROR_FILES:
        print(f'\033[31m {error_file}  {ERROR_FILES[error_file]}\033[0m')