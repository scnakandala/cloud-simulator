class WorkloadGenerator(object):
    #Simulation Context
    sim_context = None

    #Workload
    workload = []

    def __init__(self, workload, sim_context):
        self.sim_context = sim_context
        self.workload = workload

    def process(self):
        for i in range(self.sim_context.total_sim_time):
            self.workload_trace()
            yield self.sim_context.environment.timeout(1)

    def workload_trace(self):
        self.sim_context.system_demand = self.workload[self.sim_context.environment.now]
