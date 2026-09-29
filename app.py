from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)


# ---------------- CONNECT TO MYSQL ----------------

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Prothoma@777",
    database="smart_health_care"
)

print("Database connected successfully!")


# ---------------- HOME PAGE ----------------

@app.route("/")
def home():
    return render_template("index.html")


# ---------------- ADD PATIENT ----------------

@app.route("/add_patient", methods=["POST"])
def add_patient():

    name = request.form["name"]
    age = request.form["age"]
    gender = request.form["gender"]
    phone = request.form["phone"]

    cursor = db.cursor()

    query = """
        INSERT INTO patients (name, age, gender, phone)
        VALUES (%s, %s, %s, %s)
    """

    values = (name, age, gender, phone)

    cursor.execute(query, values)
    db.commit()

    cursor.close()

    return "Patient added successfully!"


# ---------------- VIEW PATIENTS ----------------

@app.route("/patients")
def view_patients():

    cursor = db.cursor()

    cursor.execute("SELECT * FROM patients")

    patients = cursor.fetchall()

    cursor.close()

    return render_template("patients.html", patients=patients)


# ---------------- ADD DOCTOR ----------------

@app.route("/add_doctor", methods=["POST"])
def add_doctor():

    name = request.form["name"]
    specialization = request.form["specialization"]
    phone = request.form["phone"]

    cursor = db.cursor()

    query = """
        INSERT INTO doctors (name, specialization, phone)
        VALUES (%s, %s, %s)
    """

    values = (name, specialization, phone)

    cursor.execute(query, values)
    db.commit()

    cursor.close()

    return "Doctor added successfully!"


# ---------------- VIEW DOCTORS ----------------

@app.route("/doctors")
def view_doctors():

    cursor = db.cursor()

    cursor.execute("SELECT * FROM doctors")

    doctors = cursor.fetchall()

    cursor.close()

    return render_template("doctors.html", doctors=doctors)


# ---------------- BOOK APPOINTMENT ----------------

@app.route("/add_appointment", methods=["POST"])
def add_appointment():

    patient_name = request.form["patient_name"]
    doctor_name = request.form["doctor_name"]
    appointment_date = request.form["appointment_date"]
    appointment_time = request.form["appointment_time"]
    status = request.form["status"]

    cursor = db.cursor()

    query = """
        INSERT INTO appointments
        (patient_name, doctor_name, appointment_date, appointment_time, status)
        VALUES (%s, %s, %s, %s, %s)
    """

    values = (
        patient_name,
        doctor_name,
        appointment_date,
        appointment_time,
        status
    )

    cursor.execute(query, values)
    db.commit()

    cursor.close()

    return "Appointment booked successfully!"


# ---------------- VIEW APPOINTMENTS ----------------

@app.route("/appointments")
def view_appointments():

    cursor = db.cursor()

    cursor.execute("SELECT * FROM appointments")

    appointments = cursor.fetchall()

    cursor.close()

    return render_template(
        "appointments.html",
        appointments=appointments
    )


# ---------------- RUN APPLICATION ----------------

if __name__ == "__main__":
    app.run(debug=True)