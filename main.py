from icecream import ic
from data import db
# import commands

db = db.Database()
# user = db.get_user(id="8524861899b1b81b832723e974988d90")
user_id = "8524861899b1b81b832723e974988d90"
new_task = db.create_task(name="test_task3", owner_id=user_id)
print(new_task)

# commands.create_database()
# ic("test")
# parent_task = commands.read_task("autopsy")
# print(parent_task)
# commands.create_database()
# new_sub_task = commands.create_task("taskman_project")
# new_sub_task2 = commands.create_task("test")
# new_sub_task3 = commands.create_task("vs_apt-project")



# print(getattr(task, "entry_date"))
# print(task)
# task = commands.DictToObj(task)

# session = commands.start_session()
# session = session.to_object()

# task.sessions.append(session)
# task = task.to

# db = commands.read_database()
# db["tasks"]["ttrk_project"] = task

# commands.update_database(db)

