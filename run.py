import os
import sys
import subprocess

input_flie_list = sorted([input_file for input_file in os.listdir(path='./inputs') if '.txt' in input_file])

def make_commands(input_file_list):
    return [
        f'python3 solve.py < ./inputs/{file_name} > ./answers/{idx + 1}.txt'
        for idx, file_name in enumerate(input_file_list)
    ]


commands = make_commands(input_flie_list)
for command in commands:
    subprocess.run(command, shell=True, text=True, stdout=sys.stdout)
