class CostCalculator(object):

    sim_context = None

    def __init__(self, sim_context):
        self.sim_context = sim_context

    def process(self):
        for i in range(self.sim_context.total_sim_time):
            self.calculate_cost()
            yield self.sim_context.environment.timeout(1)

    def calculate_cost(self):
        cost = 0;
        for vm_deploys in self.sim_context.current_vm_allocation:
            cost += int(vm_deploys[0].price) * int(vm_deploys[1])
        self.sim_context.system_cost = cost
