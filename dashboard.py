from tkinter import *
from employee import employee_form


#x=0,y=0 bcz we want it to be on top left corner
#bd=border
#cursor='hand2' means when you place cursor on button it will change to hand shape
#command=lambda: employee_frame.place_forget() means when you click on back button it will hide the employee frame and show the dashboard again
# we can use combo box by importing ttk from tkinter
#combo box means drop down menu
# grid=row=0,column=1 means we want it to be in first row and second column


#GUI part
window=Tk()
window.title("Dashboard")
window.geometry("1350x730+0+0")
window.resizable(0,0)
window.config(bg='white')
bg_image=PhotoImage(file='inventory.png')

titleLabel=Label(window,image=bg_image,compound=LEFT,text="  Inventory Management System",font=("times new roman",40,'bold'),bg='#010c48',fg='white',anchor='w',padx=20)
# #010c48 dark navy blue color 
# anchor=w means left side allignment
# padx=20 means space on left side before inventory
# relwidth=1 means taking it in the middle
# compound means merge
#fg=textcolor ,foground

titleLabel.place(x=0,y=0,relwidth=1)
logoutButton=Button(window,text="Logout",font=('times new roman',20,'bold'),fg='#010c48')
logoutButton.place(x=1180,y=10)

subtitleLabel=Label(window,text='Welcome Admin\t\t Date:24/08/2026\t\t Time:12:36:32 pm',font=('times new roman',15),bg='#4d636d',fg='white')
subtitleLabel.place(x=0,y=70,relwidth=1)
# #4d636d is a dark blue-gray / slate gray color

leftFrame=Frame(window)
leftFrame.place(x=0,y=102,width=200,height=650)

logoImage=PhotoImage(file='logo.png')
imageLabel=Label(leftFrame,image=logoImage)
imageLabel.pack()

menuLabel=Label(leftFrame,text='Menu',font=('times new roman',20),bg='#009688')
menuLabel.pack(fill=X)
# #009688 is called Teal.🎨

employee_icon=PhotoImage(file='Employee.png')
employee_button=Button(leftFrame,image=employee_icon,compound=LEFT,text=' Employee',font=('times new roman',20,'bold'),anchor='w',padx=10,command=lambda:employee_form(window))
employee_button.pack(fill=X)

supplier_icon=PhotoImage(file='supplier.png')
supplier_button=Button(leftFrame,image=supplier_icon,compound=LEFT,text=' Suppliers',font=('times new roman',20,'bold'),anchor='w',padx=10)
supplier_button.pack(fill=X)

category_icon=PhotoImage(file='category.png')
category_button=Button(leftFrame,image=category_icon,compound=LEFT,text=' Categories',font=('times new roman',20,'bold'),anchor='w',padx=10)
category_button.pack(fill=X)

product_icon=PhotoImage(file='product.png')
product_button=Button(leftFrame,image=product_icon,compound=LEFT,text=' Products',font=('times new roman',20,'bold'),anchor='w',padx=10)
product_button.pack(fill=X)

sale_icon=PhotoImage(file='sale.png')
sale_button=Button(leftFrame,image=sale_icon,compound=LEFT,text=' Sales',font=('times new roman',20,'bold'),anchor='w',padx=10)
sale_button.pack(fill=X)

exit_icon=PhotoImage(file='exit.png')
exit_button=Button(leftFrame,image=exit_icon,compound=LEFT,text=' Exit',font=('times new roman',20,'bold'),anchor='w',padx=10)
exit_button.pack(fill=X)


#total employees frame
emp_frame=Frame(window,bg='#2C3E50',bd=3,relief=RIDGE)
emp_frame.place(x=400,y=125,height=170,width=280)
# #2C3E50 is commonly called Dark Blue-Gray or Midnight Blue.
total_emp_icon=PhotoImage(file='total_emp.png')
total_emp_icon_label=Label(emp_frame,image=total_emp_icon,bg='#2C3E50')
total_emp_icon_label.pack(pady=10)


total_emp_label=Label(emp_frame,text='Total Employees',bg='#2C3E50',fg='white',font=('times new roman',15,'bold'))
total_emp_label.pack()


total_emp_label=Label(emp_frame,text='0',bg='#2C3E50',fg='white',font=('times new roman',30,'bold'))
total_emp_label.pack()

#total suppliers frame
sup_frame=Frame(window,bg='#BF6516',bd=3,relief=RIDGE)
sup_frame.place(x=800,y=125,height=170,width=280)
# #BF6516 is commonly called Dark Orange.
total_sup_icon=PhotoImage(file='total_supplier.png')
total_sup_icon_label=Label(sup_frame,image=total_sup_icon,bg='#BF6516')
total_sup_icon_label.pack(pady=10)


total_sup_label=Label(sup_frame,text='Total Suppliers',bg='#BF6516',fg='white',font=('times new roman',15,'bold'))
total_sup_label.pack()


total_sup_label=Label(sup_frame,text='0',bg='#BF6516',fg='white',font=('times new roman',30,'bold'))
total_sup_label.pack()


#total categories frame
cat_frame=Frame(window,bg='#5C1F1F',bd=3,relief=RIDGE)
cat_frame.place(x=400,y=310,height=170,width=280)
# #5C1F1F is commonly called Dark Red or Dark Wine.
total_cat_icon=PhotoImage(file='total_category.png')
total_cat_icon_label=Label(cat_frame,image=total_cat_icon,bg='#5C1F1F')
total_cat_icon_label.pack(pady=10)


total_cat_label=Label(cat_frame,text='Total Categories',bg='#5C1F1F',fg='white',font=('times new roman',15,'bold'))
total_cat_label.pack()


total_cat_label=Label(cat_frame,text='0',bg='#5C1F1F',fg='white',font=('times new roman',30,'bold'))
total_cat_label.pack()



#total products frame
prod_frame=Frame(window,bg='#343A1A',bd=3,relief=RIDGE)
prod_frame.place(x=800,y=310,height=170,width=280)
# #343A1A is commonly called Olive Night.
total_prod_icon=PhotoImage(file='total_products.png')
total_prod_icon_label=Label(prod_frame,image=total_prod_icon,bg='#343A1A')
total_prod_icon_label.pack(pady=10)


total_prod_label=Label(prod_frame,text='Total Products',bg='#343A1A',fg='white',font=('times new roman',15,'bold'))
total_prod_label.pack()


total_prod_label=Label(prod_frame,text='0',bg='#343A1A',fg='white',font=('times new roman',30,'bold'))
total_prod_label.pack()



#total Sales frame
sales_frame=Frame(window,bg='#00695C',bd=3,relief=RIDGE)
sales_frame.place(x=600,y=495,height=170,width=280)
# #00695C is commonly called Teal.
total_sales_icon=PhotoImage(file='total_sales.png')
total_sales_icon_label=Label(sales_frame,image=total_sales_icon,bg='#00695C')
total_sales_icon_label.pack(pady=10)


total_sales_label=Label(sales_frame,text='Total Sales',bg='#00695C',fg='white',font=('times new roman',15,'bold'))
total_sales_label.pack()


total_sales_label=Label(sales_frame,text='0',bg='#00695C',fg='white',font=('times new roman',30,'bold'))
total_sales_label.pack()

window.mainloop()