class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #an empty dictionary initiated
        frequency = {}
        #frequency count of each num in nums
        for num in nums:
            if num in frequency:
                frequency[num]+=1
            else:
                frequency[num]=1
        #as frequency is dictionary so we cannot use .sort directly
        #we will first do frequecy.items which will convert into tuple
        items_list=list(frequency.items())
        #now we will use sort function and will sort on basis of frequency so we did x[1] and we want greatest first so we used reverese=True
        items_list.sort(key=lambda x:x[1],reverse=True)
        #but we only want number of greatest count sox[0]
        return ([x[0] for x in items_list[:k]])

        


        
