#PROGRAM TO MANAGE STUDENT RECORDS

names=[]
while True:
   print("\n---SELECT YOUR CHOICE---")
   print("1-Add student details")
   print("2-Display all students")
   print("3-Search student by roll number")
   print("4-Delete student records")
   print("5-Exit")

   choice=int(input("Enter choice:"))

#1)ADD STUDENT   
 
   if choice==1:
      r=int(input("Enter student roll number:"))
      n=input("Enter name:")
      c=input("Enter course:")
      stud=(r,n,c)
      names.append(stud)
      print("student added successfully!")

#2)DISPLAY ALL

   elif choice==2:
       if not names:
           print("No student record found.")
       else:
           print("\nlist of student details.")
           for i in names:
               print(f"Roll No: {i[0]} | Name: {i[1]} | course: {i[2]}")

#3)SEARCH STUDENT FROM LIST

   elif choice==3:
        search_roll=int(input("Enter roll n3umber to search:"))
        found=False
        for i in names:
            if i[0]==search_roll:
                print(f"found! Roll No: {i[0]} | Names: {i[1]} | course: {i[2]}")
                found=True
                break
   
        if not found:
            print("student not found.")
   
#4)DELETE STUDENT
 
   elif choice==4:
         delete_roll=int(input("Enter roll number  to delete:"))
         found=False
         for i in names:
             if i[0]==delete_roll:
                 names.remove(i)
                 print("student record deleted successefull!")
                 found=True
                 break
         if not found:
             print("student not found.")

#5)EXIT

   elif choice==5:
          print("Exiting program. Goodbye!")
          break

   else:
          print("Invalid choice! please enter a number between 1 and 6.")


#WRITE A PROGRAM TO CREATE TO DO LIST





  






