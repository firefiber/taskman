import commands

# commands.create_database()

task = commands.create_task("ttrk_project")
session = commands.start_session(task)
task.sessions.append(session)

