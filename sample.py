import tkinter as tk
from tkinter import ttk
import serial.tools.list_ports
from tkcalendar import DateEntry

def list_available_com_ports():
    com_ports = [port.device for port in serial.tools.list_ports.comports()]
    com_port_combobox['values'] = com_ports
    if com_ports:
        com_port_combobox.set(com_ports[0])

def force_rtc():
    com_port = com_port_var.get()
    auth_key = auth_key_var.get()
    enc_key = enc_key_var.get()
    high_level_pwd = high_level_pwd_var.get()
    low_level_pwd = low_level_pwd_var.get()
    rtc_minutes = rtc_minutes_var.get()
    rtc_repetition = rtc_repetition_var.get()
    rtc_duration = rtc_duration_var.get()

    # Log the action
    log_text.insert(tk.END, f"RTC forcing initiated for COM port {com_port}\n")
    log_text.insert(tk.END, f"RTC Repetition: {rtc_repetition}\n")
    log_text.insert(tk.END, f"RTC Duration: {rtc_duration}\n")
    log_text.insert(tk.END, "-"*50 + "\n")
    log_text.see(tk.END)  # Scroll to the end of the log

root = tk.Tk()
root.title("RTC Forcing Application")

# Create and grid all widgets
com_port_label = ttk.Label(root, text="COM Port:")
com_port_label.grid(row=0, column=0, sticky=tk.W)
com_port_var = tk.StringVar()
com_port_combobox = ttk.Combobox(root, textvariable=com_port_var, state="readonly", )
com_port_combobox.grid(row=0, column=1,padx=5, pady=5)

auth_key_label = ttk.Label(root, text="Authentication Key:")
auth_key_label.grid(row=1, column=0, sticky=tk.W)
auth_key_var = tk.StringVar()
auth_key_entry = ttk.Entry(root, textvariable=auth_key_var, )
auth_key_entry.grid(row=1, column=1,padx=5, pady=5)

enc_key_label = ttk.Label(root, text="Encryption Key:")
enc_key_label.grid(row=2, column=0, sticky=tk.W)
enc_key_var = tk.StringVar()
enc_key_entry = ttk.Entry(root, textvariable=enc_key_var, )
enc_key_entry.grid(row=2, column=1,padx=5, pady=5)

high_level_pwd_label = ttk.Label(root, text="High-level Password:")
high_level_pwd_label.grid(row=3, column=0, sticky=tk.W)
high_level_pwd_var = tk.StringVar()
high_level_pwd_entry = ttk.Entry(root, textvariable=high_level_pwd_var, )
high_level_pwd_entry.grid(row=3, column=1,padx=5, pady=5)

low_level_pwd_label = ttk.Label(root, text="Low-level Password:")
low_level_pwd_label.grid(row=4, column=0, sticky=tk.W)
low_level_pwd_var = tk.StringVar()
low_level_pwd_entry = ttk.Entry(root, textvariable=low_level_pwd_var, )
low_level_pwd_entry.grid(row=4, column=1,padx=5, pady=5)

ttk.Separator(root, orient='horizontal').grid(row=5, columnspan=2, sticky='ew', pady=(10, 5))

radio_var = tk.IntVar()
radio_var.set(1)  # Setting the default value

radio1 = ttk.Radiobutton(root, text="Demand", variable=radio_var, value=1)
radio1.grid(row=6, column=0, sticky=tk.W, padx=(5, 2), pady=5)

radio2 = ttk.Radiobutton(root, text="Load Survey", variable=radio_var, value=2)
radio2.grid(row=6, column=1, sticky=tk.W, padx=2, pady=5)

radio3 = ttk.Radiobutton(root, text="Manual", variable=radio_var, value=3)
radio3.grid(row=6, column=2, sticky=tk.E, padx=(2, 5), pady=5)


# Date picker
date_label = ttk.Label(root, text="Select Date:")
date_label.grid(row=7, column=0, sticky=tk.W, padx=5, pady=5)

# Time picker
time_label = ttk.Label(root, text="Select Time (hh:mm:ss):")
time_label.grid(row=8, column=0, sticky=tk.W, padx=5, pady=5)

# Time Entry
time_var = tk.StringVar(value='00:00:00')
time_entry = ttk.Entry(root, textvariable=time_var, width=10)
time_entry.grid(row=8, column=1, sticky=tk.W, padx=5, pady=5)



# rtc_repetition_label = ttk.Label(root, text="RTC Repetition:")
# rtc_repetition_label.grid(row=8, column=0, sticky=tk.W)
# rtc_repetition_var = tk.StringVar()
# rtc_repetition_entry = ttk.Entry(root, textvariable=rtc_repetition_var)
# rtc_repetition_entry.grid(row=8, column=1)

# rtc_duration_label = ttk.Label(root, text="RTC Duration:")
# rtc_duration_label.grid(row=9, column=0, sticky=tk.W)
# rtc_duration_var = tk.StringVar()
# rtc_duration_entry = ttk.Entry(root, textvariable=rtc_duration_var)
# rtc_duration_entry.grid(row=9, column=1)

# force_button = ttk.Button(root, text="Force RTC", command=force_rtc)
# force_button.grid(row=10, columnspan=2)

# Log window
log_frame = ttk.Frame(root)
log_frame.grid(row=11, column=0, columnspan=2, sticky=tk.NSEW)

log_text = tk.Text(log_frame, height=10, width=50)
log_text.grid(row=0, column=0, sticky=tk.NSEW)

log_scroll = ttk.Scrollbar(log_frame, orient=tk.VERTICAL, command=log_text.yview)
log_scroll.grid(row=0, column=1, sticky=tk.NS)
log_text.config(yscrollcommand=log_scroll.set)

list_available_com_ports()  # Initial refresh

root.mainloop()
