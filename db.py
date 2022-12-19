import sqlite3

class BotdB:

    def _init_(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def user_exists(self, user_id):
        result = self.cursor.execute("SELECT 'id' FROM 'users' WHERE 'user_id' = ?", (user_id,))
        return bool(len(result.fetchall()))

    def get_user_id(self, user_id):
        result = self.cursor.execute("SELECT 'id' FROM 'users' WHERE 'user_id' = ?", (user_id,))
        return result.fetchone()[0]

    def add_user(self, user_id):
        self.cursor.execute("SELECT INTO 'users' ('user_id') VALUES (?)", (user_id, ))
        return self.conn.commit()

    def add_record(self, user_id, name):
        self.cursor.execute("INSERT INTO 'using' ('users_id', 'name') VALUES (?, ?)", (self.get_user_id(user_id), name))
        return self.conn.commit()   

    def close(self):
        self.conn.close()

    #####
    @staticmethod
    def How_much(self, user_id):
        self.cursor.execute("select count(*) from 'using' WHERE 'user_id' = ?", (user_id,))  
        result, = self.cursor.fetchone()
        return result


    def New_game(self, user_id):
        self.cursor.execute("DELETE FROM 'using' WHERE 'user_id' = ?", (user_id,) )
        return self.conn.commit()  
    
    def read_row(self, developer_id, user_id):
        self.cursor.execute("SELECT * from 'using' where 'id' = ? AND 'user_id' = ?", (developer_id, user_id,))
        self.record = self.cursor.fetchone()
        return(self.record[1])

    def Is_there(self, text):
        self.name = text
        self.cursor.execute("SELECT rowid FROM 'main' WHERE name = ?", (self.name,))
        data=self.cursor.fetchone()
        if data is None:
            x=0
        else:
            x=1
        return x

    def Was(self, text, user_id):
        self.name = text
        self.cursor.execute("SELECT rowid FROM 'using' WHERE name = ? AND 'user_id' = ?", (self.name, user_id,))
        data=self.cursor.fetchone()
        if data is None:
            x=0
        else:
            x=1
        return x

    def Print_answer(self, user_id):
        self.cursor.execute("select * from 'using'")
        id_last_word = How_much(user_id)
        z = cursor.fetchall()
        last_word = z[id_last_word-1][1]                        

        cursor = sqlite_connection.cursor()
        cursor.execute("select * from 'main'")
        result = cursor.fetchall()              
        cursor.close()

        if last_word[-1]=='ь' or last_word[-1]=='ъ':
            for x in result:
                if last_word[-2].upper() == x[1][0] and Was(x[-2])==0: 
                    return x[1]
        else:
            for x in result:
                if last_word[-1].upper() == x[1][0] and Was(x[-1])==0: 
                    return x[1]