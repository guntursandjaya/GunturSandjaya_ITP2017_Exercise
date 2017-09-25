current_users = ["Gun","Vin","Ric","Jay","Han"]
new_users = ["Far","Dio","Val","Vin","Gun"]

for new_user in new_users:
    if new_user in current_users:
        print("Create another Username")
    else:
        print("Username Available")
