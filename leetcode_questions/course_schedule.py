# https://neetcode.io/problems/course-schedule/question?list=blind75 

from collections import defaultdict
from typing import List

# Runtime: O(V + E) -> V is the number of courses, E is the number of prerequisites
# Space: O(V + E) -> V is the number of courses, E is the number of prerequisites

class CourseSchedule:
    def can_finish(self, prerequistes: List[List[int]], num_courses: int) -> bool:
        course_to_pre = defaultdict(list)
        for course, pre in prerequistes:
            course_to_pre[course].append(pre)

        visit = set()
        def dfs(course):
            if course in visit:
                return False
            if course_to_pre[course] == []:
                return True
            visit.add(course)
            for pre in course_to_pre[course]:
                if not dfs(pre):
                    return False
            visit.remove(course)
            course_to_pre[course] = []
            # This is to avoid revisiting the course
            return True
            
        for course in range(num_courses):
            if not dfs(course):
                return False
        return True