def encrypt_string(text, key=7):
  encrypted_blocks = []
  
  for index, char in enumerate(text):
    # Shift ASCII value by the key and the current index
    shifted_value = ord(char) + key + index
    
    # Convert to a hexadecimal string
    hex_value = hex(shifted_value)[2:]
    encrypted_blocks.append(hex_value)
    
  # Reverse the blocks for extra scrambling
  encrypted_blocks.reverse()
  
  # Join with dashes
  return "-".join(encrypted_blocks)

# Example usage
secret_message = "Hello"
encrypted_text = encrypt_string(secret_message)
print(encrypted_text)
