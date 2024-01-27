class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total_length = len(nums1) + len(nums2)
        median_point_s = [int(total_length / 2)] if total_length % 2 != 0 else [int(total_length / 2) -1, int(total_length / 2)]
        array_count_1 = 0
        array_count_2 = 0
        max_value_reached_1 = False
        max_value_reached_2 = False
        median_results_array = []

        for x in range(total_length):

            if nums1 and nums2 and nums1[array_count_1] <= nums2[array_count_2] and not max_value_reached_1:
                current_value = nums1[array_count_1]
                array_count_1 += 1
                if array_count_1 >= len(nums1):
                    array_count_1 -= 1
                    max_value_reached_1 = True
            else:
                if nums2 and not max_value_reached_2:
                    current_value = nums2[array_count_2]
                    array_count_2 += 1
                    if array_count_2 >= len(nums2):
                        array_count_2 -= 1
                        max_value_reached_2 = True
                elif max_value_reached_2 and not max_value_reached_1:
                    current_value = nums1[array_count_1]
                    array_count_1 += 1
                    if array_count_1 >= len(nums1):
                        array_count_1 -= 1
                        max_value_reached_1 = True
                        
                if nums1 and not nums2:
                    current_value = nums1[array_count_1]
                    array_count_1 += 1
                    if array_count_1 >= len(nums1):
                        array_count_1 -= 1
                        max_value_reached_1 = True

            if x in median_point_s:
                median_results_array.append(current_value)
                if len(median_results_array) == len(median_point_s):
                    break

        average_of_median_results_array = sum(median_results_array) / len(median_results_array) if median_results_array else 0

        return average_of_median_results_array

t = Solution()
r = t.findMedianSortedArrays([1,2],[3,4])

print(r)