


def func_memo(n, memoized={}):
    if n == 0 or n == 1:
        return n
    if n not in memoized:
        memoized[n] = func_memo(n-1, memoized) + func_memo(n-2, memoized)
    return memoized[n]