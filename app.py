# imports
from PIL import Image
import streamlit as st, importlib.util, os, requests, sys, subprocess, google.generativeai as genai

try:
    import replicate
except ImportError as e:
    st.error(f"Error importing replicate: {str(e)}")
    st.info("Please try installing replicate manually in your terminal:")
    st.code("pip install replicate")
    st.stop()

try:
    if 'REPLICATE_API_TOKEN' in st.secrets:
        replicate_client = replicate.Client(api_token=st.secrets['REPLICATE_API_TOKEN'])
except:
    if 'REPLICATE_API_TOKEN' in os.environ:
        replicate_client = replicate.Client(api_token=os.environ['REPLICATE_API_TOKEN'])
    else:
        st.error("REPLICATE_API_TOKEN not found in environment variables or secrets")
        st.stop()


def generate_images(prompt, aspect_ratio= "16:9", num_inference_steps=28, guidance_scale=5.0, output_quality=90, model="dev", num_outputs=6):
    try:
        output = replicate.run(
            "unikill066/nikhil-img-gen:d9dbb96a16e98eac5b3b2c082f01c7f6785163fd61d616a2c1ed0df6b43620c1",
            input={"prompt": prompt, "model": model, "num_outputs": num_outputs,
                   "aspect_ratio": aspect_ratio, "guidance_scale": guidance_scale,
                   "output_quality": output_quality, "num_inference_steps": num_inference_steps})
        return output
    except Exception as e:
        st.error(f"Error generating images: {str(e)}")
        return None

def get_image_from_url(url):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        image = Image.open(response.raw)
        return image
    except Exception as e:
        st.error(f"Error loading image from URL: {str(e)}")
        return None

genai.configure(api_key=os.environ['GEMINI_API_KEY'])

generation_config = {"temperature": 1,
  "top_p": 0.95, "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

gemini_model = genai.GenerativeModel(
  model_name="gemini-1.5-flash-8b",
  generation_config=generation_config,
  system_instruction="""You are an AI assistant for an image generation model and your task is to modify description to include a specific person in the image named NIKHIl. 
                        Your goal is to modify the user's input to create a new scene description that includes Nikhil as an active participant in the scene. 
                        Follow these guidelines:\n\n
                        1. Analyze the original input to understand the scene.\n
                        2. If Nikhil is not already mentioned, add him to the scene.\n
                        3. Choose an appropriate action or position for Nikhil that fits naturally within the described setting.\n
                        4. Make sure the scene doesn't involve covering Nikhil's face or is facing away from the perspective.\n 
                        5. Ensure the scene remains peaceful—modify any violent or harmful or illicit elements into a serene or constructive activity.\n
                        6. If the original input is Harmful and inclues Hate Speech, return a description involinvg Nikhil playing with a british shprthair orange cat \n Limit the output to 50 words""",
)

def main():
    st.title("Welcome to Nikhil's Image Generator using Flux")
    st.write("This app will generate AI Images of Nikhil based on the context")
    
    prompt = st.text_input("Enter your prompt:", 
                           "Nikhil summiting Mt. Rainier...")

    with st.expander("Advanced Settings"):
        num_steps = st.slider("Number of Inference Steps", 1, 50, 28)
        guidance_scale = st.slider("Guidance Scale", 1.0, 10.0, 5.0)
        num_outputs = st.slider("Number of Outputs", 1, 6, 3)
        output_quality = st.slider("Output Quality", 80, 100, 90)
        aspect_ratio = st.selectbox("Aspect Ratio", ['16:9', '3:4', '4:3'])
        model = st.selectbox("Model", ["dev"])

    if st.button("Generate Images"):
        if prompt:
            with st.spinner("Generating images..."):
                final_prompt = gemini_model.generate_content(prompt)
                
                st.markdown(f"This prompt is AI generated using Gemini model: {final_prompt.text}")
                print(final_prompt.text)
                outputs = generate_images(prompt=final_prompt.text,
                                          aspect_ratio=aspect_ratio, 
                                          num_inference_steps=num_steps, 
                                          guidance_scale=guidance_scale, 
                                          output_quality=output_quality,
                                          model=model, num_outputs=num_outputs)
                
                if outputs:
                    cols = st.columns(3)
                    for idx, image_url in enumerate(outputs):
                        with cols[idx % 2]:
                            image = get_image_from_url(image_url)
                            if image:
                                st.image(image, caption=f"Generated Image {idx+1}")
                                st.markdown(f"[Download Image]({image_url})")
        else:
            st.warning("Please enter a prompt first!")

if __name__ == "__main__":
    main()