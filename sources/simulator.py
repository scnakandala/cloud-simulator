import pylab as plt
from models import context

class Simulator(object):

    sim_context = None

    def __init__(self, sim_context):
        self.sim_context = sim_context

    def add_workload_generator(self, workload):
        self.sim_context.environment.process(workload.process())

    def add_statistics_collector(self, stat_collector):
        self.sim_context.environment.process(stat_collector.process())

    def add_performance_calculator(self, perf_calculator):
        self.sim_context.environment.process(perf_calculator.process())

    def add_vm_reconfigurator(self, vm_reconfigurator):
        self.sim_context.environment.process(vm_reconfigurator.process())

    def add_cost_calculator(self, cost_calculator):
        self.sim_context.environment.process(cost_calculator.process())

    def run_simulation(self):
        self.sim_context.environment.run(until=self.sim_context.total_sim_time)
        self.show_plots()

    def show_plots(self):
        plt.subplot("211")
        x = range(self.sim_context.total_sim_time)
        y_demand = self.sim_context.log_system_demand
        plt.plot(x, y_demand, 'b-', label='system demand')

        y_performance = self.sim_context.log_system_performance
        plt.plot(x, y_performance, 'r-', label='system performance')
        plt.legend(loc='upper left')

        plt.ylabel("Number of User Requests")
        plt.xlabel("Time (seconds)")

        plt.subplot("212")
        y_cost = self.sim_context.log_system_cost
        plt.plot(x, y_cost, 'r-', label='system cost')

        plt.show()
