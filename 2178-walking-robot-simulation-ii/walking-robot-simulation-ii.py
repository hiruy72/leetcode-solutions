
class Robot:

    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.perimeter = 2 * (width + height) - 4
        self.steps = 0

        self.x = 0
        self.y = 0
        self.dir = "East"

    def step(self, num: int) -> None:
        self.steps += num
        steps = self.steps % self.perimeter

        # Special case: when steps == 0 but moved before
        if steps == 0 and self.steps > 0:
            steps = self.perimeter

        if steps < self.w:
            self.x = steps
            self.y = 0
            self.dir = "East"
        elif steps < self.w + self.h - 1:
            self.x = self.w - 1
            self.y = steps - (self.w - 1)
            self.dir = "North"
        elif steps < 2 * self.w + self.h - 2:
            self.x = self.w - 1 - (steps - (self.w + self.h - 2))
            self.y = self.h - 1
            self.dir = "West"
        else:
            self.x = 0
            self.y = self.h - 1 - (steps - (2 * self.w + self.h - 3))
            self.dir = "South"

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        return self.dir