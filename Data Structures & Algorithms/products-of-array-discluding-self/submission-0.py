class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_list_l = []
        product_list_r = []
        product = 1
        for i in range(len(nums)):
            product = product * nums[i]
            product_list_l.append(product)
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            print(i)
            product = product * nums[i]
            product_list_r.append(product)
        product_list_r.reverse()
        print(product_list_l)
        print(product_list_r)

        result = []
        for n in range(len(nums)):
            if n == 0:
                l = 1
            else:
                l = product_list_l[n - 1]
            if n == len(nums) - 1:
                r = 1
            else:
                r = product_list_r[ n + 1]
            result.append(l*r)
        return result
            