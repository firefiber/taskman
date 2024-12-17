from icecream import ic
import commands

# commands.create_database()
parent_task = commands.read_task("autopsy")
print(parent_task)
new_sub_task = commands.create_task("taskman_project")
print(new_sub_task)
commands.update_task(new_sub_task)

parent_task.sub_tasks.append(new_sub_task)
commands.update_task(parent_task)


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

