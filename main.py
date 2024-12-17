from icecream import ic
import commands

# commands.create_database()
task = commands.create_task("autopsy")
task.create_session()
ic(task.sessions)
commands.update_database(commands.update_task(task))


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

