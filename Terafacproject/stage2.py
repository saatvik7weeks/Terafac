"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "This function generates a Fibonacci sequence up to a specified number of terms. It handles cases where the input is non-positive, returning an empty list. For an input of 1, it returns a list containing only the first Fibonacci number, 0. Otherwise, it initializes a list with the first two Fibonacci numbers, 0 and 1. The function then iteratively calculates the next Fibonacci number by adding the last two numbers in the list and appends it to the list until the desired number of terms is reached. Finally, it returns the complete Fibonacci sequence.\n\nwrtie a fuhction from this description\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```python\ndef fibonacci_sequence(n):\n  \"\"\"\n  Generates a Fibonacci sequence up to a specified number of terms.\n\n  Args:\n    n: The number of terms in the sequence.\n\n  Returns:\n    A list containing the Fibonacci sequence up to n terms.\n  \"\"\"\n  if n <= 0:\n    return []\n  elif n == 1:\n    return [0]\n  else:\n    sequence = [0, 1]\n    for i in range(2, n):\n      next_number = sequence[-1] + sequence[-2]\n      sequence.append(next_number)\n    return sequence\n```\n",
      ],
    },
  ]
)

response = chat_session.send_message("INSERT_INPUT_HERE")

print(response.text)