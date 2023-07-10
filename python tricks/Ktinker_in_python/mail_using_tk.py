import tkinter as tk

def send_email():
    output_label.config(text="The mail is sent, thank you.")

root = tk.Tk()
root.title("Mail Composing Interface")

provider_frame = tk.LabelFrame(root, text="Select Mail Provider")
provider_frame.pack(fill="both", expand="yes", padx=10, pady=10)

provider_var = tk.StringVar()
gmail_radio = tk.Radiobutton(provider_frame, text="Gmail", variable=provider_var, value="gmail")
outlook_radio = tk.Radiobutton(provider_frame, text="Outlook", variable=provider_var, value="outlook")
gmail_radio.grid(row=0, column=0, padx=5, pady=5)
outlook_radio.grid(row=0, column=1, padx=5, pady=5)

compose_frame = tk.LabelFrame(root, text="Compose Your Mail")
compose_frame.pack(fill="both", expand="yes", padx=10, pady=10)

from_label = tk.Label(compose_frame, text="From:")
from_label.grid(row=0, column=0, padx=5, pady=5)
from_entry = tk.Entry(compose_frame)
from_entry.grid(row=0, column=1, padx=5, pady=5)

to_label = tk.Label(compose_frame, text="To:")
to_label.grid(row=1, column=0, padx=5, pady=5)
to_entry = tk.Entry(compose_frame)
to_entry.grid(row=1, column=1, padx=5, pady=5)

subject_label = tk.Label(compose_frame, text="Subject:")
subject_label.grid(row=2, column=0, padx=5, pady=5)
subject_entry = tk.Entry(compose_frame)
subject_entry.grid(row=2, column=1, padx=5, pady=5)

scrollbar = tk.Scrollbar(compose_frame)
scrollbar.grid(row=3, column=2, sticky="NS")

message_text = tk.Text(compose_frame, yscrollcommand=scrollbar.set)
message_text.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="NSEW")

scrollbar.config(command=message_text.yview)

signature_var = tk.IntVar()
signature_check = tk.Checkbutton(compose_frame, text="Add Your Signature", variable=signature_var)
signature_check.grid(row=4, column=0, padx=5, pady=5)

send_button = tk.Button(compose_frame, text="Send Email", command=send_email)
send_button.grid(row=4, column=1, padx=5, pady=5)

output_label = tk.Label(root, text="")
output_label.pack(side="bottom", padx=10, pady=10)

root.mainloop()  