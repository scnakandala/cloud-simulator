class VirtualMachine(object):
    #Type of the vm
    vm_type = "default"

    #Available ammount of memory in GB
    memory = 0

    #Number of CPUs available
    cpu_count = 0

    #I/O availability based on some unit
    io = 0

    #cost per vm per hour
    price = 0

    #VM state
    state = ""

    #Migration time
    migration_time = 0

    #Boot time
    boot_time = 0

    #Max number of user requests that can be handles without lossing Performance
    max_users = 0

    #Constructor
    def __init__(self, vm_type, memory, cpu_count, io, price, state, migration_time, boot_time, max_users):
        self.vm_type = vm_type
        self.memory = memory
        self.cpu_count = cpu_count
        self.io = io
        self.price = price
        self.state = state
        self.migration_time = migration_time
        self.boot_time = boot_time
        self.max_users = max_users

    #Method to print VM resource configurations and price
    def print_configuration(self):
        print "VM type : %s \nMemory : %s \nNo of CPUs : %s \nIO : %s \nPrice : %s\nState : %s\nMigration time : %s\nBoot time : %s\nMax users : %s" \
            %(self.vm_type, self.memory, self.cpu_count, self.io, self.price,
                self.state, self.migration_time, self.boot_time, self.max_users)
