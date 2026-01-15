class target:
    tlst = [1, 8, 5, 6, 4, 3, 2, 9]
    def __init__(self, num):
        self.num = num

    def check(self):
        n = self.num
        lst = self.tlst
        i = 0
        while i<len(lst):
            for j in lst:
                if j!=lst[i]:
                    res=lst[i]+j
                    if res == n:
                        print(f"Target {n} met seen due to sum of numbers {lst[i]} and {j}.")
            i += 1

        

ob = target(13)
ob.check()


# OPTIMAL SOLUTION(S): https://www.w3resource.com/python-exercises/class-exercises/python-class-exercise-5.php
# FROM: https://www.w3resource.com/python-exercises/class-exercises/

#1:
# class py_solution(object):
#    def twoSum(self, nums, target_num):      
#        """
#        :type nums: list[int]
#       :type target: int
#       :return type: list[int]
#       """
#        result_dict = dict()
#        pos = 0
#        while pos < len(nums):
#            if (target_num - nums[pos]) not in result_dict:
#                result_dict[nums[pos]] = pos
#                pos += 1
#            else:
#                return [result_dict[target_num - nums[pos]], pos]
# print(py_solution().twoSum([10,20,10,40,50,60,70],50))
# print(py_solution().twoSum([10,20,10,40,50,60,70],52))


#2:
# class py_solution:
#   def twoSum(self, nums, target):
#        lookup = {}
#        for i, num in enumerate(nums):
#            if target - num in lookup:
#                return (lookup[target - num], i )
#            lookup[num] = i
# print("index1=%d, index2=%d" % py_solution().twoSum((10,20,10,40,50,60,70),50))

