import os
import subprocess

labdir = '/home/yln/work/ics46-grading/program2/program2submissions/Lab 2'
tests = [
    [
        './test_queue --gtest_filter=QueueTest.empty',
        './test_queue --gtest_filter=QueueTest.size',
        './test_queue --gtest_filter=QueueTest.peek',
        './test_queue --gtest_filter=QueueTest.enqueue',
        './test_queue --gtest_filter=QueueTest.operator_eq_ne',
        './test_queue --gtest_filter=QueueTest.operator_stream_insert',
        './test_queue --gtest_filter=QueueTest.enqueue_iterator_param',
        './test_queue --gtest_filter=QueueTest.clear',
        './test_queue --gtest_filter=QueueTest.dequeue1',
        './test_queue --gtest_filter=QueueTest.dequeue2',
        './test_queue --gtest_filter=QueueTest.assignment',
        './test_queue --gtest_filter=QueueTest.iterator_plusplus',
        './test_queue --gtest_filter=QueueTest.iterator_simple',
        './test_queue --gtest_filter=QueueTest.iterator_erase',
        './test_queue --gtest_filter=QueueTest.iterator_exception_concurrent_modification_error',
        './test_queue --gtest_filter=QueueTest.constructors',
        './test_queue --gtest_filter=QueueTest.large_scale',
        './test_queue --gtest_filter=QueueTest.large_scale_speed'
    ],
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
        './test_priority_queue --gtest_filter=PriorityQueueTest.iterator_plusplus',
        './test_priority_queue --gtest_filter=PriorityQueueTest.iterator_simple',
        './test_priority_queue --gtest_filter=PriorityQueueTest.iterator_erase',
        './test_priority_queue --gtest_filter=PriorityQueueTest.iterator_exception_concurrent_modification_error',
        './test_priority_queue --gtest_filter=PriorityQueueTest.constructors',
        './test_priority_queue --gtest_filter=PriorityQueueTest.large_scale',
        './test_priority_queue --gtest_filter=PriorityQueueTest.large_scale_speed'
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
    ('queue', 'g++ -std=c++11 -O0 -g3 -I/home/yln/work/ics46/courselib/src -I/home/yln/work/ics46/googletestlib/include -L/home/yln/work/ics46/courselib/Debug -L/home/yln/work/ics46/googletestlib/make -o test_queue test_queue.cpp -lgtest -lcourselib'),
    ('priority q', 'g++ -std=c++11 -O0 -g3 -I/home/yln/work/ics46/courselib/src -I/home/yln/work/ics46/googletestlib/include -L/home/yln/work/ics46/courselib/Debug -L/home/yln/work/ics46/googletestlib/make -o test_priority_queue test_priority_queue.cpp -lgtest -lcourselib'),
    ('set', 'g++ -std=c++11 -O0 -g3 -I/home/yln/work/ics46/courselib/src -I/home/yln/work/ics46/googletestlib/include -L/home/yln/work/ics46/courselib/Debug -L/home/yln/work/ics46/googletestlib/make -o test_set test_set.cpp -lgtest -lcourselib')
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
        large_fail = False
        for testset in tests:
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
