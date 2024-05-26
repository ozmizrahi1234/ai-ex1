12345678
87654321
*****
Comments:


[DFS]
python3 game.py -p tiny_set.txt -s 4 7 -z fill
Expanded nodes: 128, score: 17

python3 pacman.py -a fn=dfs
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
Expanded nodes: 9420, score: 17




[Blokus Corners]
python3 game.py -p small_set.txt -f astar -s 6 6 -H null_heuristic -z cover -x 3 3 "[(2,2), (5, 5), (1, 4)]"
Expanded nodes: 4075, score: 7



Expanded nodes: 8347, score: 7


