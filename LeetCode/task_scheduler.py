# LeetCode "621. Task Scheduler" Solution

from collections import Counter, deque
import heapq

class Solution(object):
    def leastInterval(self, tasks, n):
        counts = Counter(tasks)

        max_heap = [-count for count in counts.values()]
        heapq.heapify(max_heap)

        queue = deque()
        time = 0

        while max_heap or queue:
            time += 1

            if max_heap:
                count = heapq.heappop(max_heap) + 1

                if count != 0:
                    queue.append((count, time + n))

            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])

        return time