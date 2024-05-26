315178293
212032205
*****
Comments:

### Results:
[DFS]
python3 game.py -p tiny_set.txt -s 4 7 -z fill
Expanded nodes: 128, score: 17

python3 pacman.py -a fn=dfs
Path found with total cost of 130 in 0.0 seconds
Search nodes expanded: 146
Pacman emerges victorious! Score: 380
Average Score: 380.0
Scores:        380
Win Rate:      1/1 (1.00)
Record:        Win


[BFS]
python3 game.py -p tiny_set.txt -f bfs -s 4 7 -z fill
Expanded nodes: 3119, score: 17

python3 pacman.py -a fn=bfs
Path found with total cost of 68 in 0.0 seconds
Search nodes expanded: 269
Pacman emerges victorious! Score: 442
Average Score: 442.0
Scores:        442
Win Rate:      1/1 (1.00)
Record:        Win

Summary Tables:
Algorithm |	Blokus (Score)	Blokus (Nodes Expanded)	Pacman (Cost)	Pacman (Nodes Expanded)
---------------------------------------------------------------------------------------------
   DFS	  |          17	    |        128	       |      130	   |         146
   BFS    |          17	    |        3119	       |      68	   |         269


### 2.1 - Optimality
## 1. Theoretical Analysis - Optimality Guarantee:
DFS (Depth-First Search): DFS does not guarantee an optimal solution.
                          It explores as far down one branch as possible before backtracking,
                          which can lead to suboptimal solutions since it might find a solution far from the optimal one.
BFS (Breadth-First Search): BFS guarantees an optimal solution in terms of the shortest path in unweighted graphs
                            or minimum number of moves, because it explores all nodes at the present depth level before
                            moving on to nodes at the next depth level.
                            For problems like finding a route in the Pacman maze or filling a Blokus board,
                            BFS will find the shortest path if all moves have equal cost.

## 2. Empirical Analysis - Empirical Costs and Optimality:
DFS:
Reminder: results:
Blokus Board (tiny_set.txt): Expanded nodes: 128, Score: 17
Pacman Maze: Path cost: 130, Expanded nodes: 146
BFS:
Blokus Board (tiny_set.txt): Expanded nodes: 3119, Score: 17
Pacman Maze: Path cost: 68, Expanded nodes: 269

From the results, BFS found a solution with a lower path cost in the Pacman maze (68 vs. 130).
This indicates that BFS is more likely to find an optimal solution (shortest path),
whereas DFS did not find the shortest path. For the Blokus board, both algorithms achieved the same score,
but BFS expanded significantly more nodes.

## 3. Consistency between Theoretical and Empirical Results:
The results are consistent with the theoretical analysis.
BFS found the optimal path in the Pacman maze, which aligns with its theoretical guarantee of optimality
for shortest paths. DFS did not find the optimal path, consistent with its theoretical lack of optimality guarantee.
For the Blokus board, although both achieved the same score, BFS’s higher number of expanded nodes suggests it
 explored more thoroughly, reflecting its exhaustive nature.

### 2.2 Running Time
## 1. Theoretical Analysis - Time Complexity:
DFS: The time complexity of DFS is O(b^m) where b is the branching factor (maximum number of successors per state)
and m is the maximum depth of the search tree. This is because DFS can potentially explore every node in the worst case.
BFS: The time complexity of BFS is O(b^d) where d is the depth of the shallowest solution.
BFS explores all nodes at each depth level, making it exponential in the depth of the solution.

## 2. Empirical Analysis - Vertices Expanded and Running Time:
Reminder: results:
DFS:
Blokus Board (tiny_set.txt): Expanded nodes: 128
Pacman Maze: Expanded nodes: 146
BFS:
Blokus Board (tiny_set.txt): Expanded nodes: 3119
Pacman Maze: Expanded nodes: 269
BFS expanded significantly more nodes in both problems, indicating it is slower in terms of nodes expanded.
This is expected because BFS explores all nodes level by level, leading to a larger number of node expansions
compared to DFS, which may find solutions without exploring all possible nodes.

## 3. Consistency between Theoretical and Empirical Results:
The empirical results are consistent with the theoretical analysis. BFS expanded more nodes,
reflecting its O(b^d) complexity, which grows quickly with depth. DFS expanded fewer nodes, consistent with O(b^m),
 but this also means it can miss the optimal solution due to deeper, non-optimal branches being explored first.


[DFS]
python3 game.py -p tiny_set.txt -s 4 7 -z fill
Expanded nodes: 128, score: 17

python3 pacman.py -a fn=dfs
Path found with total cost of 130 in 0.0 seconds
Search nodes expanded: 146
Pacman emerges victorious! Score: 380
Average Score: 380.0
Scores:        380
Win Rate:      1/1 (1.00)
Record:        Win


[BFS]
python3 game.py -p tiny_set.txt -f bfs -s 4 7 -z fill
Expanded nodes: 3119, score: 17

python3 pacman.py -a fn=bfs
Path found with total cost of 68 in 0.0 seconds
Search nodes expanded: 269
Pacman emerges victorious! Score: 442
Average Score: 442.0
Scores:        442
Win Rate:      1/1 (1.00)
Record:        Win


python3 eightpuzzle.py
BFS found a path of 7 moves: ['right', 'down', 'left', 'up', 'right', 'up', 'left']


[CORNERS - BFS]
python3 game.py -p tiny_set_2.txt -f bfs -s 6 6 -z corners
Expanded nodes: 9285, score: 17

[CORNERS - UCS]
python3 game.py -p tiny_set_2.txt -f ucs -s 6 6 -z corners
Expanded nodes: 21940, score: 17

python3 game.py -p small_set.txt -f ucs -s 5 5 -z corners
Expanded nodes: 38682, score: 13

[CORNERS - A*]
python3 game.py -p tiny_set_2.txt -f astar -s 6 6 -z corners -H null_heuristic
Expanded nodes: 21940, score: 17

[Blokus Corners Heuristic]
python3 game.py -p tiny_set_2.txt -f astar -s 6 6 -z corners -H blokus_corners_heuristic
Expanded nodes: 960, score: 17

[Blokus Cover Heuristic]
python3 game.py -p small_set.txt -f astar -s 10 10 -H blokus_cover_heuristic -z cover -x3 3 "[(2,2), (5, 5), (6, 7)
Expanded nodes: 11378, score: 8

[Blokus Cover Null Heuristic]
python3 game.py -p small_set.txt -f astar -s 6 6 -H null_heuristic -z cover -x 3 3 "[(2,2), (5, 5), (1, 4)]"
Expanded nodes: 4075, score: 7


