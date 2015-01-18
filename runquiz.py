import os
import shutil
from subprocess import call

# Configure the following things before you start grading!
interactive = True
# Where are the submissions located?
labdir = '/home/yln/work/ics46-grading/quiz1/quiz1submissions/Lab 2/'
# On Windows, also add the binary libraries here
template_files = ['/home/yln/work/ics46-grading/quiz1/q1helper/src/test_quiz1.cpp']
# compilation command (see what Eclipse does to get an idea)
executable = 'test_quiz1'
gcc_comand_line = 'g++ -std=c++11 -O0 -g3 -I/home/yln/work/ics46/courselib/src -I/home/yln/work/ics46/googletestlib/include -L/home/yln/work/ics46/courselib/Debug -L/home/yln/work/ics46/googletestlib/make -o test_quiz1 test_quiz1.cpp -lgtest -lcourselib'


def copy_template_files(submission_dir):
    for f in template_files:
        shutil.copy(f, submission_dir)


def compile_program(submission_dir):
    binary = os.path.join(submission_dir, executable)
    if os.path.isfile(binary):
        os.remove(binary)
    # set working directory
    os.chdir(submission_dir)
    return call(gcc_comand_line.split(' '))

def test(submission_dir):
    # set working directory
    os.chdir(submission_dir)
    return call("./" + executable)


def run_quiz(name, submission_dir):
    print('\nAbout to run quiz for: ' + name)
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
    print('Compiled')
    if test(submission_dir) != 0:
        print('Testing (ITSELF) failed!')
        return 1
    return 0


def main():
    submissions = [(name, os.path.join(labdir, name)) for name in sorted(os.listdir(labdir))
                   if os.path.isdir(os.path.join(labdir, name))]

    errors = 0
    for (n, d) in submissions:
        errors += run_quiz(n, d)

    print('Done with all submissions!')
    print('ERRORS #: ', errors)


if __name__ == '__main__':
    main()
