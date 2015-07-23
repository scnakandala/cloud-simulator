from models import context
from models import vm

from random import randint

from workload import workload_generator
from statistics import statistics_collector
from performance import perf_calculator
from reconfig import dynamic_reconfigurator
from cost import cost_calculator

import simulator
import simpy
import cPickle

sim_context = context.SimulationContext(simpy.Environment(), 86400, "../data/vm_configuration.csv")
simulator = simulator.Simulator(sim_context)

workload_file = open("../data/sess.dat",'r')
workload = cPickle.load(workload_file)
workload_file.close()
workload = workload[0,86400*52:86400*53]
workload_generator = workload_generator.WorkloadGenerator(workload, sim_context)
simulator.add_workload_generator(workload_generator)

stat_collector = statistics_collector.StatisticsCollector(sim_context)
simulator.add_statistics_collector(stat_collector)

perf_calculator = perf_calculator.PerformanceCalculator(sim_context)
simulator.add_performance_calculator(perf_calculator)

vm_reconfigurator = dynamic_reconfigurator.DynamicReconfigurator(sim_context)
simulator.add_vm_reconfigurator(vm_reconfigurator)

cost_calculator = cost_calculator.CostCalculator(sim_context)
simulator.add_cost_calculator(cost_calculator)

simulator.run_simulation()
