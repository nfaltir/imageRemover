import streamlit as st
from rembg import remove
from PIL import Image

st.title("Image Background Remover")

# Upload image through Streamlit
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    # Display the uploaded image
    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

    # Check if the user wants to remove the background
    remove_bg = st.button("Remove Background")

    if remove_bg:
        try:
            # Process the image to remove the background
            image = Image.open(uploaded_image)
            output = remove(image)
            st.image(output, caption="Background Removed", use_column_width=True)

            # Save the processed image
            st.markdown("### Download Processed Image")
            st.markdown(
                f"Download your image: [Processed Image](data:image/png;base64,{output})",
                unsafe_allow_html=True,
            )

        except Exception as e:
            st.error(f"An error occurred: {e}")

st.caption("Note: This app uses the `rembg` library to remove backgrounds from images.")
