class solution:
    def collision(self, asteroid):
        stack = []
        for s in asteroid:
            while stack and s < 0 and stack[-1] > 0:
                di