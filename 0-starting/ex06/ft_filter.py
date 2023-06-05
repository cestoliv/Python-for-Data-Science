def ft_filter(func, it):
    """
    ft_filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which
    function(item) is true.
    If function is None, return the items that are true.
    """
    # for item in it:
    #     if not func and item:
    #         yield item
    #     elif func and func(item):
    #         yield item
    if not func:
        return (item for item in it if item)
    else:
        return (item for item in it if func(item))
