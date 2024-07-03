# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20230446
# Date: 29/11/2023

from graphics import *

def credit_input(prompt):
    while True:
        try:
            credits = int(input(prompt))
            if credits not in [0, 20, 40, 60, 80, 100, 120]:
                print("Out of range!")
                continue
            return credits
        except ValueError:
            print("Integer required!")

Progress = 0
Progress_module_trailer = 0
Do_not_progress_module_retriever = 0
Exclude = 0

result_data = []  #'result_data' empty list is used to store credits for pass, defer and fail.

txtfile=open('Part3(w2051669).txt','w')
print("Part 3:", file=txtfile)

while True:
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
            result_data.append(f"Progress - {pass_credits}, {defer_credits}, {fail_credits}")
            txtfile=open('Part3(w2051669).txt','a')
            txtfile.write(f"Progress - {pass_credits}, {defer_credits}, {fail_credits}\n")
            txtfile.close()

        elif pass_credits == 100:
            print("Progress (module trailer)\n")
            Progress_module_trailer += 1
            result_data.append(f"Progress (module trailer) - {pass_credits}, {defer_credits}, {fail_credits}")
            txtfile=open('Part3(w2051669).txt','a')
            txtfile.write(f"Progress (module trailer) - {pass_credits}, {defer_credits}, {fail_credits}\n")
            txtfile.close()

        elif fail_credits >= 80:
            print("Exclude\n")
            Exclude += 1
            result_data.append(f"Exclude - {pass_credits}, {defer_credits}, {fail_credits}")
            txtfile=open('Part3(w2051669).txt','a')
            txtfile.write(f"Exclude - {pass_credits}, {defer_credits}, {fail_credits}\n")
            txtfile.close()

        else:
            print("Do not Progress (module retriever)\n")
            Do_not_progress_module_retriever += 1
            result_data.append(f"Do not Progress (module retriever) - {pass_credits}, {defer_credits}, {fail_credits}")
            txtfile=open('Part3(w2051669).txt','a')
            txtfile.write(f"Do not Progress (module retriever) - {pass_credits}, {defer_credits}, {fail_credits}\n")
            txtfile.close()
        
        choice = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:")
        if choice == "q":

            total_count = (Progress + Progress_module_trailer + Do_not_progress_module_retriever + Exclude)
            max_count = max(Progress, Progress_module_trailer, Do_not_progress_module_retriever, Exclude)

            bar1_height = 400-(Progress/max_count*330)
            bar2_height = 400-(Progress_module_trailer/max_count*330)
            bar3_height = 400-(Do_not_progress_module_retriever/max_count*330)
            bar4_height = 400-(Exclude/max_count*330)
            # From this formula we don't have a limit. When the highest count is 15, 1000 or any number the Bar is gonna draw from 70 pixels (Y-axis).
                        
            def display_histogram():
                try:
                    win = GraphWin("Histogram", 700, 500)
                    win.setBackground("white")

            # Top Text,
                    top_text = Text(Point(170, 30),"Histogram Results")
                    top_text.setStyle("bold")
                    top_text.setSize(20)
                    top_text.draw(win)

            # X axis,
                    bottom_line = Line(Point(50, 400), Point(650, 400))
                    bottom_line.setWidth(1)
                    bottom_line.draw(win)

                # Bar 1,
                    bar1_top_text = Text(Point(140, bar1_height - 10), f"{Progress}")
                    bar1_top_text.setStyle("bold")
                    bar1_top_text.setTextColor("grey")
                    bar1_top_text.setSize(16)
                    bar1_top_text.draw(win)

                    bar1 = Rectangle(Point(80, 400), Point(200, bar1_height))
                    bar1.setFill("greenyellow")
                    bar1.draw(win)

                    bar1_bottom_text = Text(Point(140, 415), "Progress")
                    bar1_bottom_text.setStyle("bold")
                    bar1_bottom_text.setTextColor("grey")
                    bar1_bottom_text.setSize(15)
                    bar1_bottom_text.draw(win)

                # Bar 2,
                    bar2_top_text = Text(Point(280, bar2_height - 10), f"{Progress_module_trailer}")
                    bar2_top_text.setStyle("bold")
                    bar2_top_text.setTextColor("grey")
                    bar2_top_text.setSize(16)
                    bar2_top_text.draw(win)

                    bar2 = Rectangle(Point(220, 400), Point(340, bar2_height))
                    bar2.setFill("lightgreen")
                    bar2.draw(win)

                    bar2_bottom_text = Text(Point(280, 415), "Trailer")
                    bar2_bottom_text.setStyle("bold")
                    bar2_bottom_text.setTextColor("grey")
                    bar2_bottom_text.setSize(15)
                    bar2_bottom_text.draw(win)

                # Bar 3,
                    bar3_top_text = Text(Point(420, bar3_height - 10), f"{Do_not_progress_module_retriever}")
                    bar3_top_text.setStyle("bold")
                    bar3_top_text.setTextColor("grey")
                    bar3_top_text.setSize(16)
                    bar3_top_text.draw(win)

                    bar3 = Rectangle(Point(360, 400), Point(480, bar3_height))
                    bar3.setFill("mediumseagreen")
                    bar3.draw(win)

                    bar3_bottom_text = Text(Point(420, 415), "Retriever")
                    bar3_bottom_text.setStyle("bold")
                    bar3_bottom_text.setTextColor("grey")
                    bar3_bottom_text.setSize(15)
                    bar3_bottom_text.draw(win)

                # Bar 4,
                    bar4_top_text = Text(Point(560, bar4_height - 10), f"{Exclude}")
                    bar4_top_text.setStyle("bold")
                    bar4_top_text.setTextColor("grey")
                    bar4_top_text.setSize(16)
                    bar4_top_text.draw(win)

                    bar4 = Rectangle(Point(500, 400), Point(620, bar4_height))
                    bar4.setFill("palevioletred")
                    bar4.draw(win)

                    bar4_bottom_text = Text(Point(560, 415), "Exclude")
                    bar4_bottom_text.setStyle("bold")
                    bar4_bottom_text.setTextColor("grey")
                    bar4_bottom_text.setSize(15)
                    bar4_bottom_text.draw(win)

        # Bottom Text,
                    bottom_text = Text(Point(180, 450), f"{total_count} out comes in total.")
                    bottom_text.setTextColor("grey")
                    bottom_text.setSize(18)
                    bottom_text.setStyle("bold")
                    bottom_text.draw(win)

                    win.getMouse()
                    win.close()

                except GraphicsError:
                        pass

            display_histogram() 

            print("\nPart 2:")
            for item in result_data:
                print(item)

            print("\nPart 3:")
            for item in result_data:
                print(item)

            txtfile=open('Part3(w2051669).txt','r')
            txtfile.close()

            break