from pyMaze import maze , COLOR , agent
m = maze(15,20)
m.CreateMaze()

a = agent(m, filled=True, footprints=True)
m.markCells=[(5,5),(6,5),(4,5),(2,5),(11,5), (11,15)]
m.tracePath({a:m.path})

print(a.x)
print(a.y)
print(a.position)


m.run()

# you can increase number of loops using loopPercent=50, load maze , save maze as well, theme=COLOR.dark for black colour
