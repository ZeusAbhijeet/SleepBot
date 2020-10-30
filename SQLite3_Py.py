import sqlite3

if __name__ == '__main__':
	conn = sqlite3.connect('Database.db')
	c = conn.cursor()
	#sql_cmd = open("./SQL_CMDS/c-point_table.txt", 'r').read()
	#c.execute(sql_cmd)
	print("Created Point Table")
	#sql_cmd = open("./SQL_CMDS/c-channel_table.txt", 'r').read()
	#c.execute(sql_cmd)
	print("Created Channel Table")

	sql_cmd = open("./SQL_CMDS/i-channel_table.txt", 'r').read()
	c.execute(sql_cmd)

	conn.commit()
	conn.close()
	print("Done")
	quit()
