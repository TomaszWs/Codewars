# Create a class Ball. Ball objects should accept one argument for "ball type"
# when instantiated.
#
# If no arguments are given, ball objects should instantiate with a "ball type"
# of "regular."
#
# ball1 = Ball()
# ball2 = Ball("super")
# ball1.ball_type  #=> "regular"
# ball2.ball_type  #=> "super"


class Ball(object):
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type


if __name__ == '__main__':
    ball1 = Ball()
    ball2 = Ball("super")
    print(ball1.ball_type)
    print(ball2.ball_type)


# Best solutions:


class Ball(object):
  def __init__(self, type = "regular"):
    self.ball_type = type
