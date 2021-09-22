import os

def read_OBI_files(folder):
    current_dir = os.path.abspath(os.getcwd())
    for subdir, dirs, files in os.walk(current_dir + folder):
        for file in files:
            filepath = subdir + os.sep + file
            if filepath.endswith(".in"):
                file_input = subdir + os.sep + file
                file_output = file.split(".")[0] + ".sol"
                file_output = subdir + os.sep + file_output

                f_pointer = open(file_input, "r")
                input_lines = [line.strip() for line in f_pointer]
                f_pointer.close()

                f_pointer = open(file_output, "r")
                output_lines = [line.strip() for line in f_pointer]
                f_pointer.close()

                yield input_lines, output_lines, file_input, file_output
