from models import context

class Simulator(object):

    sim_context = None

    def __init__(self, sim_context):
        self.sim_context = sim_context

    def add_workload_generator(self, workload):
        self.sim_context.environment.process(workload.workload_trace())

    def run_simulation(self):
        self.sim_context.environment.run(until=self.sim_context.total_sim_time)
