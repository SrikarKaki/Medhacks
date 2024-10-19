import streamlit as st
import pandas as pd
from datetime import date

# Initialize session state
if "appointments" not in st.session_state:
    st.session_state["appointments"] = pd.DataFrame(columns=["Doctor", "Reason", "Date", "Notes"])
if "Abnormal_Issues" not in st.session_state:
    st.session_state["Abnormal_Issues"] = pd.DataFrame(columns=["Description", "Duration", "Date", "Severity"])
if "Medicines" not in st.session_state:
    st.session_state["Medicines"] = pd.DataFrame(columns=["name", "Prescription Date", "Dosage", "illness"])
if "Documents" not in st.session_state:
    st.session_state["Documents"] = pd.DataFrame(columns=["Name of doc", "Date", "File"])

st.sidebar.title("Navigation Menu")
Menu = st.sidebar.radio("Go to", ["Homepage", "Doctor Appointments", "Abnormal_Issues", "Medication records", "Medical Documents"])

# Homepage
if Menu == "Homepage":
    st.write("We should prolly put a picture here")

# Appointments
elif Menu == "Doctor Appointments":
    st.header("Record Doctor appointments here")
    Doctor = st.text_input("Doctor's name: ")
    Reason = st.text_input("Reason for Doctor Visit? ")
    Appointment_Date = st.date_input("Date of appointment: ", date.today())
    Notes_appt = st.text_area("Additional notes about appointment:")
    
    if st.button("Save this appointment"):
        if Doctor and Reason:
            Saved_appt = pd.DataFrame([[Doctor, Reason, Appointment_Date, Notes_appt]], columns=["Doctor", "Reason", "Date", "Notes"])
            st.session_state['appointments'] = pd.concat([st.session_state['appointments'], Saved_appt], ignore_index=True)
            st.success("Appointment saved!")
        else:
            st.error("Required fields are not filled in")

# Abnormal Issues (sidebar)
elif Menu == "Abnormal_Issues":
    st.write("Record any abnormal issues experienced here")
    with st.form("abnormal_issues_form"):
        Description = st.text_area("Description of issue")
        Duration = st.number_input("What was duration of issue (hours)", min_value=0.0, step=1.0)
        st.write(f"{Duration} hours")
        Date_Issue = st.date_input("When did you start experiencing this issue?")
        Severity_level = st.slider("What was the severity level of this issue", 1, 10)
        submit_issue = st.form_submit_button("Submit")
        
    if submit_issue:
        if Description and Duration and Date_Issue and Severity_level:
            Saved_issue = pd.DataFrame([[Description, Duration, Date_Issue, Severity_level]], columns=["Description", "Duration", "Date", "Severity"])
            st.session_state['Abnormal_Issues'] = pd.concat([st.session_state['Abnormal_Issues'], Saved_issue], ignore_index=True)
            st.success("Issue has been recorded!")
        else:
            st.error("Required fields are not filled in")

# Medications
elif Menu == "Medication records":
    st.write("Record your medications here")

    try:
        df = pd.read_csv("chronic_medications.csv")
        illnesses = df['Illness'].unique().tolist()
        st.title("Find Medications by Chronic Illness")
        selected_illness = st.selectbox("Select an illness to find related medications:", options=illnesses)
        filtered_df = df[df['Illness'] == selected_illness]
        
        if not filtered_df.empty:
            st.dataframe(filtered_df)
        else:
            st.warning("No medications found for the illness")
        
        with st.form("medication_form"):
            Name = st.text_input("Name of Medication: ")
            Prescription_Date = st.date_input("When was this medicine prescribed", date.today())
            Dosage = st.number_input("What was the dosage of medicine prescribed (mg)", min_value=0, step=1)
            st.write(f"{Dosage} mg")
            st.write(f"This medication is meant for patients with {selected_illness}")
            submit_medication = st.form_submit_button("Submit")
        
        if submit_medication:
            if Name and Prescription_Date and Dosage and selected_illness:
                Saved_medication = pd.DataFrame([[Name, Prescription_Date, Dosage, selected_illness]],  columns=["name", "Prescription Date", "Dosage", "illness"])
                st.session_state['Medicines'] = pd.concat([st.session_state['Medicines'], Saved_medication], ignore_index=True)
                st.success("Medication has been stored!")
            else:
                st.error("Required fields are not filled in")
        # Medication download buttons
        st.download_button(
            label=f'Download {selected_illness} medicine dataset',
            data=filtered_df.to_csv(index=False).encode('utf-8'),
            file_name=f'{selected_illness}-medicine.csv',
            mime='text/csv'
        )
        st.download_button(
            label="Download full dataset",
            data=df.to_csv(index=False).encode("utf-8"),
            file_name="Chronic illness data",
            mime='text/csv'
        )
    except FileNotFoundError:
        st.error("File not there")

# Medical Documents
elif Menu == "Medical Documents":
    st.write("Upload and medical documents here")
    uploaded_file = st.file_uploader("Choose a file")
    
    if uploaded_file is not None:
        name_doc = st.text_input("Name of the document")
        date_doc = st.date_input("Date of the document", date.today())
        Desc_doc = st.text_area("Description of document")
        
        if st.button("Save Document"):
            if name_doc and date_doc:
                Saved_doc = pd.DataFrame([[name_doc, date_doc, uploaded_file.name]], columns=["Name of doc", "Date", "File"])
                st.session_state['Documents'] = pd.concat([st.session_state['Documents'], Saved_doc], ignore_index=True)
                st.success(f"Document '{uploaded_file.name}' is saved!")
            else:
                st.error("Required fields are not filled in")