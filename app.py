"""IMPORT REQUIRED PACKAGES"""
import os
import streamlit as st
from PIL import Image
import pytesseract
import uuid
from textblob import TextBlob

# Set up upload directory
upload_dir = '/tmp/uploads'
if not os.path.exists(upload_dir):
    os.makedirs(upload_dir)

def save_uploaded_file(uploaded_file):
    """Save the uploaded files in /tmp/uploads"""
    unique_filename = str(uuid.uuid4())
    file_ext = os.path.splitext(uploaded_file.name)[-1]
    saved_filename = unique_filename + file_ext
    with open(os.path.join(upload_dir, saved_filename), "wb") as f:
        f.write(uploaded_file.getbuffer())
    return saved_filename

def extract_text_from_image(image_path):
    """Extracting the text data from uploaded image"""
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def analyze_sentiment(text):
    """Analyzing the sentiment of extracted text"""
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    return sentiment

def main():
    """Main function"""
    st.title("OpenShift Hosted Text Extraction Web App By Mr.R.B.Awankar")

    # Upload image
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Save the uploaded file
        saved_filename = save_uploaded_file(uploaded_file)
        st.success("Image uploaded successfully!")
        st.info("Saved Filename: " + saved_filename)

    # Display uploaded image
    if uploaded_file is not None:
        image_path = os.path.join(upload_dir, saved_filename)
        image = Image.open(image_path)
        st.image(image, caption="Uploaded Image", use_column_width=True)

    # Extract text from the uploaded image
    extract_data = st.button("Extract Data")
    extracted_text = ""

    if extract_data and uploaded_file is not None:
        image_path = os.path.join(upload_dir, saved_filename)
        extracted_text = extract_text_from_image(image_path)
        st.subheader("Extracted Text:")
        st.write(extracted_text)

        # Analyze sentiment of the extracted text
        sentiment = analyze_sentiment(extracted_text)
        st.subheader("Sentiment Analysis:")
        if sentiment > 0:
            st.write("Positive")
        elif sentiment < 0:
            st.write("Negative")
        else:
            st.write("Neutral")

if __name__ == '__main__':
    main()
