# Nikhil's Image Generator using Flux
Welcome to **Nikhil's Image Generator using Flux**, an AI-powered app that creates images of Nikhil using **Flux framework**, **Google Gemini AI**, and **Replicate API**. Gemini refines prompts, and Flux generates personalized images.

Hosted on Streamlit: [Link to Nikhil's Image Generator App on Streamlit](https://flux-image-generator-58dpp94unlwkzkaz5hmagy.streamlit.app/)

Hosted on HugginFace Spaces: [Link to Nikhil's Image Generator App on HuggingFace](https://huggingface.co/spaces/unikill066/Flux-image-generator)

More about this repo:
<audio controls>
  <source src="misc/nikhil_img_gen_audio.mp4" type="audio/mp4">
  Your browser does not support the audio element.
</audio>

---

## Preview & Example
1. User enters the prompt: "Nikhil summiting Mt. Rainier"
2. The app, using Gemini, modifies the prompt to something like: "Nikhil reaches the summit of Mt. Rainier, standing proudly with an ice axe in hand, gazing at the breathtaking sunrise over the snow-covered peaks."
3. The app uses the modified prompt to generate images with the Replicate model.
4. The generated images, showing Nikhil at the summit of Mt. Rainier, are displayed to the user.

| Nikhil - Real Madrid, petting british shorthair | Nikhil - conducting some experiments on hDRG beside a cat | Nikhil wins the race, with rustic, French-like aesthetic |
|---|---|---|
| ![Example Image 1](misc/n1.png) | ![Example Image 2](misc/n2.png) | ![Example Image 3](misc/n3.png) |


## How It Works

1. **User Inputs a Prompt** - Enter a description of the image you want.

2. **Gemini AI Refines the Prompt** - The Gemini model modifies the input to ensure Nikhil is a key part of the generated scene.

3. **Image Generation using Replicate API** - The Flux framework sends the AI-generated prompt to a Replicate model to create images.

4. **Display and Download Images** - View generated images and download them instantly.


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


## Built With

1. **[Flux Framework](https://fluxml.ai/)** - High-performance AI model execution.
2. **[Google Gemini AI](https://ai.google.dev/)** - For prompt enhancement.
3. **[Replicate API](https://replicate.com/)** - AI-powered image generation.
4. **[Streamlit](https://streamlit.io/)** - Web-based UI framework.


## Contact

Feel free to contribute or reach out!

1. **GitHub Issues** - Report bugs or request features.
2. **Pull Requests** - Improve the project with your contributions.
3. **Email** - [G-mail](unikill066@gmail.com)


## License
This project is licensed under the [MIT License](LICENSE).


 **Happy Image Generating!**
