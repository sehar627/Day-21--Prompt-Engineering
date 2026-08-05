import streamlit as st

from groq import Groq

client=Groq(api_key="YOUR_API_KEY")

st.set_page_config(page_title="Prompt Generator")

st.title("Prompt Generator Application")

st.write("Welcome to the Prompt Generator!")

topic= st.text_input("Enter a topic for the prompt:",placeholder="What is gravity?")

prompt_type=st.selectbox("Choose Prompt Type:",

                        ["Zero-shot Prompt",
                         "Few-shot Prompt",
                         "Chain-of-thought Prompt",
                         "Role Prompting",
                         "Audience Prompting",
                         "Structured Prompting",
                         "Constraint Prompting",
                         "Comparitive Prompting"]
                         )

temperature=st.slider("Creativity Level:", min_value=0.0, max_value=1.0, value=0.5, step=0.1)

max_tokens=st.slider("Maximum Tokens:", min_value=50, max_value=500, value=100, step=10)

generate_button=st.button("Generate Prompt")

if generate_button:

    if topic == "":

        st.warning("Please enter a topic to generate a prompt.")

    else:

        if prompt_type == "Zero-shot Prompt":

            prompt= f""" Explain {topic}"""

        elif prompt_type == "Few-shot Prompt":

            prompt= f"""

            Example:

            Topic:Gravity
            Explanation: Gravity is a force that attracts two bodies towards each other.

            Now Explain {topic} in a similar manner.
            """

        elif prompt_type == "Chain-of-thought Prompt":

            prompt=f"""
            Explain {topic} step by step, providing reasoning for each step.
            
            """
        elif prompt_type == "Role Prompting":

            prompt=f"""
            You are an expert in the field of {topic}. Explain {topic} in detail.
            """

        elif prompt_type == "Audience Prompting":

            prompt= f"""

            Explain {topic} to a grade 5 student"""

        elif prompt_type == "Structured Prompting":

            prompt= f"""
            Provide a structured explanation of {topic} with 

            Title:
            Subtitle:
            Description:
            Examples:
            """

        elif prompt_type == "Constraint Prompting":

            prompt= f"""
            Explain {topic} in less than 100 words.
            """

        elif prompt_type == "Comparitive Prompting":

            prompt= f"""
            Compare and contrast {topic} with a related concept.
            """

        with st.spinner("Generating Prompt..."):
            response=client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role":"user","content":prompt}
                ],
                temperature=temperature,
                max_tokens=max_tokens
            )

        output=response.choices[0].message.content

        st.success("Prompt Generated Successfully!")

        st.subheader("AI Response")

        st.text_area("Generated Prompt", value=output, height=200)