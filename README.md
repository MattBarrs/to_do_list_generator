#1.1 Page Descripition 
##Home Page 
Main page of the site, it has links to all the pages at the top of the page. 
Displays ‘Home Page’ as well as a small description on what to do on the site. 

##Completed Tasks
This page is similar to the home page, display the links at the top and it should also display the page name as well as the favicon in the top left. However, the page should only display records or tasks which have been completed.

##Uncompleted Tasks
This page is similar to the completed task, the entire layout and content is the same, except where there was ‘Completed tasks’ it is now replaced with ‘Uncompleted tasks’ and the page should only display records or tasks which have been not been completed/unfinished.

##New Task
This page is used to enter a new record into the database, to get to this page the user presses the top left link ‘New Task’. The page will display two fields which the user enters data into, the name and the details field, there is a button below that which the user should use to submit the data. 


#1.2 Description of models implemented 
I implemented one model in the site, it was the model used for the database, which stored all the data needed for the website to run properly, the model contained four items per record:
-	‘ID’, this is the primary key, which is used to uniquely identify each of the records, it was of type integer and each value is unique.
-	‘Name’, this was used as an easy identifier to help the user quickly describe the task that needed to be completed. It will allow the user to find a task they’re looking for a lot easier, of type string. Each record is not unique and can be repeated, the record is none empty meaning it must contain some data.
-	‘Details’, this is used as a short description of what the task is and what needs to be done, of type string, not unique, none empty.
-	‘Completed’, a Boolean identifier to show whether or not the task is complete, used by the queries to filter the results. Of type Boolean, not unique, the system will automatically set its value, then the user changes its value by marking the task as complete.

#1.4 Evaluation of implementation 
I was able to implement all features needed/required by the system, it took longer than expected as I found it difficult to fully implement the section which changed the status of the task to complete, this was because there was not much content supplied in the tutorials for this section. I was able to implement every other feature of the system however with no major difficulties. I did however change the layout of the site, I moved the header to above the links to other pages as I believed it made the pages easier to follow and made all of the pages more user friendly and easier to view all of the pages content. I also made changes so that the tables on the complete and uncomplete pages did not have the status of the task.
The site created uses a three tier architecture, the first tier being the presentation layer which is the front end look of the system. HTML and the CSS are responsible for this, they dictate how the pages content is displayed on the page, so for this project it will be all of the html templates and the css file which are responsible for this.  Then there’s the application tier, the python is responsible for this area of the, it’s the core of the application and is used to communicate between the data tier and the presentation layer, it creates most the variables and data used for the queries and the page content. The data tier is responsible for the data storage, for this application it uses SQL. All of the queries are embedded into   the python files.


#1.5 References 
- https://www.freepik.com/free-icon/correct-tick_698047.htm - Image of a tick, used for the favicon of every page on the site. The website contains copyright free images; therefore, permission is not needed to use the image.


