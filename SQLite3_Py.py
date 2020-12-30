import sqlite3

if __name__ == '__main__':
	conn = sqlite3.connect('Database.db')
	c = conn.cursor()
	sql_cmd = open("./SQL_CMDS/c-point_table.txt", 'r').read()
	c.execute(sql_cmd)
	print("Created Point Table")
	sql_cmd = open("./SQL_CMDS/c-channel_table.txt", 'r').read()
	c.execute(sql_cmd)
	print("Created Channel Table")
	sql_cmd = open("./SQL_CMDS/c-rule_table.txt", 'r').read()
	c.execute(sql_cmd)
	print("Created Rule Table")
	sql_cmd = open("./SQL_CMDS/c-role_table.txt", 'r').read()
	c.execute(sql_cmd)
	print("Created Role Table")
	

	sql_cmd = open("./SQL_CMDS/i-channel_table.txt", 'r').read()
	c.execute(sql_cmd)
	print("Init into channel_table")
	sql_cmd = open("./SQL_CMDS/i-rule_table.txt", 'r').read()
	c.execute(sql_cmd)
	print("Init into Rule Table")
	sql_cmd = open("./SQL_CMDS/i-role_table.txt", 'r').read()
	c.execute(sql_cmd)
	print("Init into Role Table")
	

	conn.commit()
	conn.close()
	print("Done")
	quit()
