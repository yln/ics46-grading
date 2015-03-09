import os
import subprocess

labdir = '/home/yln/work/ics46-grading/program4/program4submissions/Lab 2'
tests = [
    [
        './test_map --gtest_filter=MapTest.empty',
        './test_map --gtest_filter=MapTest.size',
        './test_map --gtest_filter=MapTest.has_key',
        './test_map --gtest_filter=MapTest.has_value',
        './test_map --gtest_filter=MapTest.put',
        './test_map --gtest_filter=MapTest.put_index',
        './test_map --gtest_filter=MapTest.operator_rel',
        './test_map --gtest_filter=MapTest.operator_stream_insert',
        './test_map --gtest_filter=MapTest.insert_iterator_param',
        './test_map --gtest_filter=MapTest.clear',
        './test_map --gtest_filter=MapTest.erase',
        './test_map --gtest_filter=MapTest.assignment',
        './test_map --gtest_filter=MapTest.iterator_plusplus',
        './test_map --gtest_filter=MapTest.iterator_simple',
        './test_map --gtest_filter=MapTest.iterator_erase',
        './test_map --gtest_filter=MapTest.iterator_exception_concurrent_modification_error',
        './test_map --gtest_filter=MapTest.constructors',
        './test_map --gtest_filter=MapTest.large_scale',
        './test_map --gtest_filter=MapTest.large_scale_speed'
    ],
    [
        './test_set --gtest_filter=SetTest.empty',
        './test_set --gtest_filter=SetTest.size',
        './test_set --gtest_filter=SetTest.contains',
        './test_set --gtest_filter=SetTest.insert',
        './test_set --gtest_filter=SetTest.operator_rel',
        './test_set --gtest_filter=SetTest.operator_stream_insert',
        './test_set --gtest_filter=SetTest.insert_iterator_param',
        './test_set --gtest_filter=SetTest.contains_iterator_param',
        './test_set --gtest_filter=SetTest.clear',
        './test_set --gtest_filter=SetTest.erase',
        './test_set --gtest_filter=SetTest.erase_iterator_param',
        './test_set --gtest_filter=SetTest.retains_iterator_param',
        './test_set --gtest_filter=SetTest.assignment',
        './test_set --gtest_filter=SetTest.iterator_plusplus',
        './test_set --gtest_filter=SetTest.iterator_simple',
        './test_set --gtest_filter=SetTest.iterator_erase',
        './test_set --gtest_filter=SetTest.iterator_exception_concurrent_modification_error',
        './test_set --gtest_filter=SetTest.constructors',
        './test_set --gtest_filter=SetTest.large_scale',
        './test_set --gtest_filter=SetTest.large_scale_speed'
    ]
]

gcc_comand_lines = [
    ('map', 'g++ -std=c++11 -O0 -g3 -I/home/yln/work/ics46/courselib/src -I/home/yln/work/ics46/googletestlib/include -L/home/yln/work/ics46/courselib/Debug -L/home/yln/work/ics46/googletestlib/make -o test_map test_map.cpp -lgtest -lcourselib'),
    ('set', 'g++ -std=c++11 -O0 -g3 -I/home/yln/work/ics46/courselib/src -I/home/yln/work/ics46/googletestlib/include -L/home/yln/work/ics46/courselib/Debug -L/home/yln/work/ics46/googletestlib/make -o test_set test_set.cpp -lgtest -lcourselib'),
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
                    res = subprocess.call(t.split(' '), stdout=fnull, stderr=fnull, timeout=60)
                    # res = subprocess.call(t.split(' '), timeout=60)
                except Exception:
                    pass
                if res == 0:
                    passing += 1
                else:
                    if 'large_scale' in t:
                        large_fail = True
            print("Passed ", passing, "/", len(testset), ' failed large scale' if large_fail else '')
        proc = input('\nMark as processed? [ENTER]: yes, [n]: no: ')
        if not proc.startswith('n'):
            open('PROCESSED', 'w+')


if __name__ == '__main__':
    main()

