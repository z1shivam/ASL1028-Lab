import tkinter as tk
from tkinter import ttk

def send_email():
    output_label.config(text="The mail is sent, thank you.")

root = tk.Tk()
root.title("Mail Composing Interface")

# Create a frame for the mail provider selection
provider_frame = ttk.LabelFrame(root, text="Select Mail Provider")
provider_frame.pack(fill="both", expand="yes", padx=10, pady=10)

# Create radio buttons for selecting mail provider
provider_var = tk.StringVar()
gmail_radio = ttk.Radiobutton(provider_frame, text="Gmail", variable=provider_var, value="gmail")
outlook_radio = ttk.Radiobutton(provider_frame, text="Outlook", variable=provider_var, value="outlook")
gmail_radio.grid(row=0, column=0, padx=5, pady=5)
outlook_radio.grid(row=0, column=1, padx=5, pady=5)

# Create a frame for the mail composing interface
compose_frame = ttk.LabelFrame(root, text="Compose Your Mail")
compose_frame.pack(fill="both", expand="yes", padx=10, pady=10)

# Create a label and entry for the "From" field
from_label = ttk.Label(compose_frame, text="From:")
from_label.grid(row=0, column=0, padx=5, pady=5)
from_entry = ttk.Entry(compose_frame)
from_entry.grid(row=0, column=1, padx=5, pady=5)

# Create a label and entry for the "To" field
to_label = ttk.Label(compose_frame, text="To:")
to_label.grid(row=1, column=0, padx=5, pady=5)
to_entry = ttk.Entry(compose_frame)
to_entry.grid(row=1, column=1, padx=5, pady=5)

# Create a label and entry for the "Subject" field
subject_label = ttk.Label(compose_frame, text="Subject:")
subject_label.grid(row=2, column=0, padx=5, pady=5)
subject_entry = ttk.Entry(compose_frame)
subject_entry.grid(row=2, column=1, padx=5, pady=5)

# Create a scrollbar for the message text box
scrollbar = ttk.Scrollbar(compose_frame)
scrollbar.grid(row=3, column=2, sticky="NS")

# Create a text box for the message
message_text = tk.Text(compose_frame, yscrollcommand=scrollbar.set)
message_text.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="NSEW")

# Configure the scrollbar to work with the message text box
scrollbar.config(command=message_text.yview)

# Create a checkbox for adding signature
signature_var = tk.IntVar()
signature_check = ttk.Checkbutton(compose_frame, text="Add Your Signature", variable=signature_var)
signature_check.grid(row=4, column=0, padx=5, pady=5)

# Create a button to send the email
send_button = ttk.Button(compose_frame, text="Send Email", command=send_email)
send_button.grid(row=4, column=1, padx=5, pady=5)

# Create a label for the output
output_label = ttk.Label(root, text="")
output_label.pack(side="bottom", padx=10, pady=10)

root.mainloop()