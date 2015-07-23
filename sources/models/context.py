import csv
import vm

class SimulationContext(object):
    #Current system demand
    system_demand = 0

    #For keeping the history of system_demand
    log_system_demand = []

    #Current system performance
    system_performance = 0

    #For keeping the history of system_performance
    log_system_performance = []

    #Current system cost
    system_cost = 0

    #For keeping the history of system cost
    log_system_cost = []

    #Currnt time
    current_time = 0

    #Total Simulation time
    total_sim_time = 0

    #Available vm resources
    vm_resources = []

    #Current vm allocation
    current_vm_allocation = []

    #Simpy simulation environment
    environment = None

    def __init__(self, environment, total_sim_time, vm_config_file):
        self.environment = environment
        self.total_sim_time = total_sim_time
        self.__init_vms(vm_config_file)

    def __init_vms(self, vm_config_file):
        ifile  = open(vm_config_file, "rb")
        reader = csv.reader(ifile)
        rownum = 0
        for row in reader:
            # omitting header row
            #file format
            #vm_type,memory,cpu_count,io,price,migration_time,boot_time,max_users,availability
            if rownum != 0:
                vm1 = vm.VirtualMachine(row[0],row[1],row[2],row[3],row[4],"none",row[5],row[6],row[7])
                self.vm_resources.append([vm1,row[8]])
            rownum += 1
        ifile.close()
