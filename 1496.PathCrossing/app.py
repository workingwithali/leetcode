class solultion:
    def path(self,path):
        dir = {
            "N":[0,1],
            "S":[0,-1],
            "E":[1,0],
            "W":[-1,0],
        }
        vist = set()
        x , y = 0 , 0
        for n in path:
            vist.add((x,y))
            print(vist)
            dx, dy = dir[n]
            x , y = x + dx, y + dy
            if (x,y) in vist:
                return True
        
        return False

solultion = solultion()
path = "NESW"
result = solultion.path(path)
print(result)