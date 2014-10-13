from os import path as osp
import unittest
import rocket

# Parameters:
ERRORMAX = 5.0
ERRORLAST = 0.02

Vect = rocket.Vect

def read_table(fpath):
    stream = open(osp.join(osp.dirname(__file__), 'input', fpath), "r")
    T = []
    for l in stream:
        s = l.split()
        if s:
            T.append([float(x.strip()) for x in s])
    # or smaller:
    # T = [ [ float(x.strip()) for x in l.split()] for l in f.xreadlines() ]
    stream.close()
    return T


class RocketTC(unittest.TestCase):

    def test_trajectory(self):
        """Checks if the rocket can follow the trajectory."""
        P = read_table("rocket_trajectory.txt")
        P0 = P[0]
        F = rocket.Rocket(Vect(P0[1], P0[2]), Vect(0, 0), Vect(0, 0))
        maxerr = 0.0
        for P1 in P[1:]:
            t, x, y = P1
            # ...
            dt = t - P0[0]
            pos = Vect(x, y)
            F.simule(pos, dt)
            lasterr = (F.X - pos).abs()
            if lasterr > maxerr:
                maxerr = lasterr
            P0 = P1
        self.assertLess(lasterr, ERRORLAST)
        self.assertLess(maxerr, ERRORMAX)


    def test_thrust(self):
        """Checks if the rocket can compute the correct thrust."""
        P = read_table("rocket_thrust.txt")
        P0 = P[0]
        F = rocket.Rocket(Vect(P0[1], P0[2]), Vect(0, 0), Vect(0, 0))
        maxerr = 0.0
        for P1 in P[1:]:
            t, x, y, px, py = P1
            # ...
            dt = t - P0[0]
            pos = Vect(x, y)
            F.simule(pos, dt)
            thrust = Vect(px, py)
            lasterr = (F.P - thrust).abs() / F.P.abs()
            if lasterr > maxerr:
                maxerr = lasterr
            P0 = P1
        self.assertLess(lasterr, ERRORLAST)
        self.assertLess(maxerr, ERRORMAX)

if __name__=="__main__":
    unittest.main()
