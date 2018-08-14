# Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different
# letters represent different tasks.Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.
#
# However, there is a non-negative cooling interval n that means between two same tasks, there must be at
# least n intervals that CPU are doing different tasks or just be idle.
#
# You need to return the least number of intervals the CPU will take to finish all the given tasks.
#
# Example 1:
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
# Note:
# The number of tasks is in the range [1, 10000].
# The integer n is in the range [0, 100].




class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        #         table = [0] * 26
        #         for task in tasks:
        #             table[ord(task) - ord('A')] += 1

        #         table.sort(reverse = True)
        #         time = 0
        #         while table[0] > 0:
        #             i = 0
        #             while i <= n:
        #                 if table[0] == 0:
        #                     break

        #                 if i < 26:
        #                     table[i] -= 1
        #                 i += 1
        #                 time += 1
        #             table.sort(reverse = True)

        #         return time





        table = collections.Counter(tasks)
        queue = [-val for key, val in table.items()]
        heapq.heapify(queue)
        time = 0
        while queue:
            i = 0
            temp = []
            while i <= n:
                if queue:
                    if queue[0] < -1:
                        temp.append(heapq.heappop(queue) + 1)
                    else:
                        heapq.heappop(queue)
                time += 1

                if not queue and not temp:
                    break

                i += 1
            for elem in temp:
                heapq.heappush(queue, elem)

        return time