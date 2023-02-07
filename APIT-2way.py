import requests
import serial

# Replace YOUR_API_KEY with your actual API key
API_KEY = "YOUR_API_KEY"

# Endpoint for the OpenAI API
API_ENDPOINT = "https://api.openai.com/v1/engines/text-davinci-002/jobs"

def generate_text(prompt):
    # Define the request data
    data = {
        "prompt": prompt,
        "max_tokens": 100,
        "temperature": 0.5,
    }

    # Send a post request to the API endpoint
    response = requests.post(
        API_ENDPOINT,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}",
        },
        json=data,
    )

    # Check if the request was successful
    if response.status_code != 200:
        raise ValueError("Failed to generate text")

    # Return the generated text
    return response.json()["choices"][0]["text"]

# Open the serial port
ser = serial.Serial("COM1", 4800)

while True:
    # Read input from the serial port
    input_text = ser.readline().decode().strip()

    # Generate text using the OpenAI API
    generated_text = generate_text(input_text)

    # Write the generated text to the serial port
    ser.write(generated_text.encode() + b'\n')

ser.close()
