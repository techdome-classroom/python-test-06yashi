# Difficulty Level: Moderate

# Problem Statement:

The Archipelago Exploration

Imagine you're a cartographer exploring a mysterious archipelago (a group of islands) hidden within a vast ocean. You have a special map where each square represents a tiny landmass or open water. 'L' symbols indicate landmasses, while 'W' symbols represent areas of open water.

An island in this archipelago is a group of connected landmasses surrounded entirely by water. Landmasses can be connected horizontally or vertically, but not diagonally. Since this is a hidden archipelago, the entire outer border of the map is considered open water.

Your task is to determine the number of distinct islands within the archipelago based on the provided map.

Envoy Dispatches (Examples):

Dispatch 1:

The first envoy reported a rectangular map with the following layout:

Input -  [
             ["L","L","L","L","W"],
             ["L","L","W","L","W"],
             ["L","L","W","W","W"],
             ["W","W","W","W","W"],
         ]
In this case, the envoy discovered a single large island formed by the connected landmasses.

Output - 1

Dispatch 2:

The second envoy encountered a more fragmented map with the following layout:

 Input -  [
              ["L","L","W","W","W"],
              ["L","L","W","W","W"],
              ["W","W","L","W","W"],
              ["W","W","W","L","L"],
          ]
Here, the envoy identified three separate islands: two small islands in the bottom right corner and a larger island occupying the top left portion of the map.

Output - 3

Cartographer's Challenge:

Given a coded map represented by a grid of 'L' and 'W' symbols, can you decipher the number of distinct islands within the hidden archipelago? Remember, the edges of the map are always considered open water.
