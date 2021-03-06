import subprocess


def make_input_file(filename, text):
    file = open(f'{filename}.in', 'w')
    file.write(text)
    file.close()


def start_sfbox(filename):
    with open(f'{filename}.out', 'w') as file:
        subprocess.run(args=["./sfbox", f"{filename}.in"], text=True, stdout=file, check=True)
