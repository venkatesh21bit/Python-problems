"""You are an intergalactic explorer traversing through a cosmic nebula in search of rare celestial artifacts. These artifacts are encoded with unique numeric identifiers that hold information about their origins. Your spacecraft's data logs contain a list of these artifacts, but they are in no particular order. Your mission is to sort the artifacts and quickly determine if a specific artifact with a given identifier is present in the collected data.

Part 1: Sorting Celestial Artifacts
Implement a function sort_celestial_artifacts that takes an unsorted list of artifact identifiers and sorts them in ascending order using the selection sort algorithm. The artifact identifiers
are positive integers, and the sorting should be based on their numerical order.

Part 2: Locating the Cosmic Relic
Implement a function locate_cosmic_relic that takes a sorted list of artifact identifiers and a target identifier as parameters. The function should use binary search to determine if the
target artifact is present in the list. Return True if the artifact is found, and False otherwise.

Tasks:

1. Implement the sort_celestial_artifacts function using the selection sort algorithm.


2. Implement the locate_cosmic_relic function using the binary search algorithm.

3. Test both functions with appropriate inputs, ensuring the correct organization of artifact identifiers and the accurate identification of the cosmic relic."""

import array as ar
a=ar.array('i',[1,5,2,5,3,3,6,1,7,8,76,5])
Sliced_array = a[3:8]
print("\nSlicing elements in a range 3-8: ")
print(Sliced_array)
