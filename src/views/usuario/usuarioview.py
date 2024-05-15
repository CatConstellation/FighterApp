def llamartareas():
    tareas = consultartareas()
    return render_template('index.html', tareas = tareas)

def llamarconsultartareas():
    return render_template('consultartarea.html')

def llamaragregartareas():
    return render_template('agregartarea.html')

def llamareliminartareas():
    return render_template('eliminartarea.html')