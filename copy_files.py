import os
import shutil

labdir = '/home/yln/work/ics46-grading/program4/program4submissions/Lab 2'
files = [
    '/home/yln/work/ics46-grading/program4/program4solution/load.txt',
    '/home/yln/work/ics46-grading/program4/program4solution/loadmap.txt',
    '/home/yln/work/ics46-grading/program4/program4solution/src/test_map.cpp',
    '/home/yln/work/ics46-grading/program4/program4solution/src/test_set.cpp',
    '/home/yln/work/ics46-grading/program4/program4solution/src/set_from_map.hpp'
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