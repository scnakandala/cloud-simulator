class PerformanceCalculator(object):

    sim_context = None

    def __init__(self, sim_context):
        self.sim_context = sim_context

    def process(self):
        for i in range(self.sim_context.total_sim_time):
            self.calculate_performance()
            yield self.sim_context.environment.timeout(1)

    def calculate_performance(self):
        perf = 0;
        vm_deploys = self.sim_context.vm_resources
        for vm_deploys in self.sim_context.current_vm_allocation:
            perf += int(vm_deploys[0].max_users) * int(vm_deploys[1])
        self.sim_context.system_performance = perf
