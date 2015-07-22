class Workload(object):
    #Simulation Context
    sim_context = None

    #Workload file name
    file_name = ""

    def __init__(self, file_name, sim_context):
        self.sim_context = sim_context
        self.file_name = file_name

    def workload_trace(self):
        pass
