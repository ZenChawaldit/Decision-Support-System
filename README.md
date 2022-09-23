# Decision-Support-System
Decision Support System to aid MBA graduates in their Management Game Capstone

Part 1


Management Game Decision Support System

Excerpt:
The Management Game course is an MBA student capstone program. In it, student teams assume the role of top management of firms competing in an international economy simulated by the Carnegie Mellon University Management Game. Each game consists of 5 companies, in which one of team of students represents one company. The companies would compete in 6 countries(Japan, Mexico, China, UK, Germany, US) over multiple periods with the objective of accumulating the most economic profit. Each team are given a report after each period of the game. The report is a excel file, consisting of different tabs including, marketing decision, operations and finance, market, production, finance, cash flow, competitor, and economic value report. For more details about the games, see this link: 
https://docs.google.com/document/d/16cIawFtLptoxLaUx8QRyyu5sQbzIJlQRtRBTHMm9hQ0/edit

Objective:
Our program’s objective is to estimate market share for six market(countries) given that the user provide the relative price, quality and marketing expense. The program received that data from Game Report Folder, which contains CSV files. 


Procedure:
1.	When running our program, a window with the welcome/instruction page will pop up. The user can read the instruction to know what our program does and press “ENTER” to start.
2.	When “ENTER”  is pressed, our program will automatically read the CSV files and print the current net incomes made by companies in a table and the total sales by all companies in each country in the last period.

Our program will print out a table that looks like this after reading the excel file.
Our program will print out a graph of predicted market shares for the user’s company and three slider bars for the user to adjust the price, quality and marketing factors.
Our program will print out a graph that looks like this after reading the excel file.
 
1.	In the header of the table, there will be five buttons, “Company 1”, “Company 2”, “Company 3”, “Company 4”, “Company 5” for the user to click and choose which company he/she is.
2.	The program then underwent multiple analysis including: 
a.	Each country market share change with respect to customer’s price,quality, and marketing percentage(via Gaussian Elimination)
b.	Find market share in percentage as function of %price, %quality, and %marketing spending.
c.	Retrieve selected companies’s past price,quality, marketing. 
d.	Combine company’s past quality with the current quality input value (80% past quality, 20% user input)(it takes some times for customers to recognize the change in product quality ), and also with the current marketing spending input value (50% past marketing, 50% user input.) (gaining brand loyalty takes time)
e.	Create an interactive bar graph that shows the predicted market share for a company in each country depending on the price, marketing and quality input from the user, and company’s past data.

