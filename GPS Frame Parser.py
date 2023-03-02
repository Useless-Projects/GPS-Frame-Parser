import tkinter as tk

def parse_gps_frame():
    text = gps_input.get()
    field = text.split(",")

    if field[0] == "$GPGGA":
        time = field[1]
        number = field[8]
        number_numerique = float(number)
        number_arrondi = round(number_numerique)

        result_text.set("Time: " + time[1:3] + "h" + " " + time[3:5] + "m" + " " + time[5:6] + "s" + " " + time[8:11] + "ms\n"
                         "Latitude: " + (field[2]) + " " + (field[3]) + "\n"
                         "Longitude: " + (field[4]) + " " + (field[5]) + "\n"
                         "Altitude: " + (field[9]) + (field[10]) + "\n"
                         "Satellites:" + (field[7]) + "\n"
                         "Reliability: " + get_reliability_string(number_arrondi))
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

# Create an input field to enter the GPS frame
gps_input = tk.Entry(window, width=50)
gps_input.pack(pady=10)

# Create a button to submit the GPS frame
submit_button = tk.Button(window, text="Parse GPS Frame", command=parse_gps_frame)
submit_button.pack(pady=10)

# Create a text field to display the result
result_text = tk.StringVar()
result_label = tk.Label(window, textvariable=result_text, wraplength=500)
result_label.pack(pady=10)

# Start the main loop of the window
window.mainloop()