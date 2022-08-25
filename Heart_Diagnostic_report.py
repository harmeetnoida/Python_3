from tkinter import *
root = Tk()
root.title("Heart_Diagnose_Report")
root.geometry("600x600")
root.configure(background="salmon")

question1_radioButton=StringVar(value="0")

Question1=Label(root, text ="Do you experience shortness of breath during routine activities?", bg = "salmon",fg= "white")
Question1.place(relx=0.5 ,rely=0.2 ,anchor= CENTER )
question1_r1=Radiobutton(root, text = "yes", variable=question1_radioButton, value="yes",bg ="salmon")
question1_r1.place(relx=0.5 ,rely=0.25 ,anchor= CENTER )
question1_r2=Radiobutton(root, text = "no", variable=question1_radioButton, value="no",bg ="salmon")
question1_r2.place(relx=0.5 ,rely=0.3 ,anchor= CENTER )

question2_radioButton=StringVar(value="0")
Question2=Label(root, text ="Do you have swelling in the feet/ ankles/legs (shoes feel tighter) or abdomen?",bg ="salmon",fg= "white")
Question2.place(relx=0.5 ,rely=0.35 ,anchor= CENTER )
question2_r1=Radiobutton(root, text = "yes", variable=question2_radioButton, value="yes",bg ="salmon")
question2_r1.place(relx=0.5 ,rely=0.4 ,anchor= CENTER )
question2_r2=Radiobutton(root, text = "no", variable=question2_radioButton, value="no",bg ="salmon")
question2_r2.place(relx=0.5 ,rely=0.45 ,anchor= CENTER )

question3_radioButton=StringVar(value="0")
Question3=Label(root, text ="Do you feel any of these symptoms - confusion, disorientation or loss of memory?",bg ="salmon",fg="white")
Question3.place(relx=0.5 ,rely=0.5 ,anchor= CENTER )
question3_r1=Radiobutton(root, text = "yes", variable=question3_radioButton, value="yes",bg ="salmon")
question3_r1.place(relx=0.5 ,rely=0.55 ,anchor= CENTER )
question3_r2=Radiobutton(root, text = "no", variable=question3_radioButton, value="no",bg ="salmon")
question3_r2.place(relx=0.5 ,rely=0.60 ,anchor= CENTER )


question4_radioButton=StringVar(value="0")
Question4=Label(root, text ="Do you experience shortness of breath while at rest/lying down?",bg ="salmon",fg= "white")
Question4.place(relx=0.5 ,rely=0.65 ,anchor= CENTER )
question4_r1=Radiobutton(root, text = "yes", variable=question4_radioButton, value="yes",bg ="salmon")
question4_r1.place(relx=0.5 ,rely=0.70 ,anchor= CENTER )
question4_r2=Radiobutton(root, text = "no", variable=question4_radioButton, value="no",bg ="salmon")
question4_r2.place(relx=0.5 ,rely=0.75,anchor= CENTER )

question5_radioButton=StringVar(value="0")
Question5=Label(root, text ="Do you experience persistent wheezing / coughing that produces white or pink blood tinged mucus?",bg ="salmon",fg= "white")
Question5.place(relx=0.5 ,rely=0.80,anchor= CENTER )
question5_r1=Radiobutton(root, text = "yes", variable=question5_radioButton, value="yes",bg ="salmon")
question5_r1.place(relx=0.5 ,rely=0.85 ,anchor= CENTER )
question5_r2=Radiobutton(root, text = "no", variable=question5_radioButton, value="no",bg ="salmon")
question5_r2.place(relx=0.5 ,rely=0.90 ,anchor= CENTER )

def heart_diagnostic_score():
    score = 0
    if question1_radioButton.get()=="yes":
        score = score+10
        print(score)
    if question2_radioButton.get()=="yes":
        score = score+10
        print(score)
    if question3_radioButton.get()=="yes":
        score = score+10
        print(score)
    if question4_radioButton.get()=="yes":
        score = score+10
        print(score)
    if question5_radioButton.get()=="yes":
        score = score+10
        print(score)
        
    if score <= 10:
        messagebox.showinfo("Report","You don't need to visit a doctor.")
    elif  score > 10 and score <= 30: 
        messagebox.showinfo("Report","You might perhaps have to visit a doctor")
    else :
        messagebox.showinfo("Report","I strongly advise you to visit a doctor")
        
btn = Button(root, text= "click me", command= heart_diagnostic_score)
btn.place(relx=0.5 ,rely=0.95 ,anchor= CENTER )

root.mainloop()