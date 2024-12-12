import unittest
import tests_12_1
import tests_12_2

runnerTest = unittest.TestSuite()
runnerTest.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
runnerTest.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runnerTest)