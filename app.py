import streamlit as st
from ocr import perform_ocr, detect_language

st.title("OCR for Hindi and English Texts")

# Upload the image file
uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

# Perform OCR and display the results
if uploaded_image is not None:
    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
    
    # Extract the text from the uploaded image
    text = perform_ocr(uploaded_image)
    
    # Display OCR text
    if text.strip():
        st.write("Extracted Text:")
        st.write(text)

        # Detect the language of the extracted text
        detected_lang = detect_language(text)
        st.write(f"Detected Language: {detected_lang}")

        # Keyword Search functionality
        keyword = st.text_input("Search for a keyword in the extracted text:")
        if keyword:
            if keyword.lower() in text.lower():
                st.write(f"Keyword '{keyword}' found!")
            else:
                st.write(f"Keyword '{keyword}' not found.")
    else:
        st.write("No text detected.")
