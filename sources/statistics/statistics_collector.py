from models import context

class StatisticsCollector(object):
    #Simulation Context
    sim_context = None

    def __init__(self, sim_context):
        self.sim_context = sim_context

    def process(self):
        for i in range(self.sim_context.total_sim_time):
            self.collect_statistics()
            yield self.sim_context.environment.timeout(1)

    def collect_statistics(self):
        self.sim_context.log_system_demand.append(self.sim_context.system_demand)
        self.sim_context.log_system_performance\
            .append(self.sim_context.system_performance)
        self.sim_context.log_system_cost.append(self.sim_context.system_cost)
