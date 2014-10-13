import math

class Vect(object):
    """A 2D vector"""
    def __init__(self, x, y):
        """Initialisation: accept x,y as parameters"""
        self.x = float(x)
        self.y = float(y)

    def __add__(self, v):
        """Operator +"""
        return Vect(self.x+v.x, self.y+v.y)

    def __mul__(self, k):
        """Operator * scalar (V to the left)"""
        return Vect(self.x*k, self.y*k)

    def __rmul__(self, k):
        """Operator * scalar (V to the right)"""
        return Vect(self.x*k, self.y*k)

    def __div__(self, k):
        """Operator / by a scalar"""
        return Vect(self.x/k, self.y/k)

    def __rdiv__(self, k):
        """Operator / by a scalar"""
        return Vect(self.x/k, self.y/k)

    def __sub__(self, v):
        """Operator - of vectors"""
        return Vect(self.x-v.x, self.y-v.y)

    def abs(self):
        return math.sqrt(self.x**2 + self.y**2)

# The acceleration of gravity
G = Vect(0, -9.81)

K = 1.0
TMAX = 200.0
TSTEP = 0.05

class Rocket(object):
    """This class simulate a rocket by computing its thrust"""

    def __init__(self, position_0, speed_0, thrust_0, mass=1000000):
        self.X = position_0
        self.V = speed_0
        self.P = thrust_0
        # The mass of the rocket
        self.M = mass
        # Maximum thrust of the rocket along the X and Y direction
        self.PXmax = 2 * self.M  # env. 0.2 G
        self.PYmax = 50 * self.M # env. 5 G
        self.T = 0

    def thrust(self, dt, X1, G):
        """Returns the estimated thrust that the rocket must provide to
        reach X1 in dt seconds"""
        X0 = self.X
        V0 = self.V
        M = self.M
        E = X1 - X0
        P = K * M * ((1./(dt*dt))*E - (1./dt)*V0 - G)
        return P

    def calc_thrust(self, P):
        # it behaves more like a flying saucer than a rocket
        D = P
        P0 = self.P
        PXmax = self.PXmax
        PYmax = self.PYmax
        if D.x > 0:
            D.x = min(D.x,PXmax)
        else:
            D.x = max(D.x,-PXmax)
        if D.y > 0:
            D.y = min(D.y,PYmax)
        else:
            D.y = max(D.y,-PYmax)
        return D

    def new_position(self, dt, G):
        """Compute the new position at t+dt of the rocket given the thrust and
        the gravity"""
        X = self.X
        V = self.V
        M = self.M
        P = self.P
        A = P/M+G
        V1 = V+dt*A
        X1 = X+dt*V+(dt*dt/2)*A
        self.T+= dt
        self.X = X1
        self.V = V1

    def simule(self, target, dt):
        """Simulate the movement of the rocket aiming 'target' at t+dt"""
        Xt = target
        P = self.thrust(dt, Xt, G)
        Preel = self.calc_thrust(P)
        self.P = Preel
        self.new_position(dt, G)
        # more subtle if we want to take gaz comsumption into account:
        # self.M -= consommation(self.P)

    def print_info(self, t, Xo):
        X = self.X
        V = self.V
        P = self.P
        # this little function will pretty print the parameter for debugging
        print "%10.2f  %10.2f  %10.2f  %10.2f  %10.2f  %10.2f  %10.2f  %10.2f  %10.2f" % (
            t, X.x, X.y, Xo.x, Xo.y, V.x, V.y, P.x, P.y )


def simulation(F, t0, t1, dt):
    """do a simulation trying to respect the trajectory returned by the
    trajectory function
    """
    t = t0
    while t < t1:
        # This part compute the new position of the rocket
        Xt = trajectory(t+dt)
        F.simule(Xt, dt)
        F.print_info(t, Xt)
        t += dt

def trajectory(t):
    # This is a parabol whose summit is at x=100 y =10000,
    # and going through y=0,x=0 and y=0,x=200
    return Vect(t, 0.05 * (-t**2 + 200*t))

def simulate():
    F = Rocket(Vect(0, 0), Vect(0, 0), Vect(0, 0))
    simulation(F, 0, TMAX, TSTEP )

def print_traj():
    t = 0
    dt = TSTEP
    while t < TMAX:
        p = trajectory(t)
        print "%f\t%f\t%f\n" % (t, p.x, p.y)
        t += dt


def usage():
    print "python rocket.py [cmd] [options]"
    print " cmd is a command among:"
    print "  --help: this help"
    print "  --sim : outputs simulation"
    print "  --traj: outputs a trajectory"
    print " options are:"
    print " -k coef : a coefficient for the feedback loop"
    print " -t time : the duration of the simulation (or trajectory)"


def main():
    import sys
    import getopt
    global K, TMAX
    options, args = getopt.getopt(sys.argv[1:], "k:t:", ["help","sim","traj"])
    mode = 1 # 0=help, 1=simulation, 2=trajectory
    for option, param in options:
        if option == "-k":
            K = float(param)
        elif option == "-t":
            TMAX = float(param)
        elif option == "--help":
            mode = 0
        elif option == "--sim":
            mode = 1
        elif option == "--traj":
            mode = 2
        else:
            print "Unknown argument: ", option
            mode = 0
            sys.exit(1)
    if mode == 0:
        usage()
    elif mode == 1:
        simulate()
    elif mode == 2:
        print_traj()


if __name__ == "__main__":
    main()
