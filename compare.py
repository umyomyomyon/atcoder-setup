import os


class NotEofLfException(Exception):
    message = None

    def __init__(self, filepath):
        self.message = f'[ファイルの最後が改行ではありません]: {filepath}\n'


class WrongAnswerException(Exception):
    message = None

    def __init__(self, filepath: str, ans_line: str, output_line: str):
        self.message = f'[WA]: {filepath}\nans: {ans_line}\nexpect: {output_line}'


def read_file(path: str):
    with open(path, mode='r') as f:
        data = f.readlines()
        return data


def compare_line(answer_line: str, output_line: str):
    if answer_line.strip() == output_line.strip():
        return
    raise


def compare_lines(answer_filepath: str, output_filepath: str):
    answer_lines = read_file(answer_filepath)
    output_lines = read_file(output_filepath)
    for idx, answer_line in enumerate(answer_lines):
        try:
            compare_line(answer_line, output_lines[idx])
        except IndexError:
            raise WrongAnswerException(answer_filepath, answer_line, '')
        except:
            raise WrongAnswerException(answer_filepath, answer_line, output_lines[idx])


def is_eof_lf(answer_file_path):
    lines = read_file(answer_file_path)
    if lines[-1][-1] != '\n':
        raise NotEofLfException(answer_file_path)


def validate_answer(ans_filepath: str, output_filepath: str):
    is_eof_lf(ans_filepath)
    compare_lines(ans_filepath, output_filepath)


def main():
    ans_file_list = sorted([input_file for input_file in os.listdir(path='./answers') if '.txt' in input_file])
    for filename in ans_file_list:
        ans_filepath = f'./answers/{filename}'
        output_filepath = f'./outputs/{filename}'
        try:
            validate_answer(ans_filepath, output_filepath)
            print(f'[AC]: {filename}')
        except (NotEofLfException, WrongAnswerException) as err:
            print(err.message)


if __name__ == '__main__':
    main()
