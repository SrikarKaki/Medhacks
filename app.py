import streamlit as st
# Title of the website
st.title("Lung Cancer")

# Subtitle
st.subheader("Understanding Lung Cancer Symptoms and Risk Factors")

# Introduction
st.write("""
Lung cancer is one of the most common types of cancer, and its symptoms can vary based on the stage of the disease.
This website provides an overview of symptoms and risk factors associated with lung cancer.
Early detection is important for successful treatment.
""")

# Risk Factors Section
st.header("Risk Factors")
st.write("""
Lung cancer can develop due to a variety of factors. The primary risk factors include:

1. **Smoking**: The leading cause of lung cancer, accounting for about 85% of cases.
2. **Secondhand Smoke**: Non-smokers who are exposed to secondhand smoke are also at risk.
3. **Exposure to Radon Gas**: Radon, a naturally occurring radioactive gas, can accumulate in homes.
4. **Asbestos Exposure**: Workers exposed to asbestos, especially in mining and construction, have an elevated risk.
5. **Genetics**: Family history of lung cancer can increase your risk.
6. **Air Pollution**: Long-term exposure to polluted air, particularly in urban areas, may also increase the risk.
""")

# Symptoms Section
st.header("Common Symptoms of Lung Cancer")
st.write("""
Lung cancer symptoms can be subtle in its early stages. Common signs include:

1. **Persistent Cough**: A cough that doesn't go away or gets worse over time.
2. **Chest Pain**: Pain in the chest that is often worse with deep breathing or coughing.
3. **Shortness of Breath**: Difficulty breathing, especially during everyday activities.
4. **Coughing up Blood**: Even a small amount of blood in the mucus can be a symptom.
5. **Hoarseness**: Changes in your voice, such as becoming more raspy or hoarse.
6. **Unexplained Weight Loss**: Losing weight without a clear reason could be a warning sign.
7. **Fatigue**: Feeling unusually tired or weak.
8. **Frequent Lung Infections**: Repeated infections like bronchitis or pneumonia.
""")

# Symptom Input Section
st.header("Check Your Symptoms")
st.write("Input the symptoms you are experiencing to receive advice:")

# Create checkboxes for symptoms input
symptom_cough = st.checkbox("Persistent Cough")
symptom_chest_pain = st.checkbox("Chest Pain")
symptom_short_breath = st.checkbox("Shortness of Breath")
symptom_blood_cough = st.checkbox("Coughing up Blood")
symptom_hoarse_voice = st.checkbox("Hoarseness")
symptom_weight_loss = st.checkbox("Unexplained Weight Loss")
symptom_fatigue = st.checkbox("Fatigue")
symptom_lung_infections = st.checkbox("Frequent Lung Infections")

# Analyze Symptoms and Provide Feedback
if st.button("Submit Symptoms"):
    if symptom_blood_cough or symptom_short_breath or symptom_weight_loss or symptom_cough:
        st.error("You are experiencing critical symptoms. Please consult a healthcare professional immediately.")
    elif symptom_fatigue or symptom_chest_pain or symptom_hoarse_voice:
        st.warning("These symptoms could be linked to lung cancer, but could also be other conditions. Consider seeing a doctor.")
    else:
        st.success("You may not have common signs of lung cancer, but it's always good to maintain regular health check-ups.")

# Provide a link to the tool
st.write("""
### Use our tool to check your symptoms anytime [Lung Cancer Symptoms Checker](#check-your-symptoms)
""")

# Footer
st.write("For more information on lung cancer, visit reputable sources like the American Cancer Society or consult with a medical professional.")
