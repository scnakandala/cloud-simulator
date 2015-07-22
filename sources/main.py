from models import context
from models import vm

from random import randint

from workload import rubis_workload
import simulator
import simpy

# vm1 = vm.VirtualMachine("default", randint(0,999999) ,3,2,3,45.4)
#
# vm1.print_configuration()

sim_context = context.SimulationContext(simpy.Environment(), 86400)
workload = rubis_workload.RubisWorkload("../data/sess.dat",sim_context)
simulator = simulator.Simulator(sim_context)
simulator.add_workload_generator(workload)
simulator.run_simulation()
