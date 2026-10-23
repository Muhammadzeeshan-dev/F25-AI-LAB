class AC_Controller:
    last_state = "Start"

    def check_room(self, temp, occupied):
        past = self.last_state
        
        if occupied == False:
            new_mode = "ECO"
        elif temp > 26:
            new_mode = "COOL"
        elif temp < 20:
            new_mode = "WARM"
        else:
            new_mode = "IDLE"

        if new_mode == self.last_state:
            status = "No"
        else:
            status = "Yes"
            self.last_state = new_mode

        return past, new_mode, status

system = AC_Controller()

data_list = [
    (28, True),
    (28, True),
    (26, True),
    (20, True),
    (19, True),
    (25, False)
]

print("Past | Temp | Occupied | New | Command")

for room_temp, people_present in data_list:
    past_mode, target_mode, command_sent = system.check_room(room_temp, people_present)
    
    print(past_mode, "|", room_temp, "|", people_present, "|", target_mode, "|", command_sent)