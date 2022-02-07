import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('contest_name', type=str, help='ex.) ABC or abc or ARC or arc ...')
parser.add_argument('contest_number', type=int, help='number of contest.')
parser.add_argument('problem_rank', type=str, help='rank of problem in contest.')
parser.add_argument('input_files', type=int, help='number of input files.')


def make_dirs(base_dir: str):
    command = f'mkdir -p {base_dir}/inputs && mkdir {base_dir}/outputs && mkdir {base_dir}/answers'
    subprocess.run(command, shell=True, text=True)


def make_files(base_dir: str, input_files: int):
    subprocess.run(f'cp ./run.py {base_dir}/run.py && touch {base_dir}/solve.py', shell=True, text=True)

    inputs_dir = f'{base_dir}/inputs'
    outputs_dir = f'{base_dir}/outputs'
    for i in range(input_files):
        command = f'touch {inputs_dir}/{i + 1}.txt && touch {outputs_dir}/{i + 1}.txt'
        subprocess.run(command, shell=True, text=True)


def main(contest_name: str, contest_number: int, problem_rank: str, input_files: int):
    base_dir = f'./{contest_name}/{str(contest_number)}/{problem_rank}'
    make_dirs(base_dir)
    make_files(base_dir, input_files)


if __name__ == '__main__':
    args = parser.parse_args()
    main(args.contest_name.upper(), args.contest_number, args.problem_rank.upper(), args.input_files)
