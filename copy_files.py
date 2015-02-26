import os
import shutil

labdir = '/home/yln/work/ics46-grading/program3/program3submissions/Lab 2'
files = [
    '/home/yln/work/ics46-grading/program3/program3/load.txt',
    '/home/yln/work/ics46-grading/program3/program3/loadmap.txt',
    '/home/yln/work/ics46-grading/program3/program3/src/test_priority_queue.cpp',
    '/home/yln/work/ics46-grading/program3/program3/src/test_map.cpp'
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