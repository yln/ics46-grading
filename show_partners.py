import os
from subprocess import call

labdir = '/home/yln/work/ics46-grading/program2/program2submissions/Lab 2'
command = "head -5 linked_queue.hpp"


def main():
    students = [s for s in sorted(os.listdir(labdir))
                if os.path.isdir(os.path.join(labdir, s))]

    for s in students:
        print("\n\n\n\nStudent: ", s, "\n")

        # change working dir
        studendir = os.path.join(labdir, s)
        os.chdir(studendir)

        # show file header
        call(command.split(' '))
        input('\nPress any key to continue!\n')


if __name__ == '__main__':
    main()