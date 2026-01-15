#Complete
class operate:
    tlst =  [-25, -10, -7, -3, 2, 4, 8, 10]
    def op(self):
        lst = self.tlst.copy()
        i = 0
        tdct = dict()
        tlst = []
        while i<len(lst):
            print(f"working on: {lst[i]}")
            j = 0
            while j<len(lst)-1:
                temp = self.tlst[:]
                temp.remove(lst[i])
                print(f"Removing {lst[i]}, lst: {temp}")
                print(f"working on j: {temp[j]}")
                current = temp[j]
                sum = lst[i]+temp[j]
                temp.remove(temp[j])
                print(f"lst: {temp}")
                k = 0
                while k<len(temp):
                    print(f"working on k: {temp[k]}")
                    if sum + temp[k] == 0:
                        tlst.append(current)
                        tlst.append(temp[k])
                        tdct.update({lst[i]:tlst})
                        # tlst.append([lst[i], current, temp[k]])
                        print(f"one zero from i={lst[i]}, j={current}, k={temp[k]}")
                        tlst = []
                    k += 1
                print()
                j += 1
            i += 1

        print(f"Final numbers whose sum = 0:")
        for k,v in tdct.items():
            result = [k, v[0], v[1]]
            print(result)
ob = operate()
ob.op()

# OPTIMAL SOLUTION: https://www.w3resource.com/python-exercises/class-exercises/python-class-exercise-6.php
# FROM: https://www.w3resource.com/python-exercises/class-exercises/

# class py_solution:
#  def threeSum(self, nums):
#         nums, result, i = sorted(nums), [], 0
#         while i < len(nums) - 2:
#             j, k = i + 1, len(nums) - 1
#             while j < k:
#                 if nums[i] + nums[j] + nums[k] < 0:
#                     j += 1
#                 elif nums[i] + nums[j] + nums[k] > 0:
#                     k -= 1
#                 else:
#                     result.append([nums[i], nums[j], nums[k]])
#                     j, k = j + 1, k - 1
#                     while j < k and nums[j] == nums[j - 1]:
#                         j += 1
#                     while j < k and nums[k] == nums[k + 1]:
#                         k -= 1
#             i += 1
#             while i < len(nums) - 2 and nums[i] == nums[i - 1]:
#                 i += 1
#         return result

# print(py_solution().threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))
