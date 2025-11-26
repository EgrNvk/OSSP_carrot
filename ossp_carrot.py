import tkinter as tk
import threading
import time
import random

NUM_STAGES = 9
carrot_states = ["empty", "empty", "empty"]
carrot_stage = [0, 0, 0]
collected_count = 0

root = tk.Tk()
root.title("Ферма моркви")

label_counter = tk.Label(root, text="Зібрано: 0", font=("Arial", 14))
label_counter.grid(row=1, column=0, columnspan=3, pady=10)

buttons = []
current_images = [None, None, None]


def load_stage_image(stage: int):
    return tk.PhotoImage(file=f"img/{stage}.png")


def update_button_bg(index: int, stage: int):
    carrot_stage[index] = stage
    img = load_stage_image(stage)
    current_images[index] = img
    buttons[index].config(image=img)


def set_state(index: int, state: str):
    carrot_states[index] = state


def update_counter():
    label_counter.config(text=f"Зібрано: {collected_count}")


def grow_carrot(index: int):
    start = carrot_stage[index]

    for stage in range(start + 1, NUM_STAGES):
        time.sleep(random.uniform(0.2, 2.0))

        def ui_update(s=stage):
            update_button_bg(index, s)
            if s == NUM_STAGES - 1:
                set_state(index, "ready")

        root.after(0, ui_update)


def on_click(index: int):
    global collected_count

    state = carrot_states[index]

    if state == "empty":
        set_state(index, "growing")
        update_button_bg(index, 0)
        threading.Thread(target=grow_carrot, args=(index,), daemon=True).start()

    elif state == "ready":
        collected_count += 1
        update_counter()
        set_state(index, "empty")
        update_button_bg(index, 0)


button1 = tk.Button(root, borderwidth=0, highlightthickness=0,
                    command=lambda: on_click(0))
button1.grid(row=0, column=0, padx=10, pady=10)
buttons.append(button1)
update_button_bg(0, 0)

button2 = tk.Button(root, borderwidth=0, highlightthickness=0,
                    command=lambda: on_click(1))
button2.grid(row=0, column=1, padx=10, pady=10)
buttons.append(button2)
update_button_bg(1, 0)

button3 = tk.Button(root, borderwidth=0, highlightthickness=0,
                    command=lambda: on_click(2))
button3.grid(row=0, column=2, padx=10, pady=10)
buttons.append(button3)
update_button_bg(2, 0)

root.mainloop()
