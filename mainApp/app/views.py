from app import app, models, forms
from flask import flash, render_template, request, redirect
from db_create import  db_session
import json

@app.route('/', methods=['GET', 'POST'])
def homePage():
    print("Showing all tasks")
    results = db_session.query(models.taskToDo).all()


    p = models.taskToDo.query.all()
    columnNames = ["Id", "Name", "Details", "Completed"]
    #return render_template('example.html')
    return render_template('results_wC.html', columns =columnNames, items = results, title = "Home Page", header1 = "Home Page" )
    #return render_template('results.html', table=table)

@app.route('/tasks_uncomplete', methods=['GET', 'POST'])
def tasks_uncomplete():
    results = []

    qry = db_session.query(models.taskToDo).filter(models.taskToDo.Completed.contains('0'))
    results = qry.all()

    columnNames = ["Id", "Name", "Details"]
    return render_template('results_wC.html', columns =columnNames, items = results, title = "Uncompleted Tasks", header1 = "Uncompleted Tasks"  )

@app.route('/tasks_finished', methods=['GET', 'POST'])
def tasks_finished():
    qry = db_session.query(models.taskToDo).filter(models.taskToDo.Completed.contains('1'))
    results = qry.all()

    columnNames = ["Id", "Name", "Details"]
    return render_template('results.html', columns =columnNames, items = results,title = "Finsihed Tasks", header1 = "Finished Tasks" )
    #return render_template('results.html', table=table)



#Add a new task
@app.route('/new_task', methods=['GET', 'POST'])
def new_task():
    form = forms.TaskForm(request.form)

    if request.method == 'POST' and form.validate():
        toDo = models.taskToDo()
        save_changes(toDo, form, new=True)
        flash('Task created successfully!')
        return redirect('/')

    return render_template('new_task.html', form=form)


def save_changes(toDo, form, new=False):
    if(form.name.data=="")and(form.details.data==""):
        return redirect('/')
    else:
        toDo.name = form.name.data
        toDo.details = form.details.data
        if new:
            db_session.add(toDo)
        # commit the data to the database
        db_session.commit()


@app.route('/mark_complete/<int:Id>', methods=['GET', 'POST'])
def mark_complete(Id):
    #qry = models.session.query(taskToDo).filter(
    #            taskToDo.Id==Id)
    #qry = db_session.query(models.taskToDo).filter(models.taskToDo.Id.(Id))
    task = db_session.query(models.taskToDo).get(Id)
    task.Completed = 1
    db_session.commit()
    flash('Updated successfully!')
    #columnNames = ["Id", "Name", "Details"]
    #return render_template('results.html', columns =columnNames, items = task,title = "Updated Task", header1 = "Updated Task" )
    return render_template('base.html', title='Update Task')
    #return redirect('/')


# Load the JSON data and use the ID of the idea that was clicked to get the object
#@app.route('/mark_complete', methods=['POST'])
#def mark_complete():
#    data = json.loads(request.data)
#    task_id = int(data.get('id'))

#    return json.dumps({'status':'OK','ID': task.id, 'Name': task.name })
    # Increment the correct vote
	#if data.get('vote_type') == "up":
	#	idea.upvotes += 1
	#else:
	#	idea.downvotes += 1
    # Save the updated vote count in the DB
        # Tell the JS .ajax() call that the data was processed OK
