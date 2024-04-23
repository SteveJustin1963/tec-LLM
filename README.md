# python serial terminal with openAI API link, so AI can talk to MINT running on a TEC-1


The OpenAI API is a cloud-based service that allows developers to access the capabilities of the OpenAI language models, including ChatGPT. The API provides a simple interface for sending input text and receiving predicted output text in real-time. The API can be integrated into a variety of applications and services, such as chatbots, language translation systems, and more. The API offers several customization options, such as controlling the length of the output and setting specific parameters for the language model's behavior. Access to the API is typically provided through API keys and usage is charged based on the amount of API requests made.

## high-level overview of the steps required to use the OpenAI API with a serial terminal app:

Register for an OpenAI API key: You will need to create an account with OpenAI and apply for an API key to access the OpenAI API.

Choose a serial terminal app: There are several serial terminal apps available for different platforms, such as Windows, macOS, and Linux. Some popular examples include PuTTY, CoolTerm, and Screen.

Connect the serial terminal app to the API: You will need to write a program or script to interface with the OpenAI API and send input text to the API and receive output text from the API. You can use a programming language such as Python or JavaScript to do this. The program or script should use the API key and send an HTTP request to the API endpoint. The output text received from the API can then be displayed in the serial terminal app.

Test the setup: Once you have the program or script set up, you can test the communication between the serial terminal app and the OpenAI API by sending input text to the API and checking the output text in the serial terminal app.

## Python script for sending input text to the OpenAI API and receiving output text from the API only
- `APIT-1way.py`
- to communicate with a serial terminal at a baud rate of 4800. 
- use a library such as pyserial that provides an interface for accessing serial ports in Python.


## Python script for two-way communication over the API using a serial connection. 
- `APIT-2way.py`
- This code uses a while loop to continuously read input from the serial port, 
- send it to the OpenAI API using the generate_text function, 
- and write the output back to the serial port. 
- The ser.readline() method is used to read a line of text from the serial port, 
- and the ser.write method is used to write a line of text to the serial port. 
- The input and output text is encoded and decoded as necessary to work with the serial connection.

