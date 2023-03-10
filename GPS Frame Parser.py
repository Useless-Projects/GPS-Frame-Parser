import tkinter as tk
import tkinter.messagebox as messagebox

def parse_gps_frame():
    text = gps_input.get()
    field = text.split(",")

    if field[0] == "$GPGGA":
        time = field[1]
        number = field[8]
        number_numerique = float(number)
        number_arrondi = round(number_numerique)
        if time[8:11] == "":
            result_text_widget.configure(state="normal")
            result_text_widget.delete("1.0", "end")
            result_text_widget.insert("1.0", "Time: " + time[1:3] + "h" + " " + time[3:5] + "m" + " " + time[5:6] + "s\n"
                            "Latitude: " + (field[2]) + " " + (field[3]) + "\n"
                            "Longitude: " + (field[4]) + " " + (field[5]) + "\n"
                            "Altitude: " + (field[9]) + (field[10]) + "\n"
                            "Satellites:" + (field[7]) + "\n"
                            "Reliability: " + get_reliability_string(number_arrondi), "center")
            result_text_widget.configure(state="disabled")
        else:
            result_text_widget.configure(state="normal")
            result_text_widget.delete("1.0", "end")
            result_text_widget.insert("1.0", "Time: " + time[1:3] + "h" + " " + time[3:5] + "m" + " " + time[5:6] + "s" + " " + time[8:11] + "ms\n"
                         "Latitude: " + (field[2]) + " " + (field[3]) + "\n"
                         "Longitude: " + (field[4]) + " " + (field[5]) + "\n"
                         "Altitude: " + (field[9]) + (field[10]) + "\n"
                         "Satellites:" + (field[7]) + "\n"
                         "Reliability: " + get_reliability_string(number_arrondi), "center")
            result_text_widget.configure(state="disabled")
    else:
        result_text.set("This is not a GPS Frame!")

def get_reliability_string(number):
    reliability_map = {
        1: "Good",
        2: "Rather good",
        3: "Fairly good",
        4: "Average",
        5: "Fairly bad",
        6: "Rather bad",
        7: "Very bad",
        8: "Extremely bad",
        9: "Bad"
    }
    return reliability_map.get(number, "Unknown")

# Create the tkinter window
window = tk.Tk()
window.title("GPS Frame Parser")

# Create the menu bar
menu_bar = tk.Menu(window)

# Add the "About" command to the menu bar
menu_bar.add_command(label="About", command=lambda: messagebox.showinfo("About", "GPS Frame Parser v1.1.0\nCoded by Thibault Savenkoff\nLicensed under the GNU General Public License v3.0.\n© 2023 Thibault Savenkoff. All rights reserved."))

# Set the menu bar for the window
window.config(menu=menu_bar)

# Create an input field to enter the GPS frame
gps_input = tk.Entry(window, width=50)
gps_input.pack(pady=10)

# Create a button to submit the GPS frame
submit_button = tk.Button(window, text="Parse GPS Frame", command=parse_gps_frame)
submit_button.pack(pady=10)

# Create a text field to display the result
result_text = tk.StringVar()
result_text_widget = tk.Text(window, wrap="word", height=8, width=50, bd=0, highlightthickness=0)
result_text_widget.insert("1.0", result_text.get())
result_text_widget.configure(state="disabled")
result_text_widget.pack(pady=10)
result_text_widget.tag_configure("center", justify="center")

def copy_to_clipboard(event):
    window.clipboard_clear()
    window.clipboard_append(result_text_widget.get("1.0", "end"))

result_text_widget.bind("<Button-1>", copy_to_clipboard)

# Start the main loop of the window
window.mainloop()