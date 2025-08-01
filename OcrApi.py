import streamlit as st
import requests

# --- Page Config ---
st.set_page_config(page_title="OCR Form - Image to Text", layout="centered")

# --- Title and Styling ---
st.markdown("""
    <h2 style='text-align: center; color: #4CAF50;'>📄 Image to Text OCR</h2>
    <p style='text-align: center;'>Upload an image and extract text using OCR.space API</p>
    <hr>
""", unsafe_allow_html=True)

# --- Your OCR.space API Key ---
api_key = "K89014143488957"  # Your fixed API key

# --- File Upload Section ---
uploaded_file = st.file_uploader("📁 Upload Image File", type=["png", "jpg", "jpeg"])

# --- Process Button ---
if uploaded_file:
    if st.button("🚀 Extract Text"):
        with st.spinner("🔍 Analyzing the image..."):
            response = requests.post(
                'https://api.ocr.space/parse/image',
                files={'file': uploaded_file},
                data={'apikey': api_key, 'language': 'eng'}
            )
            result = response.json()

            if result.get("IsErroredOnProcessing") == False:
                parsed_text = result['ParsedResults'][0]['ParsedText']
                st.success("✅ Text Extracted Successfully!")
                st.text_area("📜 Extracted Text", parsed_text, height=200)

                # Optional: Download Button
                st.download_button("⬇️ Download Text", parsed_text, file_name="extracted_text.txt")

            else:
                st.error("❌ Error: " + result.get("ErrorMessage", ["Unknown error"])[0])
else:
    st.info("👆 Upload an image to begin.")

# --- Footer ---
st.markdown("<hr><center><small>Powered by OCR.space API | Made with ❤️ in Streamlit</small></center>", unsafe_allow_html=True)
