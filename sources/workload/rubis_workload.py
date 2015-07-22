from models import context

import workload
import cPickle

class RubisWorkload(workload.Workload):
    #workload
    workload = []

    def __init__(self, file_name, sim_context):
        workload.Workload.__init__(self, file_name, sim_context)

    def workload_trace(self):
        workload_file = open(self.file_name,'r')
        self.workload = cPickle.load(workload_file)
        workload_file.close()
        self.workload = self.workload[0,86400*52:86400*53]
        for i in range(self.workload.shape[0]):
            self.sim_context.current_users = self.workload[i]
            yield self.sim_context.environment.timeout(1)
