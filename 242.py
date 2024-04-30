'''Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 '''
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
       # return sorted(s)==sorted(t)
       
     
        if len(s)!=len(t):
            return False
        
        count_s={}
        count_t={}

        for i in s:
            count_s[i]=count_s.get(i,0)+1
        for i in t:
            count_t[i]=count_t.get(i,0)+1
        return count_s==count_t