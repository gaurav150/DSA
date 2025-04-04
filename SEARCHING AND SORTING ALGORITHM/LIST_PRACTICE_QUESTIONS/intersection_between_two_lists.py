def intersection(nums1, nums2):
    """
    Function to find the intersection of two integer arrays.
    :param nums1: List[int] -> First array of integers
    :param nums2: List[int] -> Second array of integers
    :return: List[int] -> An array of unique integers present in both arrays
    """
    set1 = set(nums1)
    intersection_set = set()
    for ele in nums2:
        if ele in set1:
            intersection_set.add(ele)
    return list(intersection_set)
