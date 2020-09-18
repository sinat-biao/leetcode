"""
Given a collection of intervals, merge all overlapping intervals.
"""
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """    
        # 方法一：先按第一个数排序，再比较
        # if len(intervals) == 0:
        #     return []
        # sort_intervals = []
        # len_ = len(intervals)
        # while len(sort_intervals) < len_:
        #     max_start = -1
        #     max_idx = -1
        #     for i in range(len(intervals)):
        #         if intervals[i][0] > max_start:
        #             max_start = intervals[i][0]
        #             max_idx = i
        #     sort_intervals.insert(0, intervals.pop(max_idx))
        # # print(sort_intervals)
        # merge_intervals = []
        # tmp_ = sort_intervals[0]
        # for i in range(1, len(sort_intervals)):                
        #     if sort_intervals[i][0] >= tmp_[0] and sort_intervals[i][0] <= tmp_[1]:
        #         if sort_intervals[i][1] >= tmp_[1]:
        #             tmp_[1] = sort_intervals[i][1]
        #     else:
        #         merge_intervals.append(tmp_)
        #         tmp_ = sort_intervals[i]
        # merge_intervals.append(tmp_)
        # return merge_intervals
        
        # 方法二：利用 python 函数来进行排序（提升排序速度）
        intervals.sort()
        merge_intervals = []
        tmp_ = intervals[0]
        for i in range(1, len(intervals)):                
            if intervals[i][0] >= tmp_[0] and intervals[i][0] <= tmp_[1]:
                if intervals[i][1] >= tmp_[1]:
                    tmp_[1] = intervals[i][1]
            else:
                merge_intervals.append(tmp_)
                tmp_ = intervals[i]
        merge_intervals.append(tmp_)
        return merge_intervals
    
        # 方法三：双指针
        # 详情参见：https://leetcode-cn.com/problems/merge-intervals/solution/merge-intervals-by-ikaruga/
        

S = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(S.merge(intervals))   # [[1, 6], [8, 10], [15, 18]]
intervals = [[1,4],[4,5]]
print(S.merge(intervals))   # [[1, 5]]
intervals = [[1,4],[0,4]]
print(S.merge(intervals))   # [[0, 4]]
intervals = [[2,6],[1,3],[8,10],[15,18]]
print(S.merge(intervals))   # [[1, 6], [8, 10], [15, 18]]
intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
print(S.merge(intervals))   # 
intervals = [[2,3],[5,5],[2,2],[3,4],[3,4]]
print(S.merge(intervals))