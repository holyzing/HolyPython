# coding=utf-8
import os
import time
import random
import subprocess
from multiprocessing import Process, Pool, Queue,  Pipe, cpu_count, current_process

"""
    多任务    多核CPU    并行    并发    回调   轮询
    操作系统  资源分配和任务调度
    单核CPU同一时刻只能执行一个任务

    Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，
    调用一次，返回一次，但是fork()调用一次，返回两次，因为操作系统自动把当
    前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。

    子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程，
    所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID，
    Python的os模块封装了常见的系统调用，其中就包括fork，可以在Python程序中轻松创建子进程。

    常见的Apache服务器就是由父进程监听端口，每当有新的http请求时，就fork出子进程来处理新的http请求。

    python 提供了跨平台的进程模块 multiprocessing
"""

def unix_fork():
    a = 5
    print('Process (%s) start...' % os.getpid(), a)
    pid = os.fork()
    a = a -1
    if pid == 0:
        # fork() 做了进程克隆，并在该方法内分裂, 分裂之后会导致返回两次，以及 os.fork() 之后的代码会在主子进程中分别被执行，
        # 所以根据返回值可以执行主子进程中不同的逻辑，需要注意的是进程fork不会共享fork之前的资源，是对fork之前的所有资源的拷贝。
        print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
    else:
        print('I (%s) just created a child process (%s).' % (os.getpid(), pid), a)


class MultiProcessingDemo(object):
    print('当前电脑是 %s 核的！' %cpu_count(), current_process)

    @staticmethod
    def target(name):
        print(name, ':', os.getpid(), 'Father Process：', os.getppid())

    @staticmethod
    def run_new_process():
        # 克隆主进程（所引用的模块以及内存等资源），然后开启线程执行target
        print('Main process start')
        p = Process(target=MultiProcessingDemo.target, args=('SubProcess1',))
        p.start()
        p.join() # 等待子进程结束后再继续往下运行，通常用于进程间的同步
        print('Main process end.')

    @staticmethod
    def long_time_task(name):
        print('Run task %s (%s)...' % (name, os.getpid()))
        start = time.time()
        time.sleep(random.random() * 3)
        end = time.time()
        print('Task %s runs %0.2f seconds.' % (name, (end - start)))

    @staticmethod
    def run_process_pool():
        """
        对Pool对象调用join()方法会等待所有子进程执行完毕，之后才会执行主进程。
        调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
        Pool可传入启动子线程数量，默认为机器cpu核数。
        """
        print('Parent process %s.' % os.getpid())
        p = Pool()
        for i in range(cpu_count):
            p.apply_async(MultiProcessingDemo.long_time_task, args=(i + 1,))
        p.apply_async(MultiProcessingDemo.target, args=("target",))
        print('Waiting for all subprocesses done...')
        p.close()
        p.join()
        print('All subprocesses done.')

    '''
        An attempt has been made to start a new process before the current process has finished its bootstrapping phase.
        This probably means that you are not using fork to start your child processes and you have forgotten to use the proper idiom in the main module:
            if __name__ == '__main__':
                freeze_support()
                ...
        The "freeze_support()" line can be omitted if the program is not going to be frozen to produce an executable.

        Windows 上多进程的实现问题。在 Windows 上，子进程会自动  import 启动它的这个文件，
        而在 import 的时候是会执行这些语句的。 如果你这么写的话就会无限递归子进程报错。所以必须
        把创建子进程的部分用那个 if 判断保护起来，import 的时候 __name__ 不是 __main__ ，
        而是 __mp_main__，这样就不会递归运行了。

        在unix下,fork() 不会再子进程中导入开启它的文件！继承所有fork之前的资源并与父进程同步执行之后
        的所有逻辑 multiprocessing, 不会再子进程中导入开启它的文件,  克隆父进程启动它之前所有资源。
    '''

    @staticmethod
    def pool_map():
        with Pool(3) as p:
            coll = p.map(lambda x:x*x, [1, 2, 3, 4])
            # Apply `func` to each element in `iterable`, collecting the results in a list that is returned.

class ProcessInteractive(object):
    # multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据

    @staticmethod
    def write(q):
        print('Process to write: %s' % os.getpid())
        for value in ['A', 'B', 'C']:
            q.put(value)
            time.sleep(random.random())

    @staticmethod
    def read(q):
        print('Process to read: %s' % os.getpid())
        while True:
            value = q.get(True)  # 阻塞的  无法get到就阻塞在这里
            print('Get %s from queue.' % value)

    @staticmethod
    def interactive():
        # 父进程创建Queue，并传给各个子进程：
        q = Queue()
        pw = Process(target=ProcessInteractive.write, args=(q,))
        pr = Process(target=ProcessInteractive.read, args=(q,))
        # 启动子进程pw，写入:
        pw.start()
        # 启动子进程pr，读取:
        pr.start()
        # 等待pw结束:
        pw.join()
        # pr进程里是死循环，无法等待其结束，只能强行终止:
        pr.terminate()

    '''
        在Unix/Linux下，multiprocessing模块封装了fork()调用，使我们不需要关注fork()的细节。
        由于Windows没有fork调用，因此，multiprocessing需要“模拟”出fork的效果，父进程所有Python
        对象都必须通过pickle序列化再传到子进程去，所以，如果multiprocessing在Windows下调用失败了，
        要先考虑是不是pickle失败了。
    '''


class SubprocessDemo(object):
    #  很多时候，子进程并不是自身，而是一个外部进程。创建了子进程后，还需要控制子进程的输入和输出。
    #  subprocess 可以启动一个子进程，并控制其输入和输出，以达到直接运行程序达到一样的效果

    @staticmethod
    def run_subprocess():
        print(subprocess.call(['nslookup', 'www.python.org']))

        p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, err = p.communicate(b'set q=mx\npython.org\nexit\n')  # \n 依次输入
        print(output.decode('utf-8'))
        print('Exit code:', p.returncode)


class distributed_process():
    # TODO 分布式进程
    pass


if __name__ == '__main__':
    # __name__ : 指定当前模块为程序的执行入口
    pass

