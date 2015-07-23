class DynamicReconfigurator(object):

    sim_context = None

    def __init__(self, sim_context):
        self.sim_context = sim_context

    def process(self):
        for i in range(self.sim_context.total_sim_time):
            self.run_reconfiguration()
            yield self.sim_context.environment.timeout(1)

    def run_reconfiguration(self):
        i =  self.sim_context.environment.now
        vm = self.sim_context.vm_resources[0][0]
        if (i % (60*60)) == 0:
            self.sim_context.current_vm_allocation = [[vm,self.sim_context.system_demand / int(vm.max_users)]]
