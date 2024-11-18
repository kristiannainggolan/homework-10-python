class Dufan():
    def __init__(self):
        self.attraction_name = ''
        self.attraction_list = []
        self.waiting_list = {}
        self.list_att = []
        self.time_att = []
    
    def get_attraction_name(self):
        return self.attraction_name
    
    def set_attraction_name(self, new_name):
        self.attraction_name = new_name

    def set_attraction_list(self, new_attraction):
        self.attraction_list.append(new_attraction)
    
    def get_attration_list(self):
        return self.attraction_list


    def set_waiting_list(self, keys, values):
        for key in keys:
            for value in values:
                self.waiting_list[key] = value
                values.remove(value)
                break
    
    def get_total_time(self, plan):
        time = 0
        for i in plan:
            time += self.waiting_list.get(i)

        return time
        




df = Dufan()
list_att = ['A','B' , 'C', 'D', 'E']
time_att = [60, 45, 30, 15, 5]

df.set_waiting_list(list_att,time_att)
print(df.waiting_list)

plan_att = ['A', 'A', 'C', 'C', 'C', 'D', 'E']

print(df.get_total_time(plan_att))









# Atraksi A menunggu antrian 60 menit
# Atraksi B menunggu antrian 45 menit
# Atraksi C menunggu antrian 30 menit
# Atraksi D menunggu antrian 15 menit
# selain dari keempat 5 menit





# for i in list:
#     df.set_attraction_list(i)

# df.set_attraction_name('bola')
# print(df.get_attraction_name())
# print(df.get_attration_list())



