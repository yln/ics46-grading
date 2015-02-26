import os
import subprocess

labdir = '/home/yln/work/ics46-grading/program3/program3submissions/Lab 2'
tests = [
    [
        './test_priority_queue --gtest_filter=PriorityQueueTest.empty',
        './test_priority_queue --gtest_filter=PriorityQueueTest.size',
        './test_priority_queue --gtest_filter=PriorityQueueTest.peek',
        './test_priority_queue --gtest_filter=PriorityQueueTest.enqueue',
        './test_priority_queue --gtest_filter=PriorityQueueTest.operator_eq_ne',
        './test_priority_queue --gtest_filter=PriorityQueueTest.operator_stream_insert',
        './test_priority_queue --gtest_filter=PriorityQueueTest.enqueue_iterator_param',
        './test_priority_queue --gtest_filter=PriorityQueueTest.clear',
        './test_priority_queue --gtest_filter=PriorityQueueTest.dequeue1',
        './test_priority_queue --gtest_filter=PriorityQueueTest.dequeue2',
        './test_priority_queue --gtest_filter=PriorityQueueTest.assignment',
        './test_priority_queue --gtest_filter=PriorityQueueTest.iterator_simple',
        './test_priority_queue --gtest_filter=PriorityQueueTest.iterator_erase',
        './test_priority_queue --gtest_filter=PriorityQueueTest.iterator_erase_heap_special_case',
        './test_priority_queue --gtest_filter=PriorityQueueTest.iterator_exception_concurrent_modification_error',
        './test_priority_queue --gtest_filter=PriorityQueueTest.constructors',
        './test_priority_queue --gtest_filter=PriorityQueueTest.large_scale',
        './test_priority_queue --gtest_filter=PriorityQueueTest.large_scale_speed1',
        './test_priority_queue --gtest_filter=PriorityQueueTest.large_scale_speed2',
    ],
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
    ]
]

gcc_comand_lines = [
    ('heap', 'g++ -std=c++11 -O0 -g3 -I/home/yln/work/ics46/courselib/src -I/home/yln/work/ics46/googletestlib/include -L/home/yln/work/ics46/courselib/Debug -L/home/yln/work/ics46/googletestlib/make -o test_priority_queue test_priority_queue.cpp -lgtest -lcourselib'),
    ('hashmap', 'g++ -std=c++11 -O0 -g3 -I/home/yln/work/ics46/courselib/src -I/home/yln/work/ics46/googletestlib/include -L/home/yln/work/ics46/courselib/Debug -L/home/yln/work/ics46/googletestlib/make -o test_map test_map.cpp -lgtest -lcourselib'),
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
            if retval != 0:
                print('Could not compile', cc[0])
        # execute tests
        for testset in tests:
            large_fail = False
            passing = 0
            for t in testset:
                res = -1
                try:
                    res = subprocess.call(t.split(' '), stdout=fnull, stderr=fnull, timeout=15)
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
