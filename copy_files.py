import os
import shutil

labdir = '/home/yln/work/ics46-grading/program5/program5submissions/Lab 2'
files = [
    '/home/yln/work/ics46-grading/program5/test/graph_project/standard.txt',
    '/home/yln/work/ics46-grading/program5/test/graph_project/src/hash_map.hpp',
    '/home/yln/work/ics46-grading/program5/test/graph_project/src/hash_set.hpp',
    '/home/yln/work/ics46-grading/program5/test/graph_project/src/heap_priority_queue.hpp',
    '/home/yln/work/ics46-grading/program5/test/graph_project/src/test_graph.cpp',

    '/home/yln/work/ics46-grading/program5/test/dijkstra_project/flightdist.txt',
    '/home/yln/work/ics46-grading/program5/test/dijkstra_project/src/rich_dijkstra.hpp',
    '/home/yln/work/ics46-grading/program5/test/dijkstra_project/src/test_dijkstra.cpp'
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