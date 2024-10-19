import streamlit as st 
import pandas as pd
from datetime import date
from fpdf import FPDF
st.sidebar.title("SWAN")
Menu = st.sidebar.radio("Go to", ["Login Page", "Homepage", "Patient_Doctor Communication", "Minigames", "Chatbot"])

if Menu == "Login Page":
    "bib"
if 'Patient_Doctor Communication' not in st.session_state:
    st.session_state['Patient_Doctor Communication'] = pd.DataFrame(columns=["Name", "Illness", "Date", "Severity"])
if 'Medicines' not in st.session_state:
    st.session_state['Medicines'] = pd.DataFrame(columns=["name", "Prescription Date", "Dosage", "illness"])
def generate_pdf(doctor_name, illness, date_doctor, severity_level, medication_name, prescription_date, dosage, selected_illness):
    pdf = FPDF()
    pdf.add_page()
    
    # Add title
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, "Patient-Doctor Communication & Medication Record", ln=True, align='C')

    # Patient-Doctor Communication Section
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, "Patient-Doctor Communication", ln=True, align='L')
    pdf.set_font("Arial", "", 12)
    pdf.cell(200, 10, f"Doctor's Name: {doctor_name}", ln=True)
    pdf.cell(200, 10, f"Illness Addressed: {illness}", ln=True)
    pdf.cell(200, 10, f"Date of First Visit: {date_doctor}", ln=True)
    pdf.cell(200, 10, f"Severity Level: {severity_level}/10", ln=True)

    # Medication Section
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, "Medication Details", ln=True, align='L')
    pdf.set_font("Arial", "", 12)
    pdf.cell(200, 10, f"Medication Name: {medication_name}", ln=True)
    pdf.cell(200, 10, f"Prescription Date: {prescription_date}", ln=True)
    pdf.cell(200, 10, f"Dosage: {dosage} mg", ln=True)
    pdf.cell(200, 10, f"Illness Related to Medication: {selected_illness}", ln=True)

    # Save PDF
    pdf_output_path = "medical_record.pdf"
    pdf.output(pdf_output_path)
    return pdf_output_path

if Menu == "Login Page":
    "login"
elif Menu == "Homepage":
    st.header("Welcome to app")
elif Menu == "Patient_Doctor Communication":
    with st.form("Medical Records"):
        Doctor_Name = st.text_input("Name of Doctor: ")
        Illness = st.text_area("What illness did your doctor address:")
        Date_Doctor = st.date_input("When did you start going to this doctor?", date.today())
        Severity_level = st.slider("What was the severity level of the issues you experienced", 1, 10)
        submit_issue = st.form_submit_button("Submit")
        
    if submit_issue:
        if Doctor_Name and Illness and Date_Doctor and Severity_level:
            Saved_Records = pd.DataFrame([[Doctor_Name, Illness, Date_Doctor, Severity_level]], columns=["Name", "Illness", "Date", "Severity"])
            st.session_state['Patient_Doctor Communication'] = pd.concat([st.session_state['Patient_Doctor Communication'], Saved_Records], ignore_index=True)
            st.success("Issue has been recorded!")
        else:
            st.error("Required fields are not filled in")
    try:
        st.subheader("Catalog of Some Medications")
        df = pd.read_csv("reordered_medicines_catalog.csv")
        illnesses = df['Illness'].unique().tolist()
        selected_illness = st.selectbox("Select an illness to find related medications:", options=illnesses)
        filtered_df = df[df['Illness'] == selected_illness]
        if not filtered_df.empty:
            st.dataframe(filtered_df)
        else:
            st.warning("No medications found for the illness")
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
    if st.button("Generate PDF"):
        if Doctor_Name and Illness and Date_Doctor and Severity_level and Name and Prescription_Date and Dosage and selected_illness:
            pdf_path = generate_pdf(Doctor_Name, Illness, Date_Doctor, Severity_level, Name, Prescription_Date, Dosage, selected_illness)
            with open(pdf_path, "rb") as pdf_file:
                st.download_button("Download PDF", data=pdf_file, file_name="medical_record.pdf", mime="application/pdf")
        else:
            st.error("Please complete all the forms before generating the PDF.")