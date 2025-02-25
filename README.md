# FLUX-image-generator# Nikhil's Image Generator using Flux
Welcome to **Nikhil's Image Generator using Flux**, an AI-powered application that generates images of Nikhil using AI models and prompting techniques. This project leverages the **Flux framework**, **Google Gemini AI**, and **Replicate API** to create dynamic and personalized images. The application uses Gemini for prompt modification and FLUX for image generation.

---

## Preview & Example
1. User enters the prompt: "Nikhil summiting Mt. Rainier"
2. The app, using Gemini, modifies the prompt to something like: "Nikhil reaches the summit of Mt. Rainier, standing proudly with an ice axe in hand, gazing at the breathtaking sunrise over the snow-covered peaks."
3. The app uses the modified prompt to generate images with the Replicate model.
4. The generated images, showing Nikhil at the summit of Mt. Rainier, are displayed to the user.
| Image 1 | Image 2 | Image 3 |
|---|---|---|
| ![Example Image 1](misc/n1.png) | ![Example Image 2](misc/n2.png) | ![Example Image 3](misc/n3.png) |

## Usage
1. **Run the Streamlit app locally:**

```bash
streamlit run app.py  
```

2. **Enter a prompt:** In the app, enter a description of the scene you want to generate.

3. **Adjust settings (optional):** Use the advanced settings to customize the image generation process.

4. **Generate images:** Click the "Generate Images" button.

5. **View and download:** The generated images will be displayed. You can download them using the provided links.


---

## Features

1. **Prompt Modification with Gemini:** Takes a user-provided prompt and modifies it using Gemini to seamlessly integrate Nikhil into the scene. Ensures Nikhil is visible and actively participating.
2. **Image Generation with Replicate:** Leverages a custom Replicate model to generate high-quality images featuring Nikhil.
3. **Customizable Settings:** Allows users to adjust the number of inference steps, guidance scale, and number of output images.
4. **Image Display and Download:** Displays the generated images within the app and provides download links.

---

## How It Works

1. **User Inputs a Prompt** - Enter a description of the image you want.

2. **Gemini AI Refines the Prompt** - The Gemini model modifies the input to ensure Nikhil is a key part of the generated scene.

3. **Image Generation using Replicate API** - The Flux framework sends the AI-generated prompt to a Replicate model to create images.

4. **Display and Download Images** - View generated images and download them instantly.

---

## Installation & Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/unikill066/FLUX-image-generator
   cd FLUX-image-generator
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up API Keys:
   - Add `REPLICATE_API_TOKEN` and `GEMINI_API_KEY` to your environment variables or `st.secrets`.
   * **Replicate API Token:** Obtain your [Replicate API token](https://replicate.com/) from your Replicate account settings and set it as an environment variable `REPLICATE_API_TOKEN` or in the Streamlit secrets file (`.streamlit/secrets.toml`). Example in `.streamlit/secrets.toml`:
   ```toml
    REPLICATE_API_TOKEN="YOUR_REPLICATE_API_TOKEN"
    GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
    ```

    * **Gemini API Key:** Obtain your [Gemini API key](https://aistudio.google.com/apikey) and set it as an environment variable `GEMINI_API_KEY` or in the Streamlit secrets file (`.streamlit/secrets.toml`).


4. Run the app:
   ```bash
   streamlit run app.py
   ```

---

## Usage Guide

1. Enter a text prompt in the input field.
2. Adjust **Advanced Settings** (optional) such as inference steps, quality, aspect ratio, etc.
3. Click **Generate Images**.
4. View and download the AI-generated images of Nikhil!

---

## Built With

1. **[Flux Framework](https://fluxml.ai/)** - High-performance AI model execution.
2. **[Google Gemini AI](https://ai.google.dev/)** - For prompt enhancement.
3. **[Replicate API](https://replicate.com/)** - AI-powered image generation.
4. **[Streamlit](https://streamlit.io/)** - Web-based UI framework.

---

## Contact & Contributions

Feel free to contribute or reach out!

1. **GitHub Issues** - Report bugs or request features.
2. **Pull Requests** - Improve the project with your contributions.

---

## License
This project is licensed under the [MIT License](LICENSE).


 **Happy Image Generating!**