# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution.

# Student ID: 20230446

# Date: 29/11/2023

from graphics import *

def credit_input(prompt):
    while True:
        try:
            credits = int(input(prompt))
            if credits not in [0, 20, 40, 60, 80, 100, 120]: # if user enterd a value not in this range it will print "Out of range!'
                print("Out of range!")
                continue
            return credits
        except ValueError:
            print("Integer required!") # if entered value is not a string this will print "Integer required!".

# Set Progress, Progress_module_trailer, Do_not_progress_module_retriever and Exclude counts to zero.
Progress = 0         
Progress_module_trailer = 0
Do_not_progress_module_retriever = 0
Exclude = 0

result_data = []  #'result_data' empty list is used to store credits for pass, defer and fail.

stuent_or_staff = input("\nAre you a Student or a Staf member?\nIf you are a Student type 'student' or If you are a Staf member type 'staf': ")
if stuent_or_staff == "staf":

    while True:
        pass_credits = credit_input("\nPlease enter PASS credits:")
        defer_credits = credit_input("Please enter DEFER credits:")
        fail_credits = credit_input("Please enter FAIL credits:")

        total_credits = pass_credits + defer_credits + fail_credits
        if total_credits != 120:
            print("Total incorrect!")  # If the total is not equals to 120 it will print "Total incorrect!" and it will the user to add the credits again. And if the total is equals to 120, it will give a choice to the user.
        else:
            if pass_credits == 120:
                print("Progress\n")
                Progress += 1                   # Add 1 to the to count if the pass_credits = 120. 
            elif pass_credits == 100:
                print("Progress (module trailer)\n")
                Progress_module_trailer += 1    # Add 1 to the to count if the pass_credits = 100. 
            elif fail_credits >= 80:
                print("Exclude\n")
                Exclude += 1                    # Add 1 to the to count if the fail_credits >= 80. 
            else:
                print("Do not Progress (module retriever)\n")
                Do_not_progress_module_retriever += 1    # Add 1 to the to count if the pass_credits != 120,100 and fail_credits != 80,100,120. 
            
            result_data.append([pass_credits, defer_credits, fail_credits])  # Takes these credit values and adds them as a list to result_data.

            choice = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:")
            if choice == "q":
            # If user press q, histogram will pop up, if user press any letter except q it will loop again.


                total_count = (Progress + Progress_module_trailer + Do_not_progress_module_retriever + Exclude) # finds the total count for later.
                max_count = max(Progress, Progress_module_trailer, Do_not_progress_module_retriever, Exclude)  # finds the Progression type wich has the most counts.

                bar1_height = 400-(Progress/max_count*330)
                bar2_height = 400-(Progress_module_trailer/max_count*330)
                bar3_height = 400-(Do_not_progress_module_retriever/max_count*330)
                bar4_height = 400-(Exclude/max_count*330)
                # From this formula we don't have a limit. When the highest count is 15, 1000 or any number the Bar is gonna draw from 70 pixels (Y-axis).
                            
                def display_histogram():
                    try:
                        win = GraphWin("Histogram", 700, 500)   # creates 7:8 window.
                        win.setBackground("white")

                # Top Text,
                        top_text = Text(Point(170, 30),"Histogram Results")
                        top_text.setStyle("bold")   # Text style.
                        top_text.setSize(20)        # Text size.
                        top_text.draw(win)          # write the text in the window.

                # X axis,
                        bottom_line = Line(Point(50, 400), Point(650, 400))  # Draws a line.
                        bottom_line.setWidth(1)   # Width of the line.
                        bottom_line.draw(win)

                    # Bar 1,
                        bar1_top_text = Text(Point(140, bar1_height - 10), f"{Progress}") # Prints the progress count on the bar.
                        bar1_top_text.setStyle("bold")      # make the text bold.
                        bar1_top_text.setTextColor("grey")  #text color.
                        bar1_top_text.setSize(16)
                        bar1_top_text.draw(win)

                        bar1 = Rectangle(Point(80, 400), Point(200, bar1_height))  # Draws the bar.Height is decided by the formula(bar1_height). 
                        bar1.setFill("greenyellow")   # bar color.
                        bar1.draw(win)

                        bar1_bottom_text = Text(Point(140, 415), "Progress")  # Prints the name of the bar.
                        bar1_bottom_text.setStyle("bold")
                        bar1_bottom_text.setTextColor("grey")
                        bar1_bottom_text.setSize(15)
                        bar1_bottom_text.draw(win)

                    # Bar 2,
                        bar2_top_text = Text(Point(280, bar2_height - 10), f"{Progress_module_trailer}") # Prints the Progress_module_trailer count on the bar.
                        bar2_top_text.setStyle("bold")
                        bar2_top_text.setTextColor("grey")
                        bar2_top_text.setSize(16)
                        bar2_top_text.draw(win)

                        bar2 = Rectangle(Point(220, 400), Point(340, bar2_height)) # Draws the bar.Height is decided by the formula(bar2_height).
                        bar2.setFill("lightgreen")
                        bar2.draw(win)

                        bar2_bottom_text = Text(Point(280, 415), "Trailer")  # Prints the name of the bar.
                        bar2_bottom_text.setStyle("bold")
                        bar2_bottom_text.setTextColor("grey")
                        bar2_bottom_text.setSize(15)
                        bar2_bottom_text.draw(win)

                    # Bar 3,
                        bar3_top_text = Text(Point(420, bar3_height - 10), f"{Do_not_progress_module_retriever}")  # Prints the Do_not_progress_module_retriever count on the bar.
                        bar3_top_text.setStyle("bold")
                        bar3_top_text.setTextColor("grey")
                        bar3_top_text.setSize(16)
                        bar3_top_text.draw(win)

                        bar3 = Rectangle(Point(360, 400), Point(480, bar3_height)) # Draws the bar.Height is decided by the formula(bar3_height).
                        bar3.setFill("mediumseagreen")
                        bar3.draw(win)

                        bar3_bottom_text = Text(Point(420, 415), "Retriever")  # Prints the name of the bar.
                        bar3_bottom_text.setStyle("bold")
                        bar3_bottom_text.setTextColor("grey")
                        bar3_bottom_text.setSize(15)
                        bar3_bottom_text.draw(win)

                    # Bar 4,
                        bar4_top_text = Text(Point(560, bar4_height - 10), f"{Exclude}")  # Prints the Exclude count on the bar.
                        bar4_top_text.setStyle("bold")
                        bar4_top_text.setTextColor("grey")
                        bar4_top_text.setSize(16)
                        bar4_top_text.draw(win)

                        bar4 = Rectangle(Point(500, 400), Point(620, bar4_height)) # Draws the bar.Height is decided by the formula(bar4_height).
                        bar4.setFill("palevioletred")
                        bar4.draw(win)

                        bar4_bottom_text = Text(Point(560, 415), "Exclude")  # Prints the name of the bar.
                        bar4_bottom_text.setStyle("bold")
                        bar4_bottom_text.setTextColor("grey")
                        bar4_bottom_text.setSize(15)
                        bar4_bottom_text.draw(win)

            # Bottom Text,
                        bottom_text = Text(Point(180, 450), f"{total_count} out comes in total.") # Prints the totla count of progression in the bottom.
                        bottom_text.setTextColor("grey")
                        bottom_text.setSize(18)
                        bottom_text.setStyle("bold")
                        bottom_text.draw(win)

                        win.getMouse()  # Can Close the window by clicking anywhere except the close button.
                        win.close()

                    except GraphicsError:  # When user click the close button it shows a GraphicsError, for that i used a try except block to pass that error.
                            pass

                display_histogram()

                progression_order = ["Progress", "Progress (module trailer)", "Do not Progress (module retriever)", "Exclude"] 
                                # 'progression_order' list is used to define progression in specific order.

                f = open("Part 3(w2051669)(Student and Staff).txt", 'w')   # Opens a File named Part 3(w2051669).
                print("Part 3:", file=f)
                print("\nPart 2:")
                for progression_type in progression_order:                # Assign 'progression_type' to 'progression_order' in order.
                    for item in result_data:                              # This loop iterates through each item in the result_data list, where each item is a list containing three elements.                             
                        pass_credits, defer_credits, fail_credits = item  # This unpacks each item into the variables pass_credits, defer_credits, and fail_credits.
                        if pass_credits == 120:
                            progression = "Progress"
                        elif pass_credits == 100:
                            progression = "Progress (module trailer)"
                        elif fail_credits >= 80:
                            progression = "Exclude"
                        else:
                            progression = "Do not Progress (module retriever)"
                        if progression == progression_type:                
                        # A conditional statement that checks if the variable progression matches the current progression_type being iterated over in the loop.
                            print(f"{progression} - {pass_credits}, {defer_credits}, {fail_credits}")
                            # This uses f-string to create an output string that includes the type of progression (progression), along with the respective number of pass credits, defer credits, and fail credits.
                            print(f"{progression} - {pass_credits}, {defer_credits}, {fail_credits}", file=f) 
                            # This uses f-string to create an output string that includes the type of progression (progression), along with the respective number of pass credits, defer credits, and fail credits in the text file.              
                f.close()
                break
else:
    stuent_or_staff == "student"
    pass_credits = credit_input("\nPlease enter PASS credits:")
    defer_credits = credit_input("Please enter DEFER credits:")
    fail_credits = credit_input("Please enter FAIL credits:")

    total_credits = pass_credits + defer_credits + fail_credits
    if total_credits != 120:
            print("Total incorrect!")
    else:
        if pass_credits == 120:
            print("Progress\n")
            Progress += 1
        elif pass_credits == 100:
            print("Progress (module trailer)\n")
            Progress_module_trailer += 1
        elif fail_credits >= 80:
            print("Exclude\n")
            Exclude += 1
        else:
            print("Do not Progress (module retriever)\n")
            Do_not_progress_module_retriever += 1