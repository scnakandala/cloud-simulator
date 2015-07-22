class SimulationContext(object):
    #Current number of users in simulation
    current_users = 0

    #Current number of users which can be satisifies
    current_statifiable_user_count = 0

    #Currnt time
    current_time = 0

    #Total Simulation time
    total_sim_time = 0

    #Available max VM resources
    max_vm_resources = []

    #Current VM Allocation
    current_vm_allocation = []

    #Simpy simulation environment
    environment = None

    def __init__(self, environment, total_sim_time):
        self.environment = environment
        self.total_sim_time = total_sim_time
