import sys
import os


class UFBase:
    def __init__(self, size):
        self.N = size
        self.id_array = list(range(size))

    def find(self, p, q):
        pass

    def union(self, p, q):
        pass


class UFQuickfind(UFBase):
    def find(self, p, q):
        return self.id_array[p] == self.id_array[q]

    def union(self, p, q):
        pid = self.id_array[p]
        qid = self.id_array[q]
        for i in range(self.N):
            if self.id_array[i] == pid:
                self.id_array[i] = qid


class UFQuickunion(UFBase):
    def root(self, i):
        while i != self.id_array[i]:
            i = self.id_array[i]
        return i

    def find(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        self.id_array[i] = j


class UFQuickunionbalanced(UFBase):
    def __init__(self, size):
        UFBase.__init__(self, size)
        self.size_array = [1] * size

    def root(self, i):
        while i != self.id_array[i]:
            i = self.id_array[i]
        return i

    def find(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        if self.size_array[i] < self.size_array[j]:
            self.id_array[i] = j
            self.size_array[j] += self.size_array[i]
        else:
            self.id_array[j] = i
            self.size_array[i] += self.size_array[j]


def main():
    try:
        # https://stackoverflow.com/questions/7165749/open-file-in-a-relative-location-in-python
        rel_path = sys.argv[1]
        cwd = os.getcwd()
        abs_file_path = cwd + rel_path
        print("Input data file: {}".format(abs_file_path))
        file = open(abs_file_path)
        data_array = []
        for line in file.readlines():
            data_array.append(tuple(map(int, line.split())))
        print("Input data: {}".format(data_array))
        file.close()

        A = UFQuickfind(8192)
        B = UFQuickunion(8192)
        C = UFQuickunionbalanced(8192)

        for (left, right) in data_array:
            if not A.find(left, right):
                A.union(left, right)
            if not B.find(left, right):
                B.union(left, right)
            if not C.find(left, right):
                C.union(left, right)

        print("Not sure what the output should be...")

    except IndexError:
        print("No input data file")


if __name__ == '__main__':
    main()