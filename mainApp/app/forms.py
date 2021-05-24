from wtforms import Form, StringField, SelectField

class TaskForm(Form):
    name = StringField('Name')
    details = StringField('Details')
