#!/usr/bin/env python3
# https://stackoverflow.com/questions/2837214/python-popen-command-wait-until-the-command-is-finished/2837319#2837319
import pprint
import subprocess
import webbrowser
import os
import time


def ex_():
    # p = subprocess.Popen("sleep 10", shell=True)
    # p = subprocess.Popen(["sleep", "10"])
    # p = subprocess.Popen('xreader', executable='/usr/bin/xreader')
    p = subprocess.Popen(
        'FoxitReader',
        executable='/usr/bin/FoxitReader',
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    # Wait until process terminates
    i = 0
    while p.poll() is None:
        time.sleep(1)
        print(i, end=' ')
        i += 1

    # It's done
    print("\nProcess ended, ret code:", p.returncode)


def ex_11():
    p1 = subprocess.Popen('xreader', executable='/usr/bin/xreader')
    p1.communicate()
    # try:
    #     _, _= p1.communicate()
    # except subprocess.TimeoutExpired:
    #     p1.kill()

    # pprint.pprint(p1.__dict__)
    print(120 * '#')
    p2 = subprocess.Popen('FoxitReader', executable='/usr/bin/FoxitReader', stdout=subprocess.DEVNULL,
                          stderr=subprocess.DEVNULL)
    p2.wait()
    pprint.pprint(p2.__dict__)


def ex_10():
    p1 = subprocess.run(["ls", "-l"])
    pprint.pprint(p1.__dict__)
    p2 = subprocess.run("ls -l", capture_output=True, shell=True)
    pprint.pprint(p2.__dict__)


def ex_9():
    p1 = subprocess.run('ls tmp', capture_output=True, shell=True)
    pprint.pprint(p1.__dict__)
    p2 = subprocess.run('touch tmp2 | ls tmp2', capture_output=True, shell=True)
    pprint.pprint(p2.__dict__)
    print('all processed finished')


def ex_8():
    p1 = subprocess.Popen('touch tmp | ls tmp; rm tmp', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    pprint.pprint(p1.__dict__)
    print('all processed finished')


def ex_7():
    for _ in range(10):
        webbrowser.get('firefox').open_new_tab('https://www.linuxmint.com')
    print('all processed finished')


def ex_6():
    p = [subprocess.Popen('firefox', shell=True) for _ in range(10)]
    [pprint.pprint(pp.__dict__) for pp in p]
    print('all processed finished')


def ex_5():
    p1 = subprocess.run('firefox', shell=True)  # wait until return
    pprint.pprint(p1.__dict__)
    print('all processed finished')


def ex_4():
    p1 = subprocess.run('sleep 10', shell=True)
    pprint.pprint(p1.__dict__)
    print('all processed finished')


def ex_3():
    p1 = subprocess.Popen('sleep 10', stdout=subprocess.PIPE, shell=True)
    pprint.pprint(f"{p1.__dict__['pid']}: return code: {p1.__dict__['returncode']}")  # does not wait to process next
    w = p1.wait(3)  # need to manage timeout
    if w != 0:  # wait process is finished to return
        print(f'{p1.__dict__["pid"]}, p1.wait(3): {w}: There was an error')
    print('all processed finished')


def ex_2():
    p1 = subprocess.Popen('sleep 10', stdout=subprocess.PIPE, shell=True)
    pprint.pprint(f"{p1.__dict__['pid']}: return code: {p1.__dict__['returncode']}")  # does not wait to process next
    p2 = subprocess.Popen('sleep 5', stdout=subprocess.PIPE, shell=True)
    pprint.pprint(f"{p2.__dict__['pid']}: return code: {p2.__dict__['returncode']}")
    p3 = subprocess.Popen('sleep 5', stdout=subprocess.PIPE, shell=True)
    pprint.pprint(f"{p3.__dict__['pid']}: return code: {p3.__dict__['returncode']}")

    processes = [p1, p2, p3]

    for p in processes:
        if p.wait() != 0:  # wait process is finished to return
            print(f'{p2.__dict__["pid"]}: There was an error')

    print('all processed finished')


def ex_1():
    p1 = subprocess.Popen('sleep 3', stdout=subprocess.PIPE, shell=True)
    p2 = subprocess.Popen('sleep 3', stdout=subprocess.PIPE, shell=True)
    p3 = subprocess.Popen('sleep 3', stdout=subprocess.PIPE, shell=True)

    for p in [p1, p2, p3]:
        if p.wait() != 0:
            print('There was an error')

    print('all processed finished')


def main():
    ex_()


if __name__ == '__main__':
    main()
