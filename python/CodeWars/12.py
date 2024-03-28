"""
@it("[-8]")
def _():
    user = User()
    user.inc_progress(-8)
    test.assert_equals(user.rank, -8)
    test.assert_equals(user.progress, 3)

@test.it("[-7]")
def _():
    user = User()
    user.inc_progress(-7)
    test.assert_equals(user.rank, -8)
    test.assert_equals(user.progress, 10)

@test.it("[-6]")
def _():
    user = User()
    user.inc_progress(-6)
    test.assert_equals(user.rank, -8)
    test.assert_equals(user.progress, 40)

@test.it("[-5]")
def _():
    user = User()
    user.inc_progress(-5)
    test.assert_equals(user.rank, -8)
    test.assert_equals(user.progress, 90)

@test.it("[-4]")
def _():
    user = User()
    user.inc_progress(-4)
    test.assert_equals(user.rank, -7)
    test.assert_equals(user.progress, 60)

@test.it("[1, 1]")
def _():
    user = User()
    user.inc_progress(1)
    test.assert_equals(user.rank, -2)
    test.assert_equals(user.progress, 40)
    user.inc_progress(1)
    test.assert_equals(user.rank, -2)
    test.assert_equals(user.progress, 80)

    Write a class called User that is used to calculate the amount that a user will progress through a ranking system similar to the one Codewars uses.

Business Rules:
A user starts at rank -8 and can progress all the way to 8.
There is no 0 (zero) rank. The next rank after -1 is 1.
Users will complete activities. These activities also have ranks.
Each time the user completes a ranked activity the users rank progress is updated based off of the activity's rank
The progress earned from the completed activity is relative to what the user's current rank is compared to the rank of the activity
A user's rank progress starts off at zero, each time the progress reaches 100 the user's rank is upgraded to the next level
Any remaining progress earned while in the previous rank will be applied towards the next rank's progress
(we don't throw any progress away). The exception is if there is no other rank left to progress towards
(Once you reach rank 8 there is no more progression).

A user cannot progress beyond rank 8.
The only acceptable range of rank values is -8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8. Any other value should raise an error.
The progress is scored like so:

Completing an activity that is ranked the same as that of the user's will be worth 3 points
Completing an activity that is ranked one ranking lower than the user's will be worth 1 point
Any activities completed that are ranking 2 levels or more lower than the user's ranking will be ignored
Completing an activity ranked higher than the current user's rank will accelerate the rank progression.
The greater the difference between rankings the more the progression will be increased. The formula is
10 * d * d where d equals the difference in ranking between the activity and the user.
Logic Examples:
If a user ranked -8 completes an activity ranked -7 they will receive 10 progress
If a user ranked -8 completes an activity ranked -6 they will receive 40 progress
If a user ranked -8 completes an activity ranked -5 they will receive 90 progress
If a user ranked -8 completes an activity ranked -4 they will receive 160 progress, resulting in the user being upgraded
to rank -7 and having earned 60 progress towards their next rank
If a user ranked -1 completes an activity ranked 1 they will receive 10 progress (remember, zero rank is ignored)
"""

class User():
    rangos = [x for x in range(-8, 0)] + [x for x in range(1, 9)]

    def __init__(self):
        self.rank = -8
        self.progress = 0

    def inc_progress(self, rank):
        if rank not in self.rangos:
            raise ValueError("Invalid rank")

        if isinstance(rank, list):
            for r in rank:
                self.add_progress(self.rankear_int(r))
        else:
            self.add_progress(self.rankear_int(rank))

    def add_progress(self, progress):
        if self.rank == 8:
            return
        self.progress += progress
        while self.progress >= 100:
            self.progress -= 100
            self.rank += 1
            if self.rank == 0:
                self.rank += 1
            if self.rank == 8:
                self.progress = 0

    def diferencia(self, rango):
        indices = [i for i, r in enumerate(self.rangos) if rango == r] + [i for i, r in enumerate(self.rangos) if r == self.rank]
        return abs(indices[0] - indices[1])

    def rankear_int(self, r):
        if r < self.rank - 2:
            return 0
        elif -8 <= self.rank <= 7:
            if self.rank < r:
                d = self.diferencia(r)
                return 10 * d * d
            elif self.rank == r:
                return 3
            elif self.rank > r and self.rank > r - 1:
                return 1 

