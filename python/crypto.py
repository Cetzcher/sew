# Pierre Rieger
# 4CHIT
# 2016/17
# ------------------------------------------- #
"""
Instead of hand crafting a table of ASCII Characters like {"a" : "b", ...}

it is also possible to construct a key table like keys = [chr(y) for y in range(38, 127)]
and then produce a value list like vals = keys[:] and randomize that.

Another approach would be using arithmetic to do something like ord('A') => 65
char(65+1) = 'B'
"""
import threading as th


DECRYPT = 0
ENCRYPT = 1


def partition_all(col, size):
    """
    Partitions a collection like [1, 2, 3, 4] in 'size' chunks size = 2 result = [[1, 2], [3, 4]]
    :param col: a collection that is iterable and provides len(col)
    :param size: an integer representing the chunk's size
    :return: a newly arranged collection so that there are len(col) / size chunks.
    """
    return [col[x:x+size] for x in range(0, len(col), size)]


class ThreadedCrypto(th.Thread):

    __shift = 1
    # a shift of 16 could result in an ambiguous result
    # since shifting the number 0 ord("0") => 48
    # by 16 would result in 48 - 16 = 32 which is char(32) = SPACE

    def __init__(self, msg, mode):
        """
        Construct a thread object.
        :param msg: the message that should be encrypted
        :param mode: the mode to use see constants at the top
                     0 = ENCRYPT, 1 = DECRYPT
        """
        super(ThreadedCrypto, self).__init__()
        self.__result = ""
        self.__mode = mode
        self.__msg = msg

    @staticmethod
    def set_shift(num):
        """
        sets the shift to use for en/decrypting.
        :param num: a number
        :return: None
        """
        ThreadedCrypto.__shift = abs(int(num)) % 16

    def get_result(self):
        """
        Gets the en/decryption result
        :return: the result of the operation.
        """
        return self.__result

    def run(self):
        """
        Runs the thread in the previously set mode.
        Encrypts or Decrypts the message.
        :return: None, stores the result in self.__result see self.get_result()
        """
        res = []
        # since encryption and decryption only differ by one operation this is used
        # to provide a "anonymous" function
        if self.__mode is ENCRYPT:
            fn = lambda x, y: x + y
        elif self.__mode is DECRYPT:
            fn = lambda x, y: x - y
        else:
            raise ValueError("mode must either be ENCRYPT or DECRYPT got: " + str(self.__mode) + " instead!")

        for c in self.__msg:
            if c is not ' ':
                res.append(chr(fn(ord(c), ThreadedCrypto.__shift)))
            else:
                res.append(c)
        concat = str.join("", res)
        self.__result = concat
        print("crypt finished input: {0} output: {1}".format(self.__msg, concat.upper()))


if __name__ == '__main__':
    # I/O
    try:

        cmode = int(input("mode? [ENCRYPT=1, DECRYPT=2] ")) - 1
        shift = int(input("key? "))

        thread_count = int(input("Thread count? "))
        if thread_count <= 0:
            raise AssertionError("Thread count must be >= 1 got: {0}".format(thread_count))

        cmsg = list(input("message? "))
        cmsg = partition_all(cmsg, int(len(cmsg) / thread_count) + 1)
        thread_count = min(thread_count, len(cmsg))
        # initializing more threads then the len of the msg will lead to
        # problems

        # create threads
        ThreadedCrypto.set_shift(shift)
        threads = []
        for i in range(thread_count):
            thread = ThreadedCrypto(str.join("", cmsg[i]), cmode)
            threads.append(thread)
            thread.start()

        # wait for threads to finish ...
        for t in threads:
            t.join()

        print("Finished processed string below!")

        # build the result, I use str.join("", iter) instead of
        # "".join(iter) since that makes the instruction more clear.
        result = str.join("", map(lambda thr: thr.get_result(), threads))
        print(result)

    except Exception as e:
        print("The program encountered an Error!")
        print(str(e))
