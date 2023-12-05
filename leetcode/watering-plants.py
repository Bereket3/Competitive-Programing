class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        number_of_steps = 0
        # initalizing a variable to store the current water size in the can
        current_can_size = capacity

        for plants_index in range(len(plants)):
            if plants[plants_index] > current_can_size:
                # refilling the can and updating the current step
                number_of_steps += 2*plants_index + 1
                current_can_size = capacity - plants[plants_index]
            else:
                # using the water to water the plant
                number_of_steps += 1
                current_can_size -= plants[plants_index]

        return number_of_steps