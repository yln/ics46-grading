import os
import subprocess

labdir = '/home/yln/work/ics46-grading/program5/program5submissions/Lab 2'
tests = [
    [
        './test_graph --gtest_filter=MapTest.empty',
        './test_graph --gtest_filter=MapTest.size',
        './test_graph --gtest_filter=MapTest.add_node',
        './test_graph --gtest_filter=MapTest.add_edge1',
        './test_graph --gtest_filter=MapTest.add_edge2',
        './test_graph --gtest_filter=MapTest.remove_edge',
        './test_graph --gtest_filter=MapTest.remove_node',
        './test_graph --gtest_filter=MapTest.relations',
        './test_graph --gtest_filter=MapTest.load',
        './test_graph --gtest_filter=MapTest.store'
    ],
    [
        './test_dijkstra --gtest_filter=MapTest.flightdist'
    ]
]

gcc_comand_lines = [
    ('graph', 'g++ -std=c++11 -O0 -g3 -I/home/yln/work/ics46/courselib/src -I/home/yln/work/ics46/googletestlib/include -L/home/yln/work/ics46/courselib/Debug -L/home/yln/work/ics46/googletestlib/make -o test_graph test_graph.cpp -lgtest -lcourselib'),
    ('dijkstra', 'g++ -std=c++11 -O0 -g3 -I/home/yln/work/ics46/courselib/src -I/home/yln/work/ics46/googletestlib/include -L/home/yln/work/ics46/courselib/Debug -L/home/yln/work/ics46/googletestlib/make -o test_dijkstra test_dijkstra.cpp -lgtest -lcourselib')
]


def main():
    students = [s for s in sorted(os.listdir(labdir))
                if os.path.isdir(os.path.join(labdir, s)) and not os.path.isfile(os.path.join(labdir, s, "PROCESSED"))]

    fnull = open(os.devnull, 'w')

    for s in students:
        print("\n\n\nRunning tests for student: ", s)
        student_dir = os.path.join(labdir, s)
        # change working dir
        os.chdir(student_dir)
        # compile
        for cc in gcc_comand_lines:
            retval = subprocess.call(cc[1].split(' '), stdout=fnull, stderr=fnull)
            # retval = subprocess.call(cc[1].split(' '))
            if retval != 0:
                print('Could not compile', cc[0])
        # execute tests
        for testset in tests:
            large_fail = False
            passing = 0
            for t in testset:
                res = -1
                try:
                    res = subprocess.call(t.split(' '), stdout=fnull, timeout=60)
                    # res = subprocess.call(t.split(' '), stdout=fnull, stderr=fnull, timeout=60)
                    # res = subprocess.call(t.split(' '), timeout=60)
                except Exception:
                    pass
                if res == 0:
                    passing += 1
                else:
                    if 'large_scale' in t or 'remove_node' in t:
                        large_fail = True
            print("Passed ", passing, "/", len(testset), ' failed large scale' if large_fail else '')
        proc = input('\nMark as processed? [ENTER]: yes, [n]: no: ')
        if not proc.startswith('n'):
            open('PROCESSED', 'w+')


if __name__ == '__main__':
    main()

