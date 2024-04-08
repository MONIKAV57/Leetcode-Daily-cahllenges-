class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        counts=[0,0]
        for s in students:
            counts[s]+=1
        
        rem = len(sandwiches)
        for sa in sandwiches:
            if counts[sa]==0:
                break
            if rem ==0:
                break
            counts[sa]-=1
            rem -=1
        return rem