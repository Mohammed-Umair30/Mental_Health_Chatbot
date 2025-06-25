# Mental_Health_Chatbot

#### 💡 Objective This project aims to build a basic empathetic mental health support chatbot capable of responding to user input related to stress, anxiety, and emotional wellness in a kind, understanding, and emotionally intelligent tone.

🧪 Model & Dataset Base Model: DistilGPT2 (lightweight and suitable for low-resource systems)

Training Dataset: EmpatheticDialogues — a collection of open-domain conversations grounded in emotional situations, originally released by Facebook AI.

🎯 Project Goals Fine-tune a small language model to understand emotional context and respond empathetically.

Provide supportive replies aligned with mental health topics.

Create a basic interface (e.g., Streamlit or command-line) for interacting with the model.

⚙ Approach The model was fine-tuned using the Hugging Face Trainer API.

Preprocessing involved converting dialogue pairs (prompt, utterance) into a conversational format.

A limited training setup (2 epochs) was used due to hardware constraints (CPU-only system).

⚠ Limitations Training was done without a GPU, which impacted the performance and response quality.

Only two epochs of training were performed, leading to limited generalization and fluency in responses.

The primary goal was educational: to learn the end-to-end pipeline of fine-tuning a language model.

✅ What I Learned How to work with Hugging Face’s Trainer API.

How to load and prepare datasets like EmpatheticDialogues.

How to tokenize and format data for causal language modeling.

How to configure training arguments and monitor model performance.

The difference in model response quality with limited vs. extensive training.

📌 Future Improvements Use a GPU-enabled environment (e.g., Colab Pro or Kaggle kernels) for faster and better training.

Experiment with larger models like GPT-Neo or Mistral 7B for deeper understanding and richer responses.

Add evaluation metrics and interactive user feedback.

Improve the front-end (Streamlit) interface for real-time use.

🙌 Acknowledgments Hugging Face for providing tools and open-access models.

Facebook AI for the EmpatheticDialogues dataset.

Community resources and tutorials that inspired and guided the development.
