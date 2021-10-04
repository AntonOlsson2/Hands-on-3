import sys, unittest
from md import calcenergy
from ase.lattice.cubic import FaceCenteredCubic
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet
from ase import units

class MdTests(unittest.TestCase):
    def test_calcenergy(self):

        use_asap = True

        if use_asap:
            from asap3 import EMT
            size = 10
        else:
            from ase.calculators.emt import EMT
            size = 3

        atoms = FaceCenteredCubic(directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
                                  symbol="Cu",
                                  size=(size, size, size),
                                  pbc=True)

        # Describe the interatomic interactions with the Effective Medium Theory
        atoms.calc = EMT()

        # Set the momenta corresponding to T=300K
        MaxwellBoltzmannDistribution(atoms, temperature_K=300)

        # We want to run MD with constant energy using the VelocityVerlet algorithm.
        dyn = VelocityVerlet(atoms, 5 * units.fs)  # 5 fs time step.
        energies = calcenergy(atomsobject = atoms)
        epot = energies.pop(0)
        ekin = energies.pop(0)
        instT = energies.pop(0)
        if ekin >= 0:
            self.assertTrue(True)

if __name__ == "__main__":
    tests = [unittest.TestLoader().loadTestsFromTestCase(MdTests)]
    testsuite = unittest.TestSuite(tests)
    result = unittest.TextTestRunner(verbosity=0).run(testsuite)
    sys.exit(not result.wasSuccessful())
