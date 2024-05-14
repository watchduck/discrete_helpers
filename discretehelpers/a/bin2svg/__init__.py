import numpy as np


def bin2svg(tosvg):
    """
    :param tosvg: numpy array with binary entries, e.g. `np.array([[1, 0],
                                                                   [0, 1]])`
    :return: string describing an SVG path, e.g. 'M0,0h1v1h-1M1,1h1v1h-1'

    see also: https://en.wikiversity.org/wiki/User:Watchduck/bin2svg
    """

    def bin2corners(tocorners):
        """
        :param tocorners: binary m×n matrix; areas of 1s to be interpreted as areas of squares with no internal corners
        :return: m+1 × n+1 matrix; 0 for no corner; 1, 2, 3, 4 for corner; 13, 24 for double corner
        """

        if type(tocorners) is not np.ndarray:  # if input is plain array
            tocorners = np.array(tocorners)    # convert to numpy array

        (high, wide) = tocorners.shape
        hpad = np.zeros((1, wide+2), np.int8)
        vpad = np.zeros((high, 1), np.int8)
        tocorners = np.vstack((
            hpad,
            np.hstack((vpad, tocorners, vpad)),
            hpad
        ))

        corners = np.zeros((high+1, wide+1), np.int8)

        for m in range(high+1):
            for n in range(wide+1):
                sub = tocorners[m:m+2, n:n+2]
                if np.array_equal(sub, np.array([[0, 0],
                                                 [0, 1]])):
                    corners[m, n] = 1
                elif np.array_equal(sub, np.array([[0, 0],
                                                   [1, 0]])):
                    corners[m, n] = 2
                elif np.array_equal(sub, np.array([[1, 0],
                                                   [0, 0]])):
                    corners[m, n] = 3
                elif np.array_equal(sub, np.array([[0, 1],
                                                   [0, 0]])):
                    corners[m, n] = 4
                elif np.array_equal(sub, np.array([[1, 1],
                                                   [1, 0]])):
                    corners[m, n] = 5
                elif np.array_equal(sub, np.array([[1, 0],
                                                   [1, 1]])):
                    corners[m, n] = 6
                elif np.array_equal(sub, np.array([[0, 1],
                                                   [1, 1]])):
                    corners[m, n] = 7
                elif np.array_equal(sub, np.array([[1, 1],
                                                   [0, 1]])):
                    corners[m, n] = 8
                elif np.array_equal(sub, np.array([[1, 0],
                                                   [0, 1]])):
                    corners[m, n] = 13
                elif np.array_equal(sub, np.array([[0, 1],
                                                   [1, 0]])):
                    corners[m, n] = 24

        return corners

    def cornerfinder(corners, look):
        """
        Searches corner matrix from last position for non zero entries.
        :param corners: current corner matrix
        :param look: position where to begin searching
        :return: {'pos': [m, n], 'val': k} where [m, n] is the first position found and k the entry at this position
        """

        (high, wide) = corners.shape
        found = 0

        while found == 0:
            found = corners[tuple(look)]
            if found == 0:
                if look[1] < wide-1:
                    look[1] += 1
                elif look[1] == wide-1 and look[0] < high-1:
                    look = [look[0]+1, 0]
                else:
                    return 'reached end'
            else:
                return {'pos': look, 'val': found}

    def step(corners, cornerfound):
        """
        :param corners: current corner matrix
        :param cornerfound: last position and value found by `cornerfinder`
        :return: {'corners': corners, 'svgpath': svgpath} with `corners` sparser and `svgpath` extended
        """

        startpos = cornerfound['pos']
        pos = startpos[:]
        val = cornerfound['val']

        svgpath = 'M' + str(pos[1]) + ',' + str(pos[0])

        while True:

            if val in range(1, 9):  # 1 <= val <= 8
                corners[tuple(pos)] = 0
            elif val == 13 and (oldval in [4, 7]):  # 13 as 1 , leave 3
                val = 1
                corners[tuple(pos)] = 3
            elif val == 13 and (oldval in [2, 5]):  # 13 as 3 , leave 1
                val = 3
                corners[tuple(pos)] = 1
            elif val == 24 and (oldval in [1, 6]):  # 24 as 2 , leave 4
                val = 2
                corners[tuple(pos)] = 4
            elif val == 24 and (oldval in [3, 8]):  # 24 as 4 , leave 2
                val = 4
                corners[tuple(pos)] = 2

            oldpos = pos[:]

            creeper = 0

            if val in [1, 6]:
                while creeper == 0:
                    pos[1] += 1
                    if pos == startpos:
                        break
                    creeper = corners[tuple(pos)]
            elif val in [2, 5]:
                while creeper == 0:
                    pos[0] += 1
                    if pos == startpos:
                        break
                    creeper = corners[tuple(pos)]
            elif val in [3, 8]:
                while creeper == 0:
                    pos[1] -= 1
                    if pos == startpos:
                        break
                    creeper = corners[tuple(pos)]
            elif val in [4, 7]:
                while creeper == 0:
                    pos[0] -= 1
                    if pos == startpos:
                        break
                    creeper = corners[tuple(pos)]

            oldval = val
            val = creeper

            if pos[0] == oldpos[0]:
                append_to_svgpath = 'h' + str(pos[1]-oldpos[1])
            else:
                append_to_svgpath = 'v' + str(pos[0]-oldpos[0])

            if pos == startpos:
                break

            svgpath += append_to_svgpath

        return {'corners': corners, 'svgpath': svgpath}

    corners = bin2corners(tosvg)
    startpos = [0, 0]
    svgpath = ''

    while True:
        cornerfound = cornerfinder(corners, startpos)
        if cornerfound == 'reached end':
            break
        startpos = cornerfound['pos']
        thisstep = step(corners, cornerfound)
        corners = thisstep['corners']
        svgpath += thisstep['svgpath']

    return svgpath
