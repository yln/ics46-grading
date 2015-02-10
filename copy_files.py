import os
import shutil

labdir = '/home/yln/work/ics46-grading/program2/program2submissions/Lab 2'
files = [
    '/home/yln/work/ics46-grading/program2/xtest_queue.sh'
]


def main():
    students = [s for s in sorted(os.listdir(labdir))
                if os.path.isdir(os.path.join(labdir, s))]

    for s in students:
        student_dir = os.path.join(labdir, s)
        for f in files:
            shutil.copy(f, student_dir)


if __name__ == '__main__':
    main()