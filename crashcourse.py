import sqlite3 as lite

#functionality goes here

class DatabaseManage(object):
    def __init__(self):
        global con
        try:
            con=lite.connect("courses.db")
            with con:
                cur=con.cursor() #this is important
                cur.execute("CREATE  TABLE IF NOT EXISTS course(Id INTEGER PRIMARY KEY AUTOINCREMENT,NAME TEXT,DESCRIPTION TEXT,PRICE TEXT, is_private BOOLEAN NOT NULL DEFAULT 1)") 
                
        except Exception:
            print("unable to create DB:")
    
    
    
    #NOW WE HAVE TO CREATE HAVE TO READ AND  HAVE TO DELETE THE DATA IN THE TABLE
    def insert_data(self,data):
        try:
            with con:
                cur=con.cursor()
                cur.execute("INSERT INTO course(name,description,price,is_private) values(?,?,?,?)",data)

                return True


                            
                            
        except Exception:
            return False
        
    
            
    
    
    def fetch_data(self):
        try:
            with con:
                cur=con.cursor()
                cur.execute("SELECT * FROM course")
                return cur.fetchall()
             
        except Exception:
            return False
    
    
    def delete_data(self,id):
        try:
            with con:
                cur=con.cursor()
                sql="DELETE FROM course WHERE id = ?"
                cur.execute(sql,[id])
                return True
                
        
        except Exception:
            return False

        
#to provide interface to user

def main():
    print("@"*40) #this i made for good UI design
    print("\n ::  COURSE MANAGEMENT  :: \n")
    print("*"*40)
    print("\n")
    
    
    #now creating an object to have access to our class
    
    db= DatabaseManage()
    print("#"*40)
    
    print("\n ::user manual:: \n")
    print("#"*40)
    
    
    print('\nPRESS:1. To Insert a new course\n')
    print('PRESS:2. Show all courses\n')
    print('PRESS:3. Delete a course (NEED ID OF COURSE)\n')
    print("@"*40)
    print("\n")
    
    
    
    choice=input("\nEnter a choice:")
    
    if choice == "1":
        
        name=input("\nEnter the course name: ")
        description=input("\nEnter the course description: ")
        price=input("\nEnter the course price: ")
        private=input("\nIs this course private?(0/1): ")
    
    
#passing multiple values can be done by using array:

    

        if db.insert_data([name, description, price, private]):
            print("YOUR COURSE HAS BEEN ENTERED SUCCESSFULLY")
            
            
            
        else:
            print("oops something went wrong:")
            
            
    elif choice == "2":
        
        
        print("\n :: Course List ::\n")
        
        for index, item in enumerate(db.fetch_data()):
            print("\n s.no :", str(index + 1))#here we will do concatenation which means attaching or printing of data and strings together
            print("\n Course ID:"+ str(item[0]))
            print("\n Course Name:"+ str(item[1]))
            print("\n Course Description:"+ str(item[2]))
            print("\n Course Price:"+ str(item[3]))
            private='Yes' if item[4] else 'No'
            print("\n Is course Private:"+ private)
            print("\n")
            
    elif choice == "3":
        
        record_id= input("Enter the ID of the Course")
            
        if db.delete_data(record_id):
            print("Yous course was successfully deleted:")
                
        else:
            print("OOPS SOMETHING WENT WRONG")
    else:
        print("\n BAD CHOICE")
        
        
if __name__ == '__main__':
    main()
    
                        
        
            
    
    
        
        
        
            
        
        
    
