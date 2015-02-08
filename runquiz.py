import os
import shutil
from subprocess import call

# Configure the following things before you start grading!
interactive = True
# Where are the submissions located?
labdir = '/home/yln/work/ics46-grading/program2/program2submissions/Lab 2'
# On Windows, also add the binary libraries here
template_files = [
    '/home/yln/work/ics46-grading/program2/program2/src/test_priority_queue.cpp',
    '/home/yln/work/ics46-grading/program2/program2/src/test_queue.cpp',
    '/home/yln/work/ics46-grading/program2/program2/src/test_set.cpp',
    '/home/yln/work/ics46-grading/program2/program2/loadpq.txt',
    '/home/yln/work/ics46-grading/program2/program2/loadq.txt',
    '/home/yln/work/ics46-grading/program2/program2/loadset.txt'
]
# compilation command (see what Eclipse does to get an idea)
executables = [
    'test_queue',
    'test_priority_queue',
    'test_set'
]
gcc_comand_lines = [
    'g++ -std=c++11 -O0 -g3 -I/home/yln/work/ics46/courselib/src -I/home/yln/work/ics46/googletestlib/include -L/home/yln/work/ics46/courselib/Debug -L/home/yln/work/ics46/googletestlib/make -o test_queue test_queue.cpp -lgtest -lcourselib',
    'g++ -std=c++11 -O0 -g3 -I/home/yln/work/ics46/courselib/src -I/home/yln/work/ics46/googletestlib/include -L/home/yln/work/ics46/courselib/Debug -L/home/yln/work/ics46/googletestlib/make -o test_priority_queue test_priority_queue.cpp -lgtest -lcourselib',
    'g++ -std=c++11 -O0 -g3 -I/home/yln/work/ics46/courselib/src -I/home/yln/work/ics46/googletestlib/include -L/home/yln/work/ics46/courselib/Debug -L/home/yln/work/ics46/googletestlib/make -o test_set test_set.cpp -lgtest -lcourselib'
]


def copy_template_files(submission_dir):
    for f in template_files:
        shutil.copy(f, submission_dir)


def compile_program(submission_dir):
    binaries = [os.path.join(submission_dir, exe) for exe in executables]
    for binary in binaries:
        if os.path.isfile(binary):
            os.remove(binary)
    # set working directory
    os.chdir(submission_dir)
    for command in gcc_comand_lines:
        retval = call(command.split(' '))
        if retval != 0:
            return 1
    return 0


def run(submission_dir):
    # set working directory
    os.chdir(submission_dir)
    return os.system("./reachable  < input1  > output1") \
        or os.system("./reachable  < input2  > output2") \
        or os.system("./reachable  < input3  > output3")


def diff(submission_dir):
    # set working directory
    os.chdir(submission_dir)
    os.system("git diff output1 expected_output1")
    os.system("git diff output2 expected_output2")
    os.system("git diff output3 expected_output3")


def test(submission_dir):
    # set working directory
    os.chdir(submission_dir)
    retval = 0
    for exe in executables:
        retval += call("./" + exe)
    return retval


def view(submission_dir):
    # set working directory
    os.chdir(submission_dir)
    # os.system("sed -n '/add_ordered_r/,$p' q2solution.hpp")
    os.system("grep -B 12 --color=always '\sdelete\s' linked_queue.hpp")
    os.system("subl linked_queue.hpp &")



def run_quiz(name, submission_dir):
    print('\n\n\n\n\n\nAbout to run quiz for: ' + name)
    if interactive:
        asw = input('Press [ENTER] to continue or [s] to skip student: ')
        if asw.startswith('s'):
            print('Skipped!')
            return 0
    copy_template_files(submission_dir)
    print('Copied src files')
    if compile_program(submission_dir) != 0:
        print('Compilation failed!')
        return 1
    print('Compiled\n')
    # if run(submission_dir) != 0:
    #     print('error while running')
    #     return 1
    # diff(submission_dir)

    if test(submission_dir) != 0:
        print('Testing failed!\n')
        view(submission_dir)
        return 1
    print('\n')
    view(submission_dir)

    print('\nFinished for: ' + name)
    proc = input('Mark as processed? [ENTER]: yes, [n]: no: ')
    if not proc.startswith('n'):
        open('PROCESSED', 'w+')
    return 0


def main():
    submissions = [(name, os.path.join(labdir, name)) for name in sorted(os.listdir(labdir))
                   if os.path.isdir(os.path.join(labdir, name)) and not os.path.isfile(os.path.join(labdir, name, "PROCESSED"))]

    errors = 0
    for (n, d) in submissions:
        errors += run_quiz(n, d)

    print('\nDone with all submissions!')
    print('ERRORS #: ', errors)


if __name__ == '__main__':
    main()
