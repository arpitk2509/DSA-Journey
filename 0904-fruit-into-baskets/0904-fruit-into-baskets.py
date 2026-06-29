class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left=0
        max_fruit=0
        basket={}
        for right, fruit in enumerate(fruits):
            basket[fruit]=basket.get(fruit,0)+1
            while len(basket)>2:
                left_fruit=fruits[left]
                basket[left_fruit]-=1
                if basket[left_fruit]==0:
                    del basket[left_fruit]
                left+=1
            max_fruit= max(max_fruit, right - left + 1)
        return max_fruit