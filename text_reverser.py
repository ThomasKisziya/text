# text_reverser.py

# Function to reverse the entered text
def reverse_text(text):
    return text[::-1]

# Main function to prompt the user for input
def main():
    print("Text Reverser - Reverse the Entered Text")
    while True:
        text = input("Enter text to reverse (or 'exit' to quit): ")
        if text.lower() == 'exit':
            print("Goodbye!")
            break
        reversed_text = reverse_text(text)
        print(f"Reversed: {reversed_text}")

if __name__ == "__main__":
    main()
