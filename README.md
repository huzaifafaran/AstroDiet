# AstroDiet: Personalized Diet Plan Generator

AstroDiet is a web app that creates personalized diet plans based on your unique details and fitness goals. Whether you're looking to lose weight, build muscle, or simply eat healthier, AstroDiet generates a tailored meal plan just for you!

## Features

- **Personalized Meal Plans:** Get a custom diet plan for breakfast, lunch, dinner, and snacks.
- **Detailed Nutritional Info:** Each meal comes with portion sizes and key nutritional details.
- **User-Friendly Interface:** Built with Streamlit, it's easy to use and navigate.
- **Rapid Results:** Leverages the Together API to generate plans quickly through real-time responses.

## Live Demo

Experience AstroDiet live at:  
[https://astrodiet-b69ys4xqulgqrccv2vbjrm.streamlit.app//](https://astrodiet-b69ys4xqulgqrccv2vbjrm.streamlit.app/)

## Installation

Follow these steps to set up AstroDiet locally:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/astrodiet.git
   cd AstroDiet
   ```

2. **Create a Virtual Environment (Optional but Recommended):**
   ```bash
   python -m venv env
   source env/bin/activate  # For Windows: env\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   The `requirements.txt` includes libraries such as Streamlit, Flask, Together, python-dotenv, and others.

4. **Configure Environment Variables:**
   Create a `.env` file in the project root with your Together API key:
   ```
   TOGETHER_API_KEY=your_together_api_key_here
   ```

## Usage

Start the Streamlit application with:
```bash
streamlit run your_script_name.py
```
Replace `your_script_name.py` with the name of the Python file containing your Streamlit code. Once running, input your details—height, weight, age, gender, activity level, and goals—and click the "Generate Diet Plan" button to see your personalized plan.

## How It Works

- **Input Collection:** The app gathers your personal metrics and dietary goals.
- **Prompt Generation:** It crafts a detailed prompt for the Together API to generate a customized diet plan.
- **Real-Time Response:** The plan is streamed back and displayed in a clean, easy-to-read format.
- **Backend Support:** An accompanying Flask server handles asynchronous requests to enhance responsiveness.

## Contributing

We welcome contributions! If you have ideas for improvements or new features:
- Open an issue to discuss your ideas.
- Submit a pull request with your changes.

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- **Together API:** Thanks for powering our diet plan generation.
- **Streamlit:** For making it simple to create interactive web apps.
- **Community:** Thanks to all open source contributors for their support and inspiration.

Enjoy creating a healthier you with AstroDiet!
