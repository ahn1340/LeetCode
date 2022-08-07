class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        total = 0
        water = capacity
        for i in range(len(plants)):
            water = water - plants[i]
            if water < 0:  # need to refill
                water = capacity - plants[i]
                total += i * 2
        total += len(plants)

        return total
"""
O(n) solution. Iteratve over the array. Whenever water is not enough at ith position, add (i)*2 to the total.
Finally, add the length of the array to the total.
"""
