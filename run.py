import os
import sys
import subprocess

input_file_list = [input_file for input_file in os.listdir(path='./inputs') if '.txt' in input_file]


def make_commands():
    return [
        f'python solve.py < ./inputs/{file_name} > ./answers/answer_{idx + 1}.txt'
        for idx, file_name in enumerate(input_file_list)
    ]


commands = make_commands()
for command in commands:
    subprocess.run(command, shell=True, text=True, stdout=sys.stdout)
